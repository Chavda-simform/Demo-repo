def pri(fx):
    def val(*args,**kwargs):
        print("good morting start")
        result =fx(*args,**kwargs)
        print("good night")
        return result
    return val
@pri    
def newfunc():
    print("hellow world")
@pri
def add(a,b):
    print(a+b)
    return a+b

# newfunc()
a = add(2,4)
# print(a)
# pri(newfunc())