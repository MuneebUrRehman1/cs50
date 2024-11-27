import sys
from PIL import Image
from PIL import ImageOps

valid_extensions = ["jpg", "jpeg", "png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (
    not sys.argv[1].split(".")[-1] in valid_extensions
    or not sys.argv[2].split(".")[-1] in valid_extensions
):
    print(sys.argv[1].split(".")[-1])
    sys.exit("Invalid input")
elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(sys.argv[1]) as input_img:
        shirt_image = Image.open("shirt.png")
        img = ImageOps.fit(input_img, shirt_image.size)
        img.paste(shirt_image, (0, 0), shirt_image)
        img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
