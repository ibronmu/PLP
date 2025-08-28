class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def move(self):
        """Base move method to be overridden by subclasses"""
        return "The animal moves."
    
    def speak(self):
        """Base speak method"""
        return "The animal makes a sound."
    
    def get_info(self):
        return f"{self.name} lives in {self.habitat}"

class Bird(Animal):
    """Bird class that inherits from Animal"""
    
    def __init__(self, name, habitat, wingspan_cm):
        super().__init__(name, habitat)
        self.wingspan_cm = wingspan_cm
    
    # Polymorphism: Override move method
    def move(self):
        return f"{self.name} is flying! 🕊️"
    
    def speak(self):
        return f"{self.name} says: Tweet tweet! 🎵"
    
    def build_nest(self):
        return f"{self.name} is building a nest! 🪹"

class Fish(Animal):
    """Fish class that inherits from Animal"""
    
    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count
    
    # Polymorphism: Override move method
    def move(self):
        return f"{self.name} is swimming! 🐠"
    
    def speak(self):
        return f"{self.name} says: Blub blub! 💧"
    
    def blow_bubbles(self):
        return f"{self.name} is blowing bubbles! 💦"

class Mammal(Animal):
    """Mammal class that inherits from Animal"""
    
    def __init__(self, name, habitat, leg_count):
        super().__init__(name, habitat)
        self.leg_count = leg_count
    
    # Polymorphism: Override move method
    def move(self):
        if self.leg_count == 4:
            return f"{self.name} is running! 🐆"
        elif self.leg_count == 2:
            return f"{self.name} is walking! 🚶"
        else:
            return f"{self.name} is moving in a unique way!"
    
    def speak(self):
        return f"{self.name} makes a mammalian sound! 🐾"
    
    def give_birth(self):
        return f"{self.name} gives birth to live young! 👶"

# Specialized subclasses with additional polymorphism
class Cheetah(Mammal):
    """Cheetah class - fastest land animal"""
    
    def __init__(self, name, habitat):
        super().__init__(name, habitat, 4)
    
    # Polymorphism: Specialized move method
    def move(self):
        return f"{self.name} is sprinting at 75 mph! 💨"
    
    def speak(self):
        return f"{self.name} says: Growl! 🐆"

class Dolphin(Mammal):
    """Dolphin class - aquatic mammal"""
    
    def __init__(self, name, habitat):
        super().__init__(name, habitat, 0)  # Dolphins have flippers, not legs
    
    # Polymorphism: Specialized move method
    def move(self):
        return f"{self.name} is swimming and jumping! 🐬"
    
    def speak(self):
        return f"{self.name} says: Eee-eee! Click! 🎶"
    
    def sonar(self):
        return f"{self.name} is using echolocation! 📡"

# Demonstration of polymorphism
print("\n=== Activity 2: Polymorphism Challenge! ===\n")

# Create different animals
animals = [
    Bird("Eagle", "Mountains", 200),
    Fish("Clownfish", "Coral Reef", 7),
    Mammal("Lion", "Savannah", 4),
    Cheetah("Flash", "Grasslands"),
    Dolphin("Flipper", "Ocean")
]

# Demonstrate polymorphism - same method, different behaviors
for animal in animals:
    print(f"{animal.get_info()}")
    print(f"Move: {animal.move()}")
    print(f"Speak: {animal.speak()}")
    
    # Demonstrate additional specialized methods
    if isinstance(animal, Bird):
        print(animal.build_nest())
    elif isinstance(animal, Fish):
        print(animal.blow_bubbles())
    elif isinstance(animal, Cheetah):
        print("Special ability: Incredible acceleration! ⚡")
    elif isinstance(animal, Dolphin):
        print(animal.sonar())
    
    print("-" * 50)

# Additional polymorphism demonstration
print("\n=== Polymorphism in Action ===")
print("All animals can move(), but each does it differently:\n")

for animal in animals:
    print(f"{animal.name}: {animal.move()}")