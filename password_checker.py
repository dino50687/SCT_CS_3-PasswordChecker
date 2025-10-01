#!/usr/bin/env python3
"""
Password Strength Checker
Author: CHERUPALLI MANI KARTHIK
Domain: Cybersecurity AND blockchain

This tool assesses the strength of a password based on various criteria:
- Length
- Presence of uppercase letters
- Presence of lowercase letters
- Numbers
- Special characters
"""

import re
import string


class PasswordChecker:
    """Class to evaluate password strength"""
    
    def __init__(self):
        self.min_length_weak = 6
        self.min_length_medium = 8
        self.min_length_strong = 12
    
    def check_length(self, password):
        """Check password length and return score"""
        length = len(password)
        if length < self.min_length_weak:
            return 0, f"Too short (minimum {self.min_length_weak} characters)"
        elif length < self.min_length_medium:
            return 1, f"Short (recommended {self.min_length_medium}+ characters)"
        elif length < self.min_length_strong:
            return 2, f"Good length ({length} characters)"
        else:
            return 3, f"Excellent length ({length} characters)"
    
    def check_uppercase(self, password):
        """Check for uppercase letters"""
        if re.search(r'[A-Z]', password):
            count = sum(1 for c in password if c.isupper())
            return 1, f"Contains uppercase letters ({count})"
        return 0, "No uppercase letters"
    
    def check_lowercase(self, password):
        """Check for lowercase letters"""
        if re.search(r'[a-z]', password):
            count = sum(1 for c in password if c.islower())
            return 1, f"Contains lowercase letters ({count})"
        return 0, "No lowercase letters"
    
    def check_numbers(self, password):
        """Check for numbers"""
        if re.search(r'\d', password):
            count = sum(1 for c in password if c.isdigit())
            return 1, f"Contains numbers ({count})"
        return 0, "No numbers"
    
    def check_special_characters(self, password):
        """Check for special characters"""
        special_chars = string.punctuation
        if any(char in special_chars for char in password):
            count = sum(1 for c in password if c in special_chars)
            return 1, f"Contains special characters ({count})"
        return 0, "No special characters"
    
    def check_common_patterns(self, password):
        """Check for common weak patterns"""
        weaknesses = []
        
        # Check for sequential characters
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            weaknesses.append("Contains sequential letters")
        
        # Check for sequential numbers
        if re.search(r'(012|123|234|345|456|567|678|789)', password):
            weaknesses.append("Contains sequential numbers")
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            weaknesses.append("Contains repeated characters")
        
        # Check for common patterns
        common_patterns = ['password', 'qwerty', '12345', 'admin', 'letmein']
        for pattern in common_patterns:
            if pattern in password.lower():
                weaknesses.append(f"Contains common pattern: '{pattern}'")
        
        return weaknesses
    
    def assess_password(self, password):
        """Assess overall password strength"""
        if not password:
            return {
                'score': 0,
                'max_score': 8,
                'percentage': 0,
                'strength': 'EMPTY',
                'details': {'error': 'Password cannot be empty'},
                'weaknesses': [],
                'suggestions': ['Enter a password to check']
            }
        
        # Calculate scores for each criterion
        length_score, length_msg = self.check_length(password)
        upper_score, upper_msg = self.check_uppercase(password)
        lower_score, lower_msg = self.check_lowercase(password)
        number_score, number_msg = self.check_numbers(password)
        special_score, special_msg = self.check_special_characters(password)
        
        # Total score
        total_score = length_score + upper_score + lower_score + number_score + special_score
        max_score = 8  # 3 for length + 1 each for upper/lower/number/special
        
        # Check for weaknesses
        weaknesses = self.check_common_patterns(password)
        
        # Determine strength level
        percentage = (total_score / max_score) * 100
        
        if total_score <= 2 or weaknesses:
            strength = 'WEAK'
        elif total_score <= 4:
            strength = 'MEDIUM'
        elif total_score <= 6:
            strength = 'STRONG'
        else:
            strength = 'VERY STRONG'
        
        # Generate suggestions
        suggestions = []
        if length_score < 2:
            suggestions.append(f"Increase length to at least {self.min_length_medium} characters")
        if upper_score == 0:
            suggestions.append("Add uppercase letters (A-Z)")
        if lower_score == 0:
            suggestions.append("Add lowercase letters (a-z)")
        if number_score == 0:
            suggestions.append("Add numbers (0-9)")
        if special_score == 0:
            suggestions.append("Add special characters (!@#$%^&*)")
        if weaknesses:
            suggestions.append("Avoid common patterns and repeated characters")
        
        return {
            'score': total_score,
            'max_score': max_score,
            'percentage': percentage,
            'strength': strength,
            'details': {
                'length': length_msg,
                'uppercase': upper_msg,
                'lowercase': lower_msg,
                'numbers': number_msg,
                'special_characters': special_msg
            },
            'weaknesses': weaknesses,
            'suggestions': suggestions
        }


