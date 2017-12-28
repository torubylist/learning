#coding=utf-8
"""
quick_sort
"""
def partiton(li, a, b):
    x = li[b]
    i = a
    for j in range(a,b):
        if li[j] < x:
            li[i], li[j] = li[j], li[i]
            i += 1
    li[i], li[b] = li[b], li[i]
    return i



def quick_sort(a,l,r):
    if l > r:
        return
    x = partiton(a,l,r)
    quick_sort(a, l, x - 1)
    quick_sort(a, x + 1, r)


if __name__ == '__main__':
    array = [72, 57, 88, 60, 42, 84, 73, 42, 85, 9, 102]
    quick_sort(array, 0, 10)
    print(array)
