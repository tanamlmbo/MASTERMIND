import random #random 


def create_code():
    #doc string
    """ Function that creates the 4 digit code,  
        using random digits from 1 to 8"""

    code = [0, 0, 0, 0]

    for i in range(4): #we want to guess 4 numbers
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value #1q234567
    
    return code


def get_answer_input():
    """
    this function is used for checking if you have entered the correct code
    """
    answer = input("Input 4 digit code: ") 
    while len(answer) < 4 or len(answer) > 4: #leb(1234)
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer #1234


def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. ',end="")
    print('You have 12 turns to break it.')


def show_results(correct_digits_and_position, correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ',end="")
    print(str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ', end="")
    print(str(correct_digits_only))


def take_turn(code):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
    """

    answer = get_answer_input() #get your guess 1234
    

    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)): 
        if code[i] == int(answer[i]): #[1234] [1234]
            correct_digits_and_position += 1 
        elif int(answer[i]) in code: #if same
            correct_digits_only += 1

    show_results(correct_digits_and_position, correct_digits_only)
    return correct_digits_and_position, correct_digits_only
    


def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(turns, correct_digits_and_position):
    """Checks correctness of answer and show output to user"""

    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))#tracks how many turns have been taken
        return False

def run_game():
    """Main function for running the game"""

    correct = False

    code = create_code()
    show_instructions()

    turns = 0
   
    while not correct and turns < 12:
        correct_digits_and_position, correct_digits_only = take_turn(code)
        turns += 1
        correct = check_correctness(turns, correct_digits_and_position)

    show_code(code)



if __name__ == "__main__":
    run_game()