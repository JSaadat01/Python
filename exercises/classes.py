class Dog:
    energy = "high"
    def speak(self):
        print("woof")
bilbo_waggins = Dog()
bilbo_waggins.energy = "low"
print(bilbo_waggins.energy)
bilbo_waggins.speak()