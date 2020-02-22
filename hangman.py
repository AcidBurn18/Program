import random
print "                                   HANGMAN                      ","\n"
print "                     (Welcome to Word Guessing Game)                    ","\n"
print "Made By ANSH, ABHAY, AYUSH","\n"
x=raw_input("What's your Name := ")
print "Points are based on number of chances left and length of that word","\n"
print "Hello",x,"Let's Begin","\n"
input1=["keyboard","mouse","joystick","lightpen","trackball","scanner","graphictablt","microphone","magneticinkcard","opticalcardreader","barcodereader","opticalmarkreader"]
output=["printer","monitor","graphicplotter","speaker","television","projector"]
sports=["cricket","baseball","polo","badminton","billard","tabletennis","zudo","volleyball","basketball","swimming","squash"]
p=random.choice([input1,output,sports])#Randomly selct the list 
m=random.choice(p)#Randomly slelct the element of the list
c=0
d=(len(m))
turn=5#For number of chnaces a PLayer will get
guess=" "
print "total no. of charaters ",d,"\n"
if m in input1:
    c=list(m)
    print "Related to Input in the Field of Technology","\n"
    i=0
    k=" "
    while i < (len(c)-1):
        k=k+" "         #Creating an string of same length as the word is selected 
        i=i+1
    g=list(k)           #Converting the string to list
    print g,"\n"
    print "One Letter In The Word is:- ",c[1],"\n"#For giving a hint
    while turn>0:       #The main loop
        gu=raw_input("Enter the character:- ") #taking the guessed character from user
        z=0
        if gu in c:
            z=0
            while z<len(c):
                if c[z]==gu:
                    g[z]=gu
                    print g
                    c[z]=" "        #Replacing the correct guessed word with blank space
                    z+=1
                    break
                    
                else:
                    z+=1
            d=d-1
            print "Letters Left",d,"\n"
            guess=guess+gu
            if turn!=0 and d==0:
                print "HURRAY YOU WON THE GAME,CONGRATUALTION!!!",x,"\n"
                print "Word Is",m,"\n"
                if len(m)==3 and turn==5:         #Points pattern 
                     print "Your Score is 100","\n"
                if len(m)==3 and turn==4:
                     print "Your Score is 80" ,"\n"
                if len(m)==3 and turn==3:
                     print "Your Score is 60","\n"
                if len(m)==3 and turn==2:
                     print "Your Score is 40","\n"
                if len(m)==3 and turn==1:
                     print "Your Score is 20","\n"
                if len(m)==4 and turn==5:
                     print "Your Score is 200","\n"
                if len(m)==4 and turn==4:
                     print "Your Score is 180" ,"\n"
                if len(m)==4 and turn==3:
                     print "Your Score is 160","\n"
                if len(m)==4 and turn==2:
                     print "Your Score is 140","\n"
                if len(m)==4 and turn==1:
                     print "Your Score is 120","\n"
                if len(m)==5 and turn==5:
                     print "Your Score is 300","\n"
                if len(m)==5 and turn==4:
                     print "Your Score is 280" ,"\n"
                if len(m)==5 and turn==3:
                     print "Your Score is 260","\n"
                if len(m)==5 and turn==2:
                     print "Your Score is 240","\n"
                if len(m)==5 and turn==1:
                     print "Your Score is 220","\n"
                if len(m)==6 and turn==5:
                     print "Your Score is 400","\n"
                if len(m)==6 and turn==4:
                     print "Your Score is 380" ,"\n"
                if len(m)==6 and turn==3:
                     print "Your Score is 360","\n"
                if len(m)==6 and turn==2:
                     print "Your Score is 340","\n"
                if len(m)==6 and turn==1:
                     print "Your Score is 320","\n"
                if len(m)==7 and turn==5:
                     print "Your Score is 500","\n"
                if len(m)==7 and turn==4:
                     print "Your Score is 480" ,"\n"
                if len(m)==7 and turn==3:
                     print "Your Score is 460","\n"
                if len(m)==7 and turn==2:
                     print "Your Score is 440","\n"
                if len(m)==7 and turn==1:
                     print "Your Score is 420","\n"
                if len(m)==8 and turn==5:
                     print "Your Score is 600","\n"
                if len(m)==8 and turn==4:
                     print "Your Score is 580" ,"\n"
                if len(m)==8 and turn==3:
                     print "Your Score is 560","\n"
                if len(m)==8 and turn==2:
                     print "Your Score is 540","\n"
                if len(m)==8 and turn==1:
                     print "Your Score is 520","\n"
                if len(m)==9 and turn==5:
                     print "Your Score is 700","\n"
                if len(m)==9 and turn==4:
                     print "Your Score is 680" ,"\n"
                if len(m)==9 and turn==3:
                     print "Your Score is 660","\n"
                if len(m)==9 and turn==2:
                     print "Your Score is 640","\n"
                if len(m)==9 and turn==1:
                     print "Your Score is 620","\n"
                if len(m)==10 and turn==5:
                     print "Your Score is 800","\n"
                if len(m)==10 and turn==4:
                     print "Your Score is 780" ,"\n"
                if len(m)==6 and turn==3:
                     print "Your Score is 760","\n"
                if len(m)==10 and turn==2:
                     print "Your Score is 740","\n"
                if len(m)==10 and turn==1:
                     print "Your Score is 720","\n"
                if len(m)>10 and turn>1:
                     print "Your score is 850" ,"\n" #Point Pattern
                print "Thank You",x
                break
        
        else:                                   #if the gueessed word is not in the origina word
            print "Wrong","\n"
            turn=turn-1
            print "You Have",turn,"Turns Left","\n"
            if turn==0:
                 print "Sorry",x,"You Loose The Game, Should INcrease Your Word Power","\n"
                 print "Word Was",m,"\n"
                 print "Thank You",x

