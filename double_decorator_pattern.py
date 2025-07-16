# Implementing pattern printing with the use of double decorators.
def First_decorator(func):
    def pass_function():
        print("-----------")
        func()
        print("-----------\n\n")
    return pass_function

def Secound_decorator(func):
    def wrapper():
        print("==========")
        func()
        print("==========")
    return wrapper

# 2 decorators direct
@First_decorator
@Secound_decorator
def print_line():
    for i in range(1,4):
        for j in range(i):
            print('*',end="")
        print("",end='\n')
print_line()