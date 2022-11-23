scores=input('take scores: ').split()
for n in range(0, len(scores)):
    scores[n]=int(scores[n])
print(scores)
highestscore=0
for i in scores:
    if i>highestscore:
        highestscore=i
        
print(highestscore)
    