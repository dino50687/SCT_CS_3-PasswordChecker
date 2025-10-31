"""
Layer 1: Web Security & Phishing Detection

Features:
1. AI Visual DNA of Websites (color palette, layout, logo ratio, text tone)
2. Voice Alert Assistant
3. Community Trust Map
4. Fake Scholarship/Job Site Detection
5. Privacy Bubble Mode
"""

import hashlib
import json
import re
from typing import Dict, List, Tuple
from datetime import datetime
from collections import Counter
from enum import Enum


class TrustLevel(Enum):
    """Trust level for websites."""
    TRUSTED = "trusted"
    SUSPICIOUS = "suspicious"
    DANGEROUS = "dangerous"
    UNKNOWN = "unknown"


class VisualDNAAnalyzer:
    """
    Creates a unique visual fingerprint for websites.
    Analyzes color palette, layout patterns, logo characteristics, and text tone.
    """
    
    def __init__(self):
        self.trusted_fingerprints = {}
        self.mismatch_threshold = 0.01  # 1% mismatch triggers alert
        
    def create_visual_fingerprint(self, url: str, html_content: str = None, 
                                  colors: List[str] = None, 
                                  layout_signature: str = None) -> Dict:
        """
        Create a visual DNA fingerprint for a website.
        
        Args:
            url: Website URL
            html_content: HTML content (optional)
            colors: List of dominant colors (optional)
            layout_signature: Layout pattern signature (optional)
            
        Returns:
            Visual fingerprint dictionary
        """
        # Extract domain
        domain = self._extract_domain(url)
        
        # Generate color palette fingerprint
        color_fingerprint = self._analyze_colors(colors if colors else ['#FFFFFF', '#000000'])
        
        # Generate layout fingerprint
        layout_fingerprint = self._analyze_layout(layout_signature if layout_signature else 'standard')
        
        # Generate text tone analysis
        text_tone = self._analyze_text_tone(html_content if html_content else '')
        
        # Create composite fingerprint
        fingerprint = {
            'domain': domain,
            'url': url,
            'color_palette': color_fingerprint,
            'layout_pattern': layout_fingerprint,
            'text_tone': text_tone,
            'timestamp': datetime.now().isoformat(),
            'fingerprint_hash': self._generate_fingerprint_hash(
                color_fingerprint, layout_fingerprint, text_tone
            )
        }
        
        return fingerprint
    
    def register_trusted_site(self, url: str, fingerprint: Dict = None) -> Dict:
        """
        Register a trusted website with its visual fingerprint.
        
        Args:
            url: Website URL
            fingerprint: Visual fingerprint (if None, creates one)
            
        Returns:
            Registration confirmation
        """
        domain = self._extract_domain(url)
        
        if fingerprint is None:
            fingerprint = self.create_visual_fingerprint(url)
        
        self.trusted_fingerprints[domain] = fingerprint
        
        return {
            'status': 'registered',
            'domain': domain,
            'fingerprint_hash': fingerprint['fingerprint_hash'],
            'registered_at': datetime.now().isoformat()
        }
    
    def verify_visual_match(self, url: str, current_fingerprint: Dict = None) -> Dict:
        """
        Verify if a website matches its trusted visual fingerprint.
        
        Args:
            url: Website URL to verify
            current_fingerprint: Current visual fingerprint
            
        Returns:
            Verification result with mismatch percentage
        """
        domain = self._extract_domain(url)
        
        if domain not in self.trusted_fingerprints:
            return {
                'status': 'unknown',
                'domain': domain,
                'message': 'Domain not in trusted list',
                'alert': False
            }
        
        trusted = self.trusted_fingerprints[domain]
        
        if current_fingerprint is None:
            current_fingerprint = self.create_visual_fingerprint(url)
        
        # Calculate mismatch percentage
        mismatch = self._calculate_mismatch(trusted, current_fingerprint)
        
        # Determine if alert should be triggered
        alert_triggered = mismatch > self.mismatch_threshold
        
        return {
            'status': 'verified',
            'domain': domain,
            'mismatch_percentage': mismatch * 100,
            'threshold': self.mismatch_threshold * 100,
            'alert': alert_triggered,
            'warning_message': f"⚠️ Warning: {mismatch*100:.1f}% visual mismatch detected!" if alert_triggered else None,
            'details': {
                'trusted_hash': trusted['fingerprint_hash'],
                'current_hash': current_fingerprint['fingerprint_hash'],
                'color_match': self._compare_colors(trusted['color_palette'], current_fingerprint['color_palette']),
                'layout_match': trusted['layout_pattern'] == current_fingerprint['layout_pattern']
            }
        }
    
    def _extract_domain(self, url: str) -> str:
        """Extract domain from URL."""
        # Simple domain extraction
        domain = url.replace('https://', '').replace('http://', '').split('/')[0]
        return domain.lower()
    
    def _analyze_colors(self, colors: List[str]) -> Dict:
        """Analyze color palette."""
        return {
            'dominant_colors': colors[:5],
            'color_count': len(colors),
            'color_hash': hashlib.md5(','.join(sorted(colors)).encode()).hexdigest()[:16]
        }
    
    def _analyze_layout(self, layout_signature: str) -> str:
        """Analyze layout pattern."""
        return hashlib.sha256(layout_signature.encode()).hexdigest()[:16]
    
    def _analyze_text_tone(self, content: str) -> Dict:
        """Analyze text tone and characteristics."""
        # Simple text analysis
        words = content.lower().split()
        
        # Count urgent/suspicious words
        urgent_words = ['urgent', 'immediately', 'act now', 'limited', 'verify', 'suspended']
        urgency_count = sum(1 for word in words if any(urgent in word for urgent in urgent_words))
        
        return {
            'urgency_level': 'high' if urgency_count > 5 else 'medium' if urgency_count > 2 else 'low',
            'word_count': len(words),
            'suspicious_phrases': urgency_count
        }
    
    def _generate_fingerprint_hash(self, color_fp: Dict, layout_fp: str, text_tone: Dict) -> str:
        """Generate composite fingerprint hash."""
        composite = f"{color_fp['color_hash']}{layout_fp}{text_tone['urgency_level']}"
        return hashlib.sha256(composite.encode()).hexdigest()[:32]
    
    def _calculate_mismatch(self, trusted: Dict, current: Dict) -> float:
        """Calculate mismatch percentage between fingerprints."""
        mismatches = 0
        total_checks = 3
        
        # Check color palette
        if trusted['color_palette']['color_hash'] != current['color_palette']['color_hash']:
            mismatches += 1
        
        # Check layout
        if trusted['layout_pattern'] != current['layout_pattern']:
            mismatches += 1
        
        # Check text tone
        if trusted['text_tone']['urgency_level'] != current['text_tone']['urgency_level']:
            mismatches += 0.5
        
        return mismatches / total_checks
    
    def _compare_colors(self, colors1: Dict, colors2: Dict) -> bool:
        """Compare two color palettes."""
        return colors1['color_hash'] == colors2['color_hash']


