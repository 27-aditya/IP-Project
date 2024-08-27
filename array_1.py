arr = [1, 2, 3, 4, 5]

print(arr[0])  # 1 (first element)
print(arr[-1]) # 5 (last element)

arr[2] = 10
print(arr)  # [1, 2, 10, 4, 5]

arr.append(6)
print(arr)  # [1, 2, 10, 4, 5, 6]

arr.remove(10)
print(arr)  # [1, 2, 4, 5, 6]
