def classify_age_group(age):
    """
    Classifies a person into an age group based on their age.
    Args:
        age (int): The age of the person.
    Returns:
        str: The age group.
    """
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Take input from the user
try:
    age_input = int(input("Enter the age: "))
    group = classify_age_group(age_input)
    print(f"The person is classified as: {group}")
except ValueError:
    print("Please enter a valid integer for age.")
