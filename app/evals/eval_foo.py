from app.prompts.foo import GREET


def greet():
    return GREET.format(greeting="hello")


if __name__ == "__main__":
    print(greet())
