def euclid(a,b):
    if a==b: return a
    if a==0: return b
    if b==0: return a
    if a>b: return euclid(a-b,b)
    if a<b: return euclid(a,b-a)
print(euclid(66528, 52920))