# Configuration Reference Guide

## Backend Configuration

### Environment Variables (.env)
Create a `.env` file in the `backend/` folder to customize:

```
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Server Configuration
HOST=0.0.0.0
PORT=5000

# CORS Configuration
CORS_ORIGINS=http://localhost:8000

# Chatbot Configuration
BOT_NAME=ChatBot
BOT_PERSONALITY=friendly
```

### Loading Environment Variables
Update `backend/app.py` to use `.env`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['CORS_ORIGINS'] = os.getenv('CORS_ORIGINS', 'http://localhost:8000')
```

---

## Frontend Configuration

### API Endpoint Configuration
Edit `frontend/script.js`:

```javascript
// Change this to match your backend URL
const API_BASE_URL = 'http://localhost:5000/api';

// Timeout for API requests (milliseconds)
const API_TIMEOUT = 5000;

// Retry failed requests
const MAX_RETRIES = 3;
```

### UI Configuration
Edit `frontend/styles.css`:

```css
:root {
    /* Color Scheme */
    --primary-color: #3b82f6;      /* Main accent */
    --primary-dark: #1e40af;        /* Darker accent */
    --primary-light: #93c5fd;       /* Lighter accent */
    --secondary-color: #10b981;     /* Success color */
    --danger-color: #ef4444;        /* Error color */
    
    /* Theme Colors */
    --background: #0f172a;          /* App background */
    --surface: #1e293b;             /* Main surface */
    --surface-light: #334155;       /* Light surface */
    --text-primary: #f1f5f9;        /* Main text */
    --text-secondary: #cbd5e1;      /* Secondary text */
    --border-color: #475569;        /* Border color */
}
```

---

## Chatbot Intent Configuration

### Current Intents Available
1. **greeting** - Responds to greetings
2. **farewell** - Responds to goodbyes
3. **gratitude** - Responds to thanks
4. **how_are_you** - Status inquiries
5. **name** - Identity questions
6. **help** - Help/capability questions
7. **joke** - Humor requests
8. **time** - Time queries
9. **date** - Date queries
10. **default** - Catch-all responses

### Adding New Intent
Edit `backend/chatbot.py`:

```python
'new_intent_name': {
    'patterns': ['trigger1', 'trigger2', 'trigger3'],
    'responses': [
        'Response 1',
        'Response 2',
        'Response 3'
    ]
}
```

---

## Advanced Features Setup

### Enable Logging
Add to `backend/app.py`:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.before_request
def log_request():
    logger.info(f"Request: {request.method} {request.path}")
```

### Add Database Support
Install SQLAlchemy:
```powershell
pip install Flask-SQLAlchemy
```

Add to `backend/app.py`:
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
db = SQLAlchemy(app)
```

### Add Authentication
Install Flask-Login:
```powershell
pip install Flask-Login
```

---

## Performance Optimization

### Enable Caching
Add to `backend/app.py`:

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/suggestions')
@cache.cached(timeout=300)  # Cache for 5 minutes
def get_suggestions():
    # ...
```

### Implement Rate Limiting
Install flask-limiter:
```powershell
pip install Flask-Limiter
```

Add to `backend/app.py`:
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/chat', methods=['POST'])
@limiter.limit("10 per minute")
def chat():
    # ...
```

---

## Deployment Configuration

### Production Settings
Create `backend/config.py`:

```python
class Config:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'
```

### Docker Support
Create `backend/Dockerfile`:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Build and run:
```powershell
docker build -t chatbot-backend .
docker run -p 5000:5000 chatbot-backend
```

---

## Security Configuration

### CORS Headers
Already configured in `app.py`, but can be customized:

```python
CORS(app, 
     resources={r"/api/*": {"origins": ["http://localhost:8000"]}},
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type"])
```

### Rate Limiting
Prevent abuse by limiting requests:

```python
@app.route('/api/chat', methods=['POST'])
@limiter.limit("30 per minute")
def chat():
    # ...
```

### Input Validation
Add to `backend/app.py`:

```python
def validate_message(message):
    if not isinstance(message, str):
        raise ValueError("Message must be a string")
    if len(message) > 500:
        raise ValueError("Message too long")
    return message.strip()
```

---

## Testing Configuration

### Unit Tests
Create `backend/test_chatbot.py`:

```python
import unittest
from chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = Chatbot()
    
    def test_greeting(self):
        response = self.bot.get_response("Hello")
        self.assertIsNotNone(response)
```

Run tests:
```powershell
python -m unittest discover
```

---

## API Response Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | Success | Chat sent successfully |
| 400 | Bad Request | Missing required fields |
| 404 | Not Found | Invalid endpoint |
| 500 | Server Error | Unexpected error |

---

## Monitoring & Debugging

### Enable Debug Logging
Set in `backend/app.py`:

```python
app.config['JSON_SORT_KEYS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.logger.setLevel(logging.DEBUG)
```

### Check API Responses
```powershell
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/health"
$response.Content | ConvertFrom-Json | Format-Table
```

---

## Scaling Considerations

1. **Database**: Move from in-memory to persistent storage
2. **Caching**: Implement Redis for performance
3. **Load Balancing**: Use Nginx for multiple instances
4. **Monitoring**: Add Prometheus/Grafana
5. **Logging**: Use ELK stack (Elasticsearch, Logstash, Kibana)

---

## Version Information

- **Python**: 3.8+
- **Flask**: 2.3.3
- **Flask-CORS**: 4.0.0
- **Browser**: Modern browsers (Chrome, Firefox, Safari, Edge)

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

Last Updated: December 9, 2024
