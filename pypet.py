
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
