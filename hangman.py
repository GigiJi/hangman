from random import randint # Do not delete this line

def displayIntro():
    str = '''________________________________________________                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________
                 
     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___ 
 '''
    print(str)

def displayEnd(result):
    str = ''
    if result == True:
        str = '''________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________'''
    else:
        str = ''' __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________'''
    print(str)
def displayHangman(state):
    if state == 5:
        str = '''     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___ 
 '''
    elif state == 4:
        str = '''     ._______.   
     |/      |   
     |
     |           
     |           
     |           
     |           
 ____|___ 
 '''
    elif state == 3:
        str = '''      ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___ 
 '''
    elif state == 2:
        str = '''     ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___ 
   '''
    elif state == 1:
        str = '''     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___ 
 '''
    else:
        str = '''     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___ 
 '''
    print(str)

def getWord():
    file = open("hangman-words.txt", "r")
    lst = file.readlines()
    randNum = randint(0,len(lst)-1)
    word = list(lst[randNum])
    if randNum != len(lst) - 1:
        word = word[:len(word) - 1]
    file.close()
    return word
def valid(c):
    return c.islower() and len(c) == 1

def rec_change_txt(word,word2,c,count):
    # This is the function that recursively changes the characters in word2.
    # word is a string from the getWord function
    # word2 is a string with the same length as word but is encrypted
    # c is a character which we want to change in word2
    # count is number of times c appears in the given word
    if count == 1:
        word2 = word2[:word.index(c)] + c + word2[word.index(c) + 1:]
        return word2
    else:
        word2 = word2[:word.index(c)] + c + word2[word.index(c) + 1:]
        word = word[:word.index(c)] + '0' + word[word.index(c) + 1:]
        return rec_change_txt(word, word2, c, count-1)

def play():
    word = getWord()
    word = ''.join(word)
    state = 5
    word2 = '_' * len(word) # same length as word, but word2 is encrypted with '-'-s
    while state != 0:
        print('Guess the word:', word2)
        letter = input("Enter the letter:\n")
        while not valid(letter):
            letter = input("Enter the letter:\n")
        count = 0
        for i in word:
            if i == letter:
                count += 1  # To know how many times the input letter appears in the guessing word
        if count == 0:
            state -= 1
        elif count >= 1:
            word2 = rec_change_txt(word,word2,letter,count)
        if word2 == word:
            print('Hidden word was:', word2)
            return True
        displayHangman(state)
    print('Hidden Word Was: ', word)
    return False

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        str = input("Do you want to play again? (yes/no)\n")
        while str != 'yes' and str != 'no':
            str = input("Do you want to play again? (yes/no)\n")
        if str == 'yes':
            hangman()
            break
        else:
            break

if __name__ == "__main__":
    hangman()