if m in output:
    c=list(m)
    print "Related to Output in the field of Technology","\n"
    i=0
    k=" "
    while i < (len(c)-1): #Creating an empty string of same length as the original word
        k=k+" "
        i=i+1
    g=list(k)             #Converting the string to list
    print g
    print "One Letter In The Word is:- ",c[1],"\n" #For giving a hint
    while turn>0:
        gu=raw_input("Enter the character:- ")
        if gu in c:
            z=0
            while z<len(c):
                if c[z]==gu:
                    g[z]=gu
                    print g
                    c[z]=" "   #Replacing the correct guessed word with blank space
                    z+=1
                    break
                    
                else:
                    z+=1 
            d=d-1              #Reducing the length of original word
            print "Letters left:- ",d,"\n"
            guess=guess+gu
            if turn!=0 and d==0:
                print "HURRAY YOU WON THE GAME,CONGRATUALTION!!!",x,"\n"
                print "Word is",m,"\n"
                if len(m)==3 and turn==5:           #Point Pattern
                     print "your Score is 100","\n"
                if len(m)==3 and turn==4:
                     print "your Score is 80" ,"\n"
                if len(m)==3 and turn==3:
                     print "your Score is 60","\n"
                if len(m)==3 and turn==2:
                     print "your Score is 40","\n"
                if len(m)==3 and turn==1:
                     print "your Score is 20","\n"
                if len(m)==4 and turn==5:
                     print "your Score is 200","\n"
                if len(m)==4 and turn==4:
                     print "your Score is 180" ,"\n"
                if len(m)==4 and turn==3:
                     print "your Score is 160","\n"
                if len(m)==4 and turn==2:
                     print "your Score is 140","\n"
                if len(m)==4 and turn==1:
                     print "your Score is 120","\n"
                if len(m)==5 and turn==5:
                     print "your Score is 300","\n"
                if len(m)==5 and turn==4:
                     print "your Score is 280" ,"\n"
                if len(m)==5 and turn==3:
                     print "your Score is 260","\n"
                if len(m)==5 and turn==2:
                     print "your Score is 240","\n"
                if len(m)==5 and turn==1:
                     print "your Score is 220","\n"
                if len(m)==6 and turn==5:
                     print "your Score is 400","\n"
                if len(m)==6 and turn==4:
                     print "your Score is 380" ,"\n"
                if len(m)==6 and turn==3:
                     print "your Score is 360","\n"
                if len(m)==6 and turn==2:
                     print "your Score is 340","\n"
                if len(m)==6 and turn==1:
                     print "your Score is 320","\n"
                if len(m)==7 and turn==5:
                     print "your Score is 500","\n"
                if len(m)==7 and turn==4:
                     print "your Score is 480" ,"\n"
                if len(m)==7 and turn==3:
                     print "your Score is 460","\n"
                if len(m)==7 and turn==2:
                     print "your Score is 440","\n"
                if len(m)==7 and turn==1:
                     print "your Score is 420","\n"
                if len(m)==8 and turn==5:
                     print "your Score is 600","\n"
                if len(m)==8 and turn==4:
                     print "your Score is 580" ,"\n"
                if len(m)==8 and turn==3:
                     print "your Score is 560","\n"
                if len(m)==8 and turn==2:
                     print "your Score is 540","\n"
                if len(m)==8 and turn==1:
                     print "your Score is 520","\n"
                if len(m)==9 and turn==5:
                     print "your Score is 700","\n"
                if len(m)==9 and turn==4:
                     print "your Score is 680" ,"\n"
                if len(m)==9 and turn==3:
                     print "your Score is 660","\n"
                if len(m)==9 and turn==2:
                     print "your Score is 640","\n"
                if len(m)==9 and turn==1:
                     print "your Score is 620","\n"
                if len(m)==10 and turn==5:
                     print "your Score is 800","\n"
                if len(m)==10 and turn==4:
                     print "your Score is 780" ,"\n"
                if len(m)==10 and turn==3:
                     print "your Score is 760","\n"
                if len(m)==10 and turn==2:
                     print "your Score is 740","\n"
                if len(m)==10 and turn==1:
                     print "your Score is 720","\n"
                if len(m)>10 and turn>1:         
                    print "your score is 850","\n"  #Point Pattern
                print "Thank You",x
                break
        
        else:
            print "Wrong","\n"
            turn=turn-1
            print "You Have",turn,"Turns Left","\n"
            if turn==0:
                 print "Sorry",x,"You Loose The Game, Should Increase Your Word Power","\n"
                 print "Word Was",m,"\n"
                 print "Thank You",x


