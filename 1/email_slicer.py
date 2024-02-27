email = input("Enter your email address: ").strip()
email = email.split('@')
print("USERNAME:",email[0])
print("DOMAIN:",email[1])