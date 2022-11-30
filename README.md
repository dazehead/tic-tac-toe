# TIC-TAC-TOE Terminal Game
## My first python project as part of CS 101 on codecademy
This is a 2 player tic tac toe game that utilizes
* classes
* lists
* dictionary

The game itself was reletively simple to make; however, I did have an issue finding a way to interact with the Player class for ending the game. I eventually found it was a simple syntax error. Another challenge was refactoring the code for accidential/intentional player input errors.

The majority of the work was done using the JUNO app when I was not at home so I did not get to keep track of my commits using git like I wanted to.

# Feedback
1. I would like some feedback on how someone would code this using decorators as I feel the majority of the functions use other functions continually. 
2. I also feel like I passed in a lot of class objects to these functions and some of them might be redundant.
3. How to better improve the `display_board` function
    * As it is now the `display_board` displays on the terminal as a list I would have liked to have made that function so it does not display `['-', '-', '-']` this way and instead displayed `[  -    -    -  ]` I attempted a couple of `for` loops but my only idea would have been to convert each list item to a string and have it display on the terminal. 
    * I do plan on implementing tkinter GUI as a part of this code for a later date

You can find this repository on my [GitHub](https://github.com/dazehead)