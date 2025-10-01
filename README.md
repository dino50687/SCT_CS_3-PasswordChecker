# SCT_CS_3-PasswordChecker
**SkillCraft Cybersecurity Internship – Task 3**  
**Author:** CHERUPALLI MANI KARTHIK  
**Domain:** Cybersecurity AND blockchain
# Password Strength Analyzer 🔐

A comprehensive Python tool for assessing password strength based on multiple security criteria. This tool provides detailed analysis, scoring, and personalized recommendations to help users create stronger passwords.

## Features ✨

- **Comprehensive Analysis**: Evaluates passwords based on length, character diversity, patterns, and predictability
- **Smart Scoring System**: 0-100 scoring scale with detailed breakdown
- **Strength Classification**: Five levels from Very Weak to Very Strong
- **Detailed Feedback**: Positive reinforcement for good practices
- **Actionable Recommendations**: Specific suggestions for improvement
- **Interactive CLI**: User-friendly command-line interface
- **Pattern Detection**: Identifies common weak patterns and sequences
- **Extensive Testing**: Comprehensive test suite ensuring reliability

## Installation 🚀

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. No additional dependencies required - uses only standard library!

```bash
# Make the CLI executable
chmod +x password_checker.py

# Run the interactive tool
python password_checker.py

# Or analyze a specific password
python password_checker.py "YourPasswordHere"
```

## Usage Examples 📚

### Interactive Mode

```bash
python password_checker.py
```

This launches an interactive menu with options to:
- Test passwords with hidden input (secure)
- Test passwords with visible input (for demonstrations)
- View example analyses
- Get improvement suggestions

### Command Line Mode

```bash
# Analyze a single password
python password_checker.py "MyP@ssw0rd123"

# Use quotes for passwords with spaces
python password_checker.py "correct horse battery staple"
```

### Programmatic Usage

```python
from password_analyzer import PasswordAnalyzer

# Create analyzer instance
analyzer = PasswordAnalyzer()

# Analyze a password
result = analyzer.analyze_password("YourPassword123!")

# Access results
print(f"Score: {result['score']}/100")
print(f"Strength: {result['strength'].name}")
print("Recommendations:")
for rec in result['recommendations']:
    print(f"  - {rec}")
```

## Analysis Criteria 🔍

### Password Strength Levels

| Level | Score Range | Description |
|-------|------------|-------------|
| 🔴 **Very Weak** | 0-24 | Easily guessable, high security risk |
| 🟠 **Weak** | 25-44 | Some complexity but still vulnerable |
| 🟡 **Moderate** | 45-64 | Acceptable for low-security applications |
| 🟢 **Strong** | 65-79 | Good security for most purposes |
| 💚 **Very Strong** | 80-100 | Excellent security, resistant to attacks |

### Evaluation Criteria

#### ✅ **Length Analysis**
- **Minimum**: 8 characters (basic requirement)
- **Recommended**: 12+ characters (better security)
- **Strong**: 16+ characters (excellent security)
- **Bonus**: Extra points for 20+ character passwords

