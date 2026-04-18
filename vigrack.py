#!/usr/bin/env python3
import numpy as np
ciphtxt = input("Provide the Ciphertext: ")
#COMPARING LETTER FREQUENCES TO FIND BEST FIT FOR KEY ( the one that has the lowest X score).
freqArray = np.array([
    8.12, 1.49, 2.71, 4.32, 12.02, 2.3, 2.03, 5.92, 7.31, 0.1, 0.69, 3.92, 2.61,
    6.95, 7.68, 1.82, 0.11, 6.02, 6.28, 9.10, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07
])
key=""
bestX = float('inf')
length = 0
for posKeyLen in range(1,10):#Brute force method for finding key length and the key itself, basically whichever key gives us the lowest X^2 is the one that we will decrypt with (length and text).
    X_after_test = 0
    tempkey = ""
    for i in range(posKeyLen):
        textSl = ciphtxt[i::posKeyLen].lower()#We slice the text for every possible key length(for example if posKeyLength is 3 we take every 3rd character of the text.
        textSlLength = len(textSl)
        count = np.zeros(26)#Initializing a count list for letter's appearance.
        for char in textSl: 
            if 'a'<=char<='z':
                count[ord(char)-ord('a')] += 1 #By subtracting the char's ASCII table value with a's ASCII table value we find in which index the count will go up.
        X = float('inf') # We initialize with a big value for the comparisons afterwards.(finding the min value)
        bestShift = 0 # Initializing shift so that we can find the one that gives us the lowest X^2 score(that's the best one). 
        for shift in range(26):#We try each possible rotation of letters in the english alphabet.
            freqExp = np.roll(freqArray,shift)#It takes the english frequencies list and shifts them to the right by value=shift.
            X_curr = 0
            for j in range(26):
                expCount = (freqExp[j] / 100)*textSlLength #Converting percentages to decimal point values.
                if expCount > 0:
                    X_curr += (count[j] - expCount)**2/expCount # X^2 formula.
            if X_curr < X:#(finding the min value).
                X = X_curr
                bestShift = shift #The best shift is the one that gave us a low X^2 score. 
        tempkey += chr(ord('a') + bestShift) # Appending to the key the bestShift and converting it from a value back to an english letter.
        X_after_test += X
    avgX = X_after_test/posKeyLen #We normalize by posKeyLen(That's because if we have a test length of 20 the error in the X value will be greater than if we have a value of 3)in order to have a fair comparison.
    print(f"For key length {posKeyLen} X is equal to {avgX:.2f}")
    if avgX<bestX:
        bestX = avgX
        length = posKeyLen
        key = tempkey
print(key)
#DECRYPTION
message =""
for i,char in enumerate(ciphtxt.lower()):
    message += chr((((ord(char) - ord('a')) - (ord(key[i%length])-ord('a')))%26+ord('a')))#Vigenere's decryption formula m = (c - k)%26.
print(message.upper())            
        
                
                

    
    


    
