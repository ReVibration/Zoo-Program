# PIM_test_Bartek_Siwak
# Simple Zoo Simulator - This is the simple zoo simulator that has three types
# of animals where five of each exist.
#
# @author Bartek Siwak
# @version 0.1

# IMPORTS
import random #This import allows the program to get random numbers

# Simulation - This class is responsible for runing the actual program also it will
# update each animal when an action occurs
#
# @author Bartek Siwak
# @version 0.1

class Simulation:

    #__init__ - This is the constructor for the simulation class where variables are declared
    
    def __init__(self):

        
        self.animals = [] # This list holds all of the animal objects in the zoo

        self.timeElapsed = 0 # This holds the amount of time that occured in the zoo
        self.giraffeFood = 0 # These food variables will be the amounts that the animals
        self.monkeyFood = 0 # will be fed
        self.elephantFood = 0

    # createAnimals - This method will create the instances of the different animals
    #
    #@param numberOfEach - This is the number of animals created
    #@param typeOfAnimal - This holds the type of animals that need to be created  
    def createAnimals(self,numberOfEach,typeOfAnimal):

        # GIRAFFE CREATION
        if(typeOfAnimal == "giraffe"): # This checks what type of animal that needs to be created 
            for i in range(numberOfEach): # This loops though the creation program depending on the amount needed
                _tempAnimal = giraffe(i+1) # This creates a temporary variable to hold the animals created
                self.animals.append(_tempAnimal) # This adds the animal to the list of animals objects 

        # MONKEY CREATION    
        elif(typeOfAnimal == "monkey"):
            for i in range(numberOfEach):
                _tempAnimal = monkey(i+1)
                self.animals.append(_tempAnimal)

        # ELEPHANT CREATION        
        elif(typeOfAnimal == "elephant"):
            for i in range(numberOfEach):
                _tempAnimal = elephant(i+1)
                self.animals.append(_tempAnimal)

    # feed - This method will feed each animal also it will check whether the animal is above its health cap   
    def feed(self):

        #FOOD CREATION
        giraffeFood = random.uniform(10.0,25.0) # This creates the needed food for each animals type randomly
        elephantFood = random.uniform(10.0,25.0)
        monkeyFood = random.uniform(10.0,25.0)

        #FEEDING ANIMALS
        for i in self.animals: # This will loop through all of the animals
            if(i.species == "Giraffe"): # This checks for the type of animal
                i.health = i.health + giraffeFood # This gives the correct food amount to the animal
            elif(i.species == "Monkey"):
                i.health = i.health + monkeyFood
            elif(i.species == "Elephant"):
                i.health = i.health + elephantFood
                
            i.healthCheckCap() # This will check whether the animal has reached over its limit

    # start - This method will start the simulation and manage the actions
    def start(self):

        #ANIMAL CREATION
        self.createAnimals(5,"giraffe")# Run the method above to generate the correct animals and amounts
        self.createAnimals(5,"monkey")
        self.createAnimals(5,"elephant")        

        #WELCOME SIGN
        print("A Big Warm Welcome to Pay Monthly Zoo") # Print a nice welcome sign to the zoo

        #SIMULATION LOOP
        while True: # This will run forever untill killed

            #TIME CHECK
            print("The zoo has been open for: {} hours".format(self.timeElapsed)) # Print the amount of time elapsed

            # CHECKING ANIMAL HEALTH
            for i in self.animals: # Loop through all of the animals 
                i.healthCheckDead() # Check is the animal is dead
                if(i.health == 0): # If the animal is dead
                    self.animals.remove(i) # Remove the animal from the list
                    
                # ERROR HANDLING        
                if(i.health > 0): # This ensures that the animal is alive before printing to the screen
                    print("{} {} and it's health is {}".format(i.name,i.species,i.health)) # Print the animal to the screen       
                
            # USER INPUT    
            feed = input("Would you like to feed the animals? yes or no ").lower() # Ask the user to feed the animals 

            # HANDLE USER INPUT
            if(feed == "yes"): # If the answer is yes
                self.timeElapsed = self.timeElapsed + 1 # Add another hour to the clock
                self.feed() # Run the feed the animals method                   
            else:
                self.timeElapsed = self.timeElapsed + 1 # Add another hour to the clock
                for i in self.animals: # Loop thorugh the animals 
                    i.timePass() # Decrease animal health

