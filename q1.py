
def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = int(l + (r - l)/2) ;
         
        # Check if x is present at mid
        if arr[mid] == x:
            return True
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
     
    # If we reach here, then the element
    # was not present
    return False

n = int(input())
#d = dict()
a1, b1 = map(int, input().split())
a = []
b = []
a.append(a1)
b.append(b1)
for i in range(n-2):
	z1, z2 = map(int, input().split())
	if binarySearch(a, 0, int(len(a))-1, z1):
		b.append(z2)
	else:
		a.append(z2)
#flag = True

#print(g)

	
#print(a, b)
f = (int(len(a)) * int(len(b)) )
out = f - (n-1)
print (out)

		

