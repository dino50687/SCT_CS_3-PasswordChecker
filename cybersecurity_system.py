#!/usr/bin/env python3
"""
Comprehensive Cybersecurity System
Integrates all three layers of security features

Layer 1: Web Security & Phishing Detection
Layer 2: Account Security & Data Breach Protection  
Layer 3: Active Defense & Intelligence

Combined with the existing Password Strength Analyzer
"""

import sys
from typing import Dict
from password_analyzer import PasswordAnalyzer
from layer1_web_security import (
    VisualDNAAnalyzer, VoiceAlertAssistant, CommunityTrustMap,
    FakeSiteDetector, PrivacyBubbleMode
)
from layer2_account_security import (
    AccountRiskMeter, DataLeakPredictor, AutoPasswordHardener,
    DataShield, CyberAwarenessDashboard
)
from layer3_active_defense import (
    DecoyGenerator, AttackBehaviorLearningSystem, StudentSafetyMode,
    CorporateProtectionNetwork, CyberForensicsMode, AttackType
)


class CybersecuritySystem:
    """
    Unified cybersecurity system integrating all layers.
    """
    
    def __init__(self):
        # Original password analyzer
        self.password_analyzer = PasswordAnalyzer()
        
        # Layer 1: Web Security
        self.visual_dna = VisualDNAAnalyzer()
        self.voice_alert = VoiceAlertAssistant()
        self.trust_map = CommunityTrustMap()
        self.fake_detector = FakeSiteDetector()
        self.privacy_bubble = PrivacyBubbleMode()
        
        # Layer 2: Account Security
        self.risk_meter = AccountRiskMeter()
        self.leak_predictor = DataLeakPredictor()
        self.password_hardener = AutoPasswordHardener()
        self.data_shield = DataShield()
        self.awareness_dashboard = CyberAwarenessDashboard()
        
        # Layer 3: Active Defense
        self.decoy_generator = DecoyGenerator()
        self.attack_learning = AttackBehaviorLearningSystem()
        self.safety_mode = StudentSafetyMode()
        self.corporate_network = CorporateProtectionNetwork()
        self.forensics = CyberForensicsMode()
    
    def comprehensive_password_check(self, password: str, domain: str = None) -> Dict:
        """
        Comprehensive password analysis combining original analyzer with new features.
        
        Args:
            password: Password to analyze
            domain: Optional domain for domain-specific checks
            
        Returns:
            Comprehensive analysis results
        """
        # Original password analysis
        basic_analysis = self.password_analyzer.analyze_password(password)
        
        # Additional Layer 2 analysis
        enhanced_analysis = {
            'basic_analysis': basic_analysis,
            'password_improvements': self.password_hardener.suggest_password_improvements(password)
        }
        
        # If domain provided, check risk
        if domain:
            risk_analysis = self.risk_meter.calculate_risk_score(domain, password)
            enhanced_analysis['domain_risk'] = risk_analysis
            
            # Check domain trust
            trust_info = self.trust_map.check_domain_trust(domain)
            enhanced_analysis['domain_trust'] = trust_info
        
        return enhanced_analysis
    
    def check_website_safety(self, url: str, content: str = None) -> Dict:
        """
        Comprehensive website safety check.
        
        Args:
            url: Website URL
            content: Optional page content
            
        Returns:
            Safety analysis
        """
        domain = url.replace('https://', '').replace('http://', '').split('/')[0]
        
        # Check trust
        trust_check = self.trust_map.check_domain_trust(domain)
        
        # Check for fake site indicators
        fake_check = self.fake_detector.analyze_site(url, content)
        
        # Create visual fingerprint
        visual_fp = self.visual_dna.create_visual_fingerprint(url, content)
        
        # Privacy scan
        privacy_scan = self.privacy_bubble.scan_page(url)
        
        # Trigger voice alert if dangerous
        if trust_check['trust_level'].value == 'dangerous' or fake_check['likely_fake']:
            alert = self.voice_alert.trigger_alert(
                'phishing' if fake_check['likely_fake'] else 'high_risk',
                {'url': url, 'trust_score': trust_check.get('trust_score', 0)}
            )
        else:
            alert = None
        
        return {
            'url': url,
            'trust_check': trust_check,
            'fake_site_check': fake_check,
            'visual_fingerprint': visual_fp['fingerprint_hash'],
            'privacy_threats': privacy_scan['threats_found'],
            'voice_alert': alert,
            'overall_safety': self._calculate_overall_safety(trust_check, fake_check)
        }
    
    def generate_secure_password(self, domain: str, length: int = 16) -> Dict:
        """
        Generate a secure, domain-specific password.
        
        Args:
            domain: Domain for which to generate password
            length: Password length
            
        Returns:
            Generated password and analysis
        """
        # Generate password
        generated = self.password_hardener.generate_domain_specific_password(domain, length=length)
        
        # Analyze it
        analysis = self.password_analyzer.analyze_password(generated['password'])
        
        return {
            'generated_password': generated,
            'strength_analysis': analysis,
            'recommendation': 'Store this password in a secure password manager'
        }
    
    def activate_student_protection(self, research_topic: str = "cybersecurity") -> Dict:
        """
        Activate comprehensive student protection mode.
        
        Args:
            research_topic: Topic of research
            
        Returns:
            Protection status
        """
        # Activate sandbox
        sandbox = self.safety_mode.activate_sandbox(research_topic)
        
        # Start forensic logging
        forensics = self.forensics.start_forensic_session("educational")
        
        # Enable privacy bubble
        privacy = self.privacy_bubble.enable_privacy_mode('high')
        
        return {
            'sandbox': sandbox,
            'forensics': forensics,
            'privacy': privacy,
            'status': 'MAXIMUM PROTECTION ACTIVE',
            'note': 'All your real data is protected. Fake data will be used for any forms.'
        }
    
    def _calculate_overall_safety(self, trust_check: Dict, fake_check: Dict) -> str:
        """Calculate overall safety level."""
        trust_score = trust_check.get('trust_score', 50)
        fake_risk = fake_check.get('risk_score', 0)
        
        if trust_score >= 80 and fake_risk < 30:
            return 'SAFE ✅'
        elif trust_score >= 50 and fake_risk < 50:
            return 'CAUTION ⚠️'
        else:
            return 'DANGEROUS 🚨'


