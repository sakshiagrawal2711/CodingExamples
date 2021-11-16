
def fact(mvar):
    if mvar < 2:
        return 1
    return mvar*fact(mvar-1)
I = input()
print("Factorial of: "+I)
print("is "+str(fact(int(I))))