#the expected number
n = 18

#starting statement
print("Sixth sense game - You have only 7 guesses")
guess = int(input())
number_of_guesses = 0

#The While loop
while (True):

        #increases the number of guesses attempt by attempt.
        number_of_guesses = number_of_guesses+1


        #This is what happens if you get the correct answer - 
        if guess == n:
            print("Congrats!! You won by guessing the right number. You took", number_of_guesses, " attempts to guess.")
            break
        

        #If the number is greater than the expected number -
        elif guess > n:
            print("The number is less than", guess, ". You have", 7- number_of_guesses, "attempts left")
            guess = int(input())
            continue
        
        
        #If the number is less than the expected number -
        else:
            if guess < n:
                print("The number is greater than", guess, ". You have", 7- number_of_guesses, "attemps left")
                guess = int(input())
                continue



        if number_of_guesses == 7:
            print("Game over. Because you ran out of guesses")
            break
