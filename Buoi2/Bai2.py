def list_ends (L):
    list_ends = L[::len(L)-1]
    return list_ends
L = [2,4,6,5,2,2,43,8,9,10]
print(list_ends(L))