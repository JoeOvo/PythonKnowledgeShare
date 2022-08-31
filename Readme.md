This is the repository that I used to run a knowledge share about python. 
Briony said it might be useful to be able to play about with it, so here it is. 

# Set up 

1. clone this repo. 
2. create a new venv
3. install the requirements. (if you can't remember the syntax for this, try googling, and then feel fee to ask me)

# Debugging

The script `2_debugging.py` doesn't work. 
There are 4 problems with it, see if you can figure them out. 

# Error handling

1. Once you have the script running, you could then try changing line 46 to open the file 
   `prices2` rather than `prices`. Prices2 has some malformed data, which will
   cause the script to break. Can you add some try-catch statements so that it works correctly?
2. Can you add some validation to check that the opened csv has the expected number of
   columns, with the expected data types? How are you going to handle the column headings?