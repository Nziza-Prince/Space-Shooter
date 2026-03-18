"""
Dependency checker and installer
Checks for required packages and installs them if missing
"""
import subprocess
import sys
import importlib.util

class DependencyChecker:
    def __init__(self):
        self.required_packages = {
            'pygame': 'pygame',
        }
        self.missing_packages = []
    
    def check_package(self, package_name):
        """Check if a package is installed"""
        spec = importlib.util.find_spec(package_name)
        return spec is not None
    
    def check_all_dependencies(self):
        """Check all required dependencies"""
        print("Checking dependencies...")
        
        for display_name, import_name in self.required_packages.items():
            if not self.check_package(import_name):
                self.missing_packages.append((display_name, import_name))
                print(f"  ✗ {display_name} - NOT FOUND")
            else:
                print(f"  ✓ {display_name} - OK")
        
        return len(self.missing_packages) == 0
    
    def install_missing_packages(self):
        """Install missing packages"""
        if not self.missing_packages:
            return True
        
        print(f"\nFound {len(self.missing_packages)} missing package(s).")
        print("Installing missing dependencies...\n")
        
        for display_name, import_name in self.missing_packages:
            try:
                print(f"Installing {display_name}...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", import_name],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print(f"  ✓ {display_name} installed successfully")
            except subprocess.CalledProcessError:
                print(f"  ✗ Failed to install {display_name}")
                return False
        
        print("\nAll dependencies installed successfully!")
        return True
    
    def ensure_dependencies(self):
        """Check and install dependencies if needed"""
        if not self.check_all_dependencies():
            return self.install_missing_packages()
        else:
            print("\nAll dependencies are satisfied!")
            return True