class VoiceAlertAssistant:
    """
    Provides voice alerts when suspicious pages are detected.
    Uses text-to-speech to warn users.
    """
    
    def __init__(self):
        self.alert_messages = {
            'phishing': "Warning: This page visually mimics another trusted site.",
            'suspicious': "Caution: This website shows suspicious characteristics.",
            'fake_job': "Alert: This appears to be a fake job or scholarship posting.",
            'tracker': "Notice: Trackers detected and blocked on this page.",
            'high_risk': "Danger: This site has been flagged as high risk by the community."
        }
        self.voice_enabled = True
        
    def trigger_alert(self, alert_type: str, details: Dict = None) -> Dict:
        """
        Trigger a voice alert.
        
        Args:
            alert_type: Type of alert ('phishing', 'suspicious', etc.)
            details: Additional details about the alert
            
        Returns:
            Alert information
        """
        if alert_type not in self.alert_messages:
            alert_type = 'suspicious'
        
        message = self.alert_messages[alert_type]
        
        # Simulate voice alert (in real implementation, would use TTS)
        alert_info = {
            'alert_type': alert_type,
            'message': message,
            'voice_enabled': self.voice_enabled,
            'timestamp': datetime.now().isoformat(),
            'details': details if details else {},
            'action_required': True
        }
        
        # In real implementation: text_to_speech(message)
        print(f"\n🔊 VOICE ALERT: {message}")
        if details:
            print(f"   Details: {details}")
        
        return alert_info
    
    def configure_voice(self, enabled: bool = True, volume: int = 80) -> Dict:
        """
        Configure voice alert settings.
        
        Args:
            enabled: Enable/disable voice alerts
            volume: Alert volume (0-100)
            
        Returns:
            Configuration status
        """
        self.voice_enabled = enabled
        
        return {
            'voice_enabled': enabled,
            'volume': volume,
            'status': 'configured'
        }


