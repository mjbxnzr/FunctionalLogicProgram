a=[1,2,3]
def SumOfArray(a):
    b=sum(filter(lambda x: (x>0), a))
    return b
s=SumOfArray
print s([1,3,4,-5])

def fibbo(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else:
        return fibbo(a-1)+fibbo(a-2)

print fibbo(10)
