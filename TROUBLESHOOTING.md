# 🔧 Troubleshooting Guide

## Common Issues & Solutions

---

## 🔴 Backend Issues

### Issue 1: Backend won't start - Port 5000 already in use

**Error Message:**
```
Address already in use
OSError: [Errno 10048]
```

**Solutions:**

**Option A: Find and kill the process**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace XXXX with PID)
taskkill /PID XXXX /F
```

**Option B: Use a different port**
Edit `backend/app.py` at the end:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed from 5000
```

Then update `frontend/script.js`:
```javascript
const API_BASE_URL = 'http://localhost:5001/api';  # Updated to 5001
```

---

### Issue 2: ModuleNotFoundError - Flask not found

**Error Message:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solutions:**

**Check if virtual environment is activated:**
```powershell
# You should see (venv) at the start of your terminal
# If not, activate it:
.\venv\Scripts\Activate.ps1
```

**Reinstall requirements:**
```powershell
pip install -r requirements.txt
```

**If virtual environment is corrupted:**
```powershell
# Delete old venv
rmdir /s venv

# Create new one
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

### Issue 3: "Virtual environment won't activate"

**Error Message:**
```
PowerShell: File cannot be loaded because running scripts is disabled on this system
```

**Solution:**
```powershell
# Run PowerShell as Administrator, then:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Try activation again
.\venv\Scripts\Activate.ps1
```

---

### Issue 4: Python not found

**Error Message:**
```
'python' is not recognized as an internal or external command
```

**Solutions:**

**Check if Python is installed:**
```powershell
python --version
```

**If not installed:**
1. Download from https://www.python.org/downloads/
2. Run installer and **check "Add Python to PATH"**
3. Restart terminal

**Use full path:**
```powershell
C:\Python39\python.exe -m venv venv
```

---

### Issue 5: API returns 500 error

**Error Message:**
```json
{
  "status": "error",
  "message": "Internal server error"
}
```

**Solutions:**

1. **Check backend terminal** for error details
2. **Restart backend:**
   ```powershell
   # Stop with Ctrl+C
   # Restart
   python app.py
   ```
3. **Check chatbot.py** for syntax errors:
   ```powershell
   python -m py_compile chatbot.py
   ```

---

## 🔴 Frontend Issues

### Issue 1: Frontend can't connect to API

**Error in Browser Console (F12):**
```
CORS error / Failed to fetch / Network error
```

**Solutions:**

**Check if backend is running:**
```powershell
# In another PowerShell window
curl http://localhost:5000/api/health
# Or visit in browser
```

**Check API URL in script.js:**
```javascript
// Line 2 of frontend/script.js should be:
const API_BASE_URL = 'http://localhost:5000/api';
```

**Verify CORS is enabled in app.py:**
```python
# Should see near the top:
from flask_cors import CORS
CORS(app)
```

---

### Issue 2: Frontend page is blank

**Solutions:**

**Check browser console (F12)** for JavaScript errors

**Verify files exist:**
- Check http://localhost:8000 loads index.html
- Check styles.css is loaded (look in Network tab)
- Check script.js is loaded (look in Network tab)

**Clear browser cache:**
```
Ctrl+Shift+Delete (or Cmd+Shift+Delete on Mac)
```

---

### Issue 3: Messages don't appear

**Solutions:**

**Check browser console (F12)** for JavaScript errors

**Test API directly:**
```powershell
$body = @{message = "test"} | ConvertTo-Json
Invoke-WebRequest -Uri "http://localhost:5000/api/chat" `
  -Method POST -ContentType "application/json" -Body $body
```

**Verify message input isn't disabled:**
Press F12, check if input field has `disabled` attribute

---

### Issue 4: Buttons don't work

**Solutions:**

**Check browser console** for JavaScript errors

**Test in different browser** (Chrome, Firefox, Edge)

**Disable extensions:**
- Try in Incognito/Private mode
- Disable browser extensions

---

### Issue 5: Styling looks wrong

**Solutions:**

**Clear browser cache:**
```
Ctrl+Shift+Delete
```

**Force reload:**
```
Ctrl+Shift+R (or Cmd+Shift+R on Mac)
```

**Check CSS file loaded:**
- F12 → Network tab → Look for styles.css
- Should see 200 status code

**Check CSS syntax:**
```powershell
# Visit individual file
http://localhost:8000/styles.css
# Should see CSS code, not HTML error
```

---

## 🔴 Connection Issues

### Issue 1: Frontend running but can't access

**Error in browser:**
```
This site can't be reached / Connection refused
```

**Solutions:**

**Check if frontend server is running:**
```powershell
# Should see output like:
# Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

**Start frontend server:**
```powershell
cd frontend
python -m http.server 8000
```

**Check port 8000 is available:**
```powershell
netstat -ano | findstr :8000
```

---

### Issue 2: Mixed Content error

**Error:**
```
Mixed Content: The page was loaded over HTTPS but requested an insecure XMLHttpRequest endpoint
```

**Solution:**

Ensure both frontend and backend use HTTP or HTTPS (not mixed)

For local development, both should use HTTP:
- Frontend: http://localhost:8000
- Backend: http://localhost:5000

---

## 🟡 Performance Issues

### Issue 1: API responses are slow

**Solutions:**

**Check system resources:**
```powershell
# Use Task Manager or:
wmic OS get totalvisiblememorysize
```

**Restart the services:**
```powershell
# Stop backend (Ctrl+C)
# Stop frontend (Ctrl+C)
# Restart both
```

**Check for background processes:**
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*python*"}
```

---

### Issue 2: Frontend is laggy

**Solutions:**

**Check browser DevTools (F12):**
- Performance tab for slow JavaScript
- Network tab for slow API calls

**Reduce browser extensions:**
- Try Incognito mode
- Disable unnecessary extensions

---

## 🔵 Data Issues

### Issue 1: Chat history empty/not saving

**Solutions:**

**History is in-memory only:**
- History is cleared when backend restarts
- To persist, add a database (see CONFIG_REFERENCE.md)

**Test history endpoint:**
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/history" -Method GET
```

---

### Issue 2: Suggestions not appearing

**Solutions:**

**Test suggestions endpoint:**
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/suggestions" -Method GET
```

**Check browser console** for JavaScript errors

**Verify suggestions container is visible:**
```javascript
// Check in console
document.getElementById('suggestionsContainer').style.display
```

---

## 🟢 General Solutions

### Solution 1: Restart everything

```powershell
# Terminal 1: Stop backend (Ctrl+C)
# Terminal 2: Stop frontend (Ctrl+C)

# Then restart both:

# Terminal 1:
cd "C:\Users\ALOK PRADHAN\OneDrive\Desktop\Chatbot\backend"
.\venv\Scripts\Activate.ps1
python app.py

# Terminal 2:
cd "C:\Users\ALOK PRADHAN\OneDrive\Desktop\Chatbot\frontend"
python -m http.server 8000
```

### Solution 2: Clear all temporary data

```powershell
# Backend - clear and restart
# Frontend - refresh in browser (Ctrl+F5)
```

### Solution 3: Check logs

**Backend logs:**
```
Check the terminal output when backend is running
```

**Frontend logs:**
```
F12 → Console tab → Check for errors
```

---

## 🆘 Advanced Troubleshooting

### Enable Debug Mode

**Backend - More verbose logging:**
```python
# In app.py, add after imports:
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Frontend - More console output:**
```javascript
// In script.js, add at top:
console.log('ChatBot frontend loaded');
```

### Test Individual Components

**Test Python syntax:**
```powershell
python -m py_compile app.py
python -m py_compile chatbot.py
```

**Test JavaScript syntax:**
```powershell
# Copy script.js content and validate at:
# https://jshint.com/
```

**Test HTML:**
```powershell
# Open index.html in browser
# Check console (F12)
```

---

## 📞 Getting Help

1. **Check Browser Console (F12)**
   - Console tab shows JavaScript errors
   - Network tab shows API calls
   - Look for red errors

2. **Check Backend Terminal**
   - Error messages appear here
   - Copy full error message

3. **Read Documentation**
   - README.md - General info
   - CONFIG_REFERENCE.md - Configuration
   - API_TESTING.md - API examples

4. **Test API Directly**
   - Use PowerShell commands
   - Use Postman
   - Verify backend works independently

5. **Isolate the Problem**
   - Is it backend? Test API directly
   - Is it frontend? Test with different browser
   - Is it network? Check localhost access

---

## ✅ Verification Checklist

Use this when something doesn't work:

- [ ] Backend is running (`python app.py`)
- [ ] Frontend is running (`python -m http.server 8000`)
- [ ] Can access http://localhost:5000/api/health
- [ ] Can access http://localhost:8000
- [ ] Browser console (F12) shows no red errors
- [ ] Backend terminal shows no red errors
- [ ] Virtual environment is activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Ports 5000 and 8000 are available
- [ ] No firewall blocking localhost
- [ ] Browser is up to date

---

## 💡 Prevention Tips

1. **Keep terminals organized** - Use clear titles
2. **Watch terminal output** - Errors appear immediately
3. **Check console regularly** - F12 console shows issues
4. **Test after changes** - Always verify after editing
5. **Backup working code** - Save before major changes
6. **Use version control** - Git helps track changes

---

**Can't find your issue? Check the other documentation files or restart fresh!**

**Happy Coding! 💻**