#### ✅ **Character Diversity** 
- **Lowercase letters** (a-z): Basic requirement
- **Uppercase letters** (A-Z): Increases complexity
- **Numbers** (0-9): Adds unpredictability  
- **Special characters** (!@#$%^&*): Maximum security

#### ✅ **Pattern Detection**
- **Common passwords**: Checks against database of weak passwords
- **Dictionary words**: Identifies common words like "password"
- **Keyboard patterns**: Detects sequences like "qwerty", "asdf"
- **Sequential characters**: Finds patterns like "123", "abc"
- **Repeated characters**: Identifies excessive repetition

#### ✅ **Uniqueness Analysis**
- **Character diversity ratio**: Measures uniqueness vs repetition
- **Predictability assessment**: Evaluates overall randomness

## Example Analyses 📊

### Very Weak Password: "123456"
```
🔴 PASSWORD STRENGTH: VERY WEAK
📊 Score: 8/100

❌ Issues:
- Too short (only 6 characters)
- Only contains numbers
- Common password in breach databases
- Sequential number pattern

🚀 Recommendations:
- Increase length to at least 8 characters
- Add lowercase letters (a-z)
- Add uppercase letters (A-Z) 
- Add special characters (!@#$%^&*)
- Avoid common patterns like sequential numbers
```

### Strong Password: "Tr0ub4dor&3"
```
💚 PASSWORD STRENGTH: VERY STRONG  
📊 Score: 82/100

✅ Strengths:
- Good length (11 characters)
- Contains lowercase letters
- Contains uppercase letters  
- Contains numbers
- Contains special characters
- High character diversity
- No common patterns detected
- Not a commonly used password
```

### Passphrase Example: "correct-horse-battery-staple"
```
🟢 PASSWORD STRENGTH: STRONG
📊 Score: 71/100

✅ Strengths:
- Excellent length (28 characters)
- Contains lowercase letters
- Contains special characters (hyphens)
- High character diversity
- Not a commonly used password

💡 Recommendations:
- Add uppercase letters (A-Z)
- Add numbers (0-9)
- Consider mixing in some special characters
```

## API Reference 📖

### PasswordAnalyzer Class

#### Methods

**`analyze_password(password: str) -> Dict`**
- Performs comprehensive password analysis
- Returns detailed results dictionary

**`get_strength_color(strength: PasswordStrength) -> str`**
- Returns emoji indicator for strength level
- Useful for UI displays

#### Result Dictionary Structure

```python
{
    'password': str,           # The analyzed password
    'score': int,             # Score 0-100
    'strength': PasswordStrength,  # Enum value
    'feedback': List[str],    # Positive feedback items
    'criteria': Dict,         # Detailed criteria analysis
    'recommendations': List[str]  # Improvement suggestions
}
```

#### Criteria Dictionary

```python
{
    'length': int,                    # Password length
    'has_lowercase': bool,           # Contains a-z
    'has_uppercase': bool,           # Contains A-Z  
    'has_digits': bool,              # Contains 0-9
    'has_special': bool,             # Contains symbols
    'char_types': int,               # Number of char types (0-4)
    'unique_chars': int,             # Count of unique characters
    'unique_ratio': float,           # Uniqueness ratio (0.0-1.0)
    'has_common_patterns': bool,     # Contains weak patterns
    'is_common_password': bool,      # In common password list
    'has_sequential': bool,          # Has sequential chars
    'has_repeated': bool             # Has excessive repetition
}
```

## Running Tests 🧪

Execute the comprehensive test suite to verify functionality:

```bash
python test_password_analyzer.py
```

The test suite includes:
- ✅ **Unit tests** for all analyzer methods
- ✅ **Integration tests** for complete workflows  
- ✅ **Edge case testing** (empty passwords, unicode, etc.)
- ✅ **Real-world password examples**
- ✅ **Performance validation**

Expected output:
```
🧪 Running Password Analyzer Test Suite
============================================================
test_character_type_detection (__main__.TestPasswordAnalyzer) ... ok
test_common_password_detection (__main__.TestPasswordAnalyzer) ... ok
test_empty_password (__main__.TestPasswordAnalyzer) ... ok
...
============================================================
✅ All tests passed! The password analyzer is working correctly.

Tests run: 25
Failures: 0
Errors: 0
```

## Security Best Practices 🛡️

### Creating Strong Passwords

1. **Length First**: Aim for 12+ characters minimum
2. **Mix Character Types**: Use uppercase, lowercase, numbers, and symbols
3. **Avoid Patterns**: Don't use sequential or repeated characters
4. **Be Unpredictable**: Avoid dictionary words and common substitutions
5. **Use Passphrases**: Consider memorable phrases with modifications

### Examples of Strong Patterns

- **Random Generation**: `X9#mK2$vN8@qL5&Rt7!`
- **Modified Passphrase**: `Coffee!Loves#Me2023$`
- **Acronym Method**: `ILmJb@1985!` (I Love my Job but @ 1985!)
- **Creative Substitution**: `Tr0ub4dor&3` (Troubador&3)

### What to Avoid

- ❌ Personal information (names, birthdays, addresses)
- ❌ Common words or phrases  
- ❌ Simple patterns (123456, qwerty, password)
- ❌ Single character type only
- ❌ Passwords shorter than 8 characters
- ❌ Reusing passwords across multiple accounts

## Advanced Features 🔧

### Customization Options

You can modify the analyzer's behavior by adjusting parameters:

```python
analyzer = PasswordAnalyzer()

# Customize minimum lengths
analyzer.min_length = 10
analyzer.recommended_length = 14
analyzer.strong_length = 18

# Add custom common passwords
analyzer.common_passwords.update(['mycompany123', 'welcome2023'])

# Add custom weak patterns
analyzer.common_patterns.append(r'mycompany\d+')
```

### Integration Examples

#### Web Application Integration
```python
from flask import Flask, request, jsonify
from password_analyzer import PasswordAnalyzer

app = Flask(__name__)
analyzer = PasswordAnalyzer()

@app.route('/check-password', methods=['POST'])
def check_password():
    password = request.json.get('password', '')
    result = analyzer.analyze_password(password)
    
    return jsonify({
        'score': result['score'],
        'strength': result['strength'].name,
        'recommendations': result['recommendations']
    })
```

#### Django Forms Validation
```python
from django import forms
from password_analyzer import PasswordAnalyzer

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_password(self):
        password = self.cleaned_data['password']
        analyzer = PasswordAnalyzer()
        result = analyzer.analyze_password(password)
        
        if result['score'] < 45:
            raise forms.ValidationError(
                f"Password too weak (score: {result['score']}/100). "
                f"Suggestions: {', '.join(result['recommendations'][:2])}"
            )
        
        return password
```

## File Structure 📁

```
password-strength-analyzer/
├── password_analyzer.py      # Core analysis engine
├── password_checker.py       # Interactive CLI tool  
├── test_password_analyzer.py # Comprehensive test suite
└── README.md                 # This documentation
```

## Contributing 🤝

Contributions are welcome! Areas for improvement:

- **Additional Languages**: Support for non-English passwords
- **Custom Dictionaries**: User-defined weak password lists
- **Advanced Patterns**: More sophisticated pattern recognition
- **Performance Optimization**: Faster analysis for bulk operations
- **GUI Interface**: Desktop or web-based interface

## License 📄

This project is open source and available under the MIT License.

## Changelog 📅

### Version 1.0.0 (2024-10-01)
- ✨ Initial release
- ✅ Core password analysis functionality
- ✅ Interactive CLI interface
- ✅ Comprehensive scoring system
- ✅ Pattern detection and recommendations
- ✅ Full test suite coverage

---

**Stay secure! 🔒** Remember: The strongest password is one that's both complex and memorable to you, but unpredictable to others.
