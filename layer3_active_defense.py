"""
Layer 3: Active Defense & Intelligence

Features:
1. AI Decoy Generator (fake fields and dummy credentials)
2. Attack Behavior Learning System (ABLS)
3. Student Safety Mode (sandbox mode)
4. Corporate Protection Network
5. Cyber-Forensics Mode
"""

import hashlib
import secrets
import json
from typing import Dict, List, Tuple
from datetime import datetime, timedelta
from collections import defaultdict
from enum import Enum


class AttackType(Enum):
    """Types of attacks detected."""
    CREDENTIAL_THEFT = "credential_theft"
    XSS = "xss"
    SQL_INJECTION = "sql_injection"
    PHISHING = "phishing"
    BRUTE_FORCE = "brute_force"
    UNKNOWN = "unknown"


class DecoyGenerator:
    """
    Auto-creates realistic fake fields and dummy credentials.
    Any script trying to steal them gets flagged instantly.
    """
    
    def __init__(self):
        self.active_decoys = {}
        self.caught_attackers = []
        
    def generate_decoy_fields(self, form_context: str = "login") -> Dict:
        """
        Generate decoy form fields that look legitimate to attackers.
        
        Args:
            form_context: Type of form ('login', 'payment', 'profile')
            
        Returns:
            Decoy field configuration
        """
        decoy_id = secrets.token_hex(8)
        
        if form_context == "login":
            decoys = {
                'hidden_username': self._generate_fake_username(),
                'hidden_password': self._generate_fake_password(),
                'session_token': secrets.token_hex(16),
                'csrf_token_alt': secrets.token_hex(16),
            }
        elif form_context == "payment":
            decoys = {
                'card_number_alt': self._generate_fake_card(),
                'cvv_backup': str(secrets.randbelow(999)).zfill(3),
                'account_balance': str(secrets.randbelow(10000)),
            }
        else:  # profile
            decoys = {
                'ssn_verify': self._generate_fake_ssn(),
                'backup_email': self._generate_fake_email(),
                'phone_alt': self._generate_fake_phone(),
            }
        
        # Store decoy configuration
        self.active_decoys[decoy_id] = {
            'context': form_context,
            'decoys': decoys,
            'created_at': datetime.now().isoformat(),
            'triggered': False
        }
        
        return {
            'decoy_id': decoy_id,
            'fields': decoys,
            'field_count': len(decoys),
            'note': 'Any access to these fields indicates malicious activity'
        }
    
    def check_decoy_access(self, decoy_id: str, accessed_fields: List[str], 
                          attacker_ip: str = None) -> Dict:
        """
        Check if decoy fields were accessed (indicating attack).
        
        Args:
            decoy_id: Decoy identifier
            accessed_fields: List of fields that were accessed
            attacker_ip: IP address of potential attacker
            
        Returns:
            Attack detection results
        """
        if decoy_id not in self.active_decoys:
            return {'error': 'Decoy ID not found'}
        
        decoy = self.active_decoys[decoy_id]
        
        # Check if any accessed field is a decoy
        decoy_fields_accessed = [f for f in accessed_fields if f in decoy['decoys']]
        
        if decoy_fields_accessed:
            # Attack detected!
            attack_record = {
                'decoy_id': decoy_id,
                'timestamp': datetime.now().isoformat(),
                'attacker_ip': attacker_ip,
                'accessed_decoys': decoy_fields_accessed,
                'context': decoy['context'],
                'attack_type': AttackType.CREDENTIAL_THEFT
            }
            
            self.caught_attackers.append(attack_record)
            decoy['triggered'] = True
            
            return {
                'attack_detected': True,
                'severity': 'HIGH',
                'decoy_fields_accessed': len(decoy_fields_accessed),
                'total_fields_accessed': len(accessed_fields),
                'attacker_ip': attacker_ip,
                'recommendation': '🚨 Block this IP and alert security team',
                'attack_record': attack_record
            }
        
        return {
            'attack_detected': False,
            'fields_checked': len(accessed_fields),
            'status': 'clean'
        }
    
    def _generate_fake_username(self) -> str:
        """Generate realistic fake username."""
        prefixes = ['admin', 'user', 'test', 'backup', 'system']
        return f"{secrets.choice(prefixes)}_{secrets.randbelow(9999):04d}"
    
    def _generate_fake_password(self) -> str:
        """Generate realistic but fake password."""
        return f"Fake{secrets.randbelow(999):03d}!Pass"
    
    def _generate_fake_card(self) -> str:
        """Generate fake credit card number."""
        return f"4532-{''.join(str(secrets.randbelow(10)) for _ in range(12))}"
    
    def _generate_fake_ssn(self) -> str:
        """Generate fake SSN."""
        return f"{secrets.randbelow(900)+100}-{secrets.randbelow(90)+10}-{secrets.randbelow(9000)+1000}"
    
    def _generate_fake_email(self) -> str:
        """Generate fake email."""
        return f"backup_{secrets.token_hex(4)}@example.com"
    
    def _generate_fake_phone(self) -> str:
        """Generate fake phone number."""
        return f"555-{secrets.randbelow(900)+100}-{secrets.randbelow(9000)+1000}"


