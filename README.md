# Chatbot Application

A complete chatbot application with Python Flask backend API and a modern HTML/CSS/JavaScript frontend.

## Project Structure

```
Chatbot/
├── backend/
│   ├── app.py           # Flask API server
│   ├── chatbot.py       # Chatbot logic with pattern matching
│   └── requirements.txt  # Python dependencies
└── frontend/
    ├── index.html       # HTML interface
    ├── styles.css       # Styling
    └── script.js        # Frontend logic
```

## Features

### Backend (Python Flask)
- RESTful API endpoints for chatting
- Pattern-based response matching
- Conversation history management
- Health check endpoint
- CORS enabled for frontend communication
- Suggestion recommendations
- Clear history functionality

### Frontend (HTML/CSS/JavaScript)
- Modern, responsive chat interface
- Real-time message sending/receiving
- Quick suggestion buttons
- Conversation history display
- Loading indicators
- Timestamp on messages
- Mobile-friendly design
- Dark theme UI

## API Endpoints

### 1. Health Check
```
GET /api/health
```
Check if the API is running.

**Response:**
```json
{
    "status": "success",
    "message": "Chatbot API is running",
    "timestamp": "2024-12-09T10:30:00"
}
```

### 2. Chat
```
POST /api/chat
```
Send a message to the chatbot.

**Request:**
```json
{
    "message": "Hello!"
}
```

**Response:**
```json
{
    "status": "success",
    "user_message": "Hello!",
    "bot_response": "Hi there! What can I do for you?",
    "timestamp": "2024-12-09T10:30:05"
}
```

### 3. Conversation History
```
GET /api/history?limit=50
```
Get conversation history (limit optional).

**Response:**
```json
{
    "status": "success",
    "history": [
        {
            "user": "Hello",
            "bot": "Hi there!",
            "timestamp": "2024-12-09T10:30:05"
        }
    ],
    "total": 1
}
```

### 4. Clear History
```
POST /api/clear
```
Clear all conversation history.

**Response:**
```json
{
    "status": "success",
    "message": "Conversation history cleared"
}
```

### 5. Get Suggestions
```
GET /api/suggestions
```
Get suggested topics to discuss.

**Response:**
```json
{
    "status": "success",
    "suggestions": [
        "What can you help me with?",
        "Tell me a joke",
        "How are you?",
        "What's the date today?",
        "Help me with Python"
    ]
}
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser
- Git (optional)

### Step 1: Set Up Backend

1. Open PowerShell and navigate to the backend folder:
```powershell
cd "C:\Users\ALOK PRADHAN\OneDrive\Desktop\Chatbot\backend"
```

2. Create a Python virtual environment:
```powershell
python -m venv venv
```

3. Activate the virtual environment:
```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:
```powershell
pip install -r requirements.txt
```

5. Run the Flask server:
```powershell
python app.py
```

The API will start on `http://localhost:5000`

### Step 2: Set Up Frontend

1. Open a new PowerShell window
2. Navigate to the frontend folder:
```powershell
cd "C:\Users\ALOK PRADHAN\OneDrive\Desktop\Chatbot\frontend"
```

3. Start a simple HTTP server:
```powershell
python -m http.server 8000
```

4. Open your browser and go to:
```
http://localhost:8000
```

## Usage

1. Make sure both servers are running (backend on 5000, frontend on 8000)
2. Open the chatbot interface in your browser
3. Type a message and click send
4. Use quick suggestion buttons for common questions
5. Clear history with the 🗑️ button

## Chatbot Capabilities

The chatbot can respond to:
- **Greetings**: "Hello", "Hi", "Hey", etc.
- **Farewells**: "Bye", "Goodbye", "See you", etc.
- **Gratitude**: "Thank you", "Thanks", etc.
- **Status Queries**: "How are you?", "What's up?", etc.
- **Information**: "Who are you?", "What can you do?", etc.
- **Fun**: "Tell me a joke", "Make me laugh", etc.
- **Time/Date**: "What time is it?", "What's today's date?", etc.
- **General Conversation**: Responds intelligently to other topics

## Customization

### Add New Responses

Edit `backend/chatbot.py` and add new entries to the `self.responses` dictionary:

```python
'new_intent': {
    'patterns': ['pattern1', 'pattern2', 'pattern3'],
    'responses': [
        'Response option 1',
        'Response option 2',
        'Response option 3'
    ]
}
```

### Change Port Numbers

**Backend:** Edit `app.py` line at the bottom:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to desired port
```

**Frontend API URL:** Edit `frontend/script.js`:
```javascript
const API_BASE_URL = 'http://localhost:5000/api';  // Change port here
```

### Styling

Modify `frontend/styles.css` to customize colors, fonts, and layout.

## Troubleshooting

### Backend won't start
- Check if port 5000 is in use
- Ensure Python 3.8+ is installed
- Check if all dependencies are installed: `pip install -r requirements.txt`

### Frontend can't connect to API
- Verify backend is running on http://localhost:5000
- Check browser console for error messages (F12)
- Ensure CORS is enabled in Flask (it is by default)

### Virtual environment not activating
- Try: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then try activation again

## Development Tips

1. Use browser DevTools (F12) to debug frontend issues
2. Check backend terminal for Flask errors
3. Use the `/api/health` endpoint to verify API connectivity
4. Test API endpoints with Postman or similar tools

## Future Enhancements

- Integrate with AI APIs (OpenAI, HuggingFace)
- Add user authentication
- Store chat history in database
- Implement natural language processing
- Add multilingual support
- Mobile app version
- Voice input/output

## License

This project is open source and available for modification and distribution.

## Support

For issues or questions, please refer to the documentation or check the browser console for error messages.
