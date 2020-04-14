# a = [10,20,30,40]
# for i in a:
#     i+=i
#     print(i)

def a():
    s=1
    c=2
    return s,c

def b(c):
    s,c = c
    w=s+c
    print(w)

b(c=a())