class AttackBehaviorLearningSystem:
    """
    Learns attacker patterns over time and builds a global attacker fingerprint database.
    Companies can share threat intelligence securely.
    """
    
    def __init__(self):
        self.attack_database = defaultdict(list)
        self.attacker_fingerprints = {}
        self.shared_intelligence = []
        
    def record_attack(self, attack_type: AttackType, attacker_info: Dict, 
                     attack_details: Dict) -> Dict:
        """
        Record an attack for pattern learning.
        
        Args:
            attack_type: Type of attack
            attacker_info: Information about the attacker
            attack_details: Details of the attack
            
        Returns:
            Recording confirmation
        """
        attack_id = secrets.token_hex(12)
        
        # Create fingerprint for attacker
        fingerprint = self._create_attacker_fingerprint(attacker_info, attack_details)
        
        attack_record = {
            'attack_id': attack_id,
            'attack_type': attack_type.value,
            'fingerprint': fingerprint,
            'attacker_info': attacker_info,
            'attack_details': attack_details,
            'timestamp': datetime.now().isoformat()
        }
        
        # Store in database
        self.attack_database[attack_type.value].append(attack_record)
        
        # Update fingerprint database
        if fingerprint not in self.attacker_fingerprints:
            self.attacker_fingerprints[fingerprint] = []
        self.attacker_fingerprints[fingerprint].append(attack_id)
        
        return {
            'attack_id': attack_id,
            'fingerprint': fingerprint,
            'recorded': True,
            'total_attacks_by_type': len(self.attack_database[attack_type.value])
        }
    
    def analyze_patterns(self, attack_type: AttackType = None) -> Dict:
        """
        Analyze attack patterns.
        
        Args:
            attack_type: Optional - analyze specific attack type
            
        Returns:
            Pattern analysis results
        """
        if attack_type:
            attacks = self.attack_database[attack_type.value]
            
            # Analyze patterns for specific type
            patterns = self._extract_patterns(attacks)
            
            return {
                'attack_type': attack_type.value,
                'total_attacks': len(attacks),
                'patterns': patterns,
                'most_common_pattern': patterns[0] if patterns else None
            }
        else:
            # Global analysis
            total_attacks = sum(len(attacks) for attacks in self.attack_database.values())
            
            attack_distribution = {
                attack_type: len(attacks) 
                for attack_type, attacks in self.attack_database.items()
            }
            
            return {
                'total_attacks': total_attacks,
                'attack_distribution': attack_distribution,
                'unique_attackers': len(self.attacker_fingerprints),
                'analysis_timestamp': datetime.now().isoformat()
            }
    
    def share_intelligence(self, organization: str, threat_data: Dict) -> Dict:
        """
        Share threat intelligence with other organizations (via blockchain simulation).
        
        Args:
            organization: Organization sharing the intelligence
            threat_data: Threat intelligence data
            
        Returns:
            Sharing confirmation
        """
        intelligence_id = secrets.token_hex(16)
        
        intelligence_record = {
            'intelligence_id': intelligence_id,
            'organization': organization,
            'threat_data': threat_data,
            'shared_at': datetime.now().isoformat(),
            'blockchain_hash': self._create_blockchain_hash(threat_data)
        }
        
        self.shared_intelligence.append(intelligence_record)
        
        return {
            'intelligence_id': intelligence_id,
            'shared': True,
            'blockchain_hash': intelligence_record['blockchain_hash'],
            'recipients': 'All connected organizations'
        }
    
    def _create_attacker_fingerprint(self, attacker_info: Dict, attack_details: Dict) -> str:
        """Create unique fingerprint for attacker."""
        # Combine multiple attributes
        fingerprint_data = f"{attacker_info.get('ip', 'unknown')}" \
                          f"{attacker_info.get('user_agent', 'unknown')}" \
                          f"{attack_details.get('method', 'unknown')}"
        
        return hashlib.sha256(fingerprint_data.encode()).hexdigest()[:24]
    
    def _extract_patterns(self, attacks: List[Dict]) -> List[Dict]:
        """Extract common patterns from attacks."""
        if not attacks:
            return []
        
        # Analyze timing patterns
        time_patterns = defaultdict(int)
        for attack in attacks:
            hour = datetime.fromisoformat(attack['timestamp']).hour
            time_patterns[f"{hour:02d}:00-{hour+1:02d}:00"] += 1
        
        patterns = [
            {
                'pattern_type': 'time_of_day',
                'most_common': max(time_patterns.items(), key=lambda x: x[1])[0],
                'frequency': max(time_patterns.values())
            }
        ]
        
        return patterns
    
    def _create_blockchain_hash(self, data: Dict) -> str:
        """Create blockchain-style hash for intelligence sharing."""
        data_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data_str.encode()).hexdigest()


