#!/usr/bin/env python3
"""
Example script demonstrating programmatic use of the PasswordChecker class
"""

from password_checker import PasswordChecker

def main():
    """Demonstrate the PasswordChecker API"""
    
    checker = PasswordChecker()
    
    # List of example passwords to test
    test_passwords = [
        ("abc", "Very weak password"),
        ("password", "Common password"),
        ("Password1", "Missing special characters"),
        ("Pass@123", "Short but has variety"),
        ("MySecureP@ssw0rd2024", "Strong password"),
    ]
    
    print("=" * 70)
    print("Password Checker API Example")
    print("=" * 70 + "\n")
    
    for password, description in test_passwords:
        print(f"Testing: '{password}' - {description}")
        result = checker.assess_password(password)
        
        print(f"  Strength: {result['strength']}")
        print(f"  Score: {result['score']}/{result['max_score']} ({result['percentage']:.1f}%)")
        
        if result['weaknesses']:
            print(f"  Weaknesses: {', '.join(result['weaknesses'])}")
        
        if result['suggestions']:
            print(f"  Suggestions: {result['suggestions'][0]}")
        
        print()

if __name__ == "__main__":
    main()
