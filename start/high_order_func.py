# accept function as argument

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func('Hello')
    print(text)


hello(loud)
hello(quiet)


# Function returning a function

def divisor(x):
    def dividend(y):
        return y / x

    return dividend


num = divisor(2)
print(num(10))
