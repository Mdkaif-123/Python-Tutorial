# ? Decorators are a very powerful and useful tool in Python used to wrap a function
# into another with the specific behaviour

# * Usually decorators are used for logging a function behavior


def greet(fx):
    def mxdf(*args, **mfagrs):
        print("Good morning")
        fx(*args, **mfagrs)
        print("Thank you for using this function, Use again")

    return mxdf

@greet
def hello():
    print("Hello , this is an example program of decorators ! ")

@greet
def add(a, b):
    print("sum is ", a+b)


hello()
add(12, 34)
# Note : Decorator can also be implemented by another method

# greet(hello)()