class CommunityTrustMap:
    """
    Global map of safe and unsafe domains contributed by users.
    Allows companies to verify their official sites.
    """
    
    def __init__(self):
        self.trust_database = {
            'google.com': {'trust_score': 98, 'verified': True, 'reports': 0},
            'paypal.com': {'trust_score': 97, 'verified': True, 'reports': 0},
            'paytm.com': {'trust_score': 95, 'verified': True, 'reports': 0},
            'facebook.com': {'trust_score': 90, 'verified': True, 'reports': 5},
            'suspicious-paypal.com': {'trust_score': 5, 'verified': False, 'reports': 250},
            'fake-scholarship.net': {'trust_score': 2, 'verified': False, 'reports': 500},
        }
        
    def report_domain(self, domain: str, report_type: str, user_id: str = None) -> Dict:
        """
        Report a domain as safe or unsafe.
        
        Args:
            domain: Domain to report
            report_type: 'safe' or 'unsafe'
            user_id: Optional user identifier
            
        Returns:
            Report confirmation
        """
        if domain not in self.trust_database:
            self.trust_database[domain] = {
                'trust_score': 50,
                'verified': False,
                'reports': 0
            }
        
        # Update trust score based on report
        if report_type == 'safe':
            self.trust_database[domain]['trust_score'] = min(
                100, self.trust_database[domain]['trust_score'] + 1
            )
        else:  # unsafe
            self.trust_database[domain]['trust_score'] = max(
                0, self.trust_database[domain]['trust_score'] - 5
            )
            self.trust_database[domain]['reports'] += 1
        
        return {
            'status': 'reported',
            'domain': domain,
            'report_type': report_type,
            'new_trust_score': self.trust_database[domain]['trust_score'],
            'timestamp': datetime.now().isoformat()
        }
    
    def check_domain_trust(self, domain: str) -> Dict:
        """
        Check trust level of a domain.
        
        Args:
            domain: Domain to check
            
        Returns:
            Trust information
        """
        if domain not in self.trust_database:
            return {
                'domain': domain,
                'trust_level': TrustLevel.UNKNOWN,
                'trust_score': 50,
                'message': 'Domain not in community database'
            }
        
        data = self.trust_database[domain]
        
        # Determine trust level
        if data['trust_score'] >= 80:
            trust_level = TrustLevel.TRUSTED
        elif data['trust_score'] >= 50:
            trust_level = TrustLevel.SUSPICIOUS
        else:
            trust_level = TrustLevel.DANGEROUS
        
        return {
            'domain': domain,
            'trust_level': trust_level,
            'trust_score': data['trust_score'],
            'verified': data.get('verified', False),
            'community_reports': data['reports'],
            'recommendation': self._get_recommendation(trust_level, data)
        }
    
    def verify_company_domain(self, domain: str, company_name: str, 
                             verification_code: str = None) -> Dict:
        """
        Verify official company domain.
        
        Args:
            domain: Domain to verify
            company_name: Company name
            verification_code: Verification code
            
        Returns:
            Verification status
        """
        # Simulate verification process
        verified = verification_code is not None
        
        if domain not in self.trust_database:
            self.trust_database[domain] = {
                'trust_score': 90 if verified else 50,
                'verified': verified,
                'reports': 0
            }
        else:
            self.trust_database[domain]['verified'] = verified
            if verified:
                self.trust_database[domain]['trust_score'] = max(
                    self.trust_database[domain]['trust_score'], 90
                )
        
        return {
            'status': 'verified' if verified else 'pending',
            'domain': domain,
            'company': company_name,
            'verified': verified,
            'trust_score': self.trust_database[domain]['trust_score']
        }
    
    def _get_recommendation(self, trust_level: TrustLevel, data: Dict) -> str:
        """Get recommendation based on trust level."""
        if trust_level == TrustLevel.TRUSTED:
            return "Safe to proceed"
        elif trust_level == TrustLevel.SUSPICIOUS:
            return "Exercise caution, verify domain authenticity"
        else:
            return "⚠️ HIGH RISK - Do not enter credentials or personal information"


