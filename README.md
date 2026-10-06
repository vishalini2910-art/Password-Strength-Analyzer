# Password Strength Analyzer

A beginner-friendly Python mini project that evaluates the strength of a user-entered password.

## Features

- Checks password length.
- Checks for uppercase letters.
- Checks for lowercase letters.
- Checks for numbers.
- Checks for special characters.
- Gives a strength rating: Weak, Medium, or Strong.
- Checks whether the password has already been used in this project.
- Generates a strong random password suggestion.
- Stores only a SHA-256 hash when password history is enabled.
- Never stores the original password in the history file.

## Project Structure

```text
password-strength-analyzer/
│
├── app.py
├── README.md
└── password_history.txt   # created automatically after saving a password
```

## Requirements

- Python 3.9 or newer
- No external Python packages are required.

## How to Run

1. Install Python if it is not already installed.
2. Open this project folder in VS Code.
3. Open the VS Code terminal.
4. Run:

```bash
python app.py
```

If `python` does not work on Windows, try:

```bash
py app.py
```

## Example

```text
====================================
      PASSWORD STRENGTH ANALYZER
====================================
Enter a password to analyze: Hello@123

--- Password Analysis ---
Length >= 8       : PASS
Uppercase letter  : PASS
Lowercase letter  : PASS
Number            : PASS
Special character : PASS
Score             : 5/5
Strength           : Strong
Unique in this project: YES

Your password meets the basic strength checks.
```

## How It Works

The program gives one point for each basic requirement:

1. At least 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character

Scoring:

- 0–2: Weak
- 3–4: Medium
- 5: Strong

The project also uses `secrets` to generate stronger random password suggestions.

## Password Reuse Protection

When the user chooses `y` to save the password, the program stores a SHA-256 hash in `password_history.txt` instead of storing the actual password.

This demonstrates a basic security principle: **do not store plaintext passwords**.

> Important: This is an educational mini project, not a production-grade password manager or authentication system. Real applications should use a password-hashing algorithm designed for password storage, such as Argon2id, scrypt, or bcrypt, together with proper salting and secure authentication practices.

## Technologies Used

- Python
- `string`
- `secrets`
- `hashlib`
- `pathlib`

All of these are part of Python's standard library.

## Learning Outcomes

After completing this project, you can explain:

- Password complexity
- Password strength scoring
- Password reuse
- Cryptographic hashing
- SHA-256
- Secure random password generation
- Why plaintext password storage is unsafe

## GitHub Upload

After testing the program:

```bash
git init
git add .
git commit -m "Add Password Strength Analyzer"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your own GitHub repository URL.

## Disclaimer

This project is intended for educational purposes and basic cybersecurity learning.
