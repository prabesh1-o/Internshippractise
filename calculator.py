def Calculator(nums1,nums2,op):
    if op=="+":
        return nums1+nums2
    elif op=="-":
        return nums1-nums2
    elif op=="*":
        return nums1*nums2
    elif op=="/":
        if nums2!=0:
            return nums1/nums2
        else:
            return "cannot not be divided by zero"
    else:
        return "Invalid operator"
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
o = input("enter the operator: ")

res=Calculator(n1,n2,o)
print('Final result = ',res)