arr=[100,5,9,6,8,7,9,66,88,99,22,44,75,33,666,440000000]

n=len(arr)
maxi =0
for i in range(0,n):
    if maxi < arr[i]:
        maxi=arr[i]
print maxi
