def xor_encrypt(data, key):
    key = key.encode()
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

plaintext = b"""P: Dulles Tower, good day, N980JQ at parking, aircraft type C172. Request IFR clearance to KRDU with information Q.
P: Flag{Cleared for take off}
C - Cleared to KRDU via 
R - TAPPA V287 ANTNY RDU KRDU
A - 2', expect 7' 5"
F - 118.6
T - 4444
ATC: N980JQ readback correct, contact ground 112.6 for taxi
P: Contact ground at 112.6
"""
#ATC: N980JQ Cleared to KRDU via TAPPA V287 ANTNY RDU KRDU, climb and maintain 2 thousand, expect 7 thousand 5 hundred 10 minutes after departure. Call approach on 118.5, squawk 4444.
cipher = xor_encrypt(plaintext, "TOWER")

with open("blackbox.bin", "wb") as f:
    f.write(cipher)