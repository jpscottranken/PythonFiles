import os
import random

class RandomNumberProcessor:
  # Constructor
  def __init__(self, count = 25, lBound = 0, uBound = 100):
    self.count    = count     # How many random numbers are generated
    self.lBound   = lBound    # Lower bound for the random numbers
    self.uBound   = uBound    # Upper bound for the random numbers
    self.numbers  = []        # List that holds the random numbers
  
  # This method will remove the program output files
  # if these files do indeed exist.
  def removeOutputFiles(self):
    files = ["randomNumbers.txt", "zero.txt", "evens.txt", "odds.txt"]
    for file in files:
      if (os.path.exists(file)):
        os.remove(file)
        print(f"\nThe file {file} has been removed")
      else: 
        print(f"\nCannot delete file {file} as it does not exist.")

  # This method will generate 25 (count) random numbers
  # between 0 (lBound) and 100 (uBound).
  def generateRandomNumbers(self):
    self.numbers = [random.randint(self.lBound, self.uBound) for _ in range(self.count)]
    return self.numbers
  
  # This method will save the generated 25 random
  # numbers to a file.
  def saveRandomNumbersToFile(self, filename = "randomNumbers.txt"):
    print("")
    with open(filename, "w") as f:
      for number in self.numbers:
        f.write(f"{number}\n")
  
  # This method will process the random number file.
  # It will figure out how many 0s were generated,
  # how many even numbers were generated, and how
  # many odd numbers were generated.
  def processRandomNumbers(self, filename = "randomNumbers.txt"):
    # Set each counter to 0
    zeroCount  = 0
    evensCount = 0
    oddsCount  = 0

    # Open the file randomNumbers.txt with the 25 random 
    # numbers in read mode.
    with open(filename, "r") as f:
      numbers = [int(line.strip()) for line in f]
    
    # Open the zero.txt, evens.txt, and 
    # odds.txt files in write mode
    with open("zero.txt",  "w") as zeroFile, \
        open("evens.txt", "w") as evensFile, \
        open("odds.txt",  "w") as oddsFile:
      
      # Iterate through the 25 numbers in the file
      # randomNumbers.txt
      #
      # If the numbers is 0, print the message and
      # update the zeroCount counter.
      #
      # If the numbers is even, print the message and
      # update the evensCount counter.
      #
      # If the numbers is odd, print the message and
      # update the oddsCount counter.
      for number in numbers:
        if (number == 0):                   # Zero (0) check
          print ("0 is not odd or even.")
          # Increment zeroCount counter
          zeroCount += 1
        elif (number % 2 == 0):             # Even number check
          print(f"The number {number} is even.")
          # Write the number out to evens.txt
          evensFile.write(f"{number}\n")
          # Increment evensCount counter
          evensCount += 1
        else:                               # Odd  number check
          print(f"The number {number} is odd.")
          # Write the number out to odds.txt
          oddsFile.write(f"{number}\n")
          # Increment oddsCount counter
          oddsCount += 1
    
      if (zeroCount == 0):
        zeroFile.write(f"No 0s were generated\n")

  # This method will display the contents of
  # the zero.txt, evens.txt, and odds.txt files.
  def displayFileContents(self, filenames = ["zero.txt", "evens.txt", "odds.txt"]):
    for filename in filenames:
      print(f"\nThe Contents Of File {filename} Are: ")
      if (os.path.exists(filename)):
        with open(filename, "r") as file:
          contents = file.read().strip()
          if (contents):
            print(contents)
          else:
            print(f"File Name: {filename} Is Empty.")
      else:
        print(f"File Name: {filename} Does Not Exist.")
    
      print("")
