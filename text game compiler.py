import os
import time
import random
import sys
input_file = open("input-file.txt", "r")

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

def display_room(room_to_display):
    print room_to_display.name
    display_room_prompt(room_to_display)
    local_room_question_list = room_to_display.questions_list
    item_number = 1
    for item in local_room_question_list:
        print str(item_number) + ". " + item.question
        item_number +=1
    choice = input_safeguard("Choose one of the above option numbers ", item_number) ## User selects one of the room questions that are listed using an integer 1 to n
    choice_question = local_room_question_list[choice - 1]
    choice_room_name = choice_question.result## pulls associated room name from the pertinent question
    display_result_prompt(choice_question)
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    os.system('cls')
    display_room(find_room_in_rooms_list(choice_room_name)) ## displays the room that was in the selected option question

def display_result_prompt(question_to_display): ## this requirest a check to make sure that a prompt exists
    if question_to_display.result_prompt != False:
        print question_to_display.result_prompt

def display_room_prompt(room_to_display):
    if room_to_display.prompt != False:
        print room_to_display.prompt

def find_room_in_rooms_list(room_name): ## given a room name, returns the associated room in the rooms_list
    for room in rooms_list:
        if room.name == room_name:
            return room
            break
    while True:
        print str(room_name) + " room does not exist"
        print "You must create " + str(room_name) + " room for your game to work"
        input_safeguard("Type 'Quit' to Exit ")
        time.sleep(1)
        
def first(line):
    if type(line) == str:
        return line[0]
    else:
        print "Error: " , line , " is not a string."

def input_safeguard(string,cap = False):
    try:
        while True:
            quitter = raw_input(string)
            if quitter== 'quit' or quitter == 'Quit':
                sys.exit()
            in_num = int(quitter)
            if in_num in list_add1(range(cap)):
                return in_num
            else:
                print "Your number must be between 1 and " + str(cap -1)
    except ValueError:
        print "Try entering an integer next time"
        return input_safeguard(string,cap)

def list_add1(lon):
    out_list =[]
    for i in lon:
        out_list.append(i+1)
    del out_list[len(out_list)-1]
    return out_list

def remove_newlines(text_list):
    new_list = []
    for i in text_list:
        expanded_line = list(i)
        del expanded_line[len(expanded_line)-1]
        out_line= "".join(expanded_line)
        new_list.append(out_line)
    return new_list

def rest(line):
    return line[1:]

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

def start_game():
    if rooms_list == []:
        print "There are no valid rooms in your input-file"
    else:
        display_room(rooms_list[0])

## line_to_question: String(containing full question line
        ##Ex. "-question_text:resultant_room!" -> Question(question_text, resultant_room)
## Takes the text after the dash and before the colon and turns it into the question.
## Takes the text between the colon and ! and turns it into resulting action of selecting that option
def line_to_question(line):
    def pull_query(line):
        if first(line) == '!':
            global reply_input
            reply_input = rest(line)
            return ""
        elif first(line) == '-':
            return pull_query(rest(line))
        else:
            return first(line) + pull_query(rest(line))
    def pull_reply(line):
        if first(line) == "!":
            global prompt_input
            prompt_input = rest(line)
            if prompt_input == '':
                prompt_input = False
            return ""
        else:
            return first(line)+pull_reply(rest(line))
    def pull_prompt(line):
        if line == False:
            return False
        if first(line) == "!":
            return ""
        else:
            return first(line) + pull_prompt(rest(line))
    return question(pull_query(line),trim(pull_reply(reply_input)),pull_prompt(prompt_input))

def trim(string):
    word = ''
    for i in list(string):
        if i !=' ':
            word += i
    return word
          
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

def make_rooms():
    def pull_room_name(line):
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
    ready = [] 
    for i in lol:
        ready.append([i[0], i[1:]])
    def build_room(lol):
        try:
            name= pull_room_name(lol[0])
            prompt = pull_room_prompt(room_prompt_input)
        except IndexError:
            print "ERROR MESSAGE: Error in line: \n\n"
            print lol[0] +"\n\n"
            while True:
                input_safeguard("Type quit to exit")
        q_list = []
        for q in lol[1]:
            try:
                q_list.append(line_to_question(q))
            except IndexError: ##CREATES AN ERROR ,MESSAGE WHEN input question is bad
                print 'CRITICAL ERROR!'
                print 'ERROR MESSAGE: Missing ! in line:\n\n'
                print q + "\n"
                print 'IN ROOM: ' + name +"\n\n"
                while True:
                    input_safeguard("Type quit to exit")
        return room(name, prompt, q_list)
    for i in ready:
        rooms_list.append(build_room(i))

full_input_text = remove_newlines(input_file.readlines())
rooms_list = []
lol =[]
text_to_list(full_input_text)
make_rooms()
start_game()
