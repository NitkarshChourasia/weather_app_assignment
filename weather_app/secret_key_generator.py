import secrets

def generate_secret_key():
    return secrets.token_hex(2048)


if __name__ == "__main__":
    print(generate_secret_key())