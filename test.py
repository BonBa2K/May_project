def foo():
    r = 0
    for i in range(3):
        yield r
        r = "200 ok" + str(i)
    print("JOJO")
    yield "JJJ"


f = foo()
n1 = next(f)
print("n1 == " + str(n1))
n2 = next(f)
print("n2 == " + str(n2))
n3 = next(f)
print("n3 == " + str(n3))
n4 = next(f)
print("n4 == " + str(n4))
