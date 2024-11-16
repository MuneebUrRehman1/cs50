fileName, extension = input("File name: ").split(".")

match extension:
    case "gif" | "jpg" | "jpeg" | "png":
        print(f"image/{extension}")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")

