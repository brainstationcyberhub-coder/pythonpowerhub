# 🐍 Python PowerHub: All-in-One CLI Toolkit

![Python PowerHub Banner](https://evanxplore.site/uploads/pp.png)

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
git clone https://github.com/brainstationcyberhub-coder/pythonpowerhub.git
cd pythonpowerhub
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
requests>=2.28.0
qrcode[pil]>=7.4.2
Pillow>=9.0.0
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
└── README.md           # This file
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

## 🐛 Known Issues & Future Enhancements

### Current Limitations
- Halal database is static (consider API integration)
- File size limits for hosting (check API constraints)
- Chatbot dependent on external API availability

### Planned Features
- Add more barcodes to halal database
- Local caching for chatbot responses
- GUI version

## 🙏 Acknowledgments

- **Mistral AI** for chatbot capabilities
- **evanxplore.site** for file hosting API
- **QR Code Python Library** for QR generation

---

**Note**: This is a beta release. Features and APIs may change. Always verify critical information (like halal status) through official channels when possible.
