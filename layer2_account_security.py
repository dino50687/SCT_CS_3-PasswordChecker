"""
Layer 2: Account Security & Data Breach Protection

Features:
1. Instant Account Risk Meter
2. AI Data Leak Prediction
3. Auto Password Hardener (domain-specific password generation)
4. Student/Employee Data Shield
5. Cyber Awareness Dashboard
"""

import hashlib
import secrets
import string
import json
from datetime import datetime
from typing import Dict, List, Tuple
from enum import Enum


class RiskLevel(Enum):
    """Risk level enumeration."""
    GREEN = "green"   # Low risk
    YELLOW = "yellow"  # Medium risk
    RED = "red"        # High risk


class AccountRiskMeter:
    """
    Evaluates account risk based on multiple factors.
    """
    
    def __init__(self):
        # Simulated dark web breach database
        self.known_breaches = {
            'linkedin.com': {'date': '2021-06-01', 'records': 700000000},
            'facebook.com': {'date': '2019-04-03', 'records': 533000000},
            'yahoo.com': {'date': '2013-08-01', 'records': 3000000000},
            'adobe.com': {'date': '2013-10-01', 'records': 153000000},
        }
        
    def calculate_risk_score(self, domain: str, password: str, email: str = None) -> Dict:
        """
        Calculate risk score for an account.
        
        Args:
            domain: Website domain (e.g., 'example.com')
            password: User's password
            email: User's email (optional)
            
        Returns:
            Dict with risk assessment
        """
        risk_score = 0
        risk_factors = []
        
        # Check if domain has known breaches
        if domain in self.known_breaches:
            risk_score += 30
            breach_info = self.known_breaches[domain]
            risk_factors.append(f"Domain has known breach from {breach_info['date']}")
        
        # Check password strength (using simple heuristic)
        if len(password) < 12:
            risk_score += 20
            risk_factors.append("Password length below recommended 12 characters")
        
        if not any(c.isupper() for c in password):
            risk_score += 10
            risk_factors.append("Password lacks uppercase letters")
        
        if not any(c in string.punctuation for c in password):
            risk_score += 10
            risk_factors.append("Password lacks special characters")
        
        # Check for common passwords
        common_patterns = ['password', '123456', 'qwerty']
        if any(pattern in password.lower() for pattern in common_patterns):
            risk_score += 30
            risk_factors.append("Password contains common patterns")
        
        # Determine risk level
        if risk_score >= 50:
            risk_level = RiskLevel.RED
        elif risk_score >= 25:
            risk_level = RiskLevel.YELLOW
        else:
            risk_level = RiskLevel.GREEN
        
        return {
            'risk_score': min(risk_score, 100),
            'risk_level': risk_level,
            'risk_factors': risk_factors,
            'timestamp': datetime.now().isoformat()
        }


class DataLeakPredictor:
    """
    Predicts potential data leaks based on patterns and site analysis.
    """
    
    def __init__(self):
        # Risk indicators for domains
        self.risk_indicators = {
            'high_breach_frequency': 40,
            'outdated_security': 30,
            'code_leaks_detected': 35,
            'staff_security_posts': 20,
            'known_vulnerabilities': 45
        }
        
    def predict_leak_risk(self, domain: str, indicators: List[str]) -> Dict:
        """
        Predict if a site might face a breach soon.
        
        Args:
            domain: Website domain
            indicators: List of risk indicators present
            
        Returns:
            Dict with prediction results
        """
        total_risk = 0
        active_indicators = []
        
        for indicator in indicators:
            if indicator in self.risk_indicators:
                total_risk += self.risk_indicators[indicator]
                active_indicators.append({
                    'indicator': indicator,
                    'weight': self.risk_indicators[indicator]
                })
        
        # Determine prediction
        if total_risk >= 70:
            prediction = "HIGH - Breach likely within 3 months"
            recommendation = "Consider changing credentials and enabling 2FA"
        elif total_risk >= 40:
            prediction = "MEDIUM - Monitor closely for next 6 months"
            recommendation = "Update password and review account activity regularly"
        else:
            prediction = "LOW - No immediate concerns"
            recommendation = "Maintain current security practices"
        
        return {
            'domain': domain,
            'total_risk_score': total_risk,
            'prediction': prediction,
            'recommendation': recommendation,
            'active_indicators': active_indicators,
            'timestamp': datetime.now().isoformat()
        }


