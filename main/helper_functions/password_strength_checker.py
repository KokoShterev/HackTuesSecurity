def password_evaluation(password, username):
    n = len(password)

    has_lower = False
    has_upper = False
    has_digit = False
    special_char = False
    normal_chars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    same = False
    with open("common_passwords.txt", "r") as f:
        passwords = f.read()
    if password in passwords:
        return 1

    for i in range(n):
        if password[i].islower():
            has_lower = True
        if password[i].isupper():
            has_upper = True
        if password[i].isdigit():
            has_digit = True
        if password[i] not in normal_chars:
            special_char = True
    if username in password or password in username:
        same = True

    print("Strength of password: ", end="")

    if (same):
        return 2
    elif (has_lower and has_upper and has_digit and special_char and n >= 8):
        return 5
    elif ((has_lower or has_upper) and special_char and n >= 6):
        return 4
    elif (has_lower or has_upper or has_digit):
        return 3
    else:
        return 2