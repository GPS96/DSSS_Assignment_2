import random

#The given function generates a random number within the given parameter range of min and max.
def random_integer(min, max):
    """

    Parameters:
        -min(int): The lower bound
        -max(int): The upper bound

    Return: Random integer within the defined range of min and max

    """
    return random.randint(min, max)


#The given function selects a random operator from the given choices of operators from add, subtract, and multiply.
def random_operator():
    """

    Parameters: None

    Return: Random operator from the given choices of operators

    """
    return random.choice(['+', '-', '*'])


#The given function processes the Mathematical quiz, performs operations based on the selected operator, and provides if the
#answer is correct or not.
def math_quiz_calculator(n1, n2, operator):
    """

    Parameters:
        - n1 (int): The first number from the random integer function.
        - n2 (int): The second number from the random integer function.
        - operator: The operator ('+', '-', or '*') from the random operator function

    Return:
        A string showing the problem statement (problem) and the correct answer for it.

    """

    problem = f"{n1} {operator} {n2}"
    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer

def math_quiz():
    #Initialize the score for the users and set the total number of questions in the quiz
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Create the set of problems and display them as a string
    for _ in range(total_questions):
        number_1 = random_integer(1, 10)
        number_2 = random_integer(1, 6)
        operator = random_operator()

        problem, answer = math_quiz_calculator(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")

    #Initializing the user input with a default value
        user_answer= None

    #Error handling where the users will be warned if they entered a non-integer value.

        while user_answer is None:  #The while loop is given to ensure that users get chances to give the correct format of inputs.
            try:
                user_answer = int(input("Your answer: "))
            except ValueError:
                print("The given input is invalid. Please enter an integer.")

    #Checking if the answer provided by the user is correct or not
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1  #Score increases by 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