if m in sports:
    c=list(m)
    print "Related to Sports Game","\n"
    i=0
    k=" "
    while i < (len(c)-1):
        k=k+" "                #Creating an empty string
        i=i+1
    g=list(k)                   #Converting the string to list
    print g
    print "One Letter In The Word is:- " ,c[1],"\n"
    while turn>0:                 #Main loop
        gu=raw_input("Enter the character:- "),"\n"
        if gu in c:
            z=0
            while z<len(c):
                if c[z]==gu:
                    g[z]=gu
                    print g
                    c[z]=" "      #Replacing the correct guessed character with blank soace
                    z+=1
                    break
                    
                else:
                    z+=1 
            
            d=d-1
            print "Letters Left",d,"\n"
            guess=guess+gu
            if turn!=0 and d==0:
                print "HURRAY YOU WON THE GAME,CONGRATUALTION!!!",x,"\n"
                print "Word Is",m
                if len(m)==3 and turn==5:         #Point Pattern
                     print "your Score is 100","\n"
                if len(m)==3 and turn==4:
                     print "your Score is 80","\n"
                if len(m)==3 and turn==3:
                     print "your Score is 60","\n"
                if len(m)==3 and turn==2:
                     print "your Score is 40","\n"
                if len(m)==3 and turn==1:
                     print "your Score is 20","\n"
                if len(m)==4 and turn==5:
                     print "your Score is 200","\n"
                if len(m)==4 and turn==4:
                     print "your Score is 180","\n"
                if len(m)==4 and turn==3:
                     print "your Score is 160","\n"
                if len(m)==4 and turn==2:
                     print "your Score is 140","\n"
                if len(m)==4 and turn==1:
                     print "your Score is 120","\n"
                if len(m)==5 and turn==5:
                     print "your Score is 300","\n"
                if len(m)==5 and turn==4:
                     print "your Score is 280" ,"\n"
                if len(m)==5 and turn==3:
                     print "your Score is 260","\n"
                if len(m)==5 and turn==2:
                     print "your Score is 240","\n"
                if len(m)==5 and turn==1:
                     print "your Score is 220","\n"
                if len(m)==6 and turn==5:
                     print "your Score is 400","\n"
                if len(m)==6 and turn==4:
                     print "your Score is 380" ,"\n"
                if len(m)==6 and turn==3:
                     print "your Score is 360","\n"
                if len(m)==6 and turn==2:
                     print "your Score is 340","\n"
                if len(m)==6 and turn==1:
                     print "your Score is 320","\n"
                if len(m)==7 and turn==5:
                     print "your Score is 500","\n"
                if len(m)==7 and turn==4:
                     print "your Score is 480" ,"\n"
                if len(m)==7 and turn==3:
                     print "your Score is 460","\n"
                if len(m)==7 and turn==2:
                     print "your Score is 440","\n"
                if len(m)==7 and turn==1:
                     print "your Score is 420","\n"
                if len(m)==8 and turn==5:
                     print "your Score is 600","\n"
                if len(m)==8 and turn==4:
                     print "your Score is 580" ,"\n"
                if len(m)==8 and turn==3:
                     print "your Score is 560","\n"
                if len(m)==8 and turn==2:
                     print "your Score is 540","\n"
                if len(m)==8 and turn==1:
                     print "your Score is 520","\n"
                if len(m)==9 and turn==5:
                     print "your Score is 700","\n"
                if len(m)==9 and turn==4:
                     print "your Score is 680" ,"\n"
                if len(m)==9 and turn==3:
                     print "your Score is 660","\n"
                if len(m)==9 and turn==2:
                     print "your Score is 640","\n"
                if len(m)==9 and turn==1:
                     print "your Score is 620","\n"
                if len(m)==10 and turn==5:
                     print "your Score is 800","\n"
                if len(m)==10 and turn==4:
                     print "your Score is 780" ,"\n"
                if len(m)==6 and turn==3:
                     print "your Score is 760","\n"
                if len(m)==10 and turn==2:
                     print "your Score is 740","\n"
                if len(m)==10 and turn==1:
                     print "your Score is 720","\n"
                if len(m)>10 and turn>1:
                     print "your score is 850","\n" #Point Pattern
                print "Thank You",x
                break
        
        else:
            print "Wrong","\n"
            turn=turn-1
            print "You Have",turn,"Turns Left","\n"
            if turn==0:
                 print "Sorry",x,"You Loose The Game, Should Increase your Word Power","\n"
                 print "Word Was",m,"\n"
                 print "Thank You",x





    
       
        
          
                
            
