def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
        else:
            r=-1
    return r


data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")
