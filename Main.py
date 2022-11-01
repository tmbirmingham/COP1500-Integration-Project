# Timothy Birmingham CRN 80597
# Quiz game that will ask questions related to Python
# Inspiration drawn from group in class

print(
    "Hello and welcome to the quiz of COP 1500!")  # printing the welcome statements and introducing myself. by using
# print() I can type out what I want to display to the shell
print("I am your host Tim!")
print("Throughout this game, I will ask questions about some of the functions we have covered in COP 1500.")
player_name = input(
    "Please enter name of player: ")  # By assigning the variable player_name with an input statement, I can have the
# user input a name for me to store in the location known as "player_name"
print(player_name, "thank you for playing today!", sep=', ')
print("Without further ado, let's get right into the questions!")
print(
    "=================================================================================================================================================================================================================================")
# I did this line for formatting purposes ^ I understand there are probably easier ways to change the look of the output, but for now I went with this as well as printing a large amount of spaces later on

# keep track of score throughout the game, start at 0
player_score = 0  # I had a hard time figuring out how to do a running scoreboard but after many different things tried I think this simple counting works
# tyler pointed out to me that the variable name updates with the most recent actions done to it

# Question 1- exponentation operator with numbers
print("Question 1", end=':')  # by using the end= function, I can format the way that I want the lines to be printed
print("When performing a calculation using basic numeric operators, what does ** do?",
      "Is it (A) Divide (B) Assign (C) Exponentation (D) All of the above")
question_one = input("Please type answer as capital letter: ")

# if and else statements check to see whether or not a certain criteria are met and depending on whether or not it is met, has multiple paths that the code can go
# if the value is true, it will execute the code under the if. Alternatively, if the value is false, it will execute the code under the else.
if question_one == "C":
    print("Very good! +1 point to", player_name, sep=' ')
    player_score = player_score + 1  # by using the same variable name, the score will keep a running total of the points that the player has

else:
    print("No, I'm sorry that is incorrect")
    player_score = player_score + 0  # no points are awarded for incorrect answers, not entirely sure if I needed to define that, but I figured it was better safe than sorry

print("The ** operator represents exponentation. This means by using ** you can raise a variable (x) to a power (y).")
print("The score is as follows:", player_name, player_score, "point(s)!",
      sep=' ')  # using the sep= function, I can format the way I want a series of strings to be set up
print("Moving along now")
print(
    "                                                                                                                                                                                                                                  ")
# The line above is the print statement with a bunch of spaces to format the output into a more user friendly manner

# question 2- addition operator with numbers
print("When performing a calculation using basic numeric operators, what does + do?",
      "Is it (A) Addition (B) Subtraction (C) Integrate (D) None of the above.")
question_two = input("Please type answer as capital letter: ")

if question_two == "A":
    print("Holy smokes, you're good! +1 point to", player_name, sep=' ')
    player_score = player_score + 1
else:
    print("hmmm, not the answer I was looking for. The correct answer is A, Addition.")
    player_score = player_score + 0

print("The operator + represents addition. This means you can add variables together x + y.")
print("Score so far is:", player_name, player_score, "point(s)!", sep=' ')
print("Let's see what other questions we have in store tonight.")
print(
    "                                                                                                                                                                                                                                  ")

# Question number 3- assignment operator with numbers
print("In the real world, = means equals, but in python world, = means which of the following?",
      "Is it (A) Calculate (B) Launch (C) Assignment (D) Configure", sep=' ')
question_three = input("Please type answer as a capital letter: ")

if question_three == "C":
    print("WOWWEEE!! Good job", player_name, "Add another point to your score", sep=", ")
    player_score = player_score + 1

else:
    print("Incorrect, don't be too disappointed there is still a lot of game to be played!")
    player_score = player_score + 0

print(
    "The operator = in python language represents assingment. This is used when assigning a value to a variable x = 1.")
print("The score so far is", player_name, player_score, "point(s)!", sep=' ')
print(
    "                                                                                                                                                                                                                                  ")

# Question number 4- modulus operator with numebers
print("For this question, we are looking to see what happens when we use the % operator in numeric calculations",
      "Is it (A) Percentage (B) Modulus (C) Subtract (D) Skip.", sep=', ')
question_four = input("Please enter answer as a capital letter: ")

if question_four == "B":
    print("You my friend are on a roll", player_name, "Another +1", sep=', ')
    player_score = player_score + 1

else:
    print("Wrong... That's okay, everyone loves an underdog!")
    player_score = player_score + 0

print(
    "The % or modulus operator, when used in python, gives the user the remainder that is given when the left hand operand is divided by the right hand operand x % y.")
print("The score so far is", player_name, player_score, "point(s)!", sep=' ')
print("Next question!")
print(
    "                                                                                                                                                                                                                                  ")

