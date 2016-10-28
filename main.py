import RPi.GPIO as GPIO
import time

GPIOPorts = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40 ]

GPIODictionary = {
    "A": GPIOPorts[0], 
    "B": GPIOPorts[1],
    "C": GPIOPorts[2],
    "D": GPIOPorts[3],
    "E": GPIOPorts[4],
    "F": GPIOPorts[5],
    "G": GPIOPorts[6],
    "H": GPIOPorts[7],
    "I": GPIOPorts[8],
    "J": GPIOPorts[9],
    "K": GPIOPorts[10],
    "L": GPIOPorts[11],
    "M": GPIOPorts[12],
    "N": GPIOPorts[13],
    "O": GPIOPorts[14],
    "P": GPIOPorts[15],
    "Q": GPIOPorts[16],
    "R": GPIOPorts[17],
    "S": GPIOPorts[18],
    "T": GPIOPorts[19],
    "U": GPIOPorts[20],
    "V": GPIOPorts[21],
    "W": GPIOPorts[22],
    "X": GPIOPorts[23],
    "Y": GPIOPorts[24],
    "Z": GPIOPorts[25]
    }

def setup_GPIOPorts():
    GPIO.setmode(GPIO.BOARD)
    for i in GPIOPorts:
        GPIO.setup(i, GPIO.OUT)

setup_GPIOPorts()

REFRESH_MS = 7
current_time_ms = lambda: int(round(time.time() * 1000))




def char_on(char):
    GPIO.output(GPIODictionary[char], GPIO.HIGH)    

def char_off(char):
    GPIO.output(GPIODictionary[char], GPIO.LOW)

def chooseCharBlink(char, on_ms, off_ms):
    char_on(char)
    time.sleep(on_ms)
    char_off(char)
    time.sleep(off_ms)


def show(word, char_on_ms, char_off_ms, word_on_ms):
    [type_char(char, char_on_ms, char_off_ms) for char in word]
    word_on(word, word_on_ms)

# def type_char(char, on_ms, off_ms):
#     char_on(char)
#     time.sleep(on_ms)
#     char_off(char)
#     time.sleep(off_ms)

def word_on(word, on_ms):
    i = 0
    end_time_ms = current_time_ms + on_ms
    while current_time_ms < end_time_ms:
        char_on(word[i])
        time.sleep(REFRESH_MS)
        char_off(word[i])
        i = (i + 1) % word.len


readInput = input('Input string: ').ascii_uppercase

charList = list(readInput)

listLength = len(charList)

for i in listLength
    print(listLength[i])
    chooseCharBlink(charList(i), 5, 1)



