alphbet ={
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "siven" : 7,
    "eight" : 8,
    "nine" : 9,
}

n=0
def rec(i):
   
    n = n + 1
    return rec(n)
def element(i):
    a=0
    b=3
    tlen = len(i)
    val =i.lower()
    while(1):
        xx = val[a:b]
        if xx in alphbet:
            x = alphbet[xx]
            if(tlen > 7):
                a = b 
                b = tlen
                yy = val[a:b]
                y = alphbet[yy]
                print(x,y)
                stri = str(x) + str(y)
             
                xi = int(stri)
                return(xi)
                break
            else: 
                return(x)
                break
            
        else :
            print("IN else state")
            b = b+1; 
            continue
    return(0)


def gcd(a,b) :
    if (b == 0):
        return int(a)
    else:
        return gcd(b,a%b)

i = input("Enter input First elemnt :-" )
on = element(i)
# stri = str(on)
print("Output one is " , on , "\n")
ii = input("\nEnter input for second elemnt")
onn = element(ii)
print("value two is " , onn , "\n")

gg = gcd(on,onn)
print("final out put is " , gg)


    