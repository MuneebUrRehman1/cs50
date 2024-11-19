import sys
import random
from pyfiglet import Figlet

if len(sys.argv) == 1:
    input = input("Input: ")
    fonts = Figlet().getFonts()
    text = Figlet(font= random.choice(fonts))
    print(text.renderText(input))
elif len(sys.argv) == 3:
    input = input("Input: ")
    if sys.argv[1] in ["-f", "--font"]:
        text = Figlet(font=sys.argv[2])
        print(text.renderText(input))
    else:
         sys.exit()
else:
    sys.exit()