import time
from typing import Dict, List
from datetime import datetime

class ChatbotUtils:
    
    CHATBOT_NAME = "Alok Pradhan Chatbot"
    VERSION = "2.0"
    CREATED_DATE = "December 9, 2024"
    
    @staticmethod
    def format_response(content: str, response_type: str = 'normal') -> str:
        if response_type == 'success':
            return f"✅ {content}"
        elif response_type == 'error':
            return f"❌ {content}"
        elif response_type == 'info':
            return f"ℹ️ {content}"
        elif response_type == 'warning':
            return f"⚠️ {content}"
        else:
            return content
    
    @staticmethod
    def get_chatbot_info() -> Dict:
        return {
            'name': ChatbotUtils.CHATBOT_NAME,
            'version': ChatbotUtils.VERSION,
            'created': ChatbotUtils.CREATED_DATE,
            'features': [
                'Real-time problem solving',
                'Code analysis',
                'Learning resources',
                'Error detection',
                'Performance suggestions'
            ]
        }
    
    @staticmethod
    def format_error_message(error: str) -> str:
        explanations = {
            'syntax': 'This is a syntax error - check your code structure',
            'runtime': 'This error occurred while running your code',
            'logical': 'Your code runs but produces wrong results',
            'performance': 'Your code is too slow or uses too much memory'
        }
        
        for error_type, explanation in explanations.items():
            if error_type.lower() in error.lower():
                return f"**{error}**\n{explanation}"
        
        return f"**{error}**"
    
    @staticmethod
    def get_help_menu() -> str:
        menu = f"""
**{ChatbotUtils.CHATBOT_NAME} - Help Menu**

Commands and Topics:
1️⃣ Problem Solving: "Help with [Python/Debugging/Performance/Web/Database]"
2️⃣ Code Analysis: "Analyze code [provide code snippet]"
3️⃣ Learning: "Learn about [topic]" or "Learning path for [goal]"
4️⃣ Examples: "Show me example of [concept]"
5️⃣ Tips: "Give me [learning/debugging/performance] tips"
6️⃣ Info: "About", "Version", "Features"

Example Questions:
• "Help with AttributeError"
• "Optimize my code"
• "Learning resources for web development"
• "Show me list comprehension example"
• "Debugging tips"
        """
        return menu.strip()
    
    @staticmethod
    def get_chatbot_stats() -> Dict:
        return {
            'name': ChatbotUtils.CHATBOT_NAME,
            'version': ChatbotUtils.VERSION,
            'capabilities': {
                'problem_domains': 5,
                'code_analysis_checks': 4,
                'learning_resources': 8,
                'error_types': 20,
                'code_examples': 10
            },
            'creation_date': ChatbotUtils.CREATED_DATE
        }
    
    @staticmethod
    def validate_input(user_input: str) -> tuple:
        """Validate and categorize user input"""
        input_lower = user_input.lower().strip()
        
        categories = {
            'problem_solving': ['help', 'error', 'issue', 'solve', 'problem'],
            'code_analysis': ['analyze', 'check', 'review', 'code'],
            'learning': ['learn', 'teach', 'resource', 'course', 'tutorial'],
            'example': ['example', 'show', 'demonstrate', 'sample'],
            'tips': ['tip', 'advice', 'guide', 'best practice'],
            'info': ['about', 'version', 'features', 'info']
        }
        
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in input_lower:
                    return True, category, user_input
        
        return False, None, user_input
    
    @staticmethod
    def get_response_time() -> float:
        """Get response time"""
        return time.time()
    
    @staticmethod
    def format_code_block(code: str, language: str = 'python') -> str:
        """Format code as code block"""
        return f"```{language}\n{code}\n```"
    
    @staticmethod
    def get_emoji_for_domain(domain: str) -> str:
        """Get emoji for different domains"""
        emojis = {
            'python': '🐍',
            'debugging': '🐛',
            'performance': '⚡',
            'web': '🌐',
            'database': '💾',
            'security': '🔒',
            'learning': '📚'
        }
        return emojis.get(domain.lower(), '💡')
