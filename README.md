# SCT_CS_3-PasswordChecker
**SkillCraft Cybersecurity Internship – Task 3**  
**Author:** CHERUPALLI MANI KARTHIK  
**Domain:** Cybersecurity AND blockchain

# Comprehensive Cybersecurity System 🔐

A multi-layered cybersecurity platform that goes beyond password analysis to provide complete protection against modern cyber threats. This system integrates AI-powered threat detection, community-driven security, and active defense mechanisms.

## 🌟 New Multi-Layer Security Architecture

### Layer 1: Web Security & Phishing Detection 🛡️
Advanced protection against phishing and web-based threats:
- **AI Visual DNA**: Creates unique fingerprints of trusted websites (color palette, layout, logo characteristics)
- **Voice Alert Assistant**: Audible warnings when suspicious pages are detected
- **Community Trust Map**: Global crowdsourced domain reputation database
- **Fake Site Detection**: Identifies fraudulent scholarship, job, and internship sites
- **Privacy Bubble Mode**: Blocks trackers, fingerprinting scripts, and hidden form fields

### Layer 2: Account Security & Data Breach Protection 🔑
Proactive account protection and breach monitoring:
- **Instant Account Risk Meter**: Real-time risk assessment (green/yellow/red indicators)
- **AI Data Leak Prediction**: Predicts potential breaches before they happen
- **Auto Password Hardener**: Generates strong, domain-specific passwords locally
- **Student/Employee Data Shield**: Monitors organizational email domains in breach databases
- **Cyber Awareness Dashboard**: Visualizes breach trends by country, sector, and timeline

### Layer 3: Active Defense & Intelligence ⚔️
Intelligent defense that learns from attacks:
- **AI Decoy Generator**: Creates realistic fake fields that flag credential theft attempts
- **Attack Behavior Learning System (ABLS)**: Builds global attacker fingerprint database
- **Student Safety Mode**: Automatic sandbox with fake data for research purposes
- **Corporate Protection Network**: Shared threat intelligence across enterprise
- **Cyber-Forensics Mode**: Logs and visualizes attacks for educational analysis

### Original Feature: Password Strength Analyzer 🔐
A comprehensive Python tool for assessing password strength based on multiple security criteria. This tool provides detailed analysis, scoring, and personalized recommendations to help users create stronger passwords.

## Core Features ✨

### Password Analysis (Original)
- **Comprehensive Analysis**: Evaluates passwords based on length, character diversity, patterns, and predictability
- **Smart Scoring System**: 0-100 scoring scale with detailed breakdown
- **Strength Classification**: Five levels from Very Weak to Very Strong
- **Detailed Feedback**: Positive reinforcement for good practices
- **Actionable Recommendations**: Specific suggestions for improvement
- **Interactive CLI**: User-friendly command-line interface
- **Pattern Detection**: Identifies common weak patterns and sequences

### Multi-Layer Security Features (New)
- **Visual Website Fingerprinting**: Detects phishing sites with 1% visual mismatch detection
- **Voice Alerts**: Real-time audio warnings for suspicious pages
- **Community Trust Database**: Crowdsourced domain reputation with 1000+ entries
- **Breach Prediction AI**: Forecasts potential data leaks using pattern analysis
- **Domain-Specific Password Generation**: Creates unique passwords per domain
- **Decoy Credential Traps**: Catches credential thieves in real-time
- **Attack Pattern Learning**: Builds fingerprint database of attackers
- **Sandbox Mode**: Safe browsing with fake data for research
- **Corporate Threat Sharing**: Instant threat propagation across organization
- **Forensic Analysis Tools**: Educational attack logging and visualization

## Installation 🚀

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. No additional dependencies required - uses only standard library!

```bash
# Make the scripts executable
chmod +x password_checker.py cybersecurity_system.py

# Run the original password analyzer
python password_checker.py

# Or run the comprehensive cybersecurity system
python cybersecurity_system.py

# Or analyze a specific password
python password_checker.py "YourPasswordHere"

# Test individual layers
python layer1_web_security.py
python layer2_account_security.py
python layer3_active_defense.py
```

## Usage Examples 📚

### Comprehensive Cybersecurity System

```bash
# Interactive mode with all features
python cybersecurity_system.py
```

**Available Features in Interactive Mode:**
```
Layer 1: Web Security
  1. Check Website Safety
  2. Register Trusted Website
  3. Check Domain Trust Level
  4. Scan for Privacy Threats

Layer 2: Account Security
  5. Check Account Risk
  6. Generate Secure Password
  7. Analyze Password Strength
  8. View Cyber Awareness Dashboard

Layer 3: Active Defense
  9. Activate Student Safety Mode
  10. Generate Decoy Fields
  11. View Attack Statistics
  12. Start Forensic Session
```

### Individual Layer Demonstrations

