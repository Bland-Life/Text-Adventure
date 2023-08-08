# Text Adventure
 Uses tkinter to create a simple text adventure application.

## Story Text File

There a some simple rules to creating a story text file.

- To tell the program that a decision is coming up, on one line type [CHOOSE]
- IMMEDIATELY AFTER THAT LINE add your options, they must be capitalized and separated by a space and a comma like so: LEFT, RIGHT, UP, DOWN
- To create the block for each option
    1. START with a vertical bar followed by the option name, capitalized, like so: |LEFT
    2. IN BETWEEN add your text, and the next set of options if you need more.
    3. END the block with a minus symbol - this will tell the program that your game has ended if there are no options in between. If there are options, no worries, it'll be ignored by the program until it reaches the appropriate block.

To see an example, check out the story.txt that should be saved in this repository.