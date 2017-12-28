a = [1,2,3,4,5,6]
b = [3,5,6,7,8]
i = j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] < b [j]:
        i = i + 1
    elif a[i] > b[j]:
        j = j + 1
    else:
        result.append(a[i])
        i = i + 1
        j = j + 1
print(result)
