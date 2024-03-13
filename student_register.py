# Pseudo Code with instructions:
# Create a file called student_register.py
# ● Overview: Write a program that allows a user to register students for an exam venue.
# ● Ask the user how many students are registering.
# - Use input validation functions to fetch user values.
# ● Create a for loop that runs for that number of students.
# ● Each time the loop runs the program should ask the user to enter the next student ID number.
# - Ask the user if its okay to overwrite the file if it already exists
# - Ask the user the character length limit for the student I.D to prevent large/accidental inputs
# - Ensure there are no duplicates
# ● Write each of the ID numbers to a text file called reg_form.txt
# ● Include a dotted line after each student ID because this document will be used as an attendance
# register, which the students will sign when they arrive at the exam venue.
#===================================================================================================
import re

def get_integer(prompt):
    """Ask user for valid whole number"""
    while True:
        try:
            user_input = input(prompt)
            user_input = int(user_input) # Try to convert input to an integer
            # Validation: Ensure the input meets additional criteria
            if user_input < 0:
                print("Please enter a non-negative number.")
            else:
                return user_input # Return valid input if all conditions are met

        except ValueError:
            print("Invalid input. Please enter a valid number.")
#===================================================================================================
def basic_alphabet_input(prompt):
    """Basic keyboard input validation"""
    while True:
        try:
            input_string = input(prompt)
            # Basic keyboard character set
            pattern = re.compile(r'^[a-zA-Z]+$')
            if re.match(pattern, input_string):
                    return input_string
            else:
                print("Input contains invalid characters.")
        except ValueError:
            print("Input does not meet requirements.")
#===================================================================================================
def user_choice(option):
    """Yes or no boolean choice input function (y/n) - non case sensitive"""
    while True:
        try:
            user_input = input(option)
            # Capital letter acceptance/conversion
            user_input = user_input.lower()
            if user_input == "n":
                print("You have selected no.")
                return False
            elif user_input == "y":
                print("You have selected yes.")
                return True # Return valid input if all conditions are met
            else:
                print("Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a valid option.")
#===================================================================================================
def items_in_list(existing_list, limit):
    """Checks if input has already been entered, appends acceptable value to list for referencing"""
    while True:
        user_input = get_integer("Enter a value: ")
        # Cast validated number input to string to get input length
        length_of_input = len(str(user_input))
        # Invalid if the input exists in list or is too long
        if user_input in existing_list or length_of_input > limit:
            print(f"Can't add I.D: '{user_input}'. Please enter a different value.")
        else:
            existing_list.append(user_input)
            print(f"I.D: '{user_input}' has been added to the list.")
            return user_input
#===================================================================================================
def main():
    """Main function with the core logic"""
    # Unicode dashed low line character as ASCII value
    dotted_line = 5 * chr(65101)
    # Fetch total students
    total_students = get_integer("Please enter the total number of students who plan to sit the exam: \n")
    print(f"{total_students} entries will be created.")
    # Fetch student I.D limit
    id_limit = get_integer("What is the character limit of the student I.D? \n")
    # Ensure user is aware the program will overwrite the file if it exists
    proceed = user_choice("If the file exists, would you like to overwrite the data? y/n: \n")
    display_list = user_choice("Would you like to view the list of I.D's successfully added? y/n: \n")
    # Main file writing for loop
    if proceed:
        with open('reg_form.txt', 'w+', encoding='utf-8') as file:
            added_id = []
            counter = 0
            # Iterate through the number of students until total reached
            while counter != total_students:
                # Iterate for each student in total students
                for student_id in range(0, total_students):
                    # Add the type of exam
                    student_exam = basic_alphabet_input("Enter the students phone number: ")
                    # Student I.D declared if not already in added I.D list
                    student_id = items_in_list(added_id, id_limit)
                    # Cast I.D to string to compare the length to the input limit integer
                    student_id_string = str(student_id)
                    # If the I.D is the right length or less, add it to the file
                    if len(student_id_string) <= id_limit:
                        #for i in range(id_limit):
                        while len(student_id_string) < id_limit:
                            student_id_string = "0" + student_id_string
                            #print(student_id_string)
                        file.write(f"Exam: {student_exam}:{student_id_string}:{dotted_line}\n")
                        # Display added I.D and full list of current I.D's
                        if display_list:
                            print(f"Current List of I.D's added: {added_id}")
                        counter += 1
                    else:
                        print("The value you entered was not valid, please try again.")

    print("The registration form has been completed.")
#===================================================================================================
main()
