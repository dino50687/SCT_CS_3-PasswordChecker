"""
Password Strength Analyzer

A comprehensive tool for assessing password strength based on various criteria
including length, character diversity, and common patterns.
"""

import re
import string
from typing import Dict, List, Tuple
from enum import Enum


class PasswordStrength(Enum):
    """Enumeration for password strength levels."""
    VERY_WEAK = 1
    WEAK = 2
    MODERATE = 3
    STRONG = 4
    VERY_STRONG = 5


class PasswordAnalyzer:
    """
    A class to analyze password strength based on multiple criteria.
    """
    
    def __init__(self):
        self.min_length = 8
        self.recommended_length = 12
        self.strong_length = 16
        
        # Common weak passwords and patterns
        self.common_passwords = {
            'password', '123456', '123456789', 'qwerty', 'abc123',
            'password123', 'admin', 'letmein', 'welcome', 'monkey',
            'dragon', 'password1', 'sunshine', 'master', 'football',
            '1234567890', 'iloveyou', 'princess', 'rockyou'
        }
        
        self.common_patterns = [
            r'password|pass',        # Contains "password" or "pass"
            r'^(.)\1{2,}',           # Repeated characters at start
            r'123456|654321',        # Sequential numbers
            r'qwerty|asdf',          # Keyboard patterns
            r'^[a-z]+$',             # Only lowercase
            r'^[A-Z]+$',             # Only uppercase
            r'^\d+$',                # Only numbers
        ]

    def analyze_password(self, password: str) -> Dict:
        """
        Analyze a password and return comprehensive strength assessment.
        
        Args:
            password (str): The password to analyze
            
        Returns:
            Dict: Analysis results including score, strength level, and feedback
        """
        if not password:
            return {
                'password': '',
                'score': 0,
                'strength': PasswordStrength.VERY_WEAK,
                'feedback': ['Password cannot be empty'],
                'criteria': {},
                'recommendations': ['Please enter a password']
            }
        
        # Analyze individual criteria
        criteria = self._analyze_criteria(password)
        
        # Calculate score
        score = self._calculate_score(password, criteria)
        
        # Determine strength level
        strength = self._determine_strength(score)
        
        # Generate feedback and recommendations
        feedback = self._generate_feedback(password, criteria)
        recommendations = self._generate_recommendations(password, criteria)
        
        return {
            'password': password,
            'score': score,
            'strength': strength,
            'feedback': feedback,
            'criteria': criteria,
            'recommendations': recommendations
        }
    
    def _analyze_criteria(self, password: str) -> Dict:
        """Analyze specific password criteria."""
        length = len(password)
        
        # Character type analysis
        has_lowercase = bool(re.search(r'[a-z]', password))
        has_uppercase = bool(re.search(r'[A-Z]', password))
        has_digits = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
        
        # Count different character types
        char_types = sum([has_lowercase, has_uppercase, has_digits, has_special])
        
        # Unique characters ratio
        unique_chars = len(set(password))
        unique_ratio = unique_chars / length if length > 0 else 0
        
        # Check for common patterns
        has_common_patterns = any(re.search(pattern, password, re.IGNORECASE) 
                                for pattern in self.common_patterns)
        
        # Check if password is in common passwords list
        is_common_password = password.lower() in self.common_passwords
        
        # Sequential characters check
        has_sequential = self._has_sequential_chars(password)
        
        # Repeated characters check
        has_repeated = self._has_repeated_chars(password)
        
        return {
            'length': length,
            'has_lowercase': has_lowercase,
            'has_uppercase': has_uppercase,
            'has_digits': has_digits,
            'has_special': has_special,
            'char_types': char_types,
            'unique_chars': unique_chars,
            'unique_ratio': unique_ratio,
            'has_common_patterns': has_common_patterns,
            'is_common_password': is_common_password,
            'has_sequential': has_sequential,
            'has_repeated': has_repeated
        }
    
    def _calculate_score(self, password: str, criteria: Dict) -> int:
        """Calculate password strength score (0-100)."""
        score = 0
        
        # Length scoring (0-30 points)
        length = criteria['length']
        if length >= self.strong_length:
            score += 30
        elif length >= self.recommended_length:
            score += 25
        elif length >= self.min_length:
            score += 15
        else:
            score += max(0, length * 2)  # 2 points per character under 8
        
        # Character diversity (0-25 points)
        char_types = criteria['char_types']
        if char_types == 4:
            score += 25
        elif char_types == 3:
            score += 20
        elif char_types == 2:
            score += 15
        else:
            score += 5
        
        # Unique characters bonus (0-15 points)
        unique_ratio = criteria['unique_ratio']
        if unique_ratio >= 0.8:
            score += 15
        elif unique_ratio >= 0.6:
            score += 10
        elif unique_ratio >= 0.4:
            score += 5
        
        # Pattern and predictability penalties
        if criteria['is_common_password']:
            score -= 30
        
        if criteria['has_common_patterns']:
            score -= 15
        
        if criteria['has_sequential']:
            score -= 10
        
        if criteria['has_repeated']:
            score -= 5
        
        # Bonus points for very long passwords
        if length > 20:
            score += 10
        
        # Ensure score is between 0 and 100
        return max(0, min(100, score))
    
    def _determine_strength(self, score: int) -> PasswordStrength:
        """Determine password strength based on score."""
        if score >= 80:
            return PasswordStrength.VERY_STRONG
        elif score >= 65:
            return PasswordStrength.STRONG
        elif score >= 45:
            return PasswordStrength.MODERATE
        elif score >= 25:
            return PasswordStrength.WEAK
        else:
            return PasswordStrength.VERY_WEAK
    
    def _generate_feedback(self, password: str, criteria: Dict) -> List[str]:
        """Generate positive feedback about the password."""
        feedback = []
        
        if criteria['length'] >= self.strong_length:
            feedback.append(f"✅ Excellent length ({criteria['length']} characters)")
        elif criteria['length'] >= self.recommended_length:
            feedback.append(f"✅ Good length ({criteria['length']} characters)")
        elif criteria['length'] >= self.min_length:
            feedback.append(f"✅ Adequate length ({criteria['length']} characters)")
        
        if criteria['has_lowercase']:
            feedback.append("✅ Contains lowercase letters")
        
        if criteria['has_uppercase']:
            feedback.append("✅ Contains uppercase letters")
        
        if criteria['has_digits']:
            feedback.append("✅ Contains numbers")
        
        if criteria['has_special']:
            feedback.append("✅ Contains special characters")
        
        if criteria['unique_ratio'] >= 0.8:
            feedback.append("✅ High character diversity")
        
        if not criteria['has_common_patterns']:
            feedback.append("✅ No common patterns detected")
        
        if not criteria['is_common_password']:
            feedback.append("✅ Not a commonly used password")
        
        return feedback
    
    def _generate_recommendations(self, password: str, criteria: Dict) -> List[str]:
        """Generate recommendations for improving password strength."""
        recommendations = []
        
        if criteria['length'] < self.min_length:
            recommendations.append(f"❗ Increase length to at least {self.min_length} characters")
        elif criteria['length'] < self.recommended_length:
            recommendations.append(f"💡 Consider increasing length to {self.recommended_length}+ characters")
        
        if not criteria['has_lowercase']:
            recommendations.append("❗ Add lowercase letters (a-z)")
        
        if not criteria['has_uppercase']:
            recommendations.append("❗ Add uppercase letters (A-Z)")
        
        if not criteria['has_digits']:
            recommendations.append("❗ Add numbers (0-9)")
        
        if not criteria['has_special']:
            recommendations.append("❗ Add special characters (!@#$%^&*)")
        
        if criteria['unique_ratio'] < 0.4:
            recommendations.append("💡 Increase character diversity (avoid repetition)")
        
        if criteria['has_common_patterns']:
            recommendations.append("❗ Avoid common patterns like 'password', '123456', 'qwerty'")
        
        if criteria['is_common_password']:
            recommendations.append("❗ This is a commonly used password - choose something unique")
        
        if criteria['has_sequential']:
            recommendations.append("💡 Avoid sequential characters (123, abc, etc.)")
        
        if criteria['has_repeated']:
            recommendations.append("💡 Avoid excessive repeated characters")
        
        return recommendations
    
    def _has_sequential_chars(self, password: str) -> bool:
        """Check for sequential characters."""
        password_lower = password.lower()
        
        # Check for 3+ sequential letters or numbers
        for i in range(len(password_lower) - 2):
            if password_lower[i:i+3] in string.ascii_lowercase:
                return True
            if password_lower[i:i+3] in '0123456789':
                return True
            # Reverse sequences
            if password_lower[i:i+3] in string.ascii_lowercase[::-1]:
                return True
            if password_lower[i:i+3] in '9876543210':
                return True
        
        return False
    
    def _has_repeated_chars(self, password: str) -> bool:
        """Check for excessive repeated characters."""
        # Check for 3+ consecutive identical characters
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                return True
        
        return False

    def get_strength_color(self, strength: PasswordStrength) -> str:
        """Get color representation for password strength."""
        colors = {
            PasswordStrength.VERY_WEAK: '🔴',
            PasswordStrength.WEAK: '🟠',
            PasswordStrength.MODERATE: '🟡',
            PasswordStrength.STRONG: '🟢',
            PasswordStrength.VERY_STRONG: '💚'
        }
        return colors.get(strength, '⚪')