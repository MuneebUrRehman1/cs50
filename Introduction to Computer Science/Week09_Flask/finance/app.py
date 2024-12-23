import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    holdings = db.execute(" SELECT symbol, SUM(shares) as total_shares FROM purchases WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0",
                            session["user_id"])
    total_portfolio_value = user_cash
    for holding in holdings:
        quote_result = lookup(holding["symbol"])
        holding["name"] = quote_result["name"]
        holding["price"] = quote_result["price"]
        holding["total_value"] = holding["total_shares"] * quote_result["price"]
        total_portfolio_value += holding["total_value"]
    return render_template("index.html", user_cash=user_cash, holdings=holdings, total_portfolio_value=total_portfolio_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if not symbol or not shares:
            return apology("one or more fields are empty", 404)
        elif shares<0:
            return apology("shares can not be negative", 404)

        response = lookup(request.form.get("symbol"));
        if not response:
             return apology("stock not found")
        required_cash = response.get("price") * shares
        available_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        if available_cash < required_cash:
            return apology("insufficiant cash")
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", required_cash, session["user_id"])
        db.execute("INSERT INTO purchases (user_id, symbol, price, shares) VALUES (?,?,?,?)",session["user_id"], symbol,required_cash, shares)
        return redirect("/")
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    transactions = db.execute("""
        SELECT symbol, shares, price, date
        FROM purchases
        WHERE user_id = ?
    """, session["user_id"])
    for transaction in transactions:
        quote_result = lookup(transaction["symbol"])
        transaction["name"] = quote_result["name"]
    return render_template("history.html", transactions=transactions)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide stock symbol")
        response = lookup(request.form.get("symbol"));
        if(not response):
             return apology("stock not found")
        return render_template("quoted.html", response =response)
    else:
        return render_template("quote.html")




@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cfm_password = request.form.get("confirmation")
        if not username or not password or not cfm_password:
            return apology("one or more fields are empty")
        elif password != cfm_password:
            return apology("password do not match")
        hashed_password = generate_password_hash(password)
        result = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hashed_password);
        if not result:
            return apology("user already exists")
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)
        if not request.form.get("shares"):
            return apology("must provide number of shares", 400)
        shares = int(request.form.get("shares"))
        if shares <= 0:
             return apology("number of shares must be a positive integer", 400)
        quote_result = lookup(request.form.get("symbol"))
        if not quote_result:
            return apology("stock symbol not found", 400)
        user_holdings = db.execute("""
            SELECT SUM(shares) as total_shares
            FROM purchases
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
        """, session["user_id"], quote_result["symbol"])
        if not user_holdings or user_holdings[0]["total_shares"] < shares:
            return apology("insufficient shares to sell", 400)
        total_sale_value = shares * quote_result["price"]
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sale_value, session["user_id"])
        db.execute("INSERT INTO purchases (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                    session["user_id"], quote_result["symbol"], -shares, quote_result["price"])
        return redirect("/")
    else:
        symbols = db.execute("""
            SELECT symbol
            FROM purchases
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, session["user_id"])
        return render_template("sell.html", holdings=symbols)
