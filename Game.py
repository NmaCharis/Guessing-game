#GUESSING GAME - Is all about guessing a number between 1 to 100.
#define a function for the game
def number_guessing_games_for_students ():

#We will print the instructions or explanation of the game
  print ("welcome to my brainteaser game!")
  print("Tell us the number you are thinking of right now.......")
  print("Remember you have only 3 attempts to guess the number correctly!")

#We will set our secret number
  my_secret_number = 33
#We set the number of attempts the students will make, this is the maximum number of guesses by each player
  num_of_attempts = 5
#We are going to create the loop for the game 
  while num_of_attempts > 0:
    try:
      your_guess = int(input("Can you enter your ({num_of_attempts}) number here: ")) #We are asking a student to enter a number, convert it to an interger
      num_of_attempts -=1 # the attempts is reducing by one after each guess
#Logical check on the guessed number
      if your_guess < my_secret_number:
         print("PLEASE YOUR NUMBER IS TOO LOW")
      elif your_guess > my_secret_number:
        print("PLEASE YOUR NUMBER IS TOO HIGH!!!!!!!")
      else:
        print(f"Congratulations you have guess it right, and the number is {my_secret_number}")
        break
    except ValueError:
      print("Your guess is invalid!!!!!!!") #The students guessed a letter instead of a number  
