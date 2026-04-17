### Kush Patel ###
print("Welcome to the Boarding Pass Validator!")
print("")
print("""Rules:
1. Code must be exactly 10 characters long
2. First character must be 'A'
3. Characters at positions 4–6 must be 'GTE'
4. Sum of ASCII values of all characters must equal 700""")

code = input("Enter boarding pass code: ")
print("Validating your boarding pass...")
if len(code) != 10:
    print("Invalid length")
elif code[0] != "A":
    print("Invalid start character")
elif code[3:6] != "GTE":
    print("Invalid gate code")
elif sum(ord(c) for c in code) != 700:
    print("Invalid checksum")
else:
    print("FLAG{boarding_pass_approved}")   
