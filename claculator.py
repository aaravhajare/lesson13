
def add(p , q) :
    return p + q

def sub(p , q) :
    return p - q

def mul(p , q) :
    return p * q

def div(p , q) :
 
    if (p % 2 == 0) and (q % 2 == 0):
        return p / q
    else :
        p = float(p)
        q = float(q)

        return p / q
print("choose one opration ")
print("a.add")
print("b.sub")
print("c.multiplication")
print("d.division")

c = input("enter one shoice")

n1 = float(input("enter first number"))
n2 = float(input("enter second number"))

if (c == "a") :
    print(n1 , "+" , n2 , "=" , add(n1,n2))

if (c == "b") :
    print(n1 , "-" , n2 , "=" , sub(n1,n2))

if (c == "c") :
    print(n1 , "*" , n2 , "=" , mul(n1,n2))

if (c == "d") :
    print(n1 , "/" , n2 , "=" , div(n1,n2))