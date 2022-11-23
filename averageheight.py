h=input('heights:').split()
height=0
for n in range(0,len(h)):
    height+=int(h[n])
avg_height=float(height/len(h))  
print(round(avg_height, 3))