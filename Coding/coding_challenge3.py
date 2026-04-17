# TSA Badge Check
# Rules:
# 1) The code must be exactly 9 characters long
# 2) It must start with "TSA{" and end with "}"
# 3) The inside must be exactly 4 uppercase letters A-Z
# 4) The program transforms the inside letters and compares against a target.
# Hint: The transformation is reversible, so there is exactly one valid input.

def shift_forward(ch, amount):
    # caesar shift forward within A-Z
    return chr(((ord(ch) - 65 + amount) % 26) + 65)

def shift_backward(ch, amount):
    # caesar shift backward within A-Z
    return chr(((ord(ch) - 65 - amount) % 26) + 65)

code = input("Enter TSA badge code: ").strip()

# rule 1: length
if len(code) != 9:
    print("Rejected: invalid length")
    exit()

# rule 2: format wrapper
if not (code.startswith("TSA{") and code.endswith("}")):
    print("Rejected: invalid format (expected TSA{....})")
    exit()

inside = code[4:-1]  # 4 characters between { and }

# rule 3: inside must be 4 uppercase letters
if len(inside) != 4 or not inside.isalpha() or not inside.isupper():
    print("Rejected: inner code must be 4 uppercase letters (A-Z)")
    exit()

# rule 4: transform then compare
# transform steps:
#   a) reverse the 4-letter string
#   b) shift each character forward by its position index (1..4)
reversed_inside = inside[::-1]
transformed = ""
for i, ch in enumerate(reversed_inside):
    transformed += shift_forward(ch, i + 1)

TARGET = "QODV"  # target transform output

if transformed != TARGET:
    print("Rejected: badge checksum mismatch")
    exit()

print("Access granted: Secure corridor unlocked.")
print("FLAG{tsa_badge_solution}")


#answer = "TSA{RAMP}"
