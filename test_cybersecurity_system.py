#!/usr/bin/env python3
"""
Comprehensive Test Suite for Multi-Layer Cybersecurity System

Tests for:
- Layer 1: Web Security & Phishing Detection
- Layer 2: Account Security & Data Breach Protection
- Layer 3: Active Defense & Intelligence
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from layer1_web_security import (
    VisualDNAAnalyzer, VoiceAlertAssistant, CommunityTrustMap,
    FakeSiteDetector, PrivacyBubbleMode, TrustLevel
)
from layer2_account_security import (
    AccountRiskMeter, DataLeakPredictor, AutoPasswordHardener,
    DataShield, CyberAwarenessDashboard, RiskLevel
)
from layer3_active_defense import (
    DecoyGenerator, AttackBehaviorLearningSystem, StudentSafetyMode,
    CorporateProtectionNetwork, CyberForensicsMode, AttackType
)


class TestLayer1WebSecurity(unittest.TestCase):
    """Test cases for Layer 1 features."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.dna_analyzer = VisualDNAAnalyzer()
        self.voice_alert = VoiceAlertAssistant()
        self.trust_map = CommunityTrustMap()
        self.fake_detector = FakeSiteDetector()
        self.privacy_bubble = PrivacyBubbleMode()
    
    def test_visual_dna_fingerprint_creation(self):
        """Test visual DNA fingerprint creation."""
        result = self.dna_analyzer.create_visual_fingerprint(
            'https://example.com',
            colors=['#FF0000', '#00FF00']
        )
        self.assertIn('fingerprint_hash', result)
        self.assertIn('color_palette', result)
        self.assertEqual(result['domain'], 'example.com')
    
    def test_trusted_site_registration(self):
        """Test registering trusted sites."""
        result = self.dna_analyzer.register_trusted_site('https://test.com')
        self.assertEqual(result['status'], 'registered')
        self.assertIn('test.com', self.dna_analyzer.trusted_fingerprints)
    
    def test_visual_mismatch_detection(self):
        """Test detection of visual mismatches."""
        # Register trusted site
        self.dna_analyzer.register_trusted_site('https://paypal.com')
        
        # Create different fingerprint
        fake_fp = self.dna_analyzer.create_visual_fingerprint(
            'https://paypal.com',
            colors=['#000000']  # Different colors
        )
        
        # Verify should detect mismatch
        result = self.dna_analyzer.verify_visual_match('https://paypal.com', fake_fp)
        self.assertIn('mismatch_percentage', result)
    
    def test_voice_alert_trigger(self):
        """Test voice alert triggering."""
        result = self.voice_alert.trigger_alert('phishing', {'domain': 'test.com'})
        self.assertEqual(result['alert_type'], 'phishing')
        self.assertIn('message', result)
        self.assertTrue(result['action_required'])
    
    def test_community_trust_check(self):
        """Test community trust checking."""
        result = self.trust_map.check_domain_trust('google.com')
        self.assertEqual(result['trust_level'], TrustLevel.TRUSTED)
        self.assertGreater(result['trust_score'], 80)
    
    def test_fake_site_detection(self):
        """Test fake site detection."""
        result = self.fake_detector.analyze_site(
            'https://fake-scholarship.com',
            'URGENT: Claim your scholarship NOW! Limited time!',
            domain_age=20
        )
        self.assertGreater(result['risk_score'], 0)
        self.assertIn('red_flags', result)
    
    def test_privacy_bubble_scanning(self):
        """Test privacy bubble page scanning."""
        result = self.privacy_bubble.scan_page(
            'https://test.com',
            trackers=['doubleclick.net', 'facebook-pixel.js']
        )
        self.assertGreater(result['threats_found'], 0)
        self.assertEqual(result['protection_level'], 'high')


