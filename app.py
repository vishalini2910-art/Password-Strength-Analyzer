import string
import secrets
import hashlib
from pathlib import Path

HISTORY_FILE = Path("password_history.txt")


def check_uniqueness(password):
    """Check whether this password has been used before in this project."""
    if not HISTORY_FILE.exists():
        return True

    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    old_hashes = HISTORY_FILE.read_text(encoding="utf-8").splitlines()
    return password_hash not in old_hashes


def save_password_hash(password):
    """Store only a SHA-256 hash, never the actual password."""
    password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    with HISTORY_FILE.open("a", encoding="utf-8") as file:
        file.write(password_hash + "\n")


def evaluate_password(password):
    length_ok = len(password) >= 8
    upper_ok = any(char.isupper() for char in password)
    lower_ok = any(char.islower() for char in password)
    digit_ok = any(char.isdigit() for char in password)
    special_ok = any(char in string.punctuation for char in password)

    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "length": length_ok,
        "uppercase": upper_ok,
        "lowercase": lower_ok,
        "digit": digit_ok,
        "special": special_ok,
        "score": score,
        "strength": strength,
    }


def generate_strong_password(length=14):
    length = max(8, length)

    groups = [
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation,
    ]

    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)
    password_chars += [
        secrets.choice(all_chars)
        for _ in range(length - len(password_chars))
    ]

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def display_result(result):
    print("\n--- Password Analysis ---")
    print(f"Length >= 8       : {'PASS' if result['length'] else 'FAIL'}")
    print(f"Uppercase letter  : {'PASS' if result['uppercase'] else 'FAIL'}")
    print(f"Lowercase letter  : {'PASS' if result['lowercase'] else 'FAIL'}")
    print(f"Number            : {'PASS' if result['digit'] else 'FAIL'}")
    print(f"Special character : {'PASS' if result['special'] else 'FAIL'}")
    print(f"Score             : {result['score']}/5")
    print(f"Strength           : {result['strength']}")


def main():
    print("====================================")
    print("      PASSWORD STRENGTH ANALYZER")
    print("====================================")

    password = input("Enter a password to analyze: ")

    if not password:
        print("Password cannot be empty.")
        return

    result = evaluate_password(password)
    display_result(result)

    unique = check_uniqueness(password)
    print(f"Unique in this project: {'YES' if unique else 'NO (already used)'}")

    if result["strength"] != "Strong" or not unique:
        print("\nSuggested stronger password:")
        suggestion = generate_strong_password()
        print(suggestion)
    else:
        suggestion = None
        print("\nYour password meets the basic strength checks.")

    save_choice = input(
        "\nSave this password's hash to prevent reuse? (y/n): "
    ).strip().lower()

    if save_choice == "y":
        if unique:
            save_password_hash(password)
            print("Password hash saved. The original password was not stored.")
        else:
            print("This password is already in the history file.")

    print("\nThank you for using Password Strength Analyzer!")


if __name__ == "__main__":
    main()
