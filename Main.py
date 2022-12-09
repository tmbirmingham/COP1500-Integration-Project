# Tim Birmingham
# Quiz game for COP 1500

# Creating a function to progress the game when player is ready to continue
def ready_to_move_on():
    """Tim Birmingham"""
    want_to_continue = False
    check_loop = input("Type 'READY' when you want to continue. ANYTHING OTHER THAN 'ready or READY' will end game. ")
    if (check_loop == "READY") or (check_loop == "ready"):
        want_to_continue = True
    return want_to_continue


def test(stop_or_go):
    if stop_or_go == False:
        exit()


# defining main, will call to it later
def main():
    """
    Author
    Tim Birmingham
    """
    print("Welcome to the quiz game of COP 1500!")
    print("It is a short multiple choice quiz with questions about the programming language python")
    print("Our goal here is to have some fun and learn a little about python along the way")

    # Printing a new line to make the output look nicer and easier to read
    print('\n')
    player_name = input("Please enter your name: ")
    print(player_name, "thanks for playing today!", sep=',')
    user_choice = ready_to_move_on()
    test(user_choice)
    print("\n")

    # initialize the scoreboard to be 0 so that accurate count can be made
    player_score = 0

    # QUESTION 1
    print(" QUESTION 1: When performing a calculation using basic numeric operators, what does '**' do?")
    question = input("(A) Divide (B) Assign (C) Exponentiation (D) All of the above ")
    # using comparison operators to check if the answer is correct
    # using an if else statement to determine what to do if the answer is correct and if the answer is incorrect
    if question == "C" or question == "c":
        print("Holy smokes! +1 point")
        player_score = player_score + 1
    else:
        print("Good guess, but no.")
    print("The ** operator represents exponentiation. This means by using ** you can raise a variable"
          " (x) to a power (y).")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 2
    print("QUESTION 2: When performing a calculation using basic numeric operators, what does + do?")
    question = input("(A) Addition (B) Subtraction (C) Integrate (D) None of the above ")
    if question == "A" or question == "a":
        print("Nice job!", player_name, sep=' ')
        player_score = player_score + 1
    else:
        print("Sorry, that is not the answer I was looking for.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 3
    print("QUESTION 3: What does = mean in Python language?")
    question = input("(A) Calculate (B) Launch (C) Assignment (D) Configure ")
    if question == "C" or question == "c":
        print("Holy smokes! +1 point")
        player_score = player_score + 1
    else:
        print("Good guess, but no.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # some questions include an optional example to further explain the concept asked about in the question
    # QUESTION 4
    print("QUESTION 4: What does the % operator do in python?")
    question = input("(A) Percentage (B) Modulus (C) Subtract (D) None of the above ")
    if question == "B" or question == "b":
        print("I thought this was an amateur quiz... +1 point!")
        player_score = player_score + 1
    else:
        print("Incorrect.")
    print("The modulus operator (%) in python is used to give the remainder that is left over when dividing, x % y")
    example = input("Want an example? ")
    if example == "YES" or example == "yes":
        try:
            number1 = int(input("Enter a number: "))
            number2 = int(input("Enter another number: "))
            print(number1 % number2)
        except:
            print("ERROR OCCURRED. QUIZ WILL CONTINUE WITHOUT EXAMPLE, SORRY FOR INCONVENIENCE.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # if the user answers C on this question, it will take them to an explanation of the concept
    # QUESTION 5
    print("QUESTION 5: When working with strings, what does the * operator do?")
    question = input("(A) Repetition (B) Concatenation (C) Not sure (D) None of the above ")
    if question == "A" or question == "a":
        print("Nice job!", player_name, sep=' ')
        player_score = player_score + 1
    elif question == "C":
        print("Sorry, that is not the answer I was looking for")
        print("Let's see an example for this one")
        words = input("Please enter a word: ")
        number_example = int(input("Please enter a number: "))
        print(words * number_example)
        print("The * when working with strings will repeat the string multiple times in a row.")
    else:
        print("Sorry, that is not the answer I was looking for")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 6
    print("QUESTION 6: When working with numbers, what does the * operator do?")
    question = input("(A) Adds numbers (B) Subtracts numbers (C) Changes the datatype (D) Multiplies numbers ")
    if question == "D" or question == "d":
        print("Okay who told you all the answers? +1 point")
        player_score = player_score + 1
    else:
        print("Don't fret, still more questions to come")
    print("The * multiplies numbers together: x * y")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 7
    print("QUESTION 7: The operator for dividing numbers is which of the following")
    question = input("(A) // (B) λ (C) <= (D) / ")
    if question == "D" or question == "d":
        print("Okay who told you all the answers? +1 point")
        player_score = player_score + 1
    else:
        print("Don't fret, still more questions to come")
    print("The / is used for regular division when dealing with numbers: x / y")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 8
    print("QUESTION 8: What does the numeric operator // represent?")
    question = input("(A) Division (B) Multiplication (C) Floor Division (D) All of the above ")
    if question == "A" or question == "a":
        print("Nice job!", player_name, sep=' ')
        player_score = player_score + 1
    else:
        print("Sorry, that is not the answer I was looking for")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 9
    print("QUESTION 9: When dealing with strings, what does the + operator do?")
    question = input("(A) Adds them (B) Concatenates them (C) Multiplies them (D) Divides them ")
    if question == "B" or question == "b":
        print("I thought this was an amateur quiz... +1 point!")
        player_score = player_score + 1
    else:
        print("Incorrect.")
    print("Concatenation takes two or more strings and links them together")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 10
    print("QUESTION 10: What is the numeric operator for subtraction in python?")
    question = input("(A) = (B) - (C) + (D) * ")
    if question == "B" or question == "b":
        print("I thought this was an amateur quiz... +1 point!")
        player_score = player_score + 1
    else:
        print("Incorrect.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 11
    print("QUESTION 11: The > means that the left side is greater than the right side, x > y.")
    print("(A) True (B) False")
    question = input("A FOR TRUE B FOR FALSE. ")
    if question != "B" or question == "b":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
    print("Just like in math, the > means that the left side is greater than the right side")
    print("An example would be 10 > 3")
    print("The same goes for other comparison operators: < > == != >= <=")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 12
    print("QUESTION 12: The boolean operator 'AND' requires only one of the arguments to be correct to be True?")
    print("(A) True (B) False")
    question = input("A FOR TRUE B FOR FALSE. ")
    if question != "B" or question != "b":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
    print("The 'AND' operator requires both arguments to be correct in order for the statement to be True.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 13
    print("QUESTION 13: The boolean operator 'OR' requires only one of the arguments to be correct to be True?")
    print("(A) True (B) False")
    question = input("A FOR TRUE B FOR FALSE. ")
    if question != "B" or question != "b":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
    print("The 'OR' operator requires only one of the arguments to be correct in order for the statement to be True.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 14
    print("QUESTION 14: The boolean operator 'NOT' requires neither of the arguments to be correct to be True?")
    print("(A) True (B) False")
    question = input("A FOR TRUE B FOR FALSE. ")
    if question != "B" or question != "b":
        print("Nice job! + 1 point to", player_name)
        player_score = player_score + 1
    else:
        print("Sorry, incorrect.")
    print("The 'NOT' operator requires neither of the arguments to be correct in order for the statement to be True.")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 15
    print("QUESTION 15: Can you use a loop to make an inverted triangle?")
    print("(A) Yes (B) No")
    question = input("A for Yes B for No. ")
    if question != "B" or question != "b":
        print("Yes +1 point")
        player_score = player_score + 1
    else:
        print("Wrong, you can!")
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
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 16
    print("QUESTION 16: What do the three numbers in a range function do?")
    question = input("(A) Start (B) Stop (C) Step (D) All of the above ")
    if question == "D" or question == "d":
        print("Okay who told you all the answers? +1 point")
        player_score = player_score + 1
    else:
        print("Don't fret, still more questions to come")
    print(
        "The range() function returns a sequence of numbers, starting at 0 and going to the specified number by 1 step")
    print("For example, if you were to say 'for x in range(1,9,3)' it would count from 1 to 9 in intervals of 3")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # QUESTION 17
    print("QUESTION 17: Can you write a program to calculate area and circumference of a circle?")
    question = input("(A) Yes (B) No (C) Only on the third Monday of the month. ")
    if question == "A" or question == "a":
        print("You're really good at this game, +1 point")
        player_score = player_score + 1
    else:
        print("sorry, incorrect.")
    print("It is possible to write a program to find the circumference and area of a circle using parameter passing")
    print("\n")
    user_choice = ready_to_move_on()
    test(user_choice)

    # WRAP UP THE GAME
    print("Well, we would like to thank you for playing today", player_name)
    print("The final score of the game is", player_name + ":", player_score, "Point(s)!")
    print("I hope you enjoyed your time here and maybe learned a thing or two")
    print("Until next time, have a good night.")


main()