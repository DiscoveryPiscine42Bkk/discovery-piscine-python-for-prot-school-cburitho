def greetings(name="noble sttranger"):
    if not isinstance(name, str):
        print("Error: Name must be a string.")
    else:
        print(f"Welcome, {name}!")
    greetings()
    greetings("John")
    greetings(123)