class AutoPasswordHardener:
    """
    Generates strong, domain-specific passwords locally (never uploaded).
    """
    
    def __init__(self):
        self.min_length = 16
        self.charset = string.ascii_letters + string.digits + string.punctuation
        
    def generate_domain_specific_password(self, domain: str, user_hint: str = None, 
                                         length: int = 16) -> Dict:
        """
        Generate a strong, domain-specific password.
        
        Args:
            domain: Website domain for which to generate password
            user_hint: Optional user-provided hint for memorability
            length: Desired password length (min 16)
            
        Returns:
            Dict with generated password and metadata
        """
        length = max(length, self.min_length)
        
        # Generate random secure password
        password_chars = []
        
        # Ensure at least one of each character type
        password_chars.append(secrets.choice(string.ascii_lowercase))
        password_chars.append(secrets.choice(string.ascii_uppercase))
        password_chars.append(secrets.choice(string.digits))
        password_chars.append(secrets.choice(string.punctuation))
        
        # Fill remaining with random characters
        for _ in range(length - 4):
            password_chars.append(secrets.choice(self.charset))
        
        # Shuffle to randomize positions
        secrets.SystemRandom().shuffle(password_chars)
        password = ''.join(password_chars)
        
        # Create domain-specific salt (for identification, not security)
        domain_hash = hashlib.sha256(domain.encode()).hexdigest()[:8]
        
        return {
            'password': password,
            'length': length,
            'domain': domain,
            'domain_identifier': domain_hash,
            'user_hint': user_hint,
            'generated_at': datetime.now().isoformat(),
            'strength_score': self._calculate_strength(password)
        }
    
    def _calculate_strength(self, password: str) -> int:
        """Calculate password strength score."""
        score = 0
        
        # Length bonus
        score += min(len(password) * 2, 40)
        
        # Character diversity
        if any(c.islower() for c in password):
            score += 15
        if any(c.isupper() for c in password):
            score += 15
        if any(c.isdigit() for c in password):
            score += 15
        if any(c in string.punctuation for c in password):
            score += 15
        
        return min(score, 100)
    
    def suggest_password_improvements(self, password: str) -> List[str]:
        """
        Suggest improvements for existing passwords.
        
        Args:
            password: Current password
            
        Returns:
            List of improvement suggestions
        """
        suggestions = []
        
        if len(password) < 12:
            suggestions.append(f"Increase length to at least 12 characters (current: {len(password)})")
        
        if not any(c.isupper() for c in password):
            suggestions.append("Add uppercase letters (A-Z)")
        
        if not any(c.islower() for c in password):
            suggestions.append("Add lowercase letters (a-z)")
        
        if not any(c.isdigit() for c in password):
            suggestions.append("Add numbers (0-9)")
        
        if not any(c in string.punctuation for c in password):
            suggestions.append("Add special characters (!@#$%^&*)")
        
        # Check for patterns
        common_patterns = ['123', 'abc', 'password', 'qwerty']
        if any(pattern in password.lower() for pattern in common_patterns):
            suggestions.append("Remove common patterns")
        
        if not suggestions:
            suggestions.append("Password meets strong security standards!")
        
        return suggestions