def print_menu():
    """Print the main menu."""
    print("\n" + "=" * 70)
    print("🔐 COMPREHENSIVE CYBERSECURITY SYSTEM 🔐")
    print("=" * 70)
    print("\n🛡️  LAYER 1: Web Security & Phishing Detection")
    print("   1. Check Website Safety")
    print("   2. Register Trusted Website")
    print("   3. Check Domain Trust Level")
    print("   4. Scan for Privacy Threats")
    
    print("\n🔑 LAYER 2: Account Security & Data Breach Protection")
    print("   5. Check Account Risk")
    print("   6. Generate Secure Password")
    print("   7. Analyze Password Strength (Original)")
    print("   8. View Cyber Awareness Dashboard")
    
    print("\n⚔️  LAYER 3: Active Defense & Intelligence")
    print("   9. Activate Student Safety Mode")
    print("   10. Generate Decoy Fields")
    print("   11. View Attack Statistics")
    print("   12. Start Forensic Session")
    
    print("\n   0. Exit")
    print("=" * 70)


def interactive_mode():
    """Run interactive mode."""
    system = CybersecuritySystem()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nSelect option (0-12): ").strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye! Stay secure! 🔒")
            break
        
        if choice == '0':
            print("\nGoodbye! Stay secure! 🔒")
            break
        
        elif choice == '1':
            url = input("Enter website URL: ").strip()
            print("\n🔍 Checking website safety...")
            result = system.check_website_safety(url)
            print(f"\nURL: {result['url']}")
            print(f"Trust Level: {result['trust_check']['trust_level'].value.upper()}")
            print(f"Trust Score: {result['trust_check'].get('trust_score', 'N/A')}/100")
            print(f"Fake Site Risk: {result['fake_site_check']['risk_score']}/100")
            print(f"Privacy Threats: {result['privacy_threats']}")
            print(f"Overall Safety: {result['overall_safety']}")
            if result['voice_alert']:
                print(f"\n🔊 {result['voice_alert']['message']}")
        
        elif choice == '2':
            url = input("Enter website URL to register as trusted: ").strip()
            result = system.visual_dna.register_trusted_site(url)
            print(f"\n✅ Registered: {result['domain']}")
            print(f"Fingerprint: {result['fingerprint_hash']}")
        
        elif choice == '3':
            domain = input("Enter domain to check: ").strip()
            result = system.trust_map.check_domain_trust(domain)
            print(f"\nDomain: {result['domain']}")
            print(f"Trust Level: {result['trust_level'].value.upper()}")
            print(f"Trust Score: {result['trust_score']}/100")
            print(f"Verified: {'Yes ✅' if result.get('verified') else 'No'}")
            print(f"Recommendation: {result['recommendation']}")
        
        elif choice == '4':
            url = input("Enter URL to scan: ").strip()
            result = system.privacy_bubble.scan_page(url)
            print(f"\n🔍 Privacy Scan Results")
            print(f"Threats Found: {result['threats_found']}")
            print(f"Items Blocked: {result['items_blocked']}")
            print(f"Protection Level: {result['protection_level'].upper()}")
        
        elif choice == '5':
            domain = input("Enter domain: ").strip()
            password = input("Enter password: ").strip()
            result = system.risk_meter.calculate_risk_score(domain, password)
            print(f"\n⚠️ Account Risk Assessment")
            print(f"Risk Level: {result['risk_level'].value.upper()}")
            print(f"Risk Score: {result['risk_score']}/100")
            if result['risk_factors']:
                print("Risk Factors:")
                for factor in result['risk_factors']:
                    print(f"  • {factor}")
        
        elif choice == '6':
            domain = input("Enter domain: ").strip()
            length = input("Password length (default 16): ").strip()
            length = int(length) if length else 16
            result = system.generate_secure_password(domain, length)
            print(f"\n🔑 Generated Secure Password")
            print(f"Password: {result['generated_password']['password']}")
            print(f"Strength: {result['strength_analysis']['score']}/100")
            print(f"Level: {result['strength_analysis']['strength'].name}")
            print(f"\n💡 {result['recommendation']}")
        
        elif choice == '7':
            password = input("Enter password to analyze: ").strip()
            result = system.password_analyzer.analyze_password(password)
            print(f"\n📊 Password Analysis")
            print(f"Strength: {result['strength'].name}")
            print(f"Score: {result['score']}/100")
            print(f"\n✅ Strengths:")
            for feedback in result['feedback'][:3]:
                print(f"  {feedback}")
            if result['recommendations']:
                print(f"\n💡 Recommendations:")
                for rec in result['recommendations'][:3]:
                    print(f"  {rec}")
        
        elif choice == '8':
            stats = system.awareness_dashboard.get_global_statistics()
            print(f"\n📊 Cyber Awareness Dashboard")
            print(f"Total Breaches: {stats['total_breaches']:,}")
            print(f"Records Compromised: {stats['total_records_compromised']:,}")
            print("\nTop 3 Sectors by Breaches:")
            for sector, data in sorted(stats['by_sector'].items(), 
                                      key=lambda x: x[1]['breaches'], 
                                      reverse=True)[:3]:
                print(f"  {sector}: {data['breaches']} breaches")
        
        elif choice == '9':
            topic = input("Research topic (default: cybersecurity): ").strip()
            topic = topic if topic else "cybersecurity"
            result = system.activate_student_protection(topic)
            print(f"\n🛡️ Student Protection Activated")
            print(f"Status: {result['status']}")
            print(f"Sandbox ID: {result['sandbox']['session_id'][:16]}...")
            print(f"Forensics ID: {result['forensics']['session_id'][:16]}...")
            print(f"\n⚠️ {result['note']}")
        
        elif choice == '10':
            context = input("Form context (login/payment/profile): ").strip()
            context = context if context in ['login', 'payment', 'profile'] else 'login'
            result = system.decoy_generator.generate_decoy_fields(context)
            print(f"\n🎭 Decoy Fields Generated")
            print(f"Decoy ID: {result['decoy_id'][:16]}...")
            print(f"Fields Created: {result['field_count']}")
            print("Sample Decoys:")
            for field, value in list(result['fields'].items())[:2]:
                print(f"  {field}: {value}")
            print(f"\n💡 {result['note']}")
        
        elif choice == '11':
            analysis = system.attack_learning.analyze_patterns()
            print(f"\n📈 Attack Statistics")
            print(f"Total Attacks: {analysis['total_attacks']}")
            print(f"Unique Attackers: {analysis['unique_attackers']}")
            if analysis['attack_distribution']:
                print("Attack Distribution:")
                for attack_type, count in analysis['attack_distribution'].items():
                    print(f"  {attack_type}: {count}")
        
        elif choice == '12':
            purpose = input("Session purpose (default: educational): ").strip()
            purpose = purpose if purpose else "educational"
            result = system.forensics.start_forensic_session(purpose)
            print(f"\n🔬 Forensic Session Started")
            print(f"Session ID: {result['session_id'][:16]}...")
            print(f"Purpose: {result['purpose']}")
            print("Features Enabled:")
            for feature in result['features'][:3]:
                print(f"  ✅ {feature}")
        
        else:
            print("\n❌ Invalid option. Please select 0-12.")
        
        input("\nPress Enter to continue...")