#Animals - This class will be inherted by all of the animal classes to
# ensure that they are following the correct behaviour
#
# @author Bartek Siwak
# @version 0.1

class animals:

    # __init__ - This will initialise each each child of this class and inhert it's methods
    #
    #@param species - This is the type of animal that is being made
    #@param health - This is the amount of health that the animals has
    #@param name - This is the name of the animal usually its the number
    #@param minimumPercent - This is the minimum percentage of health that the animal can be
    #@param canWalk(OPTIONAL) - This is for the elephant to check whether it can walk
    def __init__(self,species,name,minimumPercent,canWalk = None):
        
        self.name = name
        self.health = 100.0 # This is a 100 to simulate a 100% health at the start
        self.species = species
        self.minimumPercent = minimumPercent
        self.canWalk = canWalk
        
    # timePass - This method deducts health from an animal using a random percentage
    def timePass(self):
        self.percentage = random.uniform(0.0,20.0) # Create the random percentage 
        self.health = self.health - self.percentage # Deduct that percentage from the health

    # healthCheckCap - This method will ensure that the animals cannot go above 100%
    def healthCheckCap(self):
        if(self.health >= 100.0): # Check whether health is above 100%
            self.health = 100.0 # If so chnage the health back to a 100%

    # healthCheckDead - This method will check whether an animal is dead or not and has a
    # specific function for the elephant
    def healthCheckDead(self):

        # ELEPHANT EXCEPTION
        if(self.species == "Elephant"): # This will check whether the animal is an elephant
            if(self.health < self.minimumPercent and self.canWalk == False): # Then it will check whether the elephant can't walk and is under the 70%
                self.health = 0 # If so kill the elephant
                print("{} {} has died".format(self.name,self.species)) # Print that the elephant has died
            elif self.health < self.minimumPercent: # Check whether the elephant is under the 70%
                self.canWalk = False # If so the elephant doesn't have the ability to walk
                print("{} {} can't walk and will die if not fed".format(self.name,self.species)) # Print that the elephant will die if not fed
            elif self.health > self.minimumPercent: # Check whether the elephant is above 70%
                self.canWalk = True # If so the elephant can walk
            
        # ANIMAL DEATH
        elif(self.health < self.minimumPercent): # This will check whether the animal is below its required percentage
                self.health = 0 # if so kill the animal
                print("{} {} has died".format(self.name,self.species)) # print that the animal has died
    

# Giraffe - This class is responsible for the giraffe animals attributes
#
# @author Bartek Siwak
# @version 0.1
class giraffe(animals):

    # __init__ - This initalises the giraffe object and its attributes
    #
    #@param i - This is the girrafe's name
    def __init__(self,i):
        
        species = "Giraffe" # This is the species of the giraffe
        self.name = i # this sets the name
        minimumPercent = 50.0 # this set the minimum health percentage
        super().__init__(species,i,minimumPercent) # This uses the super command to access the giraffe's parent class
    
# Monkey - This class is responsible for the monkey animals attributes
#
# @author Bartek Siwak
# @version 0.1
class monkey(animals):

    # __init__ - This initalises the monkey object and its attributes
    #
    #@param i - This is the monkey's name
    def __init__(self,i):
        species = "Monkey" # This is the species of the monkey
        self.name = i # this sets the name
        minimumPercent = 30.0 # this set the minimum health percentage
        super().__init__(species,i,minimumPercent) # This uses the super command to access the monkey's parent class

# Elephant - This class is responsible for the elephant animals attributes
#
# @author Bartek Siwak
# @version 0.1
class elephant(animals):

    # __init__ - This initalises the elephant object and its attributes
    #
    #@param i - This is the elephant's name
    def __init__(self,i):
        species = "Elephant" # This is the species of the elephant
        self.name = i # this sets the name
        minimumPercent = 70.0 # this set the minimum health percentage
        canWalk = True # this ensures that at the start the elephant can walk
        super().__init__(species,i,minimumPercent,canWalk) # This uses the super command to access the elephant's parent class with the optional walk variable

        
#RUNNING THE PROGRAM
sim = Simulation() # Create a new simulation object and call it sim
sim.start() # Call the start method from the simulation
    


