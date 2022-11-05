# Tim Birmingham
# Quiz game for COP 1500

# Creating a function to progress the game when player is ready to continue
def ready_to_move_on():
    want_to_continue = False
    while want_to_continue == False:
        check_loop = input("Type 'READY' when you want to continue. ")
        if (check_loop == "READY") or (check_loop == "ready"):
            want_to_continue = True


# defining main, will call to it later
def main():
    print("Welcome to the quiz game of COP 1500!")
    print("It is a short multiple choice quiz with questions about the programming language python")
    print("Our goal here is to have some fun and learn a little about python along the way")
    # Making a PSA that answers should be submitted as a capital letter for easy grading
    print("We ask that you please enter all answers as a capital letter.")
    # Printing a new line to make the output look nicer and easier to read
    print('\n')
    player_name = input("Please enter your name: ")
    print(player_name, "thanks for playing today!", sep=',')
    ready_to_move_on()
    print("\n")

    # initialize the scoreboard to be 0 so that accurate count can be made
    player_score = 0

    # QUESTION 1
    print(" QUESTION 1: When performing a calculation using basic numeric operators, what does '**' do?")
    print("(A) Divide (B) Assign (C) Exponentiation (D) All of the above")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    # using comparison operators to check if the answer is correct
    # using an if else statement to determine what to do if the answer is correct and if the answer is incorrect
    if question == "C":
        print("Holy smokes! +1 point")
        player_score = player_score + 1
    else:
        print("Good guess, but no.")
        player_score = player_score + 0
    print(
        "The ** operator represents exponentiation. This means by using ** you can raise a variable (x) to a power (y).")
    print("\n")
    ready_to_move_on()

    # each question has a similar format, question with multiple answer choices and then little explanation for answer
    # QUESTION 2
    print("QUESTION 2: When performing a calculation using basic numeric operators, what does + do?")
    print("(A) Addition (B) Subtraction (C) Integrate (D) None of the above")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "A":
        print("Nice job!", player_name, sep=' ')
        player_score = player_score + 1
    else:
        print("Sorry, that is not the answer I was looking for")
        player_score = player_score + 0
    print("\n")
    ready_to_move_on()

    # QUESTION 3
    print("QUESTION 3: In the real world, = means equals, what does it mean in python language?")
    print("(A) Calculate (B) Launch (C) Assignment (D) Configure")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "C":
        print("Holy smokes! +1 point")
        player_score = player_score + 1
    else:
        print("Good guess, but no.")
        player_score = player_score + 0
    print("\n")
    ready_to_move_on()

    # some questions include an optional example to further explain the concept asked about in the question
    # QUESTION 4
    print("What does the % operator do in python?")
    print("(A) Percentage (B) Modulus (C) Subtract (D) None of the above")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "B":
        print("I thought this was an amateur quiz... +1 point!")
        player_score = player_score + 1
    else:
        print("Incorrect.")
        player_score = player_score + 0
    print("The modulus operator (%) in python is used to give the remainder that is left over when dividing, x % y")
    example = input("Want an example? ")
    if example == "YES" or example == "yes":
        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        print(number1 % number2)
    else:
        print("Very well then.")
    print("\n")
    ready_to_move_on()

    # if the user answers C on this question, it will take them to an explanation of the concept
    # QUESTION 5
    print("QUESTION 5: When working with strings, what does the * operator do?")
    print("(A) Repetition (B) Concatenation (C) Not sure (D) None of the above")
    question = input("PLEASE ENTER ANSWER AS A CAPITAL LETTER. ")
    if question == "A":
        print("Nice job!", player_name, sep=' ')
        player_score = player_score + 1
    elif question == "C":
        print("Sorry, that is not the answer I was looking for")
        print("Let's see an example for this one")
        words = input("Please enter a word: ")
        number_example = int(input("Please enter a number: "))
        print(words * number_example)
    else:
        print("Sorry, that is not the answer I was looking for")
        player_score = player_score + 0
    print("\n")
    ready_to_move_on()

    # QUESTION 6
    print("QUESTION 6: When working with numbers, what does the * operator do?")
    print("(A) Adds numbers (B) Subtracts numbers (C) Changes the datatype (D) Multiplies numbers")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "D":
        print("Okay who told you all the answers? +1 point")
        player_score = player_score + 1
    else:
        print("Don't fret, still more questions to come")
        player_score = player_score + 0
    print("The * multiplies numbers together: x * y")
    print("\n")
    ready_to_move_on()

    # QUESTION 7
    print("QUESTION 7: The operator for dividing numbers is which of the following")
    print("(A) // (B) λ (C) <= (D) /")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "D":
        print("Okay who told you all the answers? +1 point")
        player_score = player_score + 1
    else:
        print("Don't fret, still more questions to come")
        player_score = player_score + 0
    print("The / is used for regular division when dealing with numbers: x / y")
    print("\n")
    ready_to_move_on()

    # QUESTION 8
    print("QUESTION 8: What does the numeric operator // represent?")
    print("(A) Division (B) Multiplication (C) Floor Division (D) All of the above")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "A":
        print("Nice job!", player_name, sep=' ')
        player_score = player_score + 1
    else:
        print("Sorry, that is not the answer I was looking for")
        player_score = player_score + 0
    print("\n")
    ready_to_move_on()

    # QUESTION 9
    print("QUESTION 9: When dealing with strings, what does the + operator do?")
    print("(A) Adds them (B) Concatenates them (C) Multiplies them (D) Divides them")
    question = input("PLEASE ENTER ANSWER AS CAPITAL LETTER. ")
    if question == "B":
        print("I thought this was an amateur quiz... +1 point!")
        player_score = player_score + 1
    else:
        print("Incorrect.")
        player_score = player_score + 0
    print("Concatenation takes two or more strings and links them together")
    print("\n")
    ready_to_move_on()

    # QUESTION 10
    print("QUESTION 10: What is the numeric operator for subtraction in python?")
    print("(A) = (B) - (C) + (D) *")
    question = input("PLEASE ENTER ANSWER AS A CAPITAL LETTER. ")
    if question == "B":
        print("I thought this was an amateur quiz... +1 point!")
        player_score = player_score + 1
    else:
        print("Incorrect.")
        player_score = player_score + 0
    print("\n")
    ready_to_move_on()

    # QUESTION 11
    print("QUESTION 11: The > means that the left side is greater than the right side, x > y.")
    print("(A) True (B) False")
    question = input("ENTER ANSWER AS A CAPITAL LETTER, A FOR TRUE B FOR FALSE. ")
    if question != "B":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
        player_score = player_score + 0
    print("Just like in math, the > means that the left side is greater than the right side")
    print("An example would be 10 > 3")
    print("The same goes for other comparison operators: < > == != >= <=")
    print("\n")
    ready_to_move_on()

    # I had some difficulty wording some questions, will revise and improve phrasing
    # QUESTION 12
    print("QUESTION 12: The boolean operator 'AND' requires only one of the arguments to be correct to be True?")
    print("(A) True (B) False")
    question = input("ENTER ANSWER AS A CAPITAL LETTER, A FOR TRUE B FOR FALSE. ")
    if question != "A":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
        player_score = player_score + 0
    print("The 'AND' operator requires both arguments to be correct in order for the statement to be True.")
    print("\n")
    ready_to_move_on()

    # QUESTION 13
    print("QUESTION 13: The boolean operator 'OR' requires only one of the arguments to be correct to be True?")
    print("(A) True (B) False")
    question = input("ENTER ANSWER AS A CAPITAL LETTER, A FOR TRUE B FOR FALSE. ")
    if question != "B":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
        player_score = player_score + 0
    print("The 'OR' operator requires only one of the arguments to be correct in order for the statement to be True.")
    print("\n")
    ready_to_move_on()

    # QUESTION 14
    print("QUESTION 14: The boolean operator 'NOT' requires neither of the arguments to be correct to be True?")
    print("(A) True (B) False")
    question = input("ENTER ANSWER AS A CAPITAL LETTER, A FOR TRUE B FOR FALSE. ")
    if question != "B":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
        player_score = player_score + 0
    print("The 'NOT' operator requires neither of the arguments to be correct in order for the statement to be True.")
    print("\n")
    ready_to_move_on()

    # QUESTION 15
    print("QUESTION 15: Can you use a loop to make an inverted triangle?")
    print("(A) yes (B) No")
    question = input("ENTER ANSWER AS CAPITAL LETTER. ")
    if question != "B":
        print("Yes +1 point")
        player_score = player_score + 1
    else:
        print("Wrong, you can!")
        player_score = player_score + 0
    print("using a nested loop, it is possible to create an inverted triangle")
    print("\n")
    question = input("Want to see an inverted triangle? ")
    if question == "yes" or question == "YES":
        rows = int(input("Enter a number in between 3 and 15: "))
        print("\n")
        for height in range(1, rows + 1):
            accumulator = 0
            rows = rows - 1
            for length in range(rows + 1):
                print(accumulator + 1, end=" ")
                accumulator = accumulator + 1
            print()
    else:
        print("Ha, your loss.")
    print("\n")
    ready_to_move_on()

    # QUESTION 16
    print("QUESTION 16: What do the three numbers in a range function do?")
    print("(A) Start (B) Stop (C) Step (D) All of the above")
    question = input("ENTER ANSWER AS A CAPITAL LETTER. ")
    if question == "D":
        print("Okay who told you all the answers? +1 point")
        player_score = player_score + 1
    else:
        print("Don't fret, still more questions to come")
        player_score = player_score + 0
    print(
        "The range() function returns a sequence of numbers, starting at 0 and going to the specified number by 1 step")
    print("For example, if you were to say 'for x in range(1,9,3)' it would count from 1 to 9 in intervals of 3")
    print("\n")
    ready_to_move_on()

    # QUESTION 17
    print("QUESTION 17: Can you write a program to calculate area and circumference of a circle?")
    print("(A) Yes (B) No (C) Only on the third Monday of the month")
    question = input("ENTER ANSWER AS A CAPITAL LETTER. ")
    if question == "A":
        print("You're really good at this game, +1 point")
        player_score = player_score + 1
    else:
        print("sorry, incorrect.")
        player_score = player_score + 0
    print("It is possible to write a program to find the circumference and area of a circle using parameter passing")
    print("\n")
    ready_to_move_on()

    # WRAP UP THE GAME
    print("Well, we would like to thank you for playing today", player_name)
    print("The final score of the game is", player_name + ":", player_score, "Point(s)!")
    print("I hope you enjoyed your time here and maybe learned a thing or two")
    print("Until next time, have a good night.")


main()
