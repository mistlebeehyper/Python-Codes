punct = "!,?"
word =input("Write a word")
count = 0
newWord = word

 
while count < len(punct):
       count2 = 0
       x=0
       while count2 < len(word):
              if punct[count] == word[count2]:
                     newWord = newWord[0:count2]+ newWord[count2+x:len(word)]
              
              x=x+1
              count2 = count2 + 1
       count = count + 1
print(newWord)


       
