status_code = 100

match status_code:
    case 200:
        print("Ok")
    case 201:
        print("Created")
    case 300:
        print("Multiple choices")
    case 404:
        print("Not found")
    case 500:
        print("Internal server error")
    case _:
        print("Invalid code")

