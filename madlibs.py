with open('madlibs_story.txt', 'r') as f: #read the file 
    story = f.read()

words = set()   # set is used as set does not allow duplicate values 
target_start = '<'
target_end = '>' 
start_word = -1
#loop to make set of words to ask user
for i, char in enumerate(story):
       if char == target_start:
             start_word = i
       if char == target_end and start_word != -1:
             words.add(story[start_word:1+i])
# create a dictionary to store all the words and user input answers              
answers = {}             
for word in words:
      answer = input('Enter the alternative word for '+ word + ': ')
      answers[word] = answer

#replace all the input words in story
for word in words:
    story = story.replace(word, answers[word])

print(story)