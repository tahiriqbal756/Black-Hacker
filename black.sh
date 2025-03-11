echo "Made by Black Hacker - Installing Requirements..."

# Update Termux
pkg update && pkg upgrade -y

# Install Required Packages
pkg install python -y
pkg install nano -y
pkg install unzip -y
pip install selenium

# Install Chrome WebDriver (for Selenium)
apt install chromium-driver -y

echo "Installation Complete! Run the script using: python black.py"