class TestLayer2AccountSecurity(unittest.TestCase):
    """Test cases for Layer 2 features."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.risk_meter = AccountRiskMeter()
        self.leak_predictor = DataLeakPredictor()
        self.password_hardener = AutoPasswordHardener()
        self.data_shield = DataShield()
        self.dashboard = CyberAwarenessDashboard()
    
    def test_risk_score_calculation(self):
        """Test account risk score calculation."""
        result = self.risk_meter.calculate_risk_score(
            'linkedin.com',
            'weakpass',
            'user@example.com'
        )
        self.assertIn('risk_score', result)
        self.assertIn('risk_level', result)
        self.assertIsInstance(result['risk_level'], RiskLevel)
    
    def test_breach_prediction(self):
        """Test data leak prediction."""
        result = self.leak_predictor.predict_leak_risk(
            'example.com',
            ['high_breach_frequency', 'outdated_security']
        )
        self.assertIn('prediction', result)
        self.assertIn('total_risk_score', result)
        self.assertGreater(result['total_risk_score'], 0)
    
    def test_password_generation(self):
        """Test domain-specific password generation."""
        result = self.password_hardener.generate_domain_specific_password(
            'github.com',
            length=20
        )
        self.assertEqual(len(result['password']), 20)
        self.assertEqual(result['domain'], 'github.com')
        self.assertGreaterEqual(result['strength_score'], 80)
    
    def test_password_improvement_suggestions(self):
        """Test password improvement suggestions."""
        suggestions = self.password_hardener.suggest_password_improvements('weak')
        self.assertGreater(len(suggestions), 0)
        self.assertTrue(any('length' in s.lower() for s in suggestions))
    
    def test_data_shield_registration(self):
        """Test domain registration for monitoring."""
        result = self.data_shield.register_domain('test.edu', 'Test University')
        self.assertEqual(result['status'], 'registered')
        self.assertTrue(result['monitoring'])
    
    def test_global_statistics(self):
        """Test cyber awareness dashboard statistics."""
        stats = self.dashboard.get_global_statistics()
        self.assertIn('total_breaches', stats)
        self.assertIn('by_country', stats)
        self.assertIn('by_sector', stats)


class TestLayer3ActiveDefense(unittest.TestCase):
    """Test cases for Layer 3 features."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.decoy_gen = DecoyGenerator()
        self.abls = AttackBehaviorLearningSystem()
        self.safety_mode = StudentSafetyMode()
        self.corp_network = CorporateProtectionNetwork()
        self.forensics = CyberForensicsMode()
    
    def test_decoy_field_generation(self):
        """Test decoy field generation."""
        result = self.decoy_gen.generate_decoy_fields('login')
        self.assertIn('decoy_id', result)
        self.assertIn('fields', result)
        self.assertGreater(result['field_count'], 0)
    
    def test_decoy_access_detection(self):
        """Test detection of decoy field access."""
        decoys = self.decoy_gen.generate_decoy_fields('login')
        decoy_field = list(decoys['fields'].keys())[0]
        
        result = self.decoy_gen.check_decoy_access(
            decoys['decoy_id'],
            [decoy_field],
            '192.168.1.1'
        )
        self.assertTrue(result['attack_detected'])
        self.assertEqual(result['severity'], 'HIGH')
    
    def test_attack_recording(self):
        """Test attack behavior recording."""
        result = self.abls.record_attack(
            AttackType.CREDENTIAL_THEFT,
            {'ip': '192.168.1.1'},
            {'method': 'form_scraping'}
        )
        self.assertIn('attack_id', result)
        self.assertIn('fingerprint', result)
        self.assertTrue(result['recorded'])
    
    def test_attack_pattern_analysis(self):
        """Test attack pattern analysis."""
        # Record some attacks first
        self.abls.record_attack(
            AttackType.PHISHING,
            {'ip': '192.168.1.1'},
            {'method': 'email'}
        )
        
        result = self.abls.analyze_patterns()
        self.assertIn('total_attacks', result)
        self.assertGreaterEqual(result['total_attacks'], 1)
    
    def test_sandbox_activation(self):
        """Test student safety sandbox activation."""
        result = self.safety_mode.activate_sandbox('research')
        self.assertIn('session_id', result)
        self.assertTrue(result['sandbox_active'])
        self.assertEqual(result['protection_level'], 'maximum')
    
    def test_sandbox_fake_data(self):
        """Test fake data generation in sandbox."""
        session = self.safety_mode.activate_sandbox()
        result = self.safety_mode.get_sandbox_data('email')
        self.assertIn('value', result)
        self.assertIn('sandbox', result['value'])
    
    def test_corporate_network_registration(self):
        """Test employee registration in corporate network."""
        result = self.corp_network.register_employee('emp001', 'TestCorp')
        self.assertIn('node_id', result)
        self.assertTrue(result['registered'])
    
    def test_threat_broadcasting(self):
        """Test threat broadcasting in corporate network."""
        # Register two employees
        node1 = self.corp_network.register_employee('emp001', 'TestCorp')
        node2 = self.corp_network.register_employee('emp002', 'TestCorp')
        
        # Broadcast threat
        result = self.corp_network.broadcast_threat(
            node1['node_id'],
            {'type': 'phishing', 'severity': 'high'}
        )
        self.assertTrue(result['broadcast'] == 'successful')
        self.assertGreaterEqual(result['nodes_alerted'], 1)
    
    def test_forensic_session(self):
        """Test forensic session creation."""
        result = self.forensics.start_forensic_session('educational')
        self.assertIn('session_id', result)
        self.assertEqual(result['status'], 'active')
    
    def test_attack_logging(self):
        """Test attack attempt logging."""
        session = self.forensics.start_forensic_session()
        result = self.forensics.log_attack_attempt(
            session['session_id'],
            {'type': 'xss', 'payload': '<script>alert(1)</script>'}
        )
        self.assertTrue(result['logged'])
        self.assertIn('log_id', result)
    
    def test_forensic_report_generation(self):
        """Test forensic report generation."""
        session = self.forensics.start_forensic_session()
        
        # Log some attacks
        self.forensics.log_attack_attempt(
            session['session_id'],
            {'type': 'xss', 'payload': 'test'}
        )
        
        report = self.forensics.generate_forensic_report(session['session_id'])
        self.assertIn('total_events', report)
        self.assertGreaterEqual(report['total_events'], 1)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system."""
    
    def test_full_workflow(self):
        """Test a complete security workflow."""
        # Layer 1: Check website
        trust_map = CommunityTrustMap()
        trust_result = trust_map.check_domain_trust('google.com')
        self.assertEqual(trust_result['trust_level'], TrustLevel.TRUSTED)
        
        # Layer 2: Generate secure password
        hardener = AutoPasswordHardener()
        password = hardener.generate_domain_specific_password('google.com')
        self.assertGreaterEqual(password['strength_score'], 80)
        
        # Layer 3: Activate protection
        safety = StudentSafetyMode()
        sandbox = safety.activate_sandbox()
        self.assertTrue(sandbox['sandbox_active'])


def run_tests():
    """Run all tests and display results."""
    print("=" * 70)
    print("🧪 COMPREHENSIVE CYBERSECURITY SYSTEM TEST SUITE")
    print("=" * 70)
    print("\nTesting:")
    print("  🛡️  Layer 1: Web Security & Phishing Detection")
    print("  🔑 Layer 2: Account Security & Data Breach Protection")
    print("  ⚔️  Layer 3: Active Defense & Intelligence")
    print("=" * 70)
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestLayer1WebSecurity))
    suite.addTests(loader.loadTestsFromTestCase(TestLayer2AccountSecurity))
    suite.addTests(loader.loadTestsFromTestCase(TestLayer3ActiveDefense))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("✅ All tests passed! The cybersecurity system is working correctly.")
    else:
        print(f"❌ {len(result.failures + result.errors)} test(s) failed.")
    
    print(f"\nTests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