class DataShield:
    """
    Monitors if official email domains are found in new leaks.
    """
    
    def __init__(self):
        self.monitored_domains = {}
        self.breach_database = {}
        
    def register_domain(self, domain: str, organization: str) -> Dict:
        """
        Register an email domain for monitoring.
        
        Args:
            domain: Email domain (e.g., 'company.com')
            organization: Organization name
            
        Returns:
            Registration confirmation
        """
        self.monitored_domains[domain] = {
            'organization': organization,
            'registered_at': datetime.now().isoformat(),
            'breach_count': 0
        }
        
        return {
            'status': 'registered',
            'domain': domain,
            'organization': organization,
            'monitoring': True
        }
    
    def check_domain_breach(self, domain: str) -> Dict:
        """
        Check if a monitored domain appears in breach databases.
        
        Args:
            domain: Email domain to check
            
        Returns:
            Breach status and details
        """
        if domain not in self.monitored_domains:
            return {
                'error': 'Domain not registered for monitoring',
                'domain': domain
            }
        
        # Check against breach database (simulated)
        breaches = []
        if domain in ['university.edu', 'oldschool.edu']:
            breaches.append({
                'source': 'DataBreach2023',
                'date': '2023-05-15',
                'records_affected': 50000,
                'data_types': ['emails', 'passwords', 'names']
            })
        
        # Update monitoring record
        if breaches:
            self.monitored_domains[domain]['breach_count'] = len(breaches)
            self.monitored_domains[domain]['last_breach'] = datetime.now().isoformat()
        
        return {
            'domain': domain,
            'organization': self.monitored_domains[domain]['organization'],
            'breaches_found': len(breaches),
            'breaches': breaches,
            'status': 'breach_detected' if breaches else 'clean',
            'checked_at': datetime.now().isoformat()
        }


class CyberAwarenessDashboard:
    """
    Visualizes breach trends and provides educational insights.
    """
    
    def __init__(self):
        self.breach_statistics = {
            'by_country': {
                'USA': {'breaches': 450, 'records': 1200000000},
                'UK': {'breaches': 120, 'records': 350000000},
                'India': {'breaches': 200, 'records': 800000000},
                'China': {'breaches': 300, 'records': 900000000},
            },
            'by_sector': {
                'Technology': {'breaches': 250, 'records': 600000000},
                'Finance': {'breaches': 180, 'records': 450000000},
                'Healthcare': {'breaches': 200, 'records': 500000000},
                'Education': {'breaches': 150, 'records': 300000000},
                'Retail': {'breaches': 170, 'records': 400000000},
            },
            'by_year': {
                '2020': {'breaches': 300, 'records': 500000000},
                '2021': {'breaches': 350, 'records': 650000000},
                '2022': {'breaches': 400, 'records': 800000000},
                '2023': {'breaches': 450, 'records': 1000000000},
            }
        }
    
    def get_global_statistics(self) -> Dict:
        """
        Get global breach statistics.
        
        Returns:
            Dict with comprehensive statistics
        """
        total_breaches = sum(data['breaches'] for data in self.breach_statistics['by_country'].values())
        total_records = sum(data['records'] for data in self.breach_statistics['by_country'].values())
        
        return {
            'total_breaches': total_breaches,
            'total_records_compromised': total_records,
            'by_country': self.breach_statistics['by_country'],
            'by_sector': self.breach_statistics['by_sector'],
            'by_year': self.breach_statistics['by_year'],
            'generated_at': datetime.now().isoformat()
        }
    
    def get_sector_trends(self, sector: str) -> Dict:
        """
        Get breach trends for a specific sector.
        
        Args:
            sector: Sector name (e.g., 'Technology', 'Finance')
            
        Returns:
            Sector-specific breach data
        """
        if sector not in self.breach_statistics['by_sector']:
            return {'error': f'Sector {sector} not found in database'}
        
        sector_data = self.breach_statistics['by_sector'][sector]
        
        return {
            'sector': sector,
            'total_breaches': sector_data['breaches'],
            'total_records': sector_data['records'],
            'avg_records_per_breach': sector_data['records'] // sector_data['breaches'],
            'risk_level': self._calculate_sector_risk(sector_data),
            'timestamp': datetime.now().isoformat()
        }
    
    def _calculate_sector_risk(self, sector_data: Dict) -> str:
        """Calculate risk level for a sector."""
        if sector_data['breaches'] > 200:
            return 'HIGH'
        elif sector_data['breaches'] > 150:
            return 'MEDIUM'
        return 'LOW'
    
    def generate_educational_insights(self) -> List[Dict]:
        """
        Generate educational insights about cybersecurity.
        
        Returns:
            List of educational tips and insights
        """
        insights = [
            {
                'category': 'Password Security',
                'tip': 'Use unique passwords for each account - password reuse is the #1 cause of account takeovers',
                'importance': 'CRITICAL'
            },
            {
                'category': 'Two-Factor Authentication',
                'tip': 'Enable 2FA on all accounts - it blocks 99.9% of automated attacks',
                'importance': 'HIGH'
            },
            {
                'category': 'Phishing Awareness',
                'tip': 'Always verify sender email addresses - 90% of breaches start with phishing',
                'importance': 'CRITICAL'
            },
            {
                'category': 'Software Updates',
                'tip': 'Keep software updated - 60% of breaches exploit known vulnerabilities',
                'importance': 'HIGH'
            },
            {
                'category': 'Data Minimization',
                'tip': 'Share only necessary information online - less data = less risk',
                'importance': 'MEDIUM'
            }
        ]
        
        return insights


