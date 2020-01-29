"""
file commandはfile openなどで良いのか？
それともファイルの種類が判別できるものなのか

file openで実装
"""
import os

f = open("test.txt","w")
def get_list(**kwargs):
    for word_1, word_2 in kwargs.items():
        print(word_1 , word_2)
        
        f.write(str( word_1)+ " ")
        f.write(str( word_2)+ "\n")
        
get_list(prog1 = 'python', prog2 = 'java', prog3 = 'c#')