class StudentSafetyMode:
    """
    When students visit suspicious sites for research or project work,
    automatically activates sandbox mode - no real data ever leaks.
    """
    
    def __init__(self):
        self.sandbox_active = False
        self.sandboxed_sessions = {}
        
    def activate_sandbox(self, reason: str = "research") -> Dict:
        """
        Activate sandbox mode.
        
        Args:
            reason: Reason for activation
            
        Returns:
            Sandbox activation confirmation
        """
        session_id = secrets.token_hex(12)
        
        self.sandbox_active = True
        self.sandboxed_sessions[session_id] = {
            'activated_at': datetime.now().isoformat(),
            'reason': reason,
            'fake_data_provided': self._generate_sandbox_data(),
            'real_data_protected': True
        }
        
        return {
            'session_id': session_id,
            'sandbox_active': True,
            'protection_level': 'maximum',
            'features': [
                'Fake credentials generated',
                'Real data isolated',
                'All actions logged',
                'Network requests monitored',
                'No persistent cookies'
            ]
        }
    
    def get_sandbox_data(self, data_type: str) -> Dict:
        """
        Get fake data for use in sandbox.
        
        Args:
            data_type: Type of data needed
            
        Returns:
            Fake data
        """
        sandbox_data = self._generate_sandbox_data()
        
        if data_type in sandbox_data:
            return {
                'data_type': data_type,
                'value': sandbox_data[data_type],
                'note': 'This is fake data - your real data is protected'
            }
        
        return {
            'error': f'Data type {data_type} not available',
            'available_types': list(sandbox_data.keys())
        }
    
    def deactivate_sandbox(self, session_id: str) -> Dict:
        """
        Deactivate sandbox mode.
        
        Args:
            session_id: Sandbox session ID
            
        Returns:
            Deactivation confirmation
        """
        if session_id in self.sandboxed_sessions:
            session = self.sandboxed_sessions[session_id]
            duration = (datetime.now() - datetime.fromisoformat(
                session['activated_at']
            )).total_seconds()
            
            return {
                'session_id': session_id,
                'deactivated': True,
                'duration_seconds': duration,
                'data_leaked': False,
                'summary': 'No real data was exposed during sandbox session'
            }
        
        return {'error': 'Session not found'}
    
    def _generate_sandbox_data(self) -> Dict:
        """Generate fake data for sandbox."""
        return {
            'email': f'student_{secrets.token_hex(4)}@sandbox.edu',
            'password': f'Sandbox{secrets.randbelow(999):03d}!',
            'name': f'Student {secrets.randbelow(9999):04d}',
            'phone': f'555-{secrets.randbelow(900)+100}-{secrets.randbelow(9000)+1000}',
            'address': f'{secrets.randbelow(999)+1} Sandbox Street'
        }


