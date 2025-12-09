# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Terminal 1: Start Backend API

```powershell
cd "C:\Users\ALOK PRADHAN\OneDrive\Desktop\Chatbot\backend"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

**Expected output:**
```
Starting Chatbot API on http://localhost:5000
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Terminal 2: Start Frontend Server

```powershell
cd "C:\Users\ALOK PRADHAN\OneDrive\Desktop\Chatbot\frontend"
python -m http.server 8000
```

**Expected output:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

### Open in Browser

Navigate to: **http://localhost:8000**

---

## 📝 Test the API with PowerShell

### Test Health Endpoint
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/health" -Method GET
```

### Test Chat Endpoint
```powershell
$payload = @{message = "Hello, how are you?"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://localhost:5000/api/chat" -Method POST -ContentType "application/json" -Body $payload
```

### Test Suggestions
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/suggestions" -Method GET
```

---

## 🛠️ Troubleshooting

### Problem: "No module named 'flask'"
**Solution:** Make sure virtual environment is activated and run:
```powershell
pip install -r requirements.txt
```

### Problem: Port 5000 already in use
**Solution:** Kill existing process:
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Problem: Can't connect to API from frontend
**Solution:** 
1. Verify backend is running
2. Check browser console (F12)
3. Ensure CORS is enabled (it is by default)

---

## 📚 API Examples

### Example 1: Simple Greeting
```
User: "Hello"
Bot: "Hi there! What can I do for you?"
```

### Example 2: Time Query
```
User: "What time is it?"
Bot: "The current time is 14:30:45"
```

### Example 3: Joke
```
User: "Tell me a joke"
Bot: "Why did the programmer quit his job? Because he didn't get arrays!"
```

---

## 🎨 Customization

### Change Bot Name
Edit `backend/chatbot.py`:
```python
self.name = "ChatBot"  # Change to your preferred name
```

### Add New Response Pattern
Edit `backend/chatbot.py` in the `_load_responses()` method:
```python
'your_topic': {
    'patterns': ['trigger1', 'trigger2'],
    'responses': ['response1', 'response2']
}
```

### Customize UI Colors
Edit `frontend/styles.css`:
```css
:root {
    --primary-color: #3b82f6;  /* Change these colors */
    --primary-dark: #1e40af;
}
```

---

## 📊 Project Files

```
Chatbot/
├── README.md                 # Main documentation
├── QUICK_START.md           # This file
├── backend/
│   ├── app.py               # Flask API server
│   ├── chatbot.py           # Chatbot logic
│   ├── requirements.txt      # Python packages
│   └── venv/                # Virtual environment (created on first setup)
└── frontend/
    ├── index.html           # Web interface
    ├── styles.css           # Styling
    └── script.js            # Frontend JavaScript
```

---

## ✅ Verification Checklist

- [ ] Backend running on http://localhost:5000
- [ ] Frontend running on http://localhost:8000
- [ ] Chatbot interface loads in browser
- [ ] Can send messages and receive responses
- [ ] Suggestion buttons work
- [ ] Clear history button works
- [ ] No console errors in browser (F12)

---

**You're all set! 🎉 Start chatting with your bot!**
