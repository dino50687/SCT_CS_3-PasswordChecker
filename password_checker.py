#!/usr/bin/env python3
"""
Password Strength Checker CLI

An interactive command-line tool for testing password strength.
"""

import sys
import getpass
from password_analyzer import PasswordAnalyzer, PasswordStrength


def print_header():
    """Print the application header."""
    print("=" * 60)
    print("🔐 PASSWORD STRENGTH ANALYZER 🔐")
    print("=" * 60)
    print("Test your password strength and get recommendations for improvement")
    print()


def print_analysis_result(result):
    """Print the password analysis result in a formatted way."""
    strength = result['strength']
    score = result['score']
    
    # Print strength with color indicator
    analyzer = PasswordAnalyzer()
    color_indicator = analyzer.get_strength_color(strength)
    
    print(f"\n{color_indicator} PASSWORD STRENGTH: {strength.name.replace('_', ' ')} {color_indicator}")
    print(f"📊 Score: {score}/100")
    print()
    
    # Print criteria analysis
    criteria = result['criteria']
    print("📋 CRITERIA ANALYSIS:")
    print("-" * 30)
    print(f"Length: {criteria['length']} characters")
    print(f"Lowercase letters: {'✅' if criteria['has_lowercase'] else '❌'}")
    print(f"Uppercase letters: {'✅' if criteria['has_uppercase'] else '❌'}")
    print(f"Numbers: {'✅' if criteria['has_digits'] else '❌'}")
    print(f"Special characters: {'✅' if criteria['has_special'] else '❌'}")
    print(f"Character diversity: {criteria['char_types']}/4 types")
    print(f"Unique characters: {criteria['unique_chars']}/{criteria['length']} ({criteria['unique_ratio']:.1%})")
    print()
    
    # Print positive feedback
    if result['feedback']:
        print("✨ STRENGTHS:")
        print("-" * 30)
        for feedback in result['feedback']:
            print(f"  {feedback}")
        print()
    
    # Print recommendations
    if result['recommendations']:
        print("🚀 RECOMMENDATIONS:")
        print("-" * 30)
        for recommendation in result['recommendations']:
            print(f"  {recommendation}")
        print()


def get_password_input(hide_input=True):
    """Get password input from user."""
    if hide_input:
        try:
            return getpass.getpass("Enter password to analyze (hidden): ")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
    else:
        try:
            return input("Enter password to analyze (visible): ")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None


def show_examples():
    """Show example passwords and their analysis."""
    print("📚 EXAMPLE ANALYSES:")
    print("=" * 60)
    
    analyzer = PasswordAnalyzer()
    examples = [
        ("123456", "Very common weak password"),
        ("password", "Dictionary word"),
        ("Password123", "Common pattern with slight complexity"),
        ("MyP@ssw0rd!", "Better but still predictable"),
        ("Tr0ub4dor&3", "Classic strong password example"),
        ("correct-horse-battery-staple", "Passphrase approach"),
        ("X9#mK2$vN8@qL5", "Random strong password")
    ]
    
    for password, description in examples:
        print(f"\n🔍 Testing: '{password}' - {description}")
        result = analyzer.analyze_password(password)
        
        strength = result['strength']
        score = result['score']
        color_indicator = analyzer.get_strength_color(strength)
        
        print(f"   {color_indicator} {strength.name.replace('_', ' ')} (Score: {score}/100)")
        
        # Show top 2 recommendations if any
        if result['recommendations']:
            print("   Top recommendations:")
            for rec in result['recommendations'][:2]:
                print(f"     • {rec}")


def interactive_mode():
    """Run the interactive password testing mode."""
    analyzer = PasswordAnalyzer()
    
    while True:
        print("\n" + "=" * 60)
        print("🔄 INTERACTIVE MODE")
        print("=" * 60)
        print("Options:")
        print("1. Test a password (hidden input)")
        print("2. Test a password (visible input)")
        print("3. Show examples")
        print("4. Exit")
        print()
        
        try:
            choice = input("Select option (1-4): ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break
        
        if choice == '1':
            password = get_password_input(hide_input=True)
            if password is not None:
                result = analyzer.analyze_password(password)
                print_analysis_result(result)
                
                # Ask if they want to try improving it
                if result['recommendations']:
                    try:
                        improve = input("\nWould you like suggestions for improvement? (y/N): ").strip().lower()
                        if improve in ['y', 'yes']:
                            print("\n💡 IMPROVEMENT TIPS:")
                            print("-" * 30)
                            for i, rec in enumerate(result['recommendations'], 1):
                                print(f"{i}. {rec}")
                    except KeyboardInterrupt:
                        pass
        
        elif choice == '2':
            password = get_password_input(hide_input=False)
            if password is not None:
                result = analyzer.analyze_password(password)
                print_analysis_result(result)
        
        elif choice == '3':
            show_examples()
        
        elif choice == '4':
            print("Goodbye! Stay secure! 🔒👋")
            break
        
        else:
            print("❌ Invalid option. Please select 1-4.")


def main():
    """Main function."""
    print_header()
    
    # Check if password was provided as command line argument
    if len(sys.argv) > 1:
        # Batch mode - analyze password from command line
        password = ' '.join(sys.argv[1:])  # Join all arguments as password
        
        analyzer = PasswordAnalyzer()
        result = analyzer.analyze_password(password)
        print_analysis_result(result)
        
        print("💡 TIP: For interactive mode, run without arguments")
        print("💡 TIP: Use quotes for passwords with spaces: 'my password 123'")
    
    else:
        # Interactive mode
        try:
            interactive_mode()
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")


if __name__ == "__main__":
    main()