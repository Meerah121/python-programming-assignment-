def caesar_cipher(text, shift, mode='encrypt'):
    """
    Function to encrypt or decrypt a message using Caesar Cipher.
    Preserves spaces and case.
    """
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            start = ord('A') if char.isupper() else ord('a')
            # Calculate shifted character
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Preserve non-alphabetic characters (like spaces)
            result += char
            
    return result

def main():
    print("--- Caesar Cipher Program ---")
    message = input("Enter message: ")
    try:
        shift_value = int(input("Enter shift value: "))
    except ValueError:
        print("Invalid shift value! Please enter an integer.")
        return
        
    choice = input("Choose mode (encrypt/decrypt): ").lower()
    
    if choice == 'encrypt':
        encrypted = caesar_cipher(message, shift_value, 'encrypt')
        print(f"Encrypted message: {encrypted}")
    elif choice == 'decrypt':
        decrypted = caesar_cipher(message, shift_value, 'decrypt')
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid mode! Defaulting to encryption.")
        encrypted = caesar_cipher(message, shift_value, 'encrypt')
        print(f"Encrypted message: {encrypted}")

if __name__ == "__main__":
    main()
