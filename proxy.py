class ExceptionProxy(Exception):
    def __init__(self, msg, funtion):
        self.msg = msg
        self.function = funtion


def transform_exceptions(func_ls):
    msg = ""
    mylist = []
    for myfunc in func_ls:
        try:
            myfunc()
        except Exception as e:
            msg = str(e)
            # print(msg)
        else:
            msg = "ok!"
        # finally:
        #     print(msg)
        finally:
            myException = ExceptionProxy(msg, myfunc)
            mylist.append(myException)

    return mylist


def f():
    1 / 0


def g():
    pass


tr_ls = transform_exceptions([f, g])

for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)
