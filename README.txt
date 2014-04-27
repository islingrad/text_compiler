The text game compiler is a simple and intuitive tool 
that allows any user to make a text adventure game.
NO PROGRAMMING EXPERIENCE REQUIRED!


HOW IT WORKS: 

You must create a file named input_file.txt, this is used as the 
foundation for the game.

In this text file you will create a series of rooms for your Rex-Text
game. The player of your game will then travel through these rooms,
encountering surprises and hilarious turns of events.

When you create a room it must have three parts:
1. Room declaration.
2. A Room Name, and optionally a room prompt ( a message to be shown
	once that room is entered)
3. A list of Questions/Actions

I will walk you through each part individually.

ROOM DECLARATION:

- simply type "<newroom>" in order to declare that a new room has begun
Notes:

- The first room in the input_text file will be the room the 
	player begins your text adventure in.

-A room will contain parts 2 and 3 from above

-The final room in your input_text file must end with the word "END"

Example (this still requires the next to parts to work):
<newroom>
.
.
.
END

ROOM NAME:

After the new room declaration the next line should be your room name.

Optionally you can include a message for when a player enters the room.

Both the name and the prompt must be followed by a "!"

Note: 
1 and 2 must be on the same line,in order, and seperated by !'s
"!" may not be used only at the end of the name and prompt.
Be careful, misplaced !'s will crash your game.

Two valid Examples (these require the last part to work as a proper game):

<newroom>
Dark library!
.
.
.
END

<newroom>
Dark library! It is very scary in here!
.
.
.
END

QUESTIONS/ACTIONS:

You may have as many questions or actions as you like, for the player to 
choose from in each room. The player may only choose one

Each question or action results in the player being shown a message relating
to their choice (optional) , and the player being transported to another 
room (required).

The format for creating a question/action is similar to the format 
for a room name.

There are three parts for every question/action however:
1. The Question/Action 
2. The room you will be brought to
3. A message to be displayed (optional)

Each of these 3 things must be followed by a "!"

Note:
-1,2, and 3 must be on the same line,in order, and seperated by !'s
-The Name in 2 must exactly match a room name given in a room declaration
-"!" may not be used only at the end of the Question, room, and message.
-Be careful, misplaced !'s will crash your game.

EXAMPLE (you can text this and play around with it to make 
your own game):

<newroom>
Beach! Very warm here!
-Go to Pool!Pool!The Pool is Nice!
-Go home!Home!
-Dig a hole!Hole! You fall far in and get trapped!

<newroom>
Pool! Ahhhh swimming is nice!
- Go home! Home! Home sweet home!
- Go to Beach! Beach!

<newroom>
Hole! You're stuck!
- Climb left! Hole! YOU FALL BACK IN!
- Climb right! Hole! YOU FALL BACK IN!
- Keep going down! Beach! You dig through to china's beach!

<newroom>
Home!
-Go Beach!Beach!
-Go Pool!Pool!

END





