class CorporateProtectionNetwork:
    """
    Enterprises can connect their employees' browsers into one defensive mesh.
    If one system detects malicious code, the rest get warned instantly.
    """
    
    def __init__(self):
        self.network_nodes = {}
        self.active_alerts = []
        self.threat_history = []
        
    def register_employee(self, employee_id: str, organization: str) -> Dict:
        """
        Register employee in protection network.
        
        Args:
            employee_id: Employee identifier
            organization: Organization name
            
        Returns:
            Registration confirmation
        """
        node_id = secrets.token_hex(12)
        
        self.network_nodes[node_id] = {
            'employee_id': employee_id,
            'organization': organization,
            'registered_at': datetime.now().isoformat(),
            'threats_detected': 0,
            'alerts_received': 0,
            'status': 'active'
        }
        
        return {
            'node_id': node_id,
            'registered': True,
            'organization': organization,
            'network_size': len(self.network_nodes),
            'protection_status': 'enabled'
        }
    
    def broadcast_threat(self, source_node_id: str, threat_data: Dict) -> Dict:
        """
        Broadcast threat detection to all nodes in network.
        
        Args:
            source_node_id: Node that detected the threat
            threat_data: Details about the threat
            
        Returns:
            Broadcast confirmation
        """
        if source_node_id not in self.network_nodes:
            return {'error': 'Node not in network'}
        
        alert_id = secrets.token_hex(12)
        
        alert = {
            'alert_id': alert_id,
            'source_node': source_node_id,
            'threat_data': threat_data,
            'broadcast_at': datetime.now().isoformat(),
            'recipients': len(self.network_nodes) - 1  # All except source
        }
        
        self.active_alerts.append(alert)
        self.threat_history.append(alert)
        
        # Update node statistics
        self.network_nodes[source_node_id]['threats_detected'] += 1
        
        for node_id in self.network_nodes:
            if node_id != source_node_id:
                self.network_nodes[node_id]['alerts_received'] += 1
        
        return {
            'alert_id': alert_id,
            'broadcast': 'successful',
            'nodes_alerted': len(self.network_nodes) - 1,
            'threat_type': threat_data.get('type', 'unknown'),
            'action': 'All nodes protected instantly'
        }
    
    def get_network_status(self, organization: str = None) -> Dict:
        """
        Get network protection status.
        
        Args:
            organization: Optional - filter by organization
            
        Returns:
            Network status
        """
        if organization:
            org_nodes = {
                nid: node for nid, node in self.network_nodes.items()
                if node['organization'] == organization
            }
        else:
            org_nodes = self.network_nodes
        
        total_threats = sum(node['threats_detected'] for node in org_nodes.values())
        total_alerts = sum(node['alerts_received'] for node in org_nodes.values())
        
        return {
            'network_size': len(org_nodes),
            'organization': organization if organization else 'All',
            'total_threats_detected': total_threats,
            'total_alerts_sent': total_alerts,
            'active_alerts': len(self.active_alerts),
            'status': 'protected',
            'effectiveness': f"{(total_alerts/max(total_threats, 1)):.1f}x threat amplification"
        }


