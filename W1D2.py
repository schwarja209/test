

# TODO: Add items to the shopping cart
# Example: Add "apple" with quantity 3
# shopping_cart["apple"] = 3

# TODO: Update quantities of existing items
# Example: Increase quantity of "apple" to 5
# shopping_cart["apple"] = 5

# TODO: Remove an item from the cart
# Example: Remove "apple"
# del shopping_cart["apple"]

# Initialize an empty shopping cart
# shopping_cart = {}

'''
shopping = "Y"
while shopping == "Y":
    item = input("What would you like to add to your shopping cart? ")
    quantity = input(f"How many {item} would you like to add? ")
    shopping_cart[f"{item}"] = int(quantity)
    shopping = input("Would you like to add another item (Y/N)? ")
      
parts = [f"{value} {key}" for key, value in shopping_cart.items()]

if not parts:
    sentence = "Your shopping cart is empty."
elif len(parts) == 1:
    sentence = "You have " + parts[0] + " in your shopping cart."
else:
    sentence = "You have " + ", ".join(parts[:-1]) + ", and " + parts[-1] + " in your shopping cart."
'''
'''    
# TODO: Print out the contents of the cart
# print("Shopping cart contents:")
# print("You have shopping_cart)


# Call your function
# print_pattern()

# Dictionary with student names as keys and scores as values
gradebook = {
    # Example:
    # "Alice": 85,
    # "Bob": 72,
    # "Charlie": 58
}

# TODO: Calculate the average score
# Hint: use sum() and len()

average_score = sum(gradebook.values())/len(gradebook)  # Replace with your code

# TODO: Find the highest score
# Hint: use max() on gradebook.values()

highest_score = max(gradebook.values())  # Replace with your code

# TODO: Create a dictionary with only passing students (score >= 60)

passing_students = {name: score for name, score in gradebook.items() if score >= 60}  # Replace with your code

# Print results
print("Average score:", average_score)
print("Highest score:", highest_score)
print("Passing students:", passing_students)
'''


# # Sets of students enrolled in each course
# course_a_students = {
#     "Alice", "Bob", "Charlie"
# }

# course_b_students = {
#     "Bob", "Diana", "Eve"
# }

# # TODO: Find students enrolled in both courses
# both_courses = course_a_students & course_b_students  # Replace with your code

# # TODO: Find students enrolled in either course
# either_course = course_a_students | course_b_students  # Replace with your code

# # TODO: Find students enrolled in course A but not course B
# only_a = course_a_students - course_b_students   # Replace with your code

# # TODO: Find students enrolled in course B but not course A
# only_b = course_b_students - course_b_students  # Replace with your code

# # Print results
# print("Both courses:", both_courses)
# print("Either course:", either_course)
# print("Only in Course A:", only_a)
# print("Only in Course B:", only_b)


def group_by_domain(email_list):
    """
    Takes a list of email addresses and returns a dictionary
    where keys are domains and values are lists of usernames.
    """
    domain_dict = {}

    for email in email_list:
        username, domain = email.split("@")  # Split into two parts
        if domain not in domain_dict:        # checks uniqueness
            domain_dict[domain] = []         # Initialize the list if not yet present
        domain_dict[domain].append(username) # Add the username to the appropriate domain

    return domain_dict


# Example input (students can add their own)
emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "carol@gmail.com",
    "dave@outlook.com"
]

# Call the function and print the result
result = group_by_domain(emails)
print(result)