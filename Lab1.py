def hello_world():
    print("Hello, World!")


def input_output():
    name = input()
    age = int(input())
    height = float(input())

    result = (
        f"Your name is {name}\n"
        f"You are {age} years old\n"
        f"You are {height} feet tall"
    )

    return result
