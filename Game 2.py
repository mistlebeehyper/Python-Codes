

# Use a dictionary
#
import random

points = 0
tries = 0

words = {
    "Love" :["A word for affection.", "A feeling of compassion.", "A feeling of great interest in something.", "A romantic feeling."],
    "Endgame" :["The highest grossing movie of all time.", "The last movie of one the most watched movie series.", "Pepperony's last movie together.", "'If I tell you, it wont happen.'"],
    "Sia" :["He/she is the inspiration of the movie 'Music'.", "He/She sang 'Move you body'.", "He/She sang 'Elastic heart'.", "In his or her song, 'I don't need money.'"],
    "Church" :["The body of Christ.", "A gathering of people who come to worship God.", "A place of worship.", "The house of God."],
    "Gay" :["To be extremely happy.", "To be attracted to the same sex.", "To be in a romantic relationship with the same sex.", "It has the letter 'y'."],
    "Game" :["To be ready for something.", "To be prepared for something", "A state of readiness.", "To be prepared."],
    "Queen" :["The name of a former popular boy-band.", "The female head of a monarchy.", "Has double letter 'e'.", "The wife of a king."]
}

scores = {}     

keys = []
for k in words.keys():
    keys.append(k)

user_valid_plays = []

word = ""
hint = ""

def set_word():
    global words, word, hint, keys, user_valid_plays
    word = random.choice(keys)
    hint = random.choice(words[word])
    user_valid_plays = []
    x = 0

def settings():
    global tries
    do = input("What level of this game do you wish to play:\n 1. Easy Level\n 2. Medium Level\n 3. Hard Level\n : ")
    if do == "1":
        tries = 5
    elif do == "2":
        tries = 3
    elif do == "3":
        tries = 1
    else:
        print("Invalid option.")
        qit = input("Do you wish to quit?\n 1. Yes\n 2. No\n : ")
        if qit == "1":
            quit()
        else:
            settings()
    game()

def is_complete():
    global user_valid_plays, word
    for w in word:
        if w.lower() not in user_valid_plays:
            return False
    return True
        
def print_dashes():
    global word, user_valid_plays
    for i in word:
        if i.lower() in user_valid_plays:
            print(i,end=" ")
        else:
            print("_",end=" ")
    print("")

def game(): 
    global x, points, tries
    name = input("Input your player name: ")
    try:
        scores[name]
    except:
        scores[name] = 0
        
    attempts = tries
    set_word()
    print_dashes()
    print("Hint:",hint)
    while attempts > 0:
        if not is_complete():
            guess = input("Guess a letter in this word: ").strip().lower()
            if len(guess) > 1:
                attempts = attempts - 1
                print("Input one letter at a time... You have",attempts,"tries left")
            elif guess in word.lower():
                user_valid_plays.append(guess)
                print("This letter is in the word") 
            else:
                attempts = attempts - 1
                print("The letter is not a in the word... You have",attempts,"tries left")
                if attempts == 0:
                    print("The word is:",word)
                    again()
            print_dashes()
            points = attempts
        else:
            print("CONGRATULATIONS!!!")
            scores[name] += points
            again()
    

def leaderboard():
    global points, scores, name
    print(">>>>>LEADERBOARD<<<<<")
    print("PLAYER NAME\t|\tSCORE")
    
    sx = list(scores.values())
    
    sy = []
    for s in sx:
        if s not in sy:
            sy.append(s)
    
    sy.sort(reverse=True)

    for y in sy:
        for s in  scores.items():
            if s[1] == y:
                print(f"{s[0]} \t\t | \t {s[1]}")
    #print(scores.items())
    
def again():
    global tries, x
    again = input("Do you wish to:\n 1. Play again.\n 2. Go to main menu.\n 3. Quit\n : ")
    if again == "1":
        game()
    elif again == "2":
        opt()
    elif again == "3":
        quit()
    else:
        print("Invalid option.")
        qit = input("Do you wish to quit?\n 1. Yes\n 2. No\n : ")
        if qit == "1":
            quit()
        else:
            opt()

def addList():
    word = input("Input the word to be added: ")
    hint = input("Input the hint to be added: ")
    words.update({word: hint})
    input("Press Enter")
    print(f"Word: {word} \t|\t Hint: {hint}\n")
    opt()

def opt():
    global tries, x
    do = input("Do you wish to:\n 1. Play a new game.\n 2. Go to settings.\n 3. Check leaderboard\n 4. Add a word\n : ")
    if do == "1":
        print("NOTE: This game will automaticlly start from the easy level.\nHowever you can change this in settings.")
        input("Press Enter")
        tries = 5
        game()
    elif do == "2":
        settings()
    elif do == "3":
        leaderboard()
    elif do == "4":
        addList()
    else:
        print("Invalid option.")
        qit = input("Do you wish to quit?\n 1. Yes\n 2. No\n : ")
        if qit == "1":
            quit()
        else:
            opt()
    
#def name():
    #name = input("Input your player name: ")
    
try:
    print(">>>>>Guess the Word<<<<<")
    opt()
except:
    print("Code Error... Restart this program")
    input("Press Enter")
    opt()
    