def demonstrate_layer2_features():
    """Demonstrate Layer 2 features."""
    print("=" * 70)
    print("LAYER 2: ACCOUNT SECURITY & DATA BREACH PROTECTION")
    print("=" * 70)
    
    # 1. Account Risk Meter
    print("\n1️⃣  INSTANT ACCOUNT RISK METER")
    print("-" * 70)
    risk_meter = AccountRiskMeter()
    risk_result = risk_meter.calculate_risk_score('linkedin.com', 'Password123', 'user@example.com')
    print(f"Domain: linkedin.com")
    print(f"Risk Level: {risk_result['risk_level'].value.upper()} 🚦")
    print(f"Risk Score: {risk_result['risk_score']}/100")
    print("Risk Factors:")
    for factor in risk_result['risk_factors']:
        print(f"  ⚠️  {factor}")
    
    # 2. Data Leak Prediction
    print("\n2️⃣  AI DATA LEAK PREDICTION")
    print("-" * 70)
    predictor = DataLeakPredictor()
    prediction = predictor.predict_leak_risk(
        'example.com',
        ['high_breach_frequency', 'outdated_security']
    )
    print(f"Domain: {prediction['domain']}")
    print(f"Prediction: {prediction['prediction']}")
    print(f"Risk Score: {prediction['total_risk_score']}/100")
    print(f"Recommendation: {prediction['recommendation']}")
    
    # 3. Auto Password Hardener
    print("\n3️⃣  AUTO PASSWORD HARDENER")
    print("-" * 70)
    hardener = AutoPasswordHardener()
    new_password = hardener.generate_domain_specific_password('github.com', length=20)
    print(f"Generated password for {new_password['domain']}:")
    print(f"  Password: {new_password['password']}")
    print(f"  Strength: {new_password['strength_score']}/100")
    print(f"  Length: {new_password['length']} characters")
    print("\n  💡 Password Improvement Suggestions for 'Pass123':")
    suggestions = hardener.suggest_password_improvements('Pass123')
    for suggestion in suggestions:
        print(f"    • {suggestion}")
    
    # 4. Data Shield
    print("\n4️⃣  STUDENT/EMPLOYEE DATA SHIELD")
    print("-" * 70)
    shield = DataShield()
    reg = shield.register_domain('university.edu', 'State University')
    print(f"Registered: {reg['domain']} for {reg['organization']}")
    check = shield.check_domain_breach('university.edu')
    print(f"Status: {check['status'].upper()}")
    print(f"Breaches Found: {check['breaches_found']}")
    
    # 5. Cyber Awareness Dashboard
    print("\n5️⃣  CYBER AWARENESS DASHBOARD")
    print("-" * 70)
    dashboard = CyberAwarenessDashboard()
    stats = dashboard.get_global_statistics()
    print(f"Total Breaches: {stats['total_breaches']:,}")
    print(f"Total Records Compromised: {stats['total_records_compromised']:,}")
    print("\nTop Sectors by Breaches:")
    for sector, data in sorted(stats['by_sector'].items(), 
                              key=lambda x: x[1]['breaches'], 
                              reverse=True)[:3]:
        print(f"  {sector}: {data['breaches']} breaches ({data['records']:,} records)")
    
    print("\n📚 Educational Insights:")
    insights = dashboard.generate_educational_insights()
    for insight in insights[:3]:
        print(f"  {insight['category']}: {insight['tip']}")


if __name__ == "__main__":
    demonstrate_layer2_features()