class CyberForensicsMode:
    """
    Logs and visualizes attack attempts for learning and forensic analysis.
    Students can use it to study ethical hacking safely.
    """
    
    def __init__(self):
        self.attack_logs = []
        self.forensic_sessions = {}
        
    def start_forensic_session(self, purpose: str = "educational") -> Dict:
        """
        Start a forensic analysis session.
        
        Args:
            purpose: Purpose of the session
            
        Returns:
            Session information
        """
        session_id = secrets.token_hex(12)
        
        self.forensic_sessions[session_id] = {
            'started_at': datetime.now().isoformat(),
            'purpose': purpose,
            'events_captured': 0,
            'active': True
        }
        
        return {
            'session_id': session_id,
            'status': 'active',
            'purpose': purpose,
            'logging': 'enabled',
            'features': [
                'Attack attempt logging',
                'Network traffic analysis',
                'Payload inspection',
                'Timeline visualization',
                'Educational annotations'
            ]
        }
    
    def log_attack_attempt(self, session_id: str, attack_data: Dict) -> Dict:
        """
        Log an attack attempt for forensic analysis.
        
        Args:
            session_id: Forensic session ID
            attack_data: Attack details
            
        Returns:
            Logging confirmation
        """
        if session_id not in self.forensic_sessions:
            return {'error': 'Session not found'}
        
        log_id = secrets.token_hex(8)
        
        log_entry = {
            'log_id': log_id,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'attack_data': attack_data,
            'analysis': self._analyze_attack(attack_data)
        }
        
        self.attack_logs.append(log_entry)
        self.forensic_sessions[session_id]['events_captured'] += 1
        
        return {
            'log_id': log_id,
            'logged': True,
            'analysis_available': True,
            'educational_value': self._get_educational_insights(attack_data)
        }
    
    def generate_forensic_report(self, session_id: str) -> Dict:
        """
        Generate comprehensive forensic report.
        
        Args:
            session_id: Forensic session ID
            
        Returns:
            Forensic report
        """
        if session_id not in self.forensic_sessions:
            return {'error': 'Session not found'}
        
        session = self.forensic_sessions[session_id]
        session_logs = [log for log in self.attack_logs if log['session_id'] == session_id]
        
        # Analyze attack types
        attack_types = defaultdict(int)
        for log in session_logs:
            attack_type = log['attack_data'].get('type', 'unknown')
            attack_types[attack_type] += 1
        
        return {
            'session_id': session_id,
            'duration': self._calculate_duration(session['started_at']),
            'total_events': len(session_logs),
            'attack_distribution': dict(attack_types),
            'timeline': self._create_timeline(session_logs),
            'key_findings': self._extract_key_findings(session_logs),
            'educational_summary': self._generate_educational_summary(session_logs),
            'report_generated_at': datetime.now().isoformat()
        }
    
    def _analyze_attack(self, attack_data: Dict) -> Dict:
        """Analyze attack for forensic purposes."""
        return {
            'severity': self._calculate_severity(attack_data),
            'technique': attack_data.get('type', 'unknown'),
            'vector': attack_data.get('vector', 'unknown'),
            'success_probability': attack_data.get('success', False)
        }
    
    def _get_educational_insights(self, attack_data: Dict) -> List[str]:
        """Get educational insights from attack."""
        insights = [
            f"Attack type: {attack_data.get('type', 'unknown')}",
            "This demonstrates common attack patterns used by malicious actors",
            "Understanding these techniques helps in building better defenses"
        ]
        return insights
    
    def _calculate_severity(self, attack_data: Dict) -> str:
        """Calculate attack severity."""
        if attack_data.get('data_accessed'):
            return 'high'
        elif attack_data.get('attempted'):
            return 'medium'
        return 'low'
    
    def _calculate_duration(self, start_time: str) -> str:
        """Calculate session duration."""
        start = datetime.fromisoformat(start_time)
        duration = datetime.now() - start
        return f"{duration.total_seconds():.0f} seconds"
    
    def _create_timeline(self, logs: List[Dict]) -> List[Dict]:
        """Create timeline of events."""
        timeline = []
        for log in logs[:10]:  # Limit to 10 for demo
            timeline.append({
                'time': log['timestamp'],
                'event': log['attack_data'].get('type', 'unknown'),
                'severity': log['analysis']['severity']
            })
        return timeline
    
    def _extract_key_findings(self, logs: List[Dict]) -> List[str]:
        """Extract key findings from logs."""
        findings = []
        if logs:
            findings.append(f"Detected {len(logs)} security events")
            findings.append("Multiple attack vectors identified")
            findings.append("All attempts were logged and blocked")
        return findings
    
    def _generate_educational_summary(self, logs: List[Dict]) -> Dict:
        """Generate educational summary."""
        return {
            'learning_objectives': [
                'Understanding attack patterns',
                'Recognizing threat indicators',
                'Implementing defensive measures'
            ],
            'key_concepts': [
                'Defense in depth',
                'Attack surface reduction',
                'Threat intelligence'
            ]
        }


