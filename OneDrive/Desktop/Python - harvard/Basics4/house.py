name = input("what is your name:")

match name:
    case "jack" | "ketie" | "mary":
        print("Totem")
    case _ :
        print("who?")
        