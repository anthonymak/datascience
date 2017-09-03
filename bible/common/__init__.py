import inspect

def currentMethodName():
    return inspect.stack()[1][3]
