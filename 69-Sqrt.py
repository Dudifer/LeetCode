print("Date started: 5/15/23")
print("Date completed: 5/15/23")
def mySqrt(x):
    for i in range(1, x+1):
        if i*i==x:
            return i


def betterSqrt(x):
    left,right=1,x
    while left<=right:
        mid=(left+right)//2
        if mid*mid==x:
            return mid
        if mid*mid>x:
            right=mid-1
        else:
            left=mid+1
    return right
