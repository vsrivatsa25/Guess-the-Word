import random
while True:
    game=int(input("Press 1 to play / Anything else to quit "))
    if game==1:
        #create a list of words of your choice
        words=['executioner','assassination','galactic','insomnia','adsorbant','improvise','overrule','objection','obesity','backwoods','classic', 'mimic', 'behavior', 'applications', 'hebrew', 'customizable', 'implement', 'installing', 'toolbar', 'website', 'instructions']
        #choice is used to select a random element from a given list
        word=random.choice(words)
        leng=len(word)
        theword=str()
        count=0
        #checking if the length of the word is even or odd
        if leng%2==0:
            for i in range(0,leng):
                #randint is used to select a random integer between the specified range
                n=random.randint(0,1)
                if n==0 or count>(leng)/2:
                    theword=theword+'_'
                    
                elif n==1 and count<leng/2:
                    theword=theword+word[i]
                    count+=1
                else:
                    theword=theword+'_'
        if leng%2!=0:
            for i in range(0,leng):
                n=random.randint(0,1)
                if n==0 or count>(leng+1)/2:
                    theword=theword+'_'
                    
                elif n==1 and count<(leng+1)/2:
                    theword=theword+word[i]
                    count+=1
                else:
                    theword=theword+'_'
        print(theword)
        n=0
        i=0
        k=0
        for i in range(0,leng):
            guess=str()
         
            while n>=0:
                c=0
                
                if theword[i]=='_':
                   
                    x=input("Enter your theword")
                    if x==word[i]:
                        print('Correct')
                        for j in range(0,leng):
                            if theword[j]!='_':
                                guess=guess+word[j]
                            elif theword[j]=='_' and c<=k:
                                guess=guess+word[j]
                                c+=1
                            elif theword[j]=='_' and c>k:
                                guess=guess+'_'
                        print(guess)
                        k+=1
                        break
                    else:
                        print('Try Again')
                        print(guess)
                        n+=1
                else:
                    #break statement is used to skip the positions where the letter is already known
                    break
            if i==leng:
                break
        print("You cracked the word in",n,"mistakes")
    else:
        break
    
        
