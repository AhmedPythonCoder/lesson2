x = 'Ahmed'

#range (start value, end value, step)
'''

for i in range(51, 71, 2):
    print(f'{i} - Ahmed')

'''




#counting numbers of characters in a sentence

s = input('Enter a sentence: ')
char_count = 0
word_count = 1
for i in s:
    if i == 'r':
        char_count = char_count + 1
    if(i==' '):
        word_count=word_count+1

        #word_count+=1
print(f'the number of characers in "{s}" is {char_count}')
print(f'the number of words in "{s}" is {word_count}')