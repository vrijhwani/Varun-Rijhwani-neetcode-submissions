class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)
print(f"Initial Attributes: Whiskers (cat) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
new_hunger = whiskers.hunger - 3
new_energy = whiskers.energy + 2
print(f"Modified Attributes: Whiskers (cat) - Hunger: {new_hunger}, Energy: {new_energy}")

# TODO: Print Whiskers' initial attributes

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

# TODO: Print Whiskers' modified attributes