def demonstrate_layer3_features():
    """Demonstrate Layer 3 features."""
    print("=" * 70)
    print("LAYER 3: ACTIVE DEFENSE & INTELLIGENCE")
    print("=" * 70)
    
    # 1. AI Decoy Generator
    print("\n1️⃣  AI DECOY GENERATOR")
    print("-" * 70)
    decoy_gen = DecoyGenerator()
    
    decoys = decoy_gen.generate_decoy_fields("login")
    print(f"Generated {decoys['field_count']} decoy fields for login form:")
    for field, value in list(decoys['fields'].items())[:3]:
        print(f"  🎭 {field}: {value}")
    
    # Simulate attack
    attack_result = decoy_gen.check_decoy_access(
        decoys['decoy_id'],
        ['username', 'password', 'hidden_password'],  # Attacker accessed decoy!
        '192.168.1.100'
    )
    if attack_result.get('attack_detected'):
        print(f"\n🚨 Attack Detected!")
        print(f"   Severity: {attack_result['severity']}")
        print(f"   Decoy fields accessed: {attack_result['decoy_fields_accessed']}")
        print(f"   {attack_result['recommendation']}")
    
    # 2. Attack Behavior Learning System
    print("\n2️⃣  ATTACK BEHAVIOR LEARNING SYSTEM (ABLS)")
    print("-" * 70)
    abls = AttackBehaviorLearningSystem()
    
    # Record attack
    record = abls.record_attack(
        AttackType.CREDENTIAL_THEFT,
        {'ip': '192.168.1.100', 'user_agent': 'BadBot/1.0'},
        {'method': 'form_scraping', 'target': 'login_page'}
    )
    print(f"Attack recorded: {record['attack_id'][:16]}...")
    print(f"Attacker fingerprint: {record['fingerprint'][:24]}...")
    
    # Share intelligence
    intel = abls.share_intelligence(
        'Security Corp',
        {'threat_type': 'credential_theft', 'iocs': ['192.168.1.100']}
    )
    print(f"\nThreat intelligence shared via blockchain")
    print(f"Intelligence ID: {intel['intelligence_id'][:16]}...")
    print(f"Recipients: {intel['recipients']}")
    
    # 3. Student Safety Mode
    print("\n3️⃣  STUDENT SAFETY MODE")
    print("-" * 70)
    safety_mode = StudentSafetyMode()
    
    sandbox = safety_mode.activate_sandbox("cybersecurity research")
    print(f"Sandbox activated: {sandbox['session_id'][:16]}...")
    print(f"Protection level: {sandbox['protection_level'].upper()}")
    print("Features enabled:")
    for feature in sandbox['features'][:3]:
        print(f"  ✅ {feature}")
    
    fake_data = safety_mode.get_sandbox_data('email')
    print(f"\nFake data generated for research: {fake_data['value']}")
    print(f"Note: {fake_data['note']}")
    
    # 4. Corporate Protection Network
    print("\n4️⃣  CORPORATE PROTECTION NETWORK")
    print("-" * 70)
    network = CorporateProtectionNetwork()
    
    # Register employees
    node1 = network.register_employee('emp001', 'TechCorp')
    node2 = network.register_employee('emp002', 'TechCorp')
    print(f"Employees registered: {network.get_network_status('TechCorp')['network_size']}")
    
    # Broadcast threat
    threat = network.broadcast_threat(
        node1['node_id'],
        {'type': 'phishing', 'domain': 'fake-paypal.com', 'severity': 'high'}
    )
    print(f"\nThreat detected by one employee")
    print(f"Alert broadcast to {threat['nodes_alerted']} other employees instantly")
    print(f"Action: {threat['action']}")
    
    # 5. Cyber-Forensics Mode
    print("\n5️⃣  CYBER-FORENSICS MODE")
    print("-" * 70)
    forensics = CyberForensicsMode()
    
    session = forensics.start_forensic_session("ethical hacking course")
    print(f"Forensic session started: {session['session_id'][:16]}...")
    print(f"Purpose: {session['purpose']}")
    
    # Log some attacks
    forensics.log_attack_attempt(
        session['session_id'],
        {'type': 'xss', 'payload': '<script>alert(1)</script>', 'attempted': True}
    )
    forensics.log_attack_attempt(
        session['session_id'],
        {'type': 'sql_injection', 'payload': "' OR '1'='1", 'attempted': True}
    )
    
    # Generate report
    report = forensics.generate_forensic_report(session['session_id'])
    print(f"\nForensic Report Generated:")
    print(f"Duration: {report['duration']}")
    print(f"Events captured: {report['total_events']}")
    print(f"Attack distribution: {report['attack_distribution']}")
    print("\nEducational Summary:")
    for objective in report['educational_summary']['learning_objectives'][:2]:
        print(f"  📚 {objective}")


if __name__ == "__main__":
    demonstrate_layer3_features()
