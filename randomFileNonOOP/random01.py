'''
	Create a non-Object-Oriented Python console program that does the following:
	
	0.	If the file(s) zero.txt, positive.txt, and/or negative.txt
		  currently exist, delete them at the start of the program.
	1.	Generates 25 random numbers between  0 - 100.
	2.	Saves the numbers to a text file.
	3.	Lets the user read the text file and calculate the following:
		  a.	The number of times 0 is the random number.
			    If 0 is generated, create a Python print
			    statement that says: "0 is not odd or even."
			    and add 1 to a "zeroCounter".
		  b.  If the number generated is not 0, modulo the number by 2.
		  b1. If the remainder is 0, create a Python print
			    statment that says: f"The number {number} is even."
			    and add 1 to a "evenCounter".
		  b2. If the remainder is not 0, create a Python print
			    statment that says: f"The number {number} is odd."
			    and add 1 to a "oddCounter".
		  c.  Write out the number of each (0, even, or odd)
			    number into a file (0 to zero.txt, even numbers to
			    evens.txt, odd number to odds.txt) and if the
			    number is odd or even, write the number out
			    to the respective file as well.
		  d.	At the end of the program, read and then write out the
			    contents of zero.txt, evens.txt, and odds.txt.
		  e.	If there is nothing in the zero.txt file (i.e. no 0s
			    were randomly generated), state this in zero.txt
'''

# https://www.w3schools.com/python/python_ref_file.asp
import os
import random

# Declare the counters as global variables
'''
zeroCount  = 0
evensCount = 0
oddsCount  = 0
'''

def main():
  # Remove file randomNumbers.txt if it currently exists.
  #removeExistingFile("randomNumbers.txt")

  # Remove file zero.txt if it currently exists.
  #removeExistingFile("zero.txt")

  # Remove file evens.txt if it currently exists.
  #removeExistingFile("evens.txt")

  # Remove file odds.txt if it currently exists.
  #removeExistingFile("odds.txt")

  # Remove randomNumbers.txt, zero.txt, evens.txt,
  # and odds.txt if they currently exist.
  removeOutputFiles(["randomNumbers.txt", "zero.txt", "evens.txt", "odds.txt"])

  # Generate 25 new random numbers, each
  # between 0 - 100.
  randomNumbers = generateRandomNumbers(25, 0, 100)

  # Save the 25 generated random numbers
  # to a text file called randomNumbers.txt
  saveRandomNumbersToFile("randomNumbers.txt", randomNumbers)

  # Call processNumbers, passing in the file
  # randomNumbers.txt As we process this file,
  # update zeroCount or evensCount or oddsCount
  # for each number in the randomNumbers.txt file.
  zeroCount, evensCount, oddsCount = processNumbers("randomNumbers.txt")

  # Call displayFileContents to display the contents
  # of the zero.txt, evens.txt, and odds.txt files.
  displayFileContents(["zero.txt", "evens.txt", "odds.txt"])

# Remove the zero.txt, evens.txt, odds.txt,
# and randomNumbers.txt files if they currently 
# exist.
# 
# This will guarantee that each file will contain 
# only the numbers from the current program run.
'''
def removeExistingFile(filename):
  if (os.path.exists(filename)):
    os.remove(filename)
    print(f"\nThe file {filename} has been removed")
  else: 
    print(f"\nCannot delete file {filename} as it does not exist.")
'''

def removeOutputFiles(filenames):
  for filename in filenames:
    if (os.path.exists(filename)):
      os.remove(filename)
      print(f"\nThe file {filename} has been removed")
    else: 
      print(f"\nCannot delete file {filename} as it does not exist.")

# This method will generate 25 (count) random numbers
# between 0 (lBound) and 100 (uBound).
def generateRandomNumbers(count, lBound, uBound):
  return [random.randint(lBound, uBound) for _ in range(count) ]

# This method will save the generated 25 random
# numbers to a file.
def saveRandomNumbersToFile(filename, numbers):
  print("")
  with open(filename, "w") as f:
    for number in numbers:
      f.write(f"{number}\n")

# This method will process the random number file.
def processNumbers(filename):
  #global zeroCount, evensCount, oddsCount
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
    
    # Print out final totals
    if (zeroCount > 0):                   # Generated 1 or > 0s
      zeroFile.write(f"Total zeros: {zeroCount}")
    else:                                 # No 0s generated
      zeroFile.write(f"No 0s were generated.")
    
    if (evensCount > 0):                  # Generated 1 or > even numbers
      evensFile.write(f"Total evens: {evensCount}")
    else:                                 # No even numbers generated
      evensFile.write(f"No even numbers were generated.")
    
    if (oddsCount > 0):                   # Generated 1 or > odd  numbers
      oddsFile.write(f"Total odds:  {oddsCount}")
    else:                                 # No odd numbers generated
      oddsFile.write(f"No odd  numbers were generated.")
    
    return zeroCount, evensCount, oddsCount

# This method will display the contents of
# the zero.txt, evens.txt, and odds.txt files.
def displayFileContents(filenames):
  for filename in filenames:
    print(f"\nThe Contents Of File: {filename}: ")
    with open(filename, "r") as f:
      print(f.read())

if (__name__ == "__main__"):
  main()