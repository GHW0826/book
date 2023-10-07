
# 1.4.1 hungry.py
print("I'm hungry!")
print()

# 1.4.2 class
class Man:
    def __init__(self, name):
        self.name = name
        print("init")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()
print()