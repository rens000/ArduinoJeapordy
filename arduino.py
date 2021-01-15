#created by aria r and jenna j
#jan 15, 2021

#use pictures on GitHub to set up breadboars        
#to connect breadboard to Arduino put 2 read wires into 11 and 12 digital slots
#and 2 black into the gnd slots


from pyfirmata import Arduino
import time

score1 = 0
score2 = 0
def green():
    board.digital[12].write(1)
    time.sleep(1)
    board.digital[12].write(0)

def red():
    board.digital[11].write(1)
    time.sleep(1)
    board.digital[11].write(0)


def question1():
    global score1
    x = input("How many countinents are there?:  ")
    if x == "6":
        green()
        score1 += 1
    else:
        red()

def question2():
    global score1
    x = input("What is the largest country in the world by area?:  ")
    if x == "russia" or x == "Russia":
        green()
        score1 += 1
    else:
        red()


def question3():
    global score1
    x = input("What country produces the most coffee?:  ")
    if x == "brazil" or x == "Brazil":
        green()
        score1 += 1
    else:
        red()


def question4():
    global score1
    x = input("How many presidents have been impeached?:  ")
    if x == "3" or x == "three" or x == "Three":
        green()
        score1 += 1
    else:
        red()


def question5():
    global score1
    x = input("Which song by Luis Fonsi and Daddy Yankee has the most views (of all time) on YouTube?:  ")
    if x == "Despacito" or x == "despacito":
        green()
        score1 += 1
    else:
        red()


def question6():
    global score2
    x = input("On what day of July is Canada Day?:  ")
    if x == "1st" or x == "1":
        green()
        score2 += 1
    else:
        red()


def question7():
    global score2
    x = input("How many eyes does a bee have?:  ")
    if x == "5" or x == "Five" or x == "five":
        green()
        score2 += 1
    else:
        red()

        
def question8():
    global score2
    x = input("What political/economic ideology did Mao Zedong prescribe to?:  ")
    if x == "communism" or x == "Communism":
        green()
        score2 += 1
    else:
        red()


def question9():
    global score2
    x = input("Which organ has 4 chambers?:  ")
    if x == "heart" or x == "Heart" or x == "the heart":
        green()
        score2 += 1
    else:
        red()
        

def question10():
    global score2
    x = input("What European nation is responsible for creating the hot dog?:  ")
    if x == "germany" or x == "Germany":
        green()
        score2 += 1
    else:
        red()


def compare_scores():
    print("Player 1 your score was:  " + str(score1))
    print("Player 2 your score was:  " + str(score2))
    if score1 > score2:
        print("CONGRATS PLAYER 1!  YOU WIN!")
    elif score2 > score1:
        print("CONGRATS PLAYER 2!  YOU WIN!")
    else:
        print("IT'S A TIE!")

        
if __name__ == '__main__':
    board = Arduino('/dev/cu.usbmodem14301')
    #print("Communication Successfully started")
    print("PLAYER 1 IT IS YOUR TURN, GET AS MANY CORRECT AS POSSIBLE")
    print()
    question1()
    print()
    question2()
    print()
    question3()
    print()
    question4()
    print()
    question5()
    print()
    print("PLAYER 2 IT IS YOUR TURN, GET AS MANY CORRECT AS POSSIBLE")
    print()
    question6()
    print()
    question7()
    print()
    question8()
    print()
    question9()
    print()
    question10()
    print()
    compare_scores()
        

