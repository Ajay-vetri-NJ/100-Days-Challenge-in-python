from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key
def save_keys(private_key, public_key):
    pem_private_key = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
    with open("private_key.pem", "wb") as pem_file:
        pem_file.write(pem_private_key)
    pem_public_key = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    with open("public_key.pem", "wb") as pem_file:
        pem_file.write(pem_public_key)
def encrypt_message(public_key, message):
    encrypted_message = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return encrypted_message
def decrypt_message(private_key, encrypted_message):
    decrypted_message = private_key.decrypt(encrypted_message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return decrypted_message
def main():
    print("Welcome to the RSA Encryption and Decryption Program!")
    text = input("Enter the text to encrypt: ").encode('utf-8')
    private_key, public_key = generate_keys()
    save_keys(private_key, public_key)
    encrypted_text = encrypt_message(public_key, text)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt_message(private_key, encrypted_text)
    print("Decrypted text:", decrypted_text.decode('utf-8'))
if __name__ == "__main__":
    main()