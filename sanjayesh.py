def decorator(validator):
    def inner_function(func):
        def ret(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return "error"

        return ret
    return inner_function


def validator(x):
    return x >= 0


@decorator(validator)
def f(x):
    return x ** 0.5


print(f(4))  # should print 2.0
print(f(-4))  # should print error