```bash
# Test Layer 1: Web Security & Phishing Detection
python layer1_web_security.py

# Test Layer 2: Account Security & Data Breach Protection
python layer2_account_security.py

# Test Layer 3: Active Defense & Intelligence
python layer3_active_defense.py
```

### Original Password Analyzer

#### Interactive Mode

```bash
python password_checker.py
```

This launches an interactive menu with options to:
- Test passwords with hidden input (secure)
- Test passwords with visible input (for demonstrations)
- View example analyses
- Get improvement suggestions

#### Command Line Mode

```bash
# Analyze a single password
python password_checker.py "MyP@ssw0rd123"

# Use quotes for passwords with spaces
python password_checker.py "correct horse battery staple"
```

### Programmatic Usage

```python
from password_analyzer import PasswordAnalyzer
from cybersecurity_system import CybersecuritySystem

# Original password analyzer
analyzer = PasswordAnalyzer()
result = analyzer.analyze_password("YourPassword123!")
print(f"Score: {result['score']}/100")

# Comprehensive security system
system = CybersecuritySystem()

# Check website safety
safety = system.check_website_safety('https://example.com')
print(f"Safety: {safety['overall_safety']}")

# Generate secure password
password = system.generate_secure_password('github.com', length=20)
print(f"Generated: {password['generated_password']['password']}")

# Activate student protection
protection = system.activate_student_protection('cybersecurity research')
print(f"Status: {protection['status']}")
```

### Layer-Specific Usage

```python
# Layer 1: Visual DNA and Phishing Detection
from layer1_web_security import VisualDNAAnalyzer, CommunityTrustMap

dna = VisualDNAAnalyzer()
fingerprint = dna.create_visual_fingerprint('https://paypal.com')
dna.register_trusted_site('https://paypal.com', fingerprint)

trust_map = CommunityTrustMap()
trust = trust_map.check_domain_trust('suspicious-site.com')

# Layer 2: Account Risk and Password Hardening
from layer2_account_security import AccountRiskMeter, AutoPasswordHardener

risk_meter = AccountRiskMeter()
risk = risk_meter.calculate_risk_score('linkedin.com', 'WeakPass123')

hardener = AutoPasswordHardener()
secure_pwd = hardener.generate_domain_specific_password('example.com')

# Layer 3: Decoy Generation and Attack Learning
from layer3_active_defense import DecoyGenerator, StudentSafetyMode

decoy = DecoyGenerator()
decoys = decoy.generate_decoy_fields('login')

safety = StudentSafetyMode()
sandbox = safety.activate_sandbox('research')
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

Execute the comprehensive test suites to verify functionality:

```bash
# Test original password analyzer
python test_password_analyzer.py

# Test all new cybersecurity features
python test_cybersecurity_system.py
```

The test suites include:
- ✅ **Unit tests** for all analyzer methods
- ✅ **Layer 1 tests** (Visual DNA, phishing detection, privacy)
- ✅ **Layer 2 tests** (Risk assessment, breach prediction, password generation)
- ✅ **Layer 3 tests** (Decoys, attack learning, sandbox, forensics)
- ✅ **Integration tests** for complete workflows
- ✅ **Edge case testing** (empty inputs, unicode, etc.)
- ✅ **Real-world scenario validation**

Expected output:
```
🧪 COMPREHENSIVE CYBERSECURITY SYSTEM TEST SUITE
======================================================================
Testing:
  🛡️  Layer 1: Web Security & Phishing Detection
  🔑 Layer 2: Account Security & Data Breach Protection
  ⚔️  Layer 3: Active Defense & Intelligence
======================================================================

... (test results) ...

✅ All tests passed! The cybersecurity system is working correctly.

