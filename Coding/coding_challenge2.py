### Kush Patel ###
# Airport PIN Checker
# Rules:
# 1. PIN must contain only digits
# 2. PIN must be exactly 4 digits long
# 3. First digit must be even
# 4. Last digit must be '5'
# 5. Sum of all digits must equal 20
# After 5 incorrect attempts, the terminal locks

MAX_ATTEMPTS = 5
attempts = 0

while attempts < MAX_ATTEMPTS:
    pin = input("Enter 4-digit PIN: ")

    if not pin.isdigit():
        attempts += 1
        print(f"PIN must be numeric. System reset. Attempts left: {MAX_ATTEMPTS - attempts}\n")
        continue

    if len(pin) != 4:
        attempts += 1
        print(f"PIN must be exactly 4 digits. System reset. Attempts left: {MAX_ATTEMPTS - attempts}\n")
        continue

    if int(pin[0]) % 2 != 0:
        attempts += 1
        print(f"First digit must be even. System reset. Attempts left: {MAX_ATTEMPTS - attempts}\n")
        continue

    if pin[3] != "5":
        attempts += 1
        print(f"Last digit must be 5. System reset. Attempts left: {MAX_ATTEMPTS - attempts}\n")
        continue

    if sum(int(d) for d in pin) != 20:
        attempts += 1
        print(f"Invalid PIN sum. System reset. Attempts left: {MAX_ATTEMPTS - attempts}\n")
        continue

    print("Access granted.")
    print("FLAG{airport_pin_unlocked}")
    break

else:
    print("ERROR: Too many failed attempts.")

#sample answer = 4655
