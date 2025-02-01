# Sqrt calculation using Newton's Method
s = 1
x =2
kmax = 10
for k in range(kmax):
    s = 0.5*(s+(x/s));
print(s)
