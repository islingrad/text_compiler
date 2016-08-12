import os
import time
import random
import sys

## A question: (Listof Question and Answer)

## functions to make: item_selection_text(), 

class question:
    def __init__ (self, question,result, result_prompt):
        self.question = question
        self.result = trim(result)
        self.result_prompt = result_prompt

## A room: (Listof Questions)
class room:
    def __init__ (self, name, prompt, questions_list):
        self.name = name
        self.prompt = prompt
        self.questions_list = questions_list


## display_room: room -> display_room
## Consumes a room_to_display and: 
## 1) Prints the Room name
## 2) Prints the Room prompt
## 3) Prints the Room Question list with numbers
## 4) Takes user choice
## 5) Displays prompt for question selected
## 6) Waits . . . .
## 7) Clears screen
## 8) Recurses with new choice room

def display_room(room_to_display):
    print(room_to_display.name)#1
    display_room_prompt(room_to_display)#2
    local_room_question_list = room_to_display.questions_list
    item_number = 1
    for item in local_room_question_list:#3
        print(str(item_number) + ". " + item.question)
        item_number +=1
    choice = input_safeguard("Choose one of the above option numbers ", item_number)#4
    choice_question = local_room_question_list[choice - 1]
    display_result_prompt(choice_question)#5
    time.sleep(.5)#6
    print(".")
    time.sleep(.5)#6
    print(".")
    time.sleep(.5)#6
    print(".")
    time.sleep(.5)#6
    os.system('cls')#7
    choice_room_name = choice_question.result
    display_room(find_room_in_rooms_list(choice_room_name)) # 8


## display_result_prompt: Question
## Consumes a question and if there is a result_prompt, prints the prompt.
def display_result_prompt(question_to_display):
    if question_to_display.result_prompt != False:
        print(question_to_display.result_prompt)

## display_room_prompt: Room
## Consumes a room and if there is a promp, prints the prompt.
def display_room_prompt(room_to_display):
    if room_to_display.prompt != False:
        print(room_to_display.prompt)

## find_room_in_rooms_list: String(a room name)
## Consumes a room name, returns the associated room(object)in the rooms_list
def find_room_in_rooms_list(room_name): 
    for room in rooms_list:
        if room.name == room_name:
            return room
            break
    while True:
        print(str(room_name) + " room does not exist")
        print("You must create " + str(room_name) + " room for your game to work")
        input_safeguard("Type 'Quit' to Exit ")
        time.sleep(1)

## first: String -> String
## Consumes a String and returns the first character
def first(line):
    if type(line) == str:
        return line[0]
    else:
        print("Error: " , line , " is not a string.")

## input_safeguard: (Num or (Num and Int)) -> Error or Int
## if given one parameter: input_safeguard is being used because of an error in the input_text, will loop until user types quit, then quits.
## if given two parameter: Takes user input and ensures its a num between 1 and cap
def input_safeguard(string,cap = False):
    try:
        while True:
            quitter = input(string)
            if quitter== 'quit' or quitter == 'Quit':
                sys.exit()
            in_num = int(quitter)
            if cap != False:
                if in_num in list_add1(range(cap)):
                    return in_num
                else:
                    print("Your number must be between 1 and " + str(cap -1))
    except ValueError:
        print("Try entering an integer next time")
        return input_safeguard(string,cap)

## list_add1: Listof Num -> Listof Num
## Consumes a lon and adds one to each element
def list_add1(lon):
    out_list =[]
    for i in lon:
        out_list.append(i+1)
    del out_list[len(out_list)-1]
    return out_list

## remove_newlines: Listof Strings -> Listof Strings
## Removes the last character from each string in the list.
## Used when reading the input_text file to remove \n at end of each string
def remove_newlines(text_list):
    new_list = []
    for i in text_list:
        expanded_line = list(i)
        del expanded_line[len(expanded_line)-1]
        out_line= "".join(expanded_line)
        new_list.append(out_line)
    return new_list

## rest: (List or String) -> (List or String)
## Returns all but the first element/character in a list or string 
def rest(line):
    return line[1:]

## room_entry_text: Null -> String
## Chooses a random String from a list to display
def room_entry_text(): ## idea for later, allow users to create a file that has room entry texts
    options= []
    options.append("You casually walk into")
    options.append("A psychic force transports you through levitation to")
    options.append("You enter")
    options.append("Fate has led to you arriving at")
    options.append("Through a miraculous turn of events you end up at")
    options.append("You air-drop into")
    options.append("You dig your way into")
    return options[random.randint(0,len(options)-1)]

## start_game: Null -> display_room
## Checks that user created a minimum of one room and displays the first room created
def start_game():
    if rooms_list == []:
        print("There are no valid rooms in your input-file")
    else:
        display_room(rooms_list[0])

## line_to_question: String(containing Question data) -> Question
        ##Ex. "-question_text:resultant_room!" -> Question(question_text, resultant_room)
