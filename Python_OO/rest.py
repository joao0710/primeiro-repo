def f1():
    return [lambda x: x * i**2 for i in range(3)]
    print [f(10) for f in f1()]