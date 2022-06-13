

a = 45
b = 67

a1 = bin(a)[2:]
b1 = bin(b)[2:]
maxim = a1
minim = b1
# maxim = a1 if len(a1) > len(b1) else b1
# minim = a1 if len(a1) < len(b1) else b1
# length = len(maxim)-len(minim)
# minim = "0"*length + minim
print(minim)
print(maxim)
print(int(minim, 2))
print(int(maxim, 2))
print(bin(a&b))

