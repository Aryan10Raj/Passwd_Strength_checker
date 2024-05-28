import re

def password_strength_check(password):
    # Initialize score and criteria checks
    score = 0
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&#]', password))

    # Evaluate length
    if length_criteria:
        score += 1
    # Evaluate uppercase
    if uppercase_criteria:
        score += 1
    # Evaluate lowercase
    if lowercase_criteria:
        score += 1
    # Evaluate numbers
    if number_criteria:
        score += 1
    # Evaluate special characters
    if special_char_criteria:
        score += 1

    # Determine password strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Example usage
password = input()
strength, feedback = password_strength_check(password)
print("Password Strength:", strength)
if feedback:
    print("Feedback:")
    for tip in feedback:
        print(tip)
