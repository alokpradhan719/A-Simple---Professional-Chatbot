// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const messagesContainer = document.getElementById('messagesContainer');
const userInput = document.getElementById('userInput');
const chatForm = document.getElementById('chatForm');
const clearBtn = document.getElementById('clearBtn');
const loadingIndicator = document.getElementById('loadingIndicator');
const suggestionsContainer = document.getElementById('suggestionsContainer');
const suggestionsGrid = document.getElementById('suggestionsGrid');

// Advanced features for Alok Pradhan Chatbot
const ADVANCED_FEATURES = {
    'problem_solving': '/api/solve-problem',
    'code_analysis': '/api/analyze-code',
    'learning_resources': '/api/learning-resources',
    'learning_path': '/api/learning-path',
    'code_example': '/api/code-example',
    'chatbot_info': '/api/chatbot-info',
    'stats': '/api/stats'
};

// Message Functions
function createMessageElement(content, isUser = false) {
    const message = document.createElement('div');
    message.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.innerHTML = escapeHtml(content);
    
    const messageTime = document.createElement('span');
    messageTime.className = 'message-time';
    messageTime.textContent = getCurrentTime();
    
    message.appendChild(messageContent);
    message.appendChild(messageTime);
    
    return message;
}

function getCurrentTime() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    return `${hours}:${minutes}`;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function addMessage(content, isUser = false) {
    const messageElement = createMessageElement(content, isUser);
    messagesContainer.appendChild(messageElement);
    scrollToBottom();
}

function scrollToBottom() {
    setTimeout(() => {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 0);
}

function showLoadingIndicator() {
    loadingIndicator.classList.remove('hidden');
    scrollToBottom();
}

function hideLoadingIndicator() {
    loadingIndicator.classList.add('hidden');
}

// API Functions
async function sendMessage(message) {
    try {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ message: message.trim() })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        if (data.status === 'success') {
            return data.bot_response;
        } else {
            throw new Error(data.message || 'Failed to get response');
        }
    } catch (error) {
        console.error('Error:', error);
        return `Sorry, I encountered an error: ${error.message}. Please try again later.`;
    }
}

async function loadSuggestions() {
    try {
        const response = await fetch(`${API_BASE_URL}/suggestions`);
        const data = await response.json();
        
        if (data.status === 'success' && data.suggestions) {
            suggestionsGrid.innerHTML = '';
            data.suggestions.forEach(suggestion => {
                const btn = document.createElement('button');
                btn.className = 'suggestion-btn';
                btn.textContent = suggestion;
                btn.type = 'button';
                btn.addEventListener('click', () => {
                    userInput.value = suggestion;
                    chatForm.dispatchEvent(new Event('submit'));
                });
                suggestionsGrid.appendChild(btn);
            });
        }
    } catch (error) {
        console.error('Error loading suggestions:', error);
    }
}

async function clearChatHistory() {
    if (!confirm('Are you sure you want to clear the entire chat history?')) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/clear`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();
        
        if (data.status === 'success') {
            messagesContainer.innerHTML = '';
            addMessage('Hey! 👋 I\'m ChatBot. How can I help you today?', false);
            await loadSuggestions();
        }
    } catch (error) {
        console.error('Error clearing history:', error);
        addMessage('Failed to clear history. Please try again.', false);
    }
}

async function checkApiHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();
        console.log('API Health:', data);
        return data.status === 'success';
    } catch (error) {
        console.error('API Health Check Failed:', error);
        return false;
    }
}

// Event Listeners
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const message = userInput.value.trim();
    
    if (!message) {
        return;
    }
    
    // Hide suggestions container
    if (suggestionsContainer.style.display !== 'none') {
        suggestionsContainer.style.display = 'none';
    }
    
    // Clear input
    userInput.value = '';
    
    // Show user message
    addMessage(message, true);
    
    // Show loading indicator and disable input
    showLoadingIndicator();
    userInput.disabled = true;
    
    try {
        // Get bot response
        const botResponse = await sendMessage(message);
        hideLoadingIndicator();
        addMessage(botResponse, false);
    } catch (error) {
        hideLoadingIndicator();
        addMessage('Sorry, something went wrong. Please try again.', false);
    } finally {
        userInput.disabled = false;
        userInput.focus();
    }
});

clearBtn.addEventListener('click', clearChatHistory);

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
    console.log('Initializing ChatBot...');
    
    // Check API health
    const isHealthy = await checkApiHealth();
    if (!isHealthy) {
        addMessage('⚠️ Unable to connect to the API. Please make sure the backend server is running on http://localhost:5000', false);
    }
    
    // Load suggestions
    await loadSuggestions();
    
    // Focus input
    userInput.focus();
    
    console.log('ChatBot initialized successfully!');
});

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + L to clear
    if ((e.ctrlKey || e.metaKey) && e.key === 'l') {
        e.preventDefault();
        clearChatHistory();
    }
});
