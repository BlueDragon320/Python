def gamefn():
    score = int(input("Enter the score:  "))
    return score

newscore = gamefn()

rd = open("Hi-score.txt", "r")  
data = int(rd.read())           
rd.close()

if newscore > data:
    wr = open("Hi-score.txt", "w")  
    wr.write(str(newscore))         
    wr.close()
    
print("New high score saved!")