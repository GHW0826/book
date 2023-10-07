print()

# 1.3.1 +-*/,**
print("1 - 2: ", 1 - 2)
print("4 * 5: ", 4 * 5)
print("7 / 5: ", 7 / 5)
print("3 ** 2: ", 3 ** 2)
print()

# 1.3.2 type
print(type(10))
print(type(2.718))
print(type("Hello"))
print()

# 1.3.3 variable
x = 10      # 초기화
print(x)    # x 축력
x = 100     # x에 대입
print(x)
y = 3.14
print(x * y)
print(type(x * y))
print()

# 1.3.4 list
a = [1, 2, 3, 4, 5]
print(a)        # 1, 2, 3, 4, 5
len(a)          # 1
print(a[0])     # 1
print(a[4])     # 5
a[4] = 99       # 1, 2, 3, 4, 99
print(a)        # 1, 2, 3, 4, 99

print(a[0:2])   # 1, 2
print(a[1:])    # 2, 3, 4, 99
print(a[:3])    # 1, 2, 3
print(a[:-1])   # 1, 2, 3, 4
print(a[:-2])   # 1, 2, 3
print(a[-1:])   # 99
print(a[-2:])   # 4, 99
print()

# 1.3.5 dic
me = { 'height': 180}   # 생성
print(me['height'])
me['height'] = 175
me['weight'] = 70
print(me['height'])
print(me)