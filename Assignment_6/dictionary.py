import sys
import os
import re
WORDS = []

def Load_Data():
    try: 
        with open ('words_bank.txt','r') as f:
            big_text = f.read()
            lines = big_text.split('\n')

            for i in range(0,len(lines),2):
                WORDS.append( {'english':lines[i] , 'persion':lines[i+1]})
    except OSError:
        print ("Could not open read file ")
        sys.exit()


def translate(user_words,from_lang,to_lang):

    output_text = ""
    for user_word in user_words :
        for WORD in WORDS :
            if user_word == WORD[from_lang]:
                output_text  += WORD[to_lang] + " "
                break
        else :
         output_text  += user_word + " "  

    return output_text   

def user_input():
    return  re.findall(r"[\w']+|[.]", input())

def show(arr):      
    for item in arr:
        print(item)
    return arr

def add(en_word,fa_word):
    with open('words_bank.txt', "a") as myfile:
            if os.path.getsize('words_bank.txt') != 0: 
                myfile.write("\n")
            myfile.write(en_word)
            myfile.write("\n")
            myfile.write(fa_word)
            myfile.close() 
    global WORDS
    WORDS=[]
    Load_Data()

def select_menu(optionsarr,methodsarr):
  
    while True:
        show(optionsarr)
        x=int(input())
        for i in range(len(optionsarr)):
            if(x==i+1) and i+1 in methodsarr.keys():
                methodsarr[i+1]();
                break
        else:
            sys.exit()

Load_Data()
select_menu(['1.add word','2.en_fa','3.fa_en','4.exit'],{1:lambda :add(input ('please write your english word :'),input ('please write your persian word :')) ,2:lambda :print(translate(user_input(),'english','persion')),3:lambda :print(translate(user_input(),'persion','english'))})

