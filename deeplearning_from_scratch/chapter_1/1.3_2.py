print()

# 1.3.6 bool
hungry = True
sleepy = False
print(type(hungry))
print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy)
print()

#1.3.7 if문
hungry = True
if hungry:
    print("I'm hungry")

hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm Sleepy")
print()

# 1.3.8 for문
for i in[1, 2, 3]:
    print(i)
print()

# 1.3.9 함수
def hello():
    print("Hello World!")

def hello2(object):
    print("Hello " + object + "!")

hello()
hello2("cat")
print()