## 1) Returns String from beginning to '!', feeds the rest of the string to 2).
## 2) Returns from beginning to '!', feeds the rest of the string to 3) or false if rest of string is empty.
## 3) Returns from beginning to '!' or False if given False
## 4) Creates question using 1,2,3 , removes leading spaces from 1,2,3
        
def line_to_question(line):
    def pull_query(line): #1
        if first(line) == '!':
            global reply_input
            reply_input = rest(line)
            return ""
        elif first(line) == '-':
            return pull_query(rest(line))
        else:
            return first(line) + pull_query(rest(line))
    def pull_reply(line): #2
        if first(line) == "!":
            global prompt_input
            prompt_input = rest(line)
            if prompt_input == '':
                prompt_input = False
            return ""
        else:
            return first(line)+pull_reply(rest(line))
    def pull_prompt(line):#3
        if line == False:
            return False
        if first(line) == "!":
            return ""
        else:
            return first(line) + pull_prompt(rest(line))
    return question(trim(pull_query(line)),trim(pull_reply(reply_input)),trim(pull_prompt(prompt_input))) #4

## trim: String -> String
## Removes leading spaces in a string

def trim(string):
    if type(string) != str:
        return string
    if first(string) == ' ':
        return trim(rest(string))
    else:
        return string

## text_to_list: remove_newlines(input_file) -> (Listof (listof room data))
## Consumes list of strings given from input_text, with newlines removed
## creates a list of lists where each nested list is the data for a single room
def text_to_list(text):
    def full_text_to_lol(full_text):
        fir = full_text[0]
        res = full_text[1:]
        if fir == '<newroom>':
            return []
        elif fir == 'END':
            return []
        elif fir == '':
            return full_text_to_lol(res)
        else:
            return [fir] + full_text_to_lol(res)
    if text ==[]:
        pass
    elif text[0] == '<newroom>':
        lol.append(full_text_to_lol(text[1:]))
        text_to_list(text[1:])
    else:
        text_to_list(text[1:])

## make_rooms: Null
## Uses the global lol, fills rooms_list with rooms (objects)
## local functions:
## i) Consumes global lol and outputs a list with room name data
##    as first elemet and list of questions as second element
## ii) Takes a name line string, extracts the room name, feeds rest of line to iii)
## iii) Takes from ii) and extracts prompt if it exists, false if doesn't exist
## iv) Makes all the rooms into room_list

## Build_rooms does the following:
## 1) Try if room name/prompt can be pulled properly, if bad !'s (line breaks), deliver error
## 2) Try if question list line can be pulled if bad !'s (line breaks), deliver error
## 3) returns a room build with pulls from 1 and 2

def make_rooms():
    def format_list(): ##i
        ready = [] 
        for i in lol:
            ready.append([i[0], i[1:]])
        return ready
    def pull_room_name(line): # iii)
        if first(line) == '!':
            global room_prompt_input
            room_prompt_input = rest(line)
            if room_prompt_input == '':
                room_prompt_input = False
            return ''
        else:
            return first(line) + pull_room_name(rest(line))
    def pull_room_prompt(line):
        if line == False:
            return False
        elif line == '!':
            return ''
        else:
            return first(line) + pull_room_prompt(rest(line))

    def build_room(lol):
        try: #1
            name= pull_room_name(lol[0])
            prompt = pull_room_prompt(room_prompt_input)
        except IndexError: #1
            print("ERROR MESSAGE: Error in line: \n\n")
            print(lol[0] +"\n\n")
            while True:
                input_safeguard("Type quit to exit")
        q_list = [] #2
        for q in lol[1]: #2
            try:
                q_list.append(line_to_question(q))
            except IndexError: #CREATES AN ERROR ,MESSAGE WHEN input question is bad
                print('CRITICAL ERROR!')
                print('ERROR MESSAGE: Missing ! in line:\n\n')
                print(q + "\n")
                print('IN ROOM: ' + name +"\n\n")
                while True:
                    input_safeguard("Type quit to exit")
        return room(trim(name), trim(prompt), q_list) #3
    ready = format_list() # Puts the list in good format
    for i in ready: # builds for each item in the list
        rooms_list.append(build_room(i))

## game_init: Null
## Begins the game by:
## 1) Reads and edits the input file into a list
## 2) Declares global variable (rooms_list)
## 3) Declares global helper variable (lol)
## 4) Places formatted input_file data into lol
## 5) Converts data from lol into rooms, adds rooms to rooms_list
## 6) Displays first room from room_list
def game_init():
    global rooms_list, lol
    input_file = open("input-file.txt", "r")
    full_input_text = remove_newlines(input_file.readlines()) 
    rooms_list = []
    lol = []
    text_to_list(full_input_text)
    make_rooms()
    start_game()

game_init() ############### STARTS THE GAME ####################