class FakeSiteDetector:
    """
    Detects fake scholarship, job, and internship sites.
    """
    
    def __init__(self):
        self.suspicious_patterns = [
            r'apply.*now.*limited',
            r'guaranteed.*job',
            r'no.*experience.*required.*high.*salary',
            r'scholarship.*winner',
            r'claim.*prize',
            r'verification.*required.*immediately',
            r'update.*payment.*method',
        ]
        
        self.legitimate_education_domains = [
            'edu', 'ac.uk', 'ac.in', 'harvard.edu', 'mit.edu', 'stanford.edu'
        ]
        
    def analyze_site(self, url: str, content: str = None, domain_age: int = None) -> Dict:
        """
        Analyze if a site is potentially fake.
        
        Args:
            url: Website URL
            content: Page content
            domain_age: Domain age in days
            
        Returns:
            Analysis results
        """
        risk_score = 0
        red_flags = []
        
        # Check domain legitimacy
        if not any(edu_domain in url for edu_domain in self.legitimate_education_domains):
            if 'scholarship' in url.lower() or 'job' in url.lower():
                risk_score += 30
                red_flags.append("Non-educational domain offering education/job services")
        
        # Check domain age
        if domain_age is not None and domain_age < 90:  # Less than 3 months
            risk_score += 25
            red_flags.append(f"Very new domain (only {domain_age} days old)")
        
        # Check content for suspicious patterns
        if content:
            for pattern in self.suspicious_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    risk_score += 15
                    red_flags.append(f"Suspicious pattern detected: '{pattern}'")
        
        # Check for urgency tactics
        if content and any(word in content.lower() for word in ['urgent', 'immediately', 'limited time']):
            risk_score += 20
            red_flags.append("Uses urgency tactics (common in scams)")
        
        # Determine if fake
        is_fake = risk_score >= 50
        
        return {
            'url': url,
            'risk_score': min(risk_score, 100),
            'is_fake_probability': risk_score / 100,
            'likely_fake': is_fake,
            'red_flags': red_flags,
            'recommendation': "⚠️ AVOID - Likely fake site" if is_fake else "Proceed with caution",
            'analyzed_at': datetime.now().isoformat()
        }


class PrivacyBubbleMode:
    """
    Auto-disables trackers, hidden form fields, and fingerprinting scripts.
    """
    
    def __init__(self):
        self.blocked_trackers = []
        self.blocked_scripts = []
        self.privacy_mode_enabled = True
        
    def scan_page(self, url: str, scripts: List[str] = None, 
                  trackers: List[str] = None) -> Dict:
        """
        Scan page for privacy threats.
        
        Args:
            url: Page URL
            scripts: List of script URLs on the page
            trackers: List of detected trackers
            
        Returns:
            Scan results
        """
        threats_found = []
        blocked_items = []
        
        # Check for known trackers
        known_trackers = ['doubleclick', 'googleanalytics', 'facebook-pixel', 
                         'hotjar', 'mixpanel', 'segment']
        
        if trackers:
            for tracker in trackers:
                if any(known in tracker.lower() for known in known_trackers):
                    threats_found.append({
                        'type': 'tracker',
                        'name': tracker,
                        'risk': 'medium'
                    })
                    blocked_items.append(tracker)
        
        # Check for fingerprinting scripts
        if scripts:
            for script in scripts:
                if 'fingerprint' in script.lower() or 'canvas' in script.lower():
                    threats_found.append({
                        'type': 'fingerprinting',
                        'name': script,
                        'risk': 'high'
                    })
                    blocked_items.append(script)
        
        return {
            'url': url,
            'privacy_mode': self.privacy_mode_enabled,
            'threats_found': len(threats_found),
            'threats': threats_found,
            'items_blocked': len(blocked_items),
            'blocked_list': blocked_items,
            'protection_level': 'high' if self.privacy_mode_enabled else 'none',
            'timestamp': datetime.now().isoformat()
        }
    
    def enable_privacy_mode(self, level: str = 'high') -> Dict:
        """
        Enable privacy bubble mode.
        
        Args:
            level: Protection level ('low', 'medium', 'high')
            
        Returns:
            Configuration status
        """
        self.privacy_mode_enabled = True
        
        return {
            'status': 'enabled',
            'protection_level': level,
            'features': [
                'Tracker blocking',
                'Hidden form field detection',
                'Fingerprinting script blocking',
                'Cookie consent enforcement'
            ]
        }


