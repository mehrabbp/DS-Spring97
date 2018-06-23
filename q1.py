#print("yaeh")
# def search(number, low, high, arr = []):
#   if (high < low):
#     return False
#   mid = (high + low) / 2
#   if (number == arr[mid]):
#     return True
#   if (number > arr[mid]):
#     return search(number, (mid + 1), high, arr)
#   else:
#     return search(number, low, (mid - 1), arr)

# def f(k, o):
# 	for i in range(int(len(a))-1, -1, -1):
# 		if k == o[i]:
# 			return True
# 	return False 

# n = int(input())
# d = dict()
# a1, b1 = map(int, input().split())
# g = []
# for i in range(n-2):
# 	z1, z2 = map(int, input().split())
# 	h = []
# 	h.append(z1)
# 	h.append(z2)
# 	g.append(h)
# flag = True
# a = []
# b = []
# a.append(a1)
# b.append(b1)
# #print(g)
# for i in range(n-2):
# 	if g[i][0] == a[int(len(a)) - 1]:
# 		b.append(g[i][1])
# 	elif g[i][0] != a[int(len(a)) - 1]:
# 		if g[i][0] in a:
# 			b.append(g[i][1])
# 		else:
# 			a.append(g[i][1])

# 	else:
# 		a.append(g[i][1])
# #print(a, b)
# f = (int(len(a)) * int(len(b)) )
# out = f - (n-1)
# print (out)

		

# #print("yaeh")
# def f(k, o):
# 	for i in reversed(o):
# 		if k == i:
# 			return True
# 	return False 
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

		

