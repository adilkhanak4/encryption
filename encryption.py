import os

# -------- FILE PATHS --------
RAW_FILE = r"C:/Users/sadaq/OneDrive/Desktop/Project/raw_text.txt"
ENCRYPTED_FILE = "encrypted_text.txt"
DECRYPTED_FILE = "decrypted_text.txt"

def encrypt_char(ch, shift1, shift2):
    # Process Lowercase: shift forward by shift1
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        new_pos = (pos + shift1) % 26
        return chr(new_pos + ord('a'))
    
    # Process Uppercase: shift forward by shift2
    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos + shift2) % 26
        return chr(new_pos + ord('A'))
    
    # Return special characters (spaces, punctuation) unchanged
    return ch

def decrypt_char(ch, shift1, shift2):
    # Process Lowercase: shift backward by shift1
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        new_pos = (pos - shift1) % 26
        return chr(new_pos + ord('a'))
    
    # Process Uppercase: shift backward by shift2
    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos - shift2) % 26
        return chr(new_pos + ord('A'))
    
    # Return special characters unchanged
    return ch

def encrypt_file(shift1, shift2):
    if not os.path.exists(RAW_FILE):
        print(f"File not found: {RAW_FILE}")
        return
    with open(RAW_FILE, "r") as f:
        text = f.read()
    
    encrypted = "".join(encrypt_char(c, shift1, shift2) for c in text)
    
    with open(ENCRYPTED_FILE, "w") as f:
        f.write(encrypted)

def decrypt_file(shift1, shift2):
    if not os.path.exists(ENCRYPTED_FILE):
        return
    with open(ENCRYPTED_FILE, "r") as f:
        text = f.read()
    
    decrypted = "".join(decrypt_char(c, shift1, shift2) for c in text)
    
    with open(DECRYPTED_FILE, "w") as f:
        f.write(decrypted)

def verify_decryption():
    if not os.path.exists(RAW_FILE) or not os.path.exists(DECRYPTED_FILE):
        return False
    with open(RAW_FILE, "r") as f1, open(DECRYPTED_FILE, "r") as f2:
        # strip() is used to avoid failure due to trailing empty lines
        return f1.read().strip() == f2.read().strip()

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    try:
        s1 = int(input("Enter shift1: "))
        s2 = int(input("Enter shift2: "))

        encrypt_file(s1, s2)
        decrypt_file(s1, s2)

        if verify_decryption():
            print("\nDecryption successful! ✅")
        else:
            print("\nDecryption failed ❌")
            # This part helps you see exactly what went wrong
            with open(RAW_FILE, "r") as f: print(f"Expected: {f.read().strip()}")
            with open(DECRYPTED_FILE, "r") as f: print(f"Got:      {f.read().strip()}")
            
    except ValueError:
        print("Please enter valid integers for the shifts.")