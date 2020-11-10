def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if arr[mid] == target:
            print(mid)
            return mid
        elif target < arr[mid]:
	        right = mid - 1
        else:
            left = mid + 1
    print("element not found")
    return "element not found"

arr1 = [-8, 3, 4, 6, 7, 8, 9, 11, 12, 13, 17, 19, 200, 219, 220]

print("\n"*2)
print("We are binary seraching in this array :")
print("\n"*2)
print(*arr1)
print("\n"*2)

n = int(input("ENTER a number to search for..."))

search(arr1, n)