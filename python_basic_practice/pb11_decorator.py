def addWrappers(func):
    def wrapper():
        print("---begin---")
        func()
        print("---end---")
    return wrapper

@addWrappers
def sayHello():
    print("hello")

sayHello()

def repeat(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()
        return wrapper
    return decorator

@repeat(5)
def sayHola():
    print("hola")

sayHola()