class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"Hello! I'm {self.name}, I have the power of {self.power} and protect {self.city}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass: FlyingSuperhero inherits from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, wing_span):
        super().__init__(name, power, city)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} soars through the sky with a wingspan of {self.wing_span} meters!")

# Creating instances
hero1 = Superhero("Captain Strength", "Super Strength", "Metropolis")
hero2 = FlyingSuperhero("Sky Ranger", "Flight and Agility", "Gotham", 15)

# Using methods
hero1.introduce()
hero1.use_power()

print()  # For spacing

hero2.introduce()
hero2.use_power()
hero2.fly()