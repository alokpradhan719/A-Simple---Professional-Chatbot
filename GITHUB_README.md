# 🤖 Alok Pradhan Chatbot

A professional, fully functional AI chatbot application built with Python Flask backend and an interactive HTML/CSS/JavaScript frontend.

**Created by:** Alok Pradhan  
**Version:** 1.0 - Professional Edition  
**Date:** December 2024

---

## ✨ Features

### Core Capabilities
- 🧮 **Mathematics** - Arithmetic operations (+, -, *, /), square, square root calculations
- 😂 **Jokes** - Programming humor and witty responses
- 📚 **Dictionary** - Technical terms and definitions
- 💬 **Chat** - Natural conversation and general assistance
- ⏰ **Utilities** - Current time, date, and information queries

### Technical Highlights
- ✅ **Standalone HTML** - No server required, works directly in browser
- ✅ **Professional Design** - Dark blue gradient theme with smooth animations
- ✅ **Responsive UI** - Works on desktop, tablet, and mobile devices
- ✅ **Real-time Chat** - Instant message responses with typing indicator
- ✅ **Quick Actions** - One-click buttons for common commands
- ✅ **Modern Architecture** - Clean JavaScript OOP design

---

## 📁 Project Structure

```
Alok-Pradhan-Chatbot/
│
├── frontend/
│   ├── index.html           # Main standalone chatbot (recommended)
│   ├── simple_chat.html     # Alternative chat interface
│   ├── script.js            # Frontend JavaScript
│   └── styles.css           # Styling
│
├── backend/
│   ├── simple_app.py        # Flask API server (optional)
│   ├── simple_chatbot.py    # Simple chatbot logic
│   ├── app.py               # Advanced API (alternative)
│   ├── chatbot.py           # Advanced chatbot engine
│   ├── problem_solver.py    # Problem solving module
│   ├── code_analyzer.py     # Code analysis module
│   ├── learning_resources.py# Learning materials
│   ├── chatbot_utils.py     # Utility functions
│   └── requirements.txt     # Python dependencies
│
├── README.md                # This file
├── .gitignore              # Git ignore rules
└── Documentation files     # Various guides and references
```

---

## 🚀 Quick Start

### Option 1: Standalone HTML (Recommended - No Setup Required!)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Alok-Pradhan-Chatbot.git
   cd Alok-Pradhan-Chatbot
   ```

2. **Open the chatbot:**
   - Navigate to `frontend/index.html`
   - Double-click to open in your browser
   - OR right-click → "Open with" → Your browser

3. **Start chatting!**
   - Type your message and click "Send"
   - Use quick action buttons for common commands

---

### Option 2: With Python Backend Server

**Prerequisites:**
- Python 3.8 or higher
- pip package manager

**Installation:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Alok-Pradhan-Chatbot.git
   cd Alok-Pradhan-Chatbot
   ```

2. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Start the backend server:**
   ```bash
   python simple_app.py
   ```
   The server will run on `http://localhost:5000`

4. **Start the frontend server (optional):**
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   Access at `http://localhost:8000`

---

## 📖 Usage Examples

### Math Operations
```
User: "5 + 3"
Bot: "Result: 8"

User: "10 * 2"
Bot: "Result: 20"

User: "square 9"
Bot: "Square of 9 is 81"

User: "sqrt 16"
Bot: "Square root of 16 is 4.00"
```

### Jokes
```
User: "tell me a joke"
Bot: "Why did the programmer quit? Because he didn't get arrays! 😂"
```

### Dictionary
```
User: "definition of python"
Bot: "📚 PYTHON: High-level programming language."
```

### General Chat
```
User: "hello"
Bot: "Hello! I'm Alok Pradhan Chatbot. How can I help?"

User: "what time is it?"
Bot: "Current time: 2:45:30 PM"
```

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5
- CSS3 (Gradient backgrounds, animations, responsive design)
- JavaScript ES6+ (Object-oriented programming)

**Backend:**
- Python 3.8+
- Flask 2.3.3
- Flask-CORS 4.0.0

**Architecture:**
- Standalone HTML with embedded JavaScript (primary)
- Optional Flask REST API backend

---

## 📝 Key Files Explained

| File | Purpose |
|------|---------|
| `frontend/index.html` | Complete standalone chatbot - open directly in browser |
| `backend/simple_chatbot.py` | Core chatbot logic and response generation |
| `backend/simple_app.py` | Flask API server (optional backend) |
| `backend/app.py` | Advanced API with 12+ endpoints |
| `backend/requirements.txt` | Python package dependencies |

---

## 🎨 Customization

### Change Chatbot Name
Edit `index.html` - search for "Alok Pradhan Chatbot" and replace with your desired name.

### Modify Jokes
Edit the `tellJoke()` method in the `<script>` section of `index.html`:
```javascript
tellJoke() {
    const jokes = [
        "Your joke here!",
        "Another joke!",
        // Add more...
    ];
    return jokes[Math.floor(Math.random() * jokes.length)];
}
```

### Add Dictionary Terms
Edit the `handleDictionary()` method:
```javascript
const dict = {
    'your_term': 'Your definition here',
    // Add more...
};
```

### Change Theme Colors
Edit CSS in `index.html` - look for color values like `#1e3c72` and `#2a5298`.

---

## 🐛 Troubleshooting

### Chatbot Not Responding
- Ensure JavaScript is enabled in your browser
- Try opening `index.html` directly instead of through a server
- Clear browser cache and reload

### Backend Server Issues
- Check if port 5000 is already in use
- Verify Python is installed: `python --version`
- Reinstall dependencies: `pip install -r requirements.txt`

### CORS Issues (if using backend)
- Ensure Flask-CORS is installed
- Check that the frontend is making requests to `http://localhost:5000`

---

## 📚 Advanced Documentation

For more detailed information, see:
- `QUICK_START.md` - Getting started guide
- `API_TESTING.md` - API endpoint testing
- `CONFIG_REFERENCE.md` - Configuration options
- `TROUBLESHOOTING.md` - Common issues and solutions

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**Alok Pradhan**
- Email: alokpradhan719@gmail.com
- GitHub: [@yourusername](https://github.com/yourusername)
- Created: December 2024

---

## ⭐ Show Your Support

If you find this project useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting improvements
- 📤 Sharing with others

---

**Happy Chatting! 🚀**
