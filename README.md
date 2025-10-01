# SCT_CS_3-PasswordChecker

**SkillCraft Cybersecurity Internship – Task 3**  
**Author:** CHERUPALLI MANI KARTHIK  
**Domain:** Cybersecurity AND blockchain

## Overview

A comprehensive password strength assessment tool that evaluates passwords based on multiple security criteria. This tool helps users create stronger passwords by providing detailed feedback and actionable suggestions.

## Features

- **Length Analysis**: Evaluates password length with graduated scoring
- **Character Type Detection**: Checks for:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **Pattern Detection**: Identifies common weaknesses:
  - Sequential characters (abc, 123)
  - Repeated characters (aaa, 111)
  - Common passwords (password, qwerty, admin)
- **Visual Feedback**: 
  - Color-coded strength indicators
  - Progress bar visualization
  - Detailed criterion breakdown
- **Actionable Suggestions**: Provides specific recommendations for improvement

## Installation

No external dependencies required! Just Python 3.6 or higher.

```bash
# Clone the repository
git clone https://github.com/dino50687/SCT_CS_3-PasswordChecker.git
cd SCT_CS_3-PasswordChecker

# Make the script executable (optional)
chmod +x password_checker.py
```

## Usage

### Interactive Mode

Run the password checker in interactive mode:

```bash
python3 password_checker.py
```

Then enter passwords to check. Type `quit`, `exit`, or `q` to exit.

### Example Session

```
Enter a password to check (or 'quit' to exit): weak

============================================================
PASSWORD STRENGTH ASSESSMENT
============================================================

Strength: WEAK
Score: 1/8 (12.5%)
[█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]

Criteria Analysis:
  ✗ Length: Too short (minimum 6 characters)
  ✗ Uppercase: No uppercase letters
  ✓ Lowercase: Contains lowercase letters (4)
  ✗ Numbers: No numbers
  ✗ Special Characters: No special characters

💡 Suggestions for Improvement:
  • Increase length to at least 8 characters
  • Add uppercase letters (A-Z)
  • Add numbers (0-9)
  • Add special characters (!@#$%^&*)
```

## Password Strength Criteria

### Scoring System

The tool uses an 8-point scoring system:

- **Length** (0-3 points):
  - 0 points: < 6 characters
  - 1 point: 6-7 characters
  - 2 points: 8-11 characters
  - 3 points: 12+ characters

- **Character Types** (0-4 points):
  - 1 point: Contains uppercase letters
  - 1 point: Contains lowercase letters
  - 1 point: Contains numbers
  - 1 point: Contains special characters

- **Pattern Detection** (reduces strength):
  - Sequential characters
  - Repeated characters
  - Common password patterns

### Strength Levels

- **EMPTY**: No password entered
- **WEAK**: Score ≤ 2 or contains common patterns
- **MEDIUM**: Score 3-4
- **STRONG**: Score 5-6
- **VERY STRONG**: Score 7-8 with no weaknesses

## Examples

### Weak Password
```
Password: password123
Strength: WEAK
Issues: Contains common pattern "password", sequential numbers
```

### Medium Password
```
Password: MyPass2023
Strength: MEDIUM
Issues: Missing special characters, could be longer
```

### Strong Password
```
Password: MyP@ssw0rd2023
Strength: STRONG
Issues: Sequential numbers detected
```

### Very Strong Password
```
Password: MyS3cur3!P@ssw0rd
Strength: VERY STRONG
All criteria met!
```

## Security Best Practices

1. **Use at least 12 characters** for optimal security
2. **Include all character types**: uppercase, lowercase, numbers, and special characters
3. **Avoid common patterns**: sequential characters, repeated characters, dictionary words
4. **Use unique passwords** for each account
5. **Consider using a password manager** for generating and storing complex passwords
6. **Enable two-factor authentication (2FA)** where available

## Technical Details

- **Language**: Python 3
- **Dependencies**: Standard library only (re, string)
- **Color Output**: ANSI color codes for terminal display
- **Pattern Matching**: Regular expressions for pattern detection

## Contributing

This project is part of the SkillCraft Cybersecurity Internship. Suggestions and improvements are welcome!

## License

This project is created as part of an educational internship program.

## Author

**CHERUPALLI MANI KARTHIK**  
Cybersecurity and Blockchain Intern  
SkillCraft Technology