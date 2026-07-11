import string

# List of common weak passwords
common_passwords = [
    "password", "123456", "12345678", "qwerty",
    "abc123", "admin", "welcome", "letmein"
]

password = input("Enter your password: ")

score = 0
suggestions = []

# Check common password
if password.lower() in common_passwords:
    print("\n⚠ This is a commonly used password!")
    print("Choose another password.")
    exit()

# Length Check
if len(password) >= 8:
    score += 20
else:
    suggestions.append("Use at least 8 characters.")

# Uppercase Check
if any(char.isupper() for char in password):
    score += 20
else:
    suggestions.append("Add at least one uppercase letter.")

# Lowercase Check
if any(char.islower() for char in password):
    score += 20
else:
    suggestions.append("Add at least one lowercase letter.")

# Digit Check
if any(char.isdigit() for char in password):
    score += 20
else:
    suggestions.append("Add at least one number.")

# Special Character Check
if any(char in string.punctuation for char in password):
    score += 20
else:
    suggestions.append("Add at least one special character.")

# Password Strength
if score <= 40:
    strength = "WEAK"
elif score <= 80:
    strength = "MEDIUM"
else:
    strength = "STRONG"

print("\n========== RESULT ==========")
print(f"Password Strength : {strength}")
print(f"Security Score    : {score}/100")

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print(f"- {s}")
else:
    print("\nExcellent! Your password is secure.")