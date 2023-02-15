import string
"""
f = "hello world"
s = "i want two things in life, loving you and be loved by you".replace(" ", "")
print(f.count("l"))
print(f.capitalize())
print(s.find("o"))
print(s.count("o",10,38))
print(s.index("you"),10,38)
print(s.find("you",s.find("you")+ 1))
print(s.rfind("you"))
print(s.rindex("you"))
print(s.swapcase())
print(s.startswith("you"))

for i in range(1,20,2):
    s = '*' * i
    print(s.rjust(20))

binary = '012a012a012a012a012a012a'
print(binary.translate(str.maketrans('01a2', '456b')))

#for i in range(1,20,2):
for j in range(21,0,-1):
    #s = "*" * i
    s1 = "*" * j
    print(s1.ljust(18)) 

b = "my name is seun"
j = b[:5] + "y" + b[6:]
print(j) """

v = "we are semicolon native"
i = v[0:] + (v[:-1] + "a")
print(i)

s = "i want two things in life, loving you and be loved by you".replace(" ", "")
print(s.find("you",s.find("you")+ 1))
print(s.find("o"))