# question number 5- repetition operator with strings
print("Question number 5: When working with strings, what does the * operator do?",
      "Is it (A) Repetition (B) Concatenation (C) Not sure (D) None of the above")
question_five = input("Please type answers as a capital letter: ")

if question_five == "A":
    print("Alright, who gave you the answer key?", "Very good +1 point", sep=' ')
    player_score = player_score + 1
else:
    print("Negative. Good try though!")
    player_score = player_score + 0

print(
    "Working with strings is a little different than other datatypes, the * operator when working with strings means repetition, useful if you wanted to print something many times!")
print("Many times!" * 3)
print("The score so far is", player_name, player_score, "point(s)!", sep=' ')
print(
    "We are now in our second half of the game, if you are doing well, good job! If you were hoping to do better, here is your chance!")
print(
    "                                                                                                                                                                                                                                  ")

# question number 6- multiplication operator with numbers
print("Question number 6 goes back to numeric operators. When using the * operator, what does it do?",
      "(A) Adds the two numbers (B) Subtracts the two numbers (C) Changes the datatype of the numbers (D) Multiplies the numbers")
question_six = input("Please enter answer as a capital letter: ")

if question_six == "D":
    print("I thought this was an amateur quiz...", "Good job,", player_name, "+1 point", sep=' ')
    player_score = player_score + 1

else:
    print("Hang tight", player_name, "we're almost done for the day.", sep=', ')
    player_score = player_score + 0

print(
    "This was a tough one, I threw it in right after the string version of it to confuse you. The * operator when dealing with numbers in python simply multiplies them x * y.")
print("The score to this point is", player_name, player_score, "point(s)!", sep=' ')
print("Next question!")
print(
    "                                                                                                                                                                                                                                  ")

# question number 7- division operator with numbers
print("The numeric operator for division is which of the following?", "Is it (A) // (B) <= (C) λ (D) /")
question_seven = input("Please enter answer as a capital letter: ")

if question_seven == "D":
    print("*sighs* Nice", "another +1 point for", player_name, sep=' ', end='. ')
    player_score = player_score + 1

else:
    print("Sorry, no", end='. ')
    player_score = player_score + 0

print("The operator / represents division and allows two numbers to be divided into eachother x / y.")
print("The score to this point is", player_name, player_score, "point(s)!", sep=' ')
print("Two questions left, let's keep rolling!")
print(
    "                                                                                                                                                                                                                                  ")

# question number 8- floor division operator
print("The numeric operator // represents what? ", "(A) Division (B) Multiplication (C) Floor Division (D) Integration")
question_eight = input("Please enter answer as a capital letter: ")

if question_eight == "C":
    print("Nice!! Good!! Excellent!!", "+1 point", player_name, sep=' ')
    player_score = player_score + 1

else:
    print("Well if you wanted to get that one wrong, you did a great job!")
    player_score = player_score + 0

print(
    "Floor division is slightly different from regular division in that it takes the answer and rounds it down to the whole number.")
print("The score so far is", player_name, player_score, "point(s)!", sep=' ')
print("Continuing on...")
print(
    "                                                                                                                                                                                                                                  ")

# question number 9- concatenation with strings
print("Coming back to string datatypes, what does the + do when dealing with strings?",
      "Is it (A) Adds them (B) Concatenates them (C) Multiplies them (D) Divides them")
question_nine = input("Please enter answer as a capital letter: ")

if question_nine == "B":
    print("Good job. 🍪 Here is a cookie.. oh and +1 point")
    player_score = player_score + 1

else:
    print("Didn't get that one? Don't trip chocolate chip, we still have one more question left.")
    player_score = player_score + 0

print(
    "When working with string datatypes, concatenation is the process of making a new string from the two separate strings before.")
print("Going into the final round, the scores are", player_name, player_score, "point(s)!", sep=' ')
print("Going into our final stretch, last question, lets make it count!")
print(
    "                                                                                                                                                                                                                                  ")

# question number 10- subtraction operator with numbers
print(
    "Last question of the day here, deals with numeric values again, what is the numeric operator for subtraction in python?",
    "Is it (A) = (B) - (C) + (D) *")
question_ten = input("Please enter answer as a capital letter: ")

if question_ten == "B":
    print("Congratulations!", player_name, "+1", sep=' ')
    player_score = player_score + 1
else:
    print("Shame we couldn't finish the last one with a right answer but thats okay!")
    player_score = player_score + 0

print(
    "The operator for subtraction when dealing with numeric values is -, it allows a number to be subtracted from another, x - y.")
print("Thank you for playing today, the final score is as follows:", player_name, player_score, "point(s)!",
      sep=' ')  # output of final score and thanks for playing
