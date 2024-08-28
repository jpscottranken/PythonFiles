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

from randomNumberProcessor import RandomNumberProcessor

class RandomNumberApp:
  def run(self):
    # Initialization. Instantiate the RandomNumberProcessor
    # class. Call the instantiated object rnProcessor.
    rnProcessor = RandomNumberProcessor(25, 0, 100)

    # Call method to remove randomNumbers.txt, zero.txt,
    # evens.txt, and odds.txt if indeed any of these exist.
    rnProcessor.removeOutputFiles()

    # Generate 25 random numbers, each between 0 - 100.
    rnProcessor.generateRandomNumbers()

    # Save the 25 generated random numbers to
    # a text file names randomNumbers.txt
    rnProcessor.saveRandomNumbersToFile("randomNumbers.txt")

    
    rnProcessor.processRandomNumbers("randomNumbers.txt")

    rnProcessor.displayFileContents(["zero.txt", "evens.txt", "odds.txt"])

if (__name__ == "__main__"):
  app = RandomNumberApp()
  app.run()