# Define: Create a hero class with attributes name and hp
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # Act: Add a method take_damage(amount) that subtracts from hp
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} takes {amount} damage and now has {self.hp} health.")

# Instantiate: Create two heroes: Arthur and Morgana
arthur = Hero("Arthur", hp =100)
morgana = Hero("Morgana", hp =100)

# Make Arthur take 10 damage
arthur.take_damage(10)

# Print both their HPs to see that Morgana is still at full health
print(f"{arthur.name}'s remaining HP: {arthur.hp}")
print(f"{morgana.name}'s remaining HP: {morgana.hp}")