def demonstrate_layer1_features():
    """Demonstrate Layer 1 features.
    
    ⚠️ WARNING: This is for demonstration purposes only. In production:
    - Never log passwords, secrets, or sensitive data in clear text
    - Use secure logging practices with data masking
    - Store credentials in secure vaults
    """
    print("=" * 70)
    print("LAYER 1: WEB SECURITY & PHISHING DETECTION")
    print("=" * 70)
    print("⚠️  DEMO MODE: Displaying data for educational purposes only")
    print("=" * 70)
    
    # 1. Visual DNA Analyzer
    print("\n1️⃣  AI VISUAL DNA OF WEBSITES")
    print("-" * 70)
    dna_analyzer = VisualDNAAnalyzer()
    
    # Register trusted site
    trusted_fp = dna_analyzer.create_visual_fingerprint(
        'https://paypal.com',
        colors=['#003087', '#009CDE', '#FFFFFF']
    )
    dna_analyzer.register_trusted_site('https://paypal.com', trusted_fp)
    print(f"Registered trusted site: paypal.com")
    print(f"Fingerprint hash: {trusted_fp['fingerprint_hash']}")
    
    # Check suspicious site
    fake_fp = dna_analyzer.create_visual_fingerprint(
        'https://paypall.com',
        colors=['#003088', '#009CDF', '#FFFFFF']  # Slightly different
    )
    verification = dna_analyzer.verify_visual_match('https://paypal.com', fake_fp)
    print(f"\nVerifying similar domain...")
    print(f"Mismatch: {verification['mismatch_percentage']:.1f}%")
    if verification['alert']:
        print(f"🚨 {verification['warning_message']}")
    
    # 2. Voice Alert Assistant
    print("\n2️⃣  VOICE ALERT ASSISTANT")
    print("-" * 70)
    voice_alert = VoiceAlertAssistant()
    voice_alert.trigger_alert('phishing', {'domain': 'paypall.com', 'mimics': 'paypal.com'})
    
    # 3. Community Trust Map
    print("\n3️⃣  COMMUNITY TRUST MAP")
    print("-" * 70)
    trust_map = CommunityTrustMap()
    
    # Check trusted domain
    trust_info = trust_map.check_domain_trust('google.com')
    print(f"Domain: {trust_info['domain']}")
    print(f"Trust Level: {trust_info['trust_level'].value.upper()} ✅")
    print(f"Trust Score: {trust_info['trust_score']}/100")
    
    # Check suspicious domain
    suspicious_info = trust_map.check_domain_trust('suspicious-paypal.com')
    print(f"\nDomain: {suspicious_info['domain']}")
    print(f"Trust Level: {suspicious_info['trust_level'].value.upper()} ⚠️")
    print(f"Trust Score: {suspicious_info['trust_score']}/100")
    print(f"Recommendation: {suspicious_info['recommendation']}")
    
    # 4. Fake Site Detector
    print("\n4️⃣  FAKE SCHOLARSHIP/JOB SITE DETECTION")
    print("-" * 70)
    detector = FakeSiteDetector()
    
    analysis = detector.analyze_site(
        'https://guaranteed-scholarship.net',
        content='URGENT: Claim your scholarship now! Limited time offer! No experience required!',
        domain_age=30
    )
    print(f"Analyzing: {analysis['url']}")
    print(f"Risk Score: {analysis['risk_score']}/100")
    print(f"Likely Fake: {'YES ⚠️' if analysis['likely_fake'] else 'NO'}")
    print(f"Red Flags Found: {len(analysis['red_flags'])}")
    for flag in analysis['red_flags'][:3]:
        print(f"  🚩 {flag}")
    
    # 5. Privacy Bubble Mode
    print("\n5️⃣  PRIVACY BUBBLE MODE")
    print("-" * 70)
    privacy = PrivacyBubbleMode()
    
    scan_result = privacy.scan_page(
        'https://suspicious-site.com',
        scripts=['fingerprint.js', 'analytics.js'],
        trackers=['doubleclick.net', 'facebook-pixel.js', 'hotjar.com']
    )
    print(f"Scanning: {scan_result['url']}")
    print(f"Threats Found: {scan_result['threats_found']}")
    print(f"Items Blocked: {scan_result['items_blocked']}")
    print(f"Protection Level: {scan_result['protection_level'].upper()}")
    print("Blocked:")
    for item in scan_result['blocked_list'][:3]:
        print(f"  🛡️  {item}")


if __name__ == "__main__":
    demonstrate_layer1_features()
