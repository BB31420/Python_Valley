# Welcome to Python Valley!
# This game teaches you about coding and Object-Oriented Programming (OOP) in a fun way.
# As you play, you'll learn about classes, objects, methods, and more!

import random

class Farmer:
    def __init__(self, name):
        self.name = name     # The name you choose for your farmer
        self.energy = 100    # Your energy level - you need this for farming activities!
        self.gold = 500      # Your in-game currency for buying and selling items
        self.backpack = {}   # A dictionary to store your items (like an inventory)

    def show_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Energy: {self.energy}")
        print(f"Gold: {self.gold}G")  # 'G' stands for gold, our game's currency

    # ASSIGNMENT 2 HINT: Upgrade Your Backpack
    # Add methods here to:
    # - Put items in your backpack
    # - Take items out of your backpack
    # - Show what's in your backpack
    # For example:
    # def add_to_backpack(self, item_name, amount):
    #     # Your code here to add items

class Crop:
    def __init__(self, name, growth_time, sell_price):
        self.name = name                # The name of the crop (e.g., "Parsnip")
        self.growth_time = growth_time  # How many days it takes to grow
        self.sell_price = sell_price    # How much gold you get when you sell it
        self.current_stage = 0          # Keeps track of the crop's growth progress

    def grow(self):
        if self.current_stage < self.growth_time:
            self.current_stage += 1

    def is_ready(self):
        return self.current_stage >= self.growth_time

    # ASSIGNMENT 3 HINT: Add Weather Effects
    # Change the grow method to account for weather
    # For example:
    # def grow(self, weather):
    #     if weather == "sunny":
    #         # Grow faster in the sun
    #     elif weather == "rainy":
    #         # Grow slower in the rain

class Farm:
    def __init__(self, size):
        self.size = size
        self.plots = [[None for _ in range(size)] for _ in range(size)]  # Creates a 2D list to represent the farm

    def show(self):
        print("\nYour Farm:")
        for row in self.plots:
            print(" ".join(["[ ]" if plot is None else "[P]" for plot in row]))  # [ ] for empty, [P] for planted

# ASSIGNMENT 4 HINT: Create Pierre's General Store
# Create a new Store class here
# class Store:
#     def __init__(self):
#         self.seed_prices = {
#             "parsnip": 20,
#             "cauliflower": 80,
#             "potato": 50,
#             # Add your new crop here too!
#         }
#
#     def show_seeds(self):
#         # Your code to display available seeds and their prices
#
#     def sell_seed(self, farmer, seed_type):
#         # Your code to handle seed purchase

class Game:
    def __init__(self):
        self.farmer = None  # We'll create the farmer when the game starts
        self.farm = Farm(5) # Create a 5x5 farm grid
        self.day = 1        # Start on day 1
        self.season = "spring"  # Start in spring, like many farming games!
        self.crops = {
            "parsnip": Crop("Parsnip", 4, 35),
            "cauliflower": Crop("Cauliflower", 12, 175),
            "potato": Crop("Potato", 6, 80)
        }
        # ASSIGNMENT 1 HINT: Add a New Crop
        # Add your new crop type here, like this:
        # "strawberry": Crop("Strawberry", 8, 120),

        # ASSIGNMENT 3 HINT: Add Weather Effects
        # Add a weather attribute here
        # self.weather = "sunny"  # Default weather

        # ASSIGNMENT 4 HINT: Create Pierre's General Store
        # Initialize the store here
        # self.store = Store()

    def start_game(self):
        name = input("Enter your farmer's name: ")
        self.farmer = Farmer(name)
        print(f"Welcome to Python Valley, {self.farmer.name}!")

    def plant_crop(self):
        print("\nSeeds you can plant:")
        for crop_name, crop in self.crops.items():
            print(f"{crop_name.capitalize()}: Takes {crop.growth_time} days to grow, sells for {crop.sell_price}G")

        crop_choice = input("What do you want to plant? ").lower()
        if crop_choice not in self.crops:
            print("Oops! We don't have those seeds. Try again.")
            return

        # ASSIGNMENT 4 HINT: Create Pierre's General Store
        # Check if the farmer has the seed in their backpack
        # If not, tell them they need to buy it from Pierre's store

        row = int(input("Which row? (0-4): "))
        col = int(input("Which column? (0-4): "))

        if self.farm.plots[row][col] is not None:
            print("There's already a plant here! Try another spot.")
            return

        if self.farmer.energy < 10:
            print("You're too tired to plant. Get some sleep!")
            return

        self.farm.plots[row][col] = self.crops[crop_choice]
        self.farmer.energy -= 10
        print(f"You planted {crop_choice}!")

    def harvest_crop(self):
        row = int(input("Which row? (0-4): "))
        col = int(input("Which column? (0-4): "))

        if self.farm.plots[row][col] is None:
            print("There's no plant here to harvest!")
            return

        crop = self.farm.plots[row][col]
        if not crop.is_ready():
            print("This crop isn't ready yet. Give it some time!")
            return

        # ASSIGNMENT 2 HINT: Upgrade Your Backpack
        # Instead of selling right away, add the crop to the farmer's backpack
        # self.farmer.add_to_backpack(crop.name, 1)
        # print(f"You harvested {crop.name} and put it in your backpack!")

        self.farmer.gold += crop.sell_price
        self.farmer.energy -= 5
        print(f"You harvested {crop.name} and got {crop.sell_price}G!")
        self.farm.plots[row][col] = None

    # ASSIGNMENT 2 HINT: Upgrade Your Backpack
    # Add a new method here to sell crops from the backpack
    # def sell_crops(self):
    #     # Show backpack contents
    #     # Ask which crop to sell
    #     # Remove from backpack and add gold to farmer

    def sleep(self):
        self.day += 1
        self.farmer.energy = 100  # Full energy after sleeping

        # ASSIGNMENT 3 HINT: Add Weather Effects
        # Add code here to randomly change the weather each day
        # self.weather = random.choice(["sunny", "rainy", "windy"])
        # print(f"Today's weather: {self.weather}")

        for row in self.farm.plots:
            for crop in row:
                if crop is not None:
                    crop.grow()
                    # If you've added weather effects, use:
                    # crop.grow(self.weather)
                    if crop.is_ready():
                        print(f"Your {crop.name} is ready to harvest!")

    # ASSIGNMENT 4 HINT: Create Pierre's General Store
    # Add a new method here to visit the store
    # def visit_store(self):
    #     self.store.show_seeds()
    #     seed_choice = input("Which seeds do you want to buy? ")
    #     self.store.sell_seed(self.farmer, seed_choice)

    def play(self):
        self.start_game()
        while True:
            print(f"\nDay {self.day} of {self.season}")
            self.farmer.show_status()
            self.farm.show()

            action = input("\nWhat do you want to do? (plant/harvest/sleep/quit): ").lower()

            if action == "plant":
                self.plant_crop()
            elif action == "harvest":
                self.harvest_crop()
            elif action == "sleep":
                self.sleep()
            # ASSIGNMENT 2 HINT: Upgrade Your Backpack
            # Add a new option here for "sell" action
            # ASSIGNMENT 4 HINT: Create Pierre's General Store
            # Add a new option here for "store" action
            elif action == "quit":
                print("Thanks for playing Python Valley!")
                break
            else:
                print("I don't understand. Try again!")

if __name__ == "__main__":
    game = Game()
    game.play()
