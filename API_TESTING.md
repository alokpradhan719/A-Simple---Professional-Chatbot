# API Testing Examples

## Using PowerShell

### 1. Health Check
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/health" -Method GET | ConvertTo-Json
```

### 2. Send a Chat Message
```powershell
$body = @{
    message = "Hello, how are you?"
} | ConvertTo-Json

$response = Invoke-WebRequest -Uri "http://localhost:5000/api/chat" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

$response.Content | ConvertFrom-Json | Format-List
```

### 3. Get Suggestions
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/suggestions" -Method GET | ConvertTo-Json
```

### 4. Get Chat History
```powershell
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/history?limit=10" -Method GET
$response.Content | ConvertFrom-Json | Format-List
```

### 5. Clear History
```powershell
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/clear" `
    -Method POST `
    -ContentType "application/json" `
    -Body "{}"

$response.Content | ConvertFrom-Json | Format-List
```

---

## Using cURL (If installed)

### Health Check
```bash
curl http://localhost:5000/api/health
```

### Chat
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Tell me a joke\"}"
```

### Get Suggestions
```bash
curl http://localhost:5000/api/suggestions
```

### Get History
```bash
curl "http://localhost:5000/api/history?limit=5"
```

### Clear History
```bash
curl -X POST http://localhost:5000/api/clear \
  -H "Content-Type: application/json" \
  -d "{}"
```

---

## Using Python Requests

Create file `backend/test_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{BASE_URL}/health")
    print("Health Check:")
    print(json.dumps(response.json(), indent=2))

def test_chat(message):
    """Test chat endpoint"""
    payload = {"message": message}
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"\nChat - User: {message}")
    print(f"Bot: {response.json()['bot_response']}")

def test_suggestions():
    """Test suggestions endpoint"""
    response = requests.get(f"{BASE_URL}/suggestions")
    print("\nSuggestions:")
    for s in response.json()['suggestions']:
        print(f"  - {s}")

def test_history():
    """Test history endpoint"""
    response = requests.get(f"{BASE_URL}/history?limit=5")
    print(f"\nHistory ({response.json()['total']} total messages):")
    for msg in response.json()['history']:
        print(f"  User: {msg['user']}")
        print(f"  Bot: {msg['bot']}")
        print()

def test_clear():
    """Test clear endpoint"""
    response = requests.post(f"{BASE_URL}/clear")
    print("Clear Result:")
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    # Run tests
    test_health()
    test_chat("Hello!")
    test_chat("Tell me a joke")
    test_chat("What time is it?")
    test_suggestions()
    test_history()
    # Uncomment to test clear
    # test_clear()
```

Run the test:
```powershell
python backend/test_api.py
```

---

## Using Postman

### Import Collection
Create `backend/postman_collection.json`:

```json
{
  "info": {
    "name": "Chatbot API",
    "description": "Chatbot API Collection"
  },
  "item": [
    {
      "name": "Health Check",
      "request": {
        "method": "GET",
        "url": "http://localhost:5000/api/health"
      }
    },
    {
      "name": "Send Message",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "url": "http://localhost:5000/api/chat",
        "body": {
          "mode": "raw",
          "raw": "{\"message\": \"Hello\"}"
        }
      }
    },
    {
      "name": "Get Suggestions",
      "request": {
        "method": "GET",
        "url": "http://localhost:5000/api/suggestions"
      }
    },
    {
      "name": "Get History",
      "request": {
        "method": "GET",
        "url": "http://localhost:5000/api/history?limit=10"
      }
    },
    {
      "name": "Clear History",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "url": "http://localhost:5000/api/clear",
        "body": {
          "mode": "raw",
          "raw": "{}"
        }
      }
    }
  ]
}
```

---

## Test Scenarios

### Scenario 1: Basic Conversation
```powershell
$messages = @(
    "Hello",
    "How are you?",
    "What's your name?"
)

foreach ($msg in $messages) {
    $body = @{message = $msg} | ConvertTo-Json
    $response = Invoke-WebRequest -Uri "http://localhost:5000/api/chat" `
        -Method POST -ContentType "application/json" -Body $body
    $result = $response.Content | ConvertFrom-Json
    Write-Host "User: $msg"
    Write-Host "Bot: $($result.bot_response)`n"
}
```

### Scenario 2: Testing All Intent Types
```powershell
$testMessages = @(
    "Hi",                      # greeting
    "Tell me a joke",          # joke
    "What time is it?",        # time
    "What's today's date?",    # date
    "Thank you",               # gratitude
    "Goodbye"                  # farewell
)

foreach ($msg in $testMessages) {
    $body = @{message = $msg} | ConvertTo-Json
    $response = Invoke-WebRequest -Uri "http://localhost:5000/api/chat" `
        -Method POST -ContentType "application/json" -Body $body
    $result = $response.Content | ConvertFrom-Json
    Write-Host "[$($result.timestamp)] User: $msg"
    Write-Host "  Bot: $($result.bot_response)`n"
}
```

### Scenario 3: Load Testing
```powershell
$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

for ($i = 1; $i -le 50; $i++) {
    $body = @{message = "Test message $i"} | ConvertTo-Json
    $response = Invoke-WebRequest -Uri "http://localhost:5000/api/chat" `
        -Method POST -ContentType "application/json" -Body $body -ErrorAction SilentlyContinue
    Write-Host "Request $i completed"
}

$stopwatch.Stop()
Write-Host "`nTotal time for 50 requests: $($stopwatch.ElapsedMilliseconds)ms"
Write-Host "Average: $($stopwatch.ElapsedMilliseconds / 50)ms per request"
```

---

## Expected Responses

### Successful Chat Response
```json
{
  "status": "success",
  "user_message": "Hello!",
  "bot_response": "Hi there! What can I do for you?",
  "timestamp": "2024-12-09T10:30:05.123456"
}
```

### Error Response
```json
{
  "status": "error",
  "message": "Message field is required"
}
```

### History Response
```json
{
  "status": "success",
  "history": [
    {
      "user": "Hello",
      "bot": "Hi there!",
      "timestamp": "2024-12-09T10:30:05.123456"
    }
  ],
  "total": 1
}
```

---

## Common Issues & Solutions

### Issue: CORS Error
**Error**: `Access to XMLHttpRequest has been blocked by CORS policy`
**Solution**: Ensure Flask-CORS is installed and CORS is enabled in app.py

### Issue: Connection Refused
**Error**: `Connection refused` or `Cannot connect to localhost:5000`
**Solution**: Verify backend is running with `python app.py`

### Issue: Invalid JSON
**Error**: `json.decoder.JSONDecodeError`
**Solution**: Ensure request body is valid JSON format

### Issue: Timeout
**Error**: Request takes too long
**Solution**: Check backend is responsive with health endpoint

---

## Performance Benchmarks

On a typical system:
- **Health Check**: ~5ms
- **Chat Response**: ~10-20ms
- **Get History**: ~5ms
- **Get Suggestions**: ~3ms

---

**Happy Testing! 🧪**
