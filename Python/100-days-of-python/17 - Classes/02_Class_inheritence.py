# Preuzivanje metoda i atributa iz druge klase

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        # da bi dobio sve iz Animal
        super().__init__()

    def swim(self):
        print("Moving in water")

    def breathe(self):
        print("Under the sea")
        # da se pozove varijanta iz roditelja
        super().breathe()

nemo = Fish()
nemo.breathe()
nemo.swim()