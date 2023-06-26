from time import time
print("press enter t start typing")
print("press Enter twice to finish typing" )
input()
start=time()

text=[]
while True:
    line=input()
    if not line:
        break
    text.append(line)
end=time()
print('-------------------------------')
elapsed_time=(end-start)/60
char_count=sum(len(item)for item in text)
word_count=char_count/5

wpm=round(word_count/elapsed_time)
print(f'your average Words Per Minute(wPM) is {wpm}')
if wpm<30:
    print('You should learn proper typing techniqueand and practice more to improve your speed')
elif wpm<40:
    print('not bad,but still below average keep practicing')
elif wpm<50:
    print('You are an average typist.you still have significant room for improvement')
elif wpm<60:
    print('Congratulations! you are above average')
else:
    print('your can now be a professional typist') 
                   