Tests run: 43
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
SCT_CS_3-PasswordChecker/
├── password_analyzer.py           # Core password analysis engine (original)
├── password_checker.py            # Interactive password CLI tool (original)
├── test_password_analyzer.py      # Password analyzer test suite (original)
│
├── layer1_web_security.py         # Layer 1: Web Security & Phishing Detection
├── layer2_account_security.py     # Layer 2: Account Security & Breach Protection
├── layer3_active_defense.py       # Layer 3: Active Defense & Intelligence
│
├── cybersecurity_system.py        # Unified security system interface
├── test_cybersecurity_system.py   # Comprehensive test suite for all layers
│
├── .gitignore                     # Git ignore file
└── README.md                      # This documentation
```

## Key Features by Layer 🎯

### Layer 1: Web Security & Phishing Detection 🛡️

**1. AI Visual DNA of Websites**
- Creates unique visual fingerprints for trusted websites
- Analyzes color palette, layout patterns, and text tone
- Detects 1% or greater visual mismatches
- Alerts users to potential phishing sites

**2. Voice Alert Assistant**
- Text-to-speech warnings for suspicious pages
- Configurable alert types and volume
- Real-time threat notifications

**3. Community Trust Map**
- Global crowdsourced domain reputation database
- Company verification system
- Trust score calculation (0-100)
- Community reporting functionality

**4. Fake Scholarship/Job Site Detection**
- Pattern-based detection of fraudulent education sites
- Domain age verification
- Urgency tactic identification
- Risk scoring and red flag reporting

**5. Privacy Bubble Mode**
- Automatic tracker blocking
- Fingerprinting script detection
- Hidden form field identification
- Configurable protection levels

### Layer 2: Account Security & Data Breach Protection 🔑

**1. Instant Account Risk Meter**
- Real-time risk assessment (green/yellow/red)
- Factors: breaches, password strength, reuse detection
- Domain-specific risk evaluation
- Actionable security recommendations

**2. AI Data Leak Prediction**
- Predictive analytics for potential breaches
- Pattern recognition across multiple indicators
- Timeline-based risk forecasting
- Proactive security recommendations

**3. Auto Password Hardener**
- Domain-specific password generation
- Minimum 16-character secure passwords
- Local generation (never uploaded)
- Strength scoring and validation
- Improvement suggestions for existing passwords

**4. Student/Employee Data Shield**
- Domain monitoring for breach databases
- Organization email tracking
- Automated breach notifications
- Historical breach tracking

**5. Cyber Awareness Dashboard**
- Global breach statistics visualization
- Country, sector, and temporal analysis
- Educational insights and tips
- Trend identification and reporting

### Layer 3: Active Defense & Intelligence ⚔️

**1. AI Decoy Generator**
- Realistic fake form fields
- Dummy credential generation
- Real-time attacker detection
- Automatic IP flagging and blocking

**2. Attack Behavior Learning System (ABLS)**
- Attacker fingerprint database
- Pattern recognition and analysis
- Blockchain-based threat intelligence sharing
- Cross-organization threat propagation

**3. Student Safety Mode**
- Automatic sandbox activation
- Fake data generation for forms
- Real data isolation and protection
- Research-safe browsing environment

**4. Corporate Protection Network**
- Enterprise-wide threat sharing
- Instant alert propagation
- Network-based collective immunity
- Unified security dashboard

**5. Cyber-Forensics Mode**
- Attack attempt logging
- Timeline visualization
- Educational analysis tools
- Forensic report generation
- Safe ethical hacking environment


## Use Cases 💼

### For Students 🎓
- **Safe Research**: Use Student Safety Mode to research suspicious sites without risk
- **Learning Tool**: Cyber-Forensics Mode teaches ethical hacking concepts
- **Scholarship Protection**: Detect fake scholarship and internship scams
- **Privacy Protection**: Block trackers on educational websites

### For Organizations 🏢
- **Enterprise Security**: Corporate Protection Network for instant threat sharing
- **Employee Protection**: Monitor company email domains in breach databases
- **Security Training**: Use forensic tools for staff cybersecurity education
- **Compliance**: Comprehensive audit trails and attack logging

### For Individuals 👤
- **Password Security**: Generate and analyze strong passwords
- **Phishing Protection**: Visual DNA prevents phishing attacks
- **Privacy Control**: Block trackers and fingerprinting automatically
- **Risk Awareness**: Real-time account risk assessment

### For Security Professionals 🔐
- **Threat Intelligence**: ABLS for pattern recognition and threat sharing
- **Forensic Analysis**: Detailed attack logs and visualization
- **Decoy Deployment**: Catch attackers with honeypot credentials
- **Research Platform**: Safe environment for security research

## Contributing 🤝

Contributions are welcome! Areas for improvement:

- **Additional Languages**: Support for non-English content
- **Machine Learning**: Enhanced AI for pattern recognition
- **Browser Extension**: Direct browser integration
- **Mobile Support**: iOS and Android applications
- **API Development**: RESTful API for third-party integration
- **GUI Interface**: Desktop or web-based interface
- **Database Integration**: Persistent storage for analytics

## Changelog 📅

### Version 2.0.0 (2024-10-31)
- ✨ **Major Update**: Multi-layer cybersecurity system
- ✅ Layer 1: Web Security & Phishing Detection
- ✅ Layer 2: Account Security & Data Breach Protection
- ✅ Layer 3: Active Defense & Intelligence
- ✅ Unified cybersecurity system interface
- ✅ Comprehensive test suite (43+ tests)
- ✅ Educational forensics and sandbox modes

### Version 1.0.0 (2024-10-01)
- ✨ Initial release
- ✅ Core password analysis functionality
- ✅ Interactive CLI interface
- ✅ Comprehensive scoring system
- ✅ Pattern detection and recommendations
- ✅ Full test suite coverage

---

**Stay secure! 🔒** Remember: The strongest password is one that's both complex and memorable to you, but unpredictable to others.
