arr = []
with open("nums.txt") as nums:   
    for line in nums:
        line = line.strip("") # remove newline at end and other whitespace
        n = list(map(int, line.split(",")))
        arr.append(n)
print(arr)

bigger = 0
smaller = 0
ind = -1

for i in arr:
	if ind >= len(arr):
		pass
	elif i > arr[ind]:
		print(i,">",arr[ind], sep="")
		bigger += 1
		ind += 1
	else:
		print(i,"<",arr[ind], sep="")
		smaller += 1
		ind +=1
print("bigger: ",bigger)
print("smaller: ",smaller)