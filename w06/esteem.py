""" Calculates the user's level of self-esteem out of 30 pts """

print()

def main():

    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")

    score = ask_questions()

    print(f"Your final score is {score}")
    print("A score below 15 may indicate problematic low self-esteem.")

def ask_questions():
    """ This program asks the user 10 questions and uses the results to give a score of self-esteem from 0 to 30.
    Questions 1, 2, 4, 6, and 7 are positive questions, so agreeing gives a higher score.
    Questions 3, 5, 8, 9, and 10 are negative questions, so disagreeing gives a higher score.
    Returns: the total score (out of 30)
    """
        
    questions = [
        "I feel that I am a person of worth, at least on an equal plane with others.",
        "I feel that I have a number of good qualities.",
        "All in all, I am inclined to feel that I am a failure.",
        "I am able to do things as well as most other people.",
        "I feel I do not have much to be proud of.",
        "I take a positive attitude toward myself.",
        "On the whole, I am satisfied with myself.",
        "I wish I could have more respect for myself.",
        "I certainly feel useless at times.",
        "At times I think I am no good at all."
    ]

    score = 0

    print()

    # asks the questions and collects the results
    for i in range(len(questions)):

        # asks the question
        answer = input(questions[i] + "\nAnswer: ")

        # for the positive questions, D = 0, d = 1, so on
        if i in (0, 1, 3, 5, 6):
            if answer == "D":
                score += 0
            elif answer == "d":
                score += 1
            elif answer == "a":
                score += 2
            elif answer == "A":
                score += 3
                
        # for negative questions, D = 3, d = 2, so on
        elif i in (2, 4, 7, 8, 9):
            if answer == "D":
                score += 3
            elif answer == "d":
                score += 2
            elif answer == "a":
                score += 1
            elif answer == "A":
                score += 0

    return(score)
                

if __name__ == "__main__":
    main()

    print()