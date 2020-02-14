def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nl"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
