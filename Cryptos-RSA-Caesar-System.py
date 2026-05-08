import math

# -------------------------------
# Check if number is prime
# -------------------------------
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# -------------------------------
# RSA Helper (Extended Euclid)
# -------------------------------
def get_private_key(e, phi):
    """Calculate private key d"""
    d_old, d_new = 0, 1
    phi_old, phi_new = phi, e

    while phi_new != 0:
        quotient = phi_old // phi_new
        phi_old, phi_new = phi_new, phi_old - quotient * phi_new
        d_old, d_new = d_new, d_old - quotient * d_new

    return d_old % phi


# -------------------------------
# Caesar Cipher
# -------------------------------
def caesar_cipher(text, shift, mode='encrypt'):
    """Encrypt or decrypt using Caesar Cipher"""
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            p = ord(char) - base
            c = (p + shift) % 26
            result += chr(c + base)
        else:
            result += char

    return result


# -------------------------------
# RSA Encryption
# -------------------------------
def rsa_encrypt(text, e, n):
    """Encrypt message using RSA"""
    encrypted = []

    for char in text:
        m = ord(char)

        if m >= n:
            raise ValueError("n must be greater than ASCII values")

        c = pow(m, e, n)
        encrypted.append(c)

    return encrypted


# -------------------------------
# RSA Decryption
# -------------------------------
def rsa_decrypt(cipher_list, d, n):
    """Decrypt RSA message"""
    decrypted = ""

    for num in cipher_list:
        m = pow(num, d, n)
        decrypted += chr(m)

    return decrypted


# -------------------------------
# Main Program
# -------------------------------
def main():
    while True:
        print("\n=== Cryptography System ===")
        print("1. Caesar Cipher")
        print("2. RSA Algorithm")
        print("3. Exit")

        choice = input("Select an option: ")

        # Caesar
        if choice == '1':
            try:
                msg = input("Enter text: ")
                shift = int(input("Enter shift value: "))

                encrypted = caesar_cipher(msg, shift, 'encrypt')
                decrypted = caesar_cipher(encrypted, shift, 'decrypt')

                print("Encrypted:", encrypted)
                print("Decrypted:", decrypted)

            except ValueError:
                print("Invalid input!")

        # RSA
        elif choice == '2':
            try:
                msg = input("Enter text: ")

                p = int(input("Enter prime p: "))
                q = int(input("Enter prime q: "))
                e = int(input("Enter public key e: "))

                if not is_prime(p) or not is_prime(q):
                    print("p and q must be prime!")
                    continue

                n = p * q
                phi = (p - 1) * (q - 1)

                if math.gcd(e, phi) != 1:
                    print("e must be coprime with phi!")
                    continue

                d = get_private_key(e, phi)

                print(f"n = {n}, phi = {phi}, d = {d}")

                encrypted = rsa_encrypt(msg, e, n)
                print("Encrypted:", encrypted)

                decrypted = rsa_decrypt(encrypted, d, n)
                print("Decrypted:", decrypted)

            except ValueError as err:
                print("Error:", err)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()