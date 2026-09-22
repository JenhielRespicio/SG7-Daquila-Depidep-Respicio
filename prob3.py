# SET OF ACCEPTED VALUES
valid_grade_levels = [7, 8, 9, 10, 11, 12]

# INPUT STAGE - PROMPT ASKS FOR GRADE LEVEL
grade_level = int(input("Enter your grade level: "))

# CONDITION - TO VALIDATE THE INPUT
if grade_level in valid_grade_levels:
    print("Valid grade level.")
else:
    print("Invalid grade level.")