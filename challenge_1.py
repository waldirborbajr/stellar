from stellar_sdk import Server, Keypair
import requests

def main():
    pair = Keypair.random()
    print(f"Private Key: {pair.secret}")
    print(f"Public Key: {pair.public_key}")

    mnemonic_phrase = Keypair.generate_mnemonic_phrase()
    print(f"mnemonic_phrase: {mnemonic_phrase}")

if __name__ == "__main__":
    main()
