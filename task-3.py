def check_password_strength(password):
    length = len(password)
    special_characters = set("!@#$%^&*()-_=+[]{};:'\",.<>?/|`~")
    strength = 0
    if length >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in special_characters for char in password):
        strength += 1
    if strength >= 5:
        return "Your password is strong."
    else:
        return "Your password is weak. It should have at least 8 characters, one uppercase and one lowercase letter, one digit, and one special character."

password = input("Enter your password: ")
print(check_password_strength(password))