def print_colored(text, color_code):
    """Print colored text for terminal output"""
    colors = {
        'red': '\033[91m',
        'yellow': '\033[93m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'reset': '\033[0m',
        'bold': '\033[1m'
    }
    print(f"{colors.get(color_code, '')}{text}{colors['reset']}")


def display_results(result):
    """Display password strength results in a formatted way"""
    print("\n" + "="*60)
    print_colored("PASSWORD STRENGTH ASSESSMENT", 'bold')
    print("="*60 + "\n")
    
    # Display strength with color
    strength = result['strength']
    if strength == 'EMPTY':
        print_colored(f"Strength: {strength}", 'red')
    elif strength == 'WEAK':
        print_colored(f"Strength: {strength}", 'red')
    elif strength == 'MEDIUM':
        print_colored(f"Strength: {strength}", 'yellow')
    elif strength == 'STRONG':
        print_colored(f"Strength: {strength}", 'green')
    else:  # VERY STRONG
        print_colored(f"Strength: {strength}", 'cyan')
    
    # Display score
    print(f"Score: {result['score']}/{result['max_score']} ({result['percentage']:.1f}%)")
    
    # Progress bar
    bar_length = 40
    filled = int((result['score'] / result['max_score']) * bar_length)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"[{bar}]\n")
    
    # Display details
    if 'error' not in result['details']:
        print_colored("Criteria Analysis:", 'bold')
        for criterion, message in result['details'].items():
            symbol = '✓' if 'No' not in message and 'short' not in message.lower() else '✗'
            color = 'green' if symbol == '✓' else 'red'
            print_colored(f"  {symbol} {criterion.replace('_', ' ').title()}: {message}", color)
        
        # Display weaknesses
        if result['weaknesses']:
            print_colored("\n⚠ Weaknesses Detected:", 'yellow')
            for weakness in result['weaknesses']:
                print(f"  • {weakness}")
        
        # Display suggestions
        if result['suggestions']:
            print_colored("\n💡 Suggestions for Improvement:", 'cyan')
            for suggestion in result['suggestions']:
                print(f"  • {suggestion}")
        else:
            print_colored("\n✓ Your password meets all security criteria!", 'green')
    
    print("\n" + "="*60 + "\n")


def main():
    """Main function to run the password checker"""
    print_colored("\n╔════════════════════════════════════════════════════════════╗", 'cyan')
    print_colored("║         PASSWORD STRENGTH CHECKER TOOL                     ║", 'cyan')
    print_colored("║         Cybersecurity Task #3                              ║", 'cyan')
    print_colored("╚════════════════════════════════════════════════════════════╝\n", 'cyan')
    
    checker = PasswordChecker()
    
    try:
        while True:
            password = input("Enter a password to check (or 'quit' to exit): ")
            
            if password.lower() in ['quit', 'exit', 'q']:
                print_colored("\nThank you for using Password Strength Checker!", 'cyan')
                break
            
            result = checker.assess_password(password)
            display_results(result)
            
    except KeyboardInterrupt:
        print_colored("\n\nExiting Password Strength Checker. Goodbye!", 'cyan')
    except Exception as e:
        print_colored(f"\nAn error occurred: {e}", 'red')


if __name__ == "__main__":
    main()
