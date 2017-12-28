"""
Recursive implementation
"""

# def isSubString(s1,s2,m,n):
#     if m == 0:
#         return True
#     if n == 0:
#         return False
#     if s1[m-1] == s2[n-1]:
#         return isSubString(s1,s2,m-1,n-1)
#     return isSubString(s1,s2,m,n-1)
# if __name__ == '__main__':
#     s1 = raw_input('input first string:')
#     s2 = raw_input('input second string:')
#     m = len(s1)
#     n = len(s2)
#     if isSubString(s1,s2,m,n):
#         print('Yes, {} is substring of {}'.format(s1,s2))
#     else:
#         print('No, {} is not substring of {}'.format(s1,s2))

"""
Iterative implementation
"""
def isSubString(s1,s2,m,n):
    i = j = 0
    while j<m and i<n:
        if s1[j] == s2[i]:
            j = j + 1
        i = i + 1
    return j == m

if __name__ == '__main__':
    s1 = raw_input('input first string:')
    s2 = raw_input('input second string:')
    m = len(s1)
    n = len(s2)
    if isSubString(s1,s2,m,n):
        print('Yes, %s is substring of %s' % (s1,s2))
    else:
        print('No, %s is not substring of %s' % (s1,s2))
