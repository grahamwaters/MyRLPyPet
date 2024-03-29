# MyRLPyPet
Reinforcement Learning Applied to digital pet behaviors.

## Introduction

The idea behind this project is quite simple. I want a digital pet. We love animals because they love us seemingly unconditionally. They also are cute because they act in ways that we find endearing. Using reinforcement learning and some machine learning modeling I would like to create a digital twin of a pet that I can interact with and that will act in ways that I find endearing. I will model the pet on my teacup Yorkie "Annie" and assign behaviors as a baseline that she exhibits. I will then use reinforcement learning to train the pet to behave (and misbehave) like a real pet would.

# Digital Twin of a Pet
The digital twin of a pet is a computer-generated version of a real-life animal. It is designed to mimic the behavior and characteristics of the pet it is modeled on. By using reinforcement learning, the digital twin can be trained to behave like the real pet, making it a virtual representation of the animal.

# Logical Steps in Development

To create a digital twin of a pet using reinforcement learning, the following steps are typically involved:

Collect data on the real pet's behavior and characteristics. This can include observing the pet's actions, taking measurements of its physical features, and recording its vocalizations and other sounds.

Create a digital model of the pet using a computer graphics program or other software. This model should be as realistic and detailed as possible, including the pet's appearance, movements, and sounds.

Develop a reinforcement learning algorithm that can be used to train the digital pet. This algorithm should be able to take in data on the pet's behavior and use it to adjust the digital pet's actions and characteristics in real-time.

Use the collected data and the reinforcement learning algorithm to train the digital pet. This can involve providing the digital pet with rewards for behaving in certain ways and punishments for behaving in other ways. The algorithm should be able to learn from this feedback and adjust the digital pet's behavior accordingly.

Test the trained digital pet to ensure that it behaves like the real pet it is modeled on. This can involve interacting with the digital pet and observing its behavior in various scenarios.

Refine the digital pet's behavior and characteristics as needed based on the results of the testing. This can involve adjusting the reinforcement learning algorithm, collecting more data on the real pet, or making changes to the digital pet's model.

Once the digital pet is behaving satisfactorily, it can be made available for others to interact with and enjoy. This can involve creating a virtual environment for the digital pet to live in, or providing a user interface for interacting with the digital pet.

# A Basic Digital Pet Class

```python

class pypet:
    # This is the basic class for a digital pet.
    # It will be used to create a digital twin of my teacup Yorkie "Annie"
    def __init__(self):
        self.name = 'Annie'
        self.age = 0
        self.hunger = 0
        self.hungry = False # is the pet hungry?
        self.thirst = 0
        self.thirsty = False # is the pet thirsty?
        self.happiness = 100 # 100% happy
        self.health = 100 # 100% healthy
        self.energy = 100 # 100% energy
        self.weight = 5 # 5 lbs
        self.height = 5 # 5 inches
        self.breed = 'Yorkie'

    def feed(self): # feed the pet
        self.hunger = self.hunger - 10 # subtract ten hunger points when fed
        self.thirst = self.thirst + 5 # add thirst from eating
        self.happiness = self.happiness + 10 # add happiness from eating
        self.health = self.health + 10 # add health from eating
        self.energy = self.energy + 10 # add energy from eating
        self.weight = self.weight + 1 # add weight for eating
        if self.hunger < 50: # if hunger is less than 50, pet is not hungry
            self.hungry = False
        else:
            self.hungry = True

    def give_water(self): # give the pet water
        self.thirst = self.thirst - 10 # subtract thirst when watered
        self.hunger = self.hunger + 5 # add hunger from drinking
        self.happiness = self.happiness + 10 # add happiness from drinking
        self.health = self.health + 10 # add health from drinking
        self.energy = self.energy + 10 # add energy from drinking
        self.weight = self.weight + 1 # add weight for drinking
        if self.thirst < 50: # if thirst is less than 50, pet is not thirsty
            self.thirsty = False
        else:
            self.thirsty = True

    def play(self): # play with the pet
        self.happiness = self.happiness + 10 # add happiness from playing
        self.health = self.health + 10 # add health from playing
        self.energy = self.energy - 10 # subtract energy from playing
        self.weight = self.weight - 1 # subtract weight for playing

    def sleep(self): # put the pet to sleep
        self.happiness = self.happiness + 10 # add happiness from sleeping
        self.health = self.health + 10 # add health from sleeping
        self.energy = self.energy + 10 # add energy from sleeping
        self.weight = self.weight - 1 # subtract weight for sleeping

    def walk(self): # take the pet for a walk
        self.happiness = self.happiness + 10 # add happiness from walking
        self.health = self.health + 10 # add health from walking
        self.energy = self.energy - 10 # subtract energy from walking
        self.weight = self.weight - 1 # subtract weight for walking

    def groom(self): # groom the pet
        self.happiness = self.happiness + random.randint(-1, 1) # add happiness from grooming (randomly +/- 1) Annie may or may not like grooming. She is a Yorkie.
        self.health = self.health + 4 # add health from grooming
        self.energy = self.energy + random.randint(-3, 3) # vary energy from grooming.
        self.weight = self.weight - 1 # subtract weight for grooming because hair is removed

    def vet(self): # take the pet to the vet
        self.happiness = self.happiness - 10 # subtract happiness from vet visit
        self.health = self.health + 10 # add health from vet visit
        self.energy = self.energy - 2 # subtract energy from vet visit

    def use_the_facilities(self): # pet poops
        # pet can only poop if it has eaten in the last 24 hours
        if self.hungry is not True: # if the pet is hungry then it will not poop. It will only poop if it is not hungry.
            self.hunger = self.hunger + 10 # add hunger from pooping
            self.thirst = self.thirst + 5 # add thirst from pooping
            self.happiness = self.happiness + random.randint(-1, 3) # could be happy or sad about pooping
            self.health = self.health - 10 # subtract health from pooping
            self.energy = self.energy - 10 # subtract energy from pooping
            self.weight = self.weight - 1 # subtract weight for pooping
        else:
            self.hunger = self.hunger + 10 # add hunger from pooping
            self.thirst = self.thirst + 5 # add thirst from pooping

        # thirst and peeing
        if self.thirsty is not True: # if the pet is thirsty then it will not pee. It will only pee if it is not thirsty.
            self.thirst = self.thirst + 10 # add thirst from peeing
            self.happiness = self.happiness + random.randint(-1, 3) # could be happy or sad about peeing
            self.weight = self.weight - 1 # subtract weight for peeing




```