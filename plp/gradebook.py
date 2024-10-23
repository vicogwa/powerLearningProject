# Define the weightings for different components of the grade
weights = {'test': 50, 'quizzes': 20, 'homework': 30}

# Dictionary to store students' grades as tuples (test_score, quiz_score, homework_score)
students = {'seyi': (90, 80, 75), 'tope': (100, 80, 90)}

def initialize():
    """
    Display the main menu and get the user's selection.
    Returns:
        int: The selected menu option.
    """
    while True:  # Loop until a valid integer input is received
        try:
            print("Welcome to your grade book! Make a selection: ")
            selection = int(input("1: Modify weights, 2: Add students, 3: View grades, 4: Exit "))
            if selection in [1, 2, 3, 4]:  # Check if the input is within the valid options
                return selection
            else:
                print("Please enter a valid option (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")

def modify_weights():
    """
    Allows the user to modify the weighting of test, quizzes, and homework.
    """
    print("The current weighting is " + str(weights))
    repeat = input("Would you like to modify this? (yes/no): ")

    # Loop to modify weights until the user is satisfied
    while repeat == 'yes':
        modify = input("What item would you like to modify? (test/quizzes/homework) ")
        
        # Update the selected weight
        weights[modify] = int(input("Enter the new weight for the item: "))
        print("The current weighting is " + str(weights))
        
        # Ask if the user wants to modify another item
        repeat = input("Would you like to modify again? (yes/no): ")

def add_students():
    """
    Allows the user to add a new student along with their scores.
    """
    student_name = input("Enter the student's name: ")
    
    # Get the student's scores for test, quiz, and homework
    test_score = int(input("Enter the student's test score (0-100): "))
    quiz_score = int(input("Enter the student's quiz score (0-100): "))
    homework_score = int(input("Enter the student's homework score (0-100): "))
    
    # Store the scores in a tuple and add to the students dictionary
    grades = (test_score, quiz_score, homework_score)
    students[student_name] = grades
    print("Current student table is: " + str(students))

def view_grades():
    """
    Displays the current grade for a specific student based on the weights.
    """
    student_name = input("Enter the name of the student you want to view: ")
    
    # Check if the student exists in the dictionary
    if student_name in students:
        # Retrieve the student's scores
        grades = students[student_name]
        test_score = grades[0]
        quiz_score = grades[1]
        homework_score = grades[2]
        
        # Calculate the final grade based on the weights
        final_grade = (weights["test"] * test_score / 100) + \
                      (weights["quizzes"] * quiz_score / 100) + \
                      (weights["homework"] * homework_score / 100)
        
        # Display the student's grade
        print(f"{student_name} is currently getting a {final_grade:.2f} in the class.")
    else:
        print("Student not found.")

# Start the program by showing the menu
action = initialize()

# Loop to keep showing the menu until the user decides to exit (option 4)
while action != 4:
    if action == 1:
        modify_weights() 
    elif action == 2:
        add_students()   
    elif action == 3:
        view_grades()      
    else:
        print("Invalid selection. Please try again.")
    
    # Show the menu again after performing an action
    action = initialize()

# End the program
print("Thanks for using the grade book!")
