#take an input file
#two integers are left and right margins in inches, string must stay in between
#12 char = 1 inch
#print 0-9 to 80 to layout the grid to measure when testing
from __future__ import print_function #allows python 3 print


def createGrid(): # prints grid
  for x in range(8): # counts to 10, 8 times
     n = 1
     while(n<10): 
       print (n, end="")
       n += 1
     print("0",end="")
  print ("")

def createIndent(l):
  for s in range(l):
    print(" ", end="") # indent the number of spaces for the left margin

    
def Text():
  # input margins for the text
  left = input("Insert left margin: ")
  right = input("Insert right margin: ")
  #must have at least 10 characters of text
  if 80 - left - right < 10:
    print("Margins are too small.")
    return 0

  # line is composed of 30 characters
  endsAt = 80 - right
  startsAt = left
  textMargin = 80 - left - right
  # print("Text margin is: ", textMargin)

  # replace file with string
  word = ""
  file = raw_input("Insert the text file: ")
  fi = open(file, "r") # set the file to read
  f = fi.read() # open its contents
  createGrid()
  createIndent(left)
  count = 0 # character count to determine if in boundaries
  with open(file) as f:
    st = f.readline()
    while st:
      for ch in st:
        if ch != " ": #letter means that it's pard of a word
          word += ch
        else:
          count += len(word)
          if count > textMargin: # word would be out of bounds
            # print("The count is: ", count, " and the word is: ", word)
            count = len(word) # include the count of the new word
            # print("The new count is: ", count)
            print(" ") # create a new line
            createIndent(left) 
            print(word, end=" ")
          else:
            print(word, end=" ")
          count += 1 # add the space
          word = "" 
      # print("The count is: ", count, " and the word is: ", word)
      st = f.readline() #essentially restart for new line
      # dealing with the last word of a line since it doesn't end with a space
      if count + len(word) > textMargin: # word would be out of bounds
        print(" ") # create a new line
        createIndent(left) 
        print(word, end="")
      else:
        print(word, end="")
        
      word = ""
      createIndent(left)
      count = 0
      # print("   End of line")
    print(word) # last word won't be printed yet
  
Text()