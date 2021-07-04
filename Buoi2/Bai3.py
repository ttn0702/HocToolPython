import random
# for i in a:
#     if i in b:
#         L.append(i)
# newlist = [expression for item in iterable if condition == True]

def list_comprehensions(L1,L2):
    L = set([i for i in L1 if i in L2])
    if not L:
        return "Khong co phan tu nao trung nhau!"
    else:
        return L
x = int(input("Nhap do dai List a: "))
a = random.sample(range(100),x)
y = int(input("Nhap do dai List b: "))
b = random.sample(range(100),y)
print(list_comprehensions(a,b))