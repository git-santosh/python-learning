a = 12
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b) #it will return floating point numner
print(a//b)#it will return integer without decimal
print(a%b)

print()
for i in range(1,a//b):
    print(i)

print()

print(a+b/3-4*12) # 13 - 48 = -35 

print((((a+b)/3)-4)*12)

d = a + b
e = d/3
f = e-4
print('Expression:\t','((((12+3)/3)-4)*12) = ',f*12)

p =8
q =2

# ** exponent operator
print( 'Exponent:\t ' , p , '² = ' , p ** q , sep = '' )