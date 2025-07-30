import string

# Check if the password is in a common passwords list
def is_common_password(password):
    try:
        with open("rockyou.txt", "r", encoding="latin-1", errors="ignore") as file:
            for line in file:
                if password == line.strip():
                    return True
        return False
    except FileNotFoundError:
        return False


# Calculate password's strength and assign a score
def password_strength(password):
    score = 0
    length = len(password)

    # Check for character types
    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digits]
    # Scoring based on length
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    # Scoring based on variety of characters
    score += sum(characters) - 1

    # Change score if the password is in the common passwords list
    if is_common_password(password):
        score = 0

    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score
    
def feedback(password):
    if is_common_password(password):
        return "Password was found in a common list. Score: 0/7"

    strength, score = password_strength(password)

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback += "- Make your password longer (more than 8 characters). \n"
        if not any(c.isupper() for c in password):
            feedback += "- Include uppercase letters.\n"
        if not any(c.islower() for c in password):
            feedback += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Add numbers.\n"

    return feedback


def main():
    
    print("Password Strength Checker\n")
    password = input("Enter a password to check: ")

    strength, score = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Score: {score}/6")

    if is_common_password(password):
        print("⚠️ This password is very common. Choose a more unique one.")

if __name__ == "__main__":
    main()