# 🤖 Alok Pradhan Chatbot - Advanced API Documentation

## Overview

**Alok Pradhan Chatbot v2.0** is an advanced problem-solving chatbot with real-time capabilities including code analysis, learning resources, and intelligent problem solving.

---

## API Endpoints

### 1. Health Check
```
GET /api/health
```

**Response:**
```json
{
    "status": "success",
    "message": "Chatbot API is running",
    "timestamp": "2024-12-09T10:30:00"
}
```

---

### 2. Chat (Main Endpoint)
```
POST /api/chat
```

**Request:**
```json
{
    "message": "Help with AttributeError"
}
```

**Response:**
```json
{
    "status": "success",
    "user_message": "Help with AttributeError",
    "bot_response": "**AttributeError Solution:**\nThis error occurs when trying to access an attribute that doesn't exist...",
    "timestamp": "2024-12-09T10:30:05"
}
```

---

### 3. Chatbot Information
```
GET /api/chatbot-info
```

**Response:**
```json
{
    "status": "success",
    "info": {
        "name": "Alok Pradhan Chatbot",
        "version": "2.0",
        "features": [
            "Problem solving (Python, Debugging, Performance, Web, Database)",
            "Code analysis and feedback",
            "Learning resources and tutorials",
            "Code examples and best practices",
            "Performance optimization tips",
            "Error diagnosis and solutions"
        ],
        "domains": ["python", "debugging", "performance", "web", "database"],
        "total_messages": 42
    },
    "timestamp": "2024-12-09T10:30:00"
}
```

---

### 4. Solve Problem
```
POST /api/solve-problem
```

**Request:**
```json
{
    "problem": "TypeError in my code",
    "domain": "python"
}
```

**Response:**
```json
{
    "status": "success",
    "problem": "TypeError in my code",
    "solution": "**TypeError Solution:**\nThis error means you're performing an operation on incompatible data types...",
    "timestamp": "2024-12-09T10:30:05"
}
```

**Supported Domains:**
- `python` - Python programming errors
- `debugging` - Debugging techniques
- `performance` - Performance optimization
- `web` - Web development issues
- `database` - Database issues

---

### 5. Analyze Code
```
POST /api/analyze-code
```

**Request:**
```json
{
    "code": "for i in range(10):\n    print(i)"
}
```

**Response:**
```json
{
    "status": "success",
    "issues": {
        "syntax_errors": [],
        "style_issues": ["Line 1 contains camelCase variable"],
        "performance_issues": [],
        "security_issues": []
    },
    "report": "**Alok Pradhan Chatbot - Code Analysis Report**\n\n✅ No major issues found!",
    "suggestions": ["Add docstrings to functions"],
    "timestamp": "2024-12-09T10:30:05"
}
```

---

### 6. Get Learning Resources
```
GET /api/learning-resources
```

**Response:**
```json
{
    "status": "success",
    "resources": "**Alok Pradhan Chatbot - Available Learning Resources**\n\n📚 **Python Basics** (Beginner)\n   ⏱️ 2-3 hours\n   Topics: variables, data types, operators, conditionals, loops...",
    "timestamp": "2024-12-09T10:30:00"
}
```

---

### 7. Get Learning Path
```
POST /api/learning-path
```

**Request:**
```json
{
    "goal": "web development"
}
```

**Response:**
```json
{
    "status": "success",
    "goal": "web development",
    "learning_path": "**Alok Pradhan Chatbot - Learning Path for Web Development**\n\n1. **Python Basics** (2-3 hours)\n2. **Functions and Scope** (2 hours)...",
    "timestamp": "2024-12-09T10:30:05"
}
```

---

### 8. Get Code Example
```
POST /api/code-example
```

**Request:**
```json
{
    "topic": "list_comprehension"
}
```

**Response:**
```json
{
    "status": "success",
    "topic": "list_comprehension",
    "example": "**List Comprehension Example:**\n```python\n# Instead of:\nresult = []\nfor i in range(10):\n    result.append(i * 2)\n\n# Use:\nresult = [i * 2 for i in range(10)]\n```",
    "timestamp": "2024-12-09T10:30:05"
}
```

**Available Topics:**
- `list_comprehension`
- `try_except`
- `lambda`
- `decorator`

---

### 9. Get Statistics
```
GET /api/stats
```

**Response:**
```json
{
    "status": "success",
    "stats": {
        "chatbot_name": "Alok Pradhan Chatbot",
        "chatbot_version": "2.0",
        "total_conversations": 42,
        "problems_solved": 15,
        "code_analyses": 8,
        "available_domains": ["python", "debugging", "performance", "web", "database"]
    },
    "timestamp": "2024-12-09T10:30:00"
}
```

---

### 10. Get Chat History
```
GET /api/history?limit=10
```

**Response:**
```json
{
    "status": "success",
    "history": [
        {
            "user": "Help with AttributeError",
            "bot": "**AttributeError Solution:**...",
            "timestamp": "2024-12-09T10:30:05"
        }
    ],
    "total": 1
}
```

---

### 11. Clear History
```
POST /api/clear
```

**Response:**
```json
{
    "status": "success",
    "message": "Conversation history cleared"
}
```

---

### 12. Get Suggestions
```
GET /api/suggestions
```

**Response:**
```json
{
    "status": "success",
    "suggestions": [
        "Help with Python errors",
        "Analyze my code",
        "Learning resources for web development",
        "Show me a code example",
        "Debugging tips",
        "Performance optimization",
        "Tell me about your features"
    ]
}
```

---

## Example Usage

### PowerShell Examples

**1. Get Chatbot Info:**
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/chatbot-info" -Method GET | ConvertTo-Json
```

**2. Solve a Problem:**
```powershell
$body = @{
    problem = "How do I fix a TypeError?"
    domain = "python"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/solve-problem" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body | ConvertTo-Json
```

**3. Analyze Code:**
```powershell
$body = @{
    code = "for i in range(10):`n    print(i)"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/analyze-code" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body | ConvertTo-Json
```

**4. Get Learning Path:**
```powershell
$body = @{
    goal = "web development"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/learning-path" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body | ConvertTo-Json
```

---

## Features by Domain

### Python Domain
**Errors:**
- AttributeError
- TypeError
- ValueError
- KeyError
- IndexError
- NameError

### Debugging Domain
**Capabilities:**
- Print debugging
- Python debugger (pdb)
- Typo detection
- Type checking
- Function testing
- Error handling

### Performance Domain
**Optimization Tips:**
- List comprehensions
- Set usage for O(1) lookup
- Avoid nested loops
- Caching with lru_cache
- Generators for large datasets
- Code profiling with cProfile

### Web Domain
**Issues:**
- CORS errors
- 404 Not Found
- 500 Server errors
- Request timeouts

### Database Domain
**Issues:**
- Connection problems
- SQL syntax errors
- Constraint violations
- Transaction errors

---

## Error Responses

### Bad Request (400)
```json
{
    "status": "error",
    "message": "Message field is required"
}
```

### Not Found (404)
```json
{
    "status": "error",
    "message": "Endpoint not found"
}
```

### Server Error (500)
```json
{
    "status": "error",
    "message": "Internal server error"
}
```

---

## Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Server Error |

---

## Features

✅ Real-time problem solving
✅ Code analysis and feedback
✅ Learning resources and tutorials
✅ Code examples with best practices
✅ Error diagnosis and solutions
✅ Performance optimization tips
✅ Conversation history
✅ Advanced statistics

---

## Request/Response Format

**All requests should include:**
- `Content-Type: application/json`

**All responses include:**
- `status` - "success" or "error"
- `timestamp` - ISO format timestamp
- Additional fields based on endpoint

---

## Rate Limiting

Currently no rate limiting. For production use, consider implementing rate limiting per IP.

---

## Authentication

Currently no authentication required. For production use, consider implementing:
- API key authentication
- JWT tokens
- OAuth2

---

## Version Information

- **Chatbot Name:** Alok Pradhan Chatbot
- **Version:** 2.0
- **Created:** December 9, 2024
- **Base URL:** http://localhost:5000

---

## Support

For issues or questions about the API, refer to the comprehensive documentation in the project README files.

---

**Last Updated:** December 9, 2024
**Status:** ✅ Active and Ready
