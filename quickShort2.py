def qs(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        left =[x for x in arr[:1] if x<= pivot]
        right =[x for x in arr[1:] if x >= pivot]
        return qs(left)+[pivot]+qs(right)
arr  =[1,3,4,2,5,6,9,7,8]
qs(arr)
