# Advanced Password Generator

A feature-rich, modern password generator with a beautiful GUI built using Python and Tkinter. Generate secure, customizable passwords with advanced options for complexity, character types, and batch generation.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-pyperclip-green.svg)

## Features

### Core Features
- **Customizable Password Length**: Generate passwords from 4 to 128 characters
- **Character Type Selection**: Choose from lowercase, uppercase, numbers, and symbols
- **Security Options**: 
  - Ensure complexity (recommended)
  - Avoid ambiguous characters (0, O, l, 1, I)
  - No repeating characters option
- **Real-time Password Strength Indicator**: Visual feedback showing password strength (Weak/Moderate/Strong)
- **One-Click Copy**: Copy generated passwords to clipboard instantly
- **Batch Generation**: Generate multiple passwords at once (2-20 passwords)

### Advanced Customization
- **Exclude Specific Characters**: Remove unwanted characters from generation
- **Must-Include Characters**: Force specific characters to be included in passwords
- **Modern, Scrollable UI**: Beautiful card-based design with smooth scrolling
- **Responsive Layout**: Works on various screen sizes

### Security Features
- Cryptographically secure random generation
- Complexity enforcement for stronger passwords
- Character diversity validation
- Strength analysis with visual indicators

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Password-Generator.git
cd Password-Generator
```

### 2. Install Dependencies

The application uses minimal dependencies:

```bash
pip install -r requirements.txt
```

**Note**: `tkinter` comes pre-installed with most Python distributions. If you encounter issues, install it:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**macOS:**
```bash
brew install python-tk
```

**Windows:**
Tkinter is included with the official Python installer.

## Usage

### Running the Application

Simply run the main Python file:

```bash
python "password generator.py"
```

Or if you have multiple Python versions:

```bash
python3 "password generator.py"
```

### Basic Usage Guide

1. **Set Password Length**: Use the spinner to select desired password length (4-128 characters)

2. **Choose Character Types**: Select which character types to include:
   - Lowercase letters (a-z)
   - Uppercase letters (A-Z)
   - Numbers (0-9)
   - Symbols (!@#$%^&*)

3. **Configure Security Options**:
   - ✅ **Ensure complexity**: Guarantees at least one character from each selected type
   - **Avoid ambiguous**: Excludes easily confused characters (0, O, l, 1, I)
   - **No repeating**: Ensures all characters are unique

4. **Customize (Optional)**:
   - **Exclude characters**: Enter characters you don't want in your password
   - **Must include**: Enter characters that must appear in your password

5. **Generate**: Click "Generate Password" button

6. **Copy**: Use the "Copy" button to copy password to clipboard

### Batch Generation

1. Set your desired password configuration
2. Choose the number of passwords to generate (2-20)
3. Click "Generate Batch"
4. A new window will display all generated passwords with their strength ratings
5. Use "Copy All Passwords" to copy all passwords at once

## User Interface

The application features a modern, calming design with:

- **Card-based Layout**: Organized sections for easy navigation
- **Scrollable Interface**: Access all features without window resizing
- **Color-coded Strength Indicators**:
  - Red: Weak password
  - Orange: Moderate password
  - Green: Strong password
- **Responsive Design**: Adapts to different screen sizes
- **Clean Typography**: Uses Segoe UI font for optimal readability

## Password Strength Calculation

The strength indicator evaluates passwords based on:

- **Length** (longer = stronger)
- **Character diversity** (multiple character types)
- **Unique characters** (high character variety)
- **Complexity** (balanced composition)

**Scoring System:**
- **Weak (0-3 points)**: Basic passwords
- **Moderate (4-6 points)**: Acceptable passwords
- **Strong (7+ points)**: Highly secure passwords

## Configuration

### Default Settings

```python
Password Length: 12 characters
Lowercase: ✅ Enabled
Uppercase: ✅ Enabled
Numbers: ✅ Enabled
Symbols: ✅ Enabled
Ensure Complexity: ✅ Enabled
Avoid Ambiguous: ❌ Disabled
No Repeating: ❌ Disabled
```

### Color Scheme

The application uses a soft, modern color palette:
- Background: Light blue-gray (#f8fafc)
- Cards: Pure white (#ffffff)
- Primary: Beautiful blue (#3b82f6)
- Text: Dark blue-gray (#1e293b)
- Success: Calm green (#10b981)
- Warning: Soft orange (#f59e0b)
- Danger: Soft red (#ef4444)

## Project Structure

```
Password-Generator/
│
├── password generator.py    # Main application file
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
└── .gitignore               # Git ignore rules
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test thoroughly before submitting
- Update documentation for new features

## Known Issues

- On some Linux distributions, clipboard functionality may require additional setup
- Very long passwords (100+ characters) may extend beyond the display field

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's Tkinter library
- Uses pyperclip for clipboard functionality
- Inspired by modern password security best practices

## Support

If you encounter any issues or have questions:

1. Check the [Known Issues](#-known-issues) section
2. Search existing issues on GitHub
3. Create a new issue with detailed information

## Security Note

This password generator creates cryptographically secure random passwords suitable for most applications. However:

- Always use unique passwords for different accounts
- Consider using a password manager for storage
- Enable two-factor authentication when available
- Regularly update important passwords
- Never share your passwords

---

