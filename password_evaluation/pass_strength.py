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
		print("Password is weak because it's common")
		return

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

	print("Strength of password: ", end = "")

	if (same):
		print("Very Weak")
	elif (has_lower and has_upper and has_digit and special_char and n >= 8):
		print("Strong")
	elif ((has_lower or has_upper) and special_char and n >= 6):
		print("Medium")
	elif (has_lower or has_upper or has_digit):
		print("Weak")
	else:
		print("Very Weak")



if __name__ == "__main__":
	password = "P@ssw0rd123"
	username = "kokoshterev"
	password_evaluation(password, username)


