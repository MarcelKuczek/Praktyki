import signal
import sys

def signal_handler(sig, frame):
    print('Good Bye')
    sys.exit()

def Convert(word):
    word_list = []
    for i in range(0 ,len(word)):
        temp_word = word [:]
        temp_word[i] = temp_word[i].upper()
        word_list.append(temp_word)
    print (word_list)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')
while(True):

    word = input("Write word to convert: ")
    word = list(word)
    Convert(word)