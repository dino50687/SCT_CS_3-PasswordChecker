#!/usr/bin/env python3
"""
Test Suite for Password Strength Analyzer

Comprehensive tests to validate password strength assessment logic.
"""

import unittest
import sys
import os

# Add the current directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from password_analyzer import PasswordAnalyzer, PasswordStrength


class TestPasswordAnalyzer(unittest.TestCase):
    """Test cases for the PasswordAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.analyzer = PasswordAnalyzer()
    
    def test_empty_password(self):
        """Test analysis of empty password."""
        result = self.analyzer.analyze_password("")
        self.assertEqual(result['score'], 0)
        self.assertEqual(result['strength'], PasswordStrength.VERY_WEAK)
        self.assertIn('Password cannot be empty', result['feedback'])
    
    def test_very_weak_passwords(self):
        """Test very weak passwords."""
        weak_passwords = ['1', '12', '123', 'a', 'password', '123456']
        
        for password in weak_passwords:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertLessEqual(result['score'], 25, 
                                   f"Password '{password}' should have score <= 25, got {result['score']}")
                self.assertIn(result['strength'], [PasswordStrength.VERY_WEAK, PasswordStrength.WEAK])
    
    def test_moderate_passwords(self):
        """Test moderately strong passwords."""
        moderate_passwords = ['Hello123!', 'MyP@ss99', 'Test1234$', 'Strong9!']
        
        for password in moderate_passwords:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertGreater(result['score'], 25)
                self.assertLess(result['score'], 65)
    
    def test_strong_passwords(self):
        """Test strong passwords."""
        strong_passwords = [
            'MyStr0ngP@ssw0rd!',
            'Tr0ub4dor&3',
            'C0mpl3x!P@ssw0rd',
            'Sup3rS3cur3#2023'
        ]
        
        for password in strong_passwords:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertGreaterEqual(result['score'], 45)
    
    def test_very_strong_passwords(self):
        """Test very strong passwords."""
        very_strong_passwords = [
            'X9#mK2$vN8@qL5&Rt7!',
            'MyVery$tr0ng!P@ssw0rd#2023',
            'Sup3r!C0mpl3x#P@ssw0rd$123'
        ]
        
        for password in very_strong_passwords:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertGreaterEqual(result['score'], 65)
    
    def test_length_criteria(self):
        """Test password length analysis."""
        # Test short password
        result = self.analyzer.analyze_password('Ab1!')
        criteria = result['criteria']
        self.assertEqual(criteria['length'], 4)
        self.assertLess(result['score'], 55)  # Updated expectation
        
        # Test adequate length
        result = self.analyzer.analyze_password('Ab1!2345')
        criteria = result['criteria']
        self.assertEqual(criteria['length'], 8)
        
        # Test long password
        result = self.analyzer.analyze_password('Ab1!' * 5)  # 20 characters
        criteria = result['criteria']
        self.assertEqual(criteria['length'], 20)
    
    def test_character_type_detection(self):
        """Test detection of different character types."""
        # Test lowercase detection
        result = self.analyzer.analyze_password('lowercase')
        self.assertTrue(result['criteria']['has_lowercase'])
        self.assertFalse(result['criteria']['has_uppercase'])
        self.assertFalse(result['criteria']['has_digits'])
        self.assertFalse(result['criteria']['has_special'])
        
        # Test uppercase detection
        result = self.analyzer.analyze_password('UPPERCASE')
        self.assertFalse(result['criteria']['has_lowercase'])
        self.assertTrue(result['criteria']['has_uppercase'])
        self.assertFalse(result['criteria']['has_digits'])
        self.assertFalse(result['criteria']['has_special'])
        
        # Test digits detection
        result = self.analyzer.analyze_password('123456789')
        self.assertFalse(result['criteria']['has_lowercase'])
        self.assertFalse(result['criteria']['has_uppercase'])
        self.assertTrue(result['criteria']['has_digits'])
        self.assertFalse(result['criteria']['has_special'])
        
        # Test special characters detection
        result = self.analyzer.analyze_password('!@#$%^&*()')
        self.assertFalse(result['criteria']['has_lowercase'])
        self.assertFalse(result['criteria']['has_uppercase'])
        self.assertFalse(result['criteria']['has_digits'])
        self.assertTrue(result['criteria']['has_special'])
        
        # Test all character types
        result = self.analyzer.analyze_password('Test123!')
        self.assertTrue(result['criteria']['has_lowercase'])
        self.assertTrue(result['criteria']['has_uppercase'])
        self.assertTrue(result['criteria']['has_digits'])
        self.assertTrue(result['criteria']['has_special'])
        self.assertEqual(result['criteria']['char_types'], 4)
    
    def test_common_password_detection(self):
        """Test detection of common passwords."""
        common_passwords = ['password', '123456', 'qwerty', 'admin']
        
        for password in common_passwords:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertTrue(result['criteria']['is_common_password'],
                              f"Should detect '{password}' as common password")
        
        # Test non-common password
        result = self.analyzer.analyze_password('UniqueP@ssw0rd!')
        self.assertFalse(result['criteria']['is_common_password'])
    
    def test_pattern_detection(self):
        """Test detection of common patterns."""
        # Test passwords containing "password"
        result = self.analyzer.analyze_password('mypassword123')
        self.assertTrue(result['criteria']['has_common_patterns'])
        
        # Test sequential numbers
        result = self.analyzer.analyze_password('test123456')
        self.assertTrue(result['criteria']['has_common_patterns'])
        
        # Test keyboard patterns
        result = self.analyzer.analyze_password('myqwerty')
        self.assertTrue(result['criteria']['has_common_patterns'])
        
        # Test password without patterns
        result = self.analyzer.analyze_password('RandomStr0ng!')
        self.assertFalse(result['criteria']['has_common_patterns'])
    
    def test_sequential_characters(self):
        """Test detection of sequential characters."""
        # Test with sequential letters
        result = self.analyzer.analyze_password('abcdef123')
        self.assertTrue(result['criteria']['has_sequential'])
        
        # Test with sequential numbers
        result = self.analyzer.analyze_password('password123456')
        self.assertTrue(result['criteria']['has_sequential'])
        
        # Test with reverse sequential
        result = self.analyzer.analyze_password('zyxwvu321')
        self.assertTrue(result['criteria']['has_sequential'])
        
        # Test without sequential characters
        result = self.analyzer.analyze_password('Rand0mStr!ng')
        self.assertFalse(result['criteria']['has_sequential'])
    
    def test_repeated_characters(self):
        """Test detection of repeated characters."""
        # Test with repeated characters
        result = self.analyzer.analyze_password('aaaapassword')
        self.assertTrue(result['criteria']['has_repeated'])
        
        result = self.analyzer.analyze_password('pass111word')
        self.assertTrue(result['criteria']['has_repeated'])
        
        # Test without excessive repetition
        result = self.analyzer.analyze_password('password11')  # Only 2 repeated
        self.assertFalse(result['criteria']['has_repeated'])
        
        result = self.analyzer.analyze_password('UniqueP@ssw0rd')
        self.assertFalse(result['criteria']['has_repeated'])
    
    def test_unique_character_ratio(self):
        """Test unique character ratio calculation."""
        # Test password with all unique characters
        result = self.analyzer.analyze_password('abcdef')
        self.assertEqual(result['criteria']['unique_ratio'], 1.0)
        
        # Test password with repeated characters
        result = self.analyzer.analyze_password('aabbcc')
        self.assertEqual(result['criteria']['unique_ratio'], 0.5)
        
        # Test password with all same characters
        result = self.analyzer.analyze_password('aaaa')
        self.assertEqual(result['criteria']['unique_ratio'], 0.25)
    
    def test_score_bounds(self):
        """Test that scores are always within valid bounds."""
        test_passwords = [
            '',
            '1',
            'password',
            'Password123',
            'Str0ng!P@ssw0rd',
            'VeryStr0ng!P@ssw0rd#2023$',
            'X' * 50  # Very long password
        ]
        
        for password in test_passwords:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertGreaterEqual(result['score'], 0,
                                      f"Score should be >= 0, got {result['score']}")
                self.assertLessEqual(result['score'], 100,
                                   f"Score should be <= 100, got {result['score']}")
    
    def test_feedback_generation(self):
        """Test that appropriate feedback is generated."""
        # Test strong password feedback
        result = self.analyzer.analyze_password('VeryStr0ng!P@ssw0rd')
        self.assertGreater(len(result['feedback']), 0)
        self.assertTrue(any('✅' in feedback for feedback in result['feedback']))
        
        # Test weak password recommendations
        result = self.analyzer.analyze_password('weak')
        self.assertGreater(len(result['recommendations']), 0)
        self.assertTrue(any('❗' in rec or '💡' in rec for rec in result['recommendations']))
    
    def test_strength_enum_mapping(self):
        """Test that strength enum values are correctly mapped."""
        # Test very weak
        result = self.analyzer.analyze_password('1')
        self.assertEqual(result['strength'], PasswordStrength.VERY_WEAK)
        
        # Test that strength enum values are valid
        self.assertIn(result['strength'], list(PasswordStrength))
    
    def test_color_indicator(self):
        """Test color indicator functionality."""
        for strength in PasswordStrength:
            color = self.analyzer.get_strength_color(strength)
            self.assertIsInstance(color, str)
            self.assertGreater(len(color), 0)


class TestPasswordCheckerIntegration(unittest.TestCase):
    """Integration tests for the password checker CLI."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = PasswordAnalyzer()
    
    def test_analyze_complete_workflow(self):
        """Test complete analysis workflow."""
        password = 'TestP@ssw0rd123!'
        result = self.analyzer.analyze_password(password)
        
        # Verify all expected keys are present
        expected_keys = ['password', 'score', 'strength', 'feedback', 'criteria', 'recommendations']
        for key in expected_keys:
            self.assertIn(key, result)
        
        # Verify criteria has all expected fields
        criteria = result['criteria']
        expected_criteria = [
            'length', 'has_lowercase', 'has_uppercase', 'has_digits',
            'has_special', 'char_types', 'unique_chars', 'unique_ratio',
            'has_common_patterns', 'is_common_password', 'has_sequential',
            'has_repeated'
        ]
        for criterion in expected_criteria:
            self.assertIn(criterion, criteria)
    
    def test_real_world_passwords(self):
        """Test with real-world password examples."""
        test_cases = [
            # (password, expected_min_score, expected_max_score)
            ('123456', 0, 20),           # Very weak
            ('password', 0, 25),         # Very weak
            ('Password1', 0, 50),        # Weak (heavy penalties for common word)
            ('MyP@ssw0rd!', 45, 75),     # Moderate to strong
            ('Tr0ub4dor&3', 50, 85),     # Strong
            ('correct-horse-battery-staple', 55, 85),  # Passphrase
            ('X9#mK2$vN8@qL5&Rt7!', 65, 100)  # Very strong
        ]
        
        for password, min_score, max_score in test_cases:
            with self.subTest(password=password):
                result = self.analyzer.analyze_password(password)
                self.assertGreaterEqual(result['score'], min_score,
                                      f"'{password}' score {result['score']} should be >= {min_score}")
                self.assertLessEqual(result['score'], max_score,
                                   f"'{password}' score {result['score']} should be <= {max_score}")


def run_tests():
    """Run all tests and display results."""
    print("🧪 Running Password Analyzer Test Suite")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordCheckerIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("✅ All tests passed! The password analyzer is working correctly.")
    else:
        print(f"❌ {len(result.failures + result.errors)} test(s) failed.")
        if result.failures:
            print("\nFailures:")
            for test, traceback in result.failures:
                print(f"  - {test}: {traceback}")
        if result.errors:
            print("\nErrors:")
            for test, traceback in result.errors:
                print(f"  - {test}: {traceback}")
    
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)