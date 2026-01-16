from abc import ABC, abstractmethod

# 1. Abstrakt sinf (Shablon)
class Athlete(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def train(self):
        pass

# 2. Footballer sinfi
class Footballer(Athlete):
    def train(self):
        print(f"{self.name}: Maydonda to'p bilan mashq qilmoqda.")

# 3. Swimmer sinfi
class Swimmer(Athlete):
    def train(self):
        print(f"{self.name}: Hovuzda suzish mashqlarini bajarmoqda.")

# 4. Asosiy qism
if __name__ == "__main__":
    s1 = Footballer("Ronaldo")
    s2 = Swimmer("Phelps")

    s1.train()
    s2.train()
