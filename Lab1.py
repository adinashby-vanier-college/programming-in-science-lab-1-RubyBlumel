def hello_world():
    print("Hello, World!")


def input_output():
    name = input("what is your name")
    age = int(input("how old are you"))
    height = float(input("how tall are you"))

    print(
        "your name is " + name + "\n"
        "and you are " + str(age) + " years old\n"
        "you are " + str(height) + " feet tall"
    )
