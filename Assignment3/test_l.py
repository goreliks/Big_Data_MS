from lithops import FunctionExecutor


def hello(num):

    return num*10


with FunctionExecutor() as fexec:
    fut = fexec.call_async(hello, 2)
    print(fut.result())