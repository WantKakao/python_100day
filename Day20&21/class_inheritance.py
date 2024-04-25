class Animal:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.eyes = 3

    def breath(self):
        super().breath()
        print("Ah phu...")


fish = Fish()
fish.breath()
print(fish.eyes)