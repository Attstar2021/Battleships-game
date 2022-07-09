# My Battleships game!
This is a logical game written mainly in python language. A short yet very interesting game can be played in Heroku mock terminal. 
please click on https://my-battleships-game.herokuapp.com/ to play this game.

<img width="958" alt="image" src="https://user-images.githubusercontent.com/91749477/178085049-bfaa7474-2d70-4de9-bdc0-198837403ffe.png">


This simple game was created for entertainment. The logic for the game was built using python language. The target audience for this website is users who would like to avail of a quick, simple game of battleship. It has an old navel-style message which will take you to memories of old-time wars.


<img width="630" alt="image" src="https://user-images.githubusercontent.com/91749477/178085438-ff0eee9a-4664-42c0-b60e-e5e01a3d26df.png">

# Feature

### The below outlines key features of the game.

#### Welcome Screen

user is welcomed by an initial message.


<img width="597" alt="image" src="https://user-images.githubusercontent.com/91749477/178088845-344b8fd5-b835-4aa1-9878-d7ef6a4209a4.png">


#### Name Input

User is required to input their name in order to commence the game. The input of the name is used to personalise the welcome message to the user.


<img width="677" alt="image" src="https://user-images.githubusercontent.com/91749477/178088940-f5376977-780d-472f-bed8-a6a0043cdfe8.png">


#### Key selection

in this game, you need to select an alphabet from a row and number from a column which is essential to place a shot on the board and for your convenience, you don't need to worry about typing in upper case just play!


<img width="677" alt="image" src="https://user-images.githubusercontent.com/91749477/178089095-0b413352-e780-4f36-8c24-f5333d4865b6.png">



It is fairly responsive and can be played on all devices.


<img width="924" alt="image" src="https://user-images.githubusercontent.com/91749477/178085937-70150757-39f2-450d-be33-0e32d8d478e8.png">


## How to play.
It is a mini single-player game more similar like Battleship Solitaire game. In this game player guess a computer's battleship and shot it down.
It is program in

The Battleships game is played on grids. The locations of the fleets are concealed from the other player, (In my game it is a computer ship hidden from players) Players call shots at the computer's fleet, and the objective of the game is to destroy the computer's fleet.
The application provides a working battleships game for a single user to play against the computer and it has a set grid size and also it warns the user if his guess if off-grid

Here are the images for test case of this game!

### This game will let you know your progress throughout the play:

borad will update you about what is happening and how much fire remain and if you hit or miss here are the examples;

#### When you missed:


<img width="589" alt="image" src="https://user-images.githubusercontent.com/91749477/178085091-feb88832-5517-4261-a106-445ed9e339f2.png">



#### When you shot on same place:


<img width="592" alt="image" src="https://user-images.githubusercontent.com/91749477/178085148-5bcb83f6-753f-40c5-9400-efecacf53775.png">



#### When you hit a part of ship:


<img width="625" alt="image" src="https://user-images.githubusercontent.com/91749477/178085416-a2ac048f-8221-4743-b12f-53bce1b544d6.png">



#### When you sunk the whole ship:


<img width="630" alt="image" src="https://user-images.githubusercontent.com/91749477/178085438-ff0eee9a-4664-42c0-b60e-e5e01a3d26df.png">



#### When you sunk all ships:


<img width="655" alt="image" src="https://user-images.githubusercontent.com/91749477/178085470-32f9d6b0-2e23-4158-b928-89c383fdf4d5.png">



#### When you run out of shots:


<img width="621" alt="image" src="https://user-images.githubusercontent.com/91749477/178085510-9bd947f9-1997-4dcb-95ba-655b1ce1e897.png">




### Out of range example

This is an easy and user-friendly game. if you add an input which is not listed on the board it will show an error message and guide you to a pattern decided by the programmer.  Error messages are short and easy to understand and give you different examples to help you understand.

#### out of range example 1:


<img width="620" alt="image" src="https://user-images.githubusercontent.com/91749477/178085237-38bdfb83-4e3f-4e8d-84b0-0beeeee84ce1.png">



#### out of range example 2 with single alphabet:


<img width="650" alt="image" src="https://user-images.githubusercontent.com/91749477/178085400-02db036a-a21f-4177-ad25-5ec5ab8995fe.png">



#### out of range example 3 with single number:


<img width="619" alt="image" src="https://user-images.githubusercontent.com/91749477/178085286-1bf3b319-69ea-4d2d-890d-b76449cb548a.png">



#### out of range example 4 with blank input:


<img width="618" alt="image" src="https://user-images.githubusercontent.com/91749477/178085303-ea1c45fd-bcef-4a1e-bde8-a668334c6e69.png">



#### out of range example 5 with double numbers and single alphabet:


<img width="583" alt="image" src="https://user-images.githubusercontent.com/91749477/178085361-7dbecc09-9064-4447-ba3f-916897e22277.png">



#### out of range example 6 with double alphabets and single number:


<img width="632" alt="image" src="https://user-images.githubusercontent.com/91749477/178085385-2d6d7837-dad9-4447-b4cc-01c65139b36b.png">






## Technology used



Validator Testing
This site is created with help of the following coding languages;

### python 

Some external python libraries are imported and used in this game.

The code itself has been validated through PEP8 validator available at http://pep8online.com/ The result of code testing has not detected any error or issues requiring an immediate attention.


<img width="955" alt="image" src="https://user-images.githubusercontent.com/91749477/178086023-5fa706dd-0ced-4f3a-99f4-8b3769787a4c.png">


although the other languages files are there in the template but the only focus was python.




## Bugs and unfixed bugs

1. when I created all functions I forgot to call the relevant global variable within it and that cause not displaying grid.
2. forgot to add values within functions for col and rows.
3. incorrect indentatin in function which causes trouble in printing out to terminal.
4. Extra spaces which the all functions, blank white spaces, etc.
5. Validate_board was not executing properly as I made two for loop for row and col each and this was resolved by coding col as a nested loop.
6. The app was crashing because place_a_ship was not defined properly and by adding direction as a parameter this problem resolve
7. Another reason for the game crashing was that alphabet and number were not added in the if statement of  fire_placement function, which is resolved by adding length as <=1 or length == alphabet.
8. To add more precision I used while loop instead of an If statement in the main function, which was acctually another culprit of crashing.




### Unfix bugs

This game is extensively and thoroughly checked and no major unfix bugs remain up to the best of my knowledge.

### Deployment


The site was deployed to Heroku pages using the following steps:

1. Sign up and Login to Heroku
2. Click on the "NEW APPLICATION" and create an App name and choose your region (Europe for this project)
3. Click on "Deploy" and choose your deployment method
4. If you are connecting with Github choose your main branch and find your repository
5. Add config vars PORT = 8000 and buildpacks python and nodejs
6. Click on deploy manually or automatically (automaticlaly for this project)
7. When selecting Automatic deploayment, Deploy Branch still needs to be selected also.
8. The project has now been deployed
9. When deployed click on View on the bottom of the page



## Acknowledgements
1. Stockoverflow for giving idea about single player coding. https://stackoverflow.com/questions/17952870/simple-python-battleship-game
2. The project has been inspired by a number of external projects available on the web. Number of external projects have been reviewed as part of my research into suitable approach for my project.
3. Thanky you to Code Institute for excellent module content, Code Institue support team and my mentor Rohit for guidance and support.
4. Wikipedia for the details of battleships game
5. Codeacadmy for global variable examples 
6. Pythondex for coding stucture.
7. And learn.adafruit for tutorial on girds.