def main():
    """Main function."""
    print("=" * 70)
    print("🔐 COMPREHENSIVE CYBERSECURITY SYSTEM 🔐")
    print("=" * 70)
    print("\nIntegrating:")
    print("  🛡️  Layer 1: Web Security & Phishing Detection")
    print("  🔑 Layer 2: Account Security & Data Breach Protection")
    print("  ⚔️  Layer 3: Active Defense & Intelligence")
    print("  🔐 Password Strength Analyzer (Original)")
    print("=" * 70)
    
    if len(sys.argv) > 1:
        # Command-line mode: analyze password
        password = ' '.join(sys.argv[1:])
        system = CybersecuritySystem()
        result = system.comprehensive_password_check(password)
        
        print("\n📊 COMPREHENSIVE PASSWORD ANALYSIS")
        print("=" * 70)
        basic = result['basic_analysis']
        print(f"Strength: {basic['strength'].name}")
        print(f"Score: {basic['score']}/100")
        
        if basic['feedback']:
            print("\n✅ Strengths:")
            for feedback in basic['feedback'][:3]:
                print(f"  {feedback}")
        
        if result['password_improvements']:
            print("\n💡 Improvements:")
            for improvement in result['password_improvements'][:3]:
                print(f"  {improvement}")
    else:
        # Interactive mode
        try:
            interactive_mode()
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")


if __name__ == "__main__":
    main()
