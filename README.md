# 🐍 Python PowerHub: All-in-One CLI Toolkit

![Python PowerHub Banner]([https://via.placeholder.com/800x200/2D3748/FFFFFF?text=Python+PowerHub+-+Multi-Tool+CLI+Application](https://evanxplore.site/uploads/pp.png))

## 📋 Overview

**Python PowerHub** is a comprehensive, multi-functional Command Line Interface (CLI) application that bundles several useful tools into one streamlined package. Designed for developers, tech enthusiasts, and everyday users, this toolkit provides practical utilities ranging from chatbot interactions to barcode verification and file hosting.

## ✨ Features

### 🛠️ **Core Tools**

| Tool | Description | Version |
|------|-------------|---------|
| **CLI Chatbot** | AI-powered chatbot using Mistral API for intelligent conversations | β0.1 |
| **Halal Food Checker** | Verify product halal status using barcode database | v0.1 |
| **File Hosting Tool** | Upload and host files with instant public URLs | β0.1 |
| **QR Code Generator** | Create custom QR codes for URLs/text with folder management | v1.0 |

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/brainstationcyberhub-coder/pythonpowerhub
cd python-powerhub
```

2. **Install required dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

## 📦 Dependencies

Create a `requirements.txt` file with:
```
requests
qrcode
Pillow
```

## 🎯 Tool Details

### 🤖 **CLI Chatbot**
- **API Integration**: Connects to Mistral AI via REST API
- **Features**: 
  - Natural language conversations
  - Clean response formatting
  - Easy exit with 'exit' command
- **Usage**: Perfect for quick AI assistance without browser overhead

### 🕌 **Halal Food Checker**
- **Database**: 30+ pre-verified halal barcodes
- **Features**:
  - Personal greeting system
  - Instant verification
  - Multiple check capability
- **Usage**: Quickly verify product halal status before purchase

### ☁️ **File Hosting Tool**
- **Backend**: evanxplore.site API integration
- **Features**:
  - Drag-and-drop style file uploading
  - Instant public URL generation
  - Batch upload support
- **Security**: Local file validation before upload

### 🔳 **QR Code Generator**
- **Features**:
  - Custom folder creation
  - PNG output with naming control
  - URL or text QR codes
- **Usage**: Generate QR codes for websites, contact info, Wi-Fi credentials, etc.

## 🏗️ Project Structure

```
python-powerhub/
│
├── main.py              # Main application launcher
├── cli.py               # Chatbot module
├── halal.py             # Halal checker module
├── webhosting.py        # File hosting module
├── qrgen.py             # QR generator module
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── LICENSE             # MIT License (recommended)
```

## 🖥️ Usage Examples

### Starting the Application
```bash
python main.py
```

### Main Menu Interface
```
=== PYTHON POWERHUB MENU ===
    1. CLI CHATBOT
    2. HALAL FOOD CHECKER
    3. File Hosting Tool
    4. QR Code Generator
    5. Exit
```

### Sample QR Generation Flow
1. Select option 4 from main menu
2. Choose "Start QR Generator"
3. Specify folder name for organization
4. Enter text/URL for encoding
5. Name your QR file
6. Access generated PNG in specified folder

## 🔧 Technical Details

### API Endpoints
- **Chatbot**: `https://evanxplore.site/api/mistral.php`
- **File Hosting**: `https://evanxplore.site/api/upload.php`

### Error Handling
- Invalid input validation across all modules
- File existence checks before operations
- Graceful exit options at every step
- User-friendly error messages

### Code Quality
- Modular design with separate tool modules
- Consistent function naming conventions
- Comprehensive input sanitization
- ASCII art banners for visual appeal

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Maintain consistent ASCII art style
- Add input validation for new features
- Include clear exit options in all tools
- Test thoroughly before submitting PRs

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

## 🐛 Known Issues & Future Enhancements

### Current Limitations
- Halal database is static (consider API integration)
- File size limits for hosting (check API constraints)
- Chatbot dependent on external API availability

### Planned Features
- [ ] Add more barcodes to halal database
- [ ] Local caching for chatbot responses
- [ ] Image preview for QR codes
- [ ] Configuration file for API endpoints
- [ ] Docker containerization
- [ ] GUI version using Tkinter/PyQt

## 🙏 Acknowledgments

- **Mistral AI** for chatbot capabilities
- **evanxplore.site** for file hosting API
- **QR Code Python Library** for QR generation
- **All contributors** helping improve this toolkit

## 📞 Support

For questions, suggestions, or issues:
1. Check existing [Issues](https://github.com/yourusername/python-powerhub/issues)
2. Create a new issue with detailed description
3. Include Python version and error logs if applicable

---

<div align="center">
  <p><strong>Python PowerHub</strong> - One toolkit to rule them all! 🐍✨</p>
  
  ![Stars](https://img.shields.io/github/stars/yourusername/python-powerhub?style=social)
  ![Forks](https://img.shields.io/github/forks/yourusername/python-powerhub?style=social)
  ![License](https://img.shields.io/github/license/yourusername/python-powerhub)
  ![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
</div>

---

**Note**: This is a beta release. Features and APIs may change. Always verify critical information (like halal status) through official channels when possible.
