import re

def assess_password_strength(password):
    length = len(password)
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    numbers = bool(re.search(r'[0-9]', password))
    special_chars = bool(re.search(r'[^A-Za-z0-9]', password))

    score = 0

    if length >= 8:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if numbers:
        score += 1
    if special_chars:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

# Example usage
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
