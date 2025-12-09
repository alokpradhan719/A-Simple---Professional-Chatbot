import json
from datetime import datetime
import random
from problem_solver import ProblemSolver
from code_analyzer import CodeAnalyzer
from learning_resources import LearningResources
from chatbot_utils import ChatbotUtils

class Chatbot:
    
    def __init__(self):
        self.name = "Alok Pradhan Chatbot"
        self.version = "2.0"
        self.responses = self._load_responses()
        self.conversation_count = 0
        self.problem_solver = ProblemSolver()
        self.code_analyzer = CodeAnalyzer()
        self.learning_resources = LearningResources()
        self.utils = ChatbotUtils()
    
    def _load_responses(self):
        return {
            'greeting': {
                'patterns': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
                'responses': [
                    f'Hello! I\'m {self.name}. How can I help you today?',
                    f'Hi there! I\'m {self.name}. What can I do for you?',
                    f'Greetings! I\'m {self.name}. How may I assist you?',
                    f'Hey! I\'m {self.name}. Nice to meet you. What do you need?'
                ]
            },
            'farewell': {
                'patterns': ['bye', 'goodbye', 'see you', 'farewell', 'take care', 'gotta go', 'talk to you later'],
                'responses': [
                    'Goodbye! Have a great day!',
                    'See you later! Take care!',
                    'Bye! Thanks for chatting with me!',
                    'Farewell! Come back soon!'
                ]
            },
            'gratitude': {
                'patterns': ['thank you', 'thanks', 'thank u', 'appreciate', 'thanks so much', 'thank you so much'],
                'responses': [
                    'You\'re welcome! Happy to help!',
                    'My pleasure! Anything else?',
                    'Glad I could help! Let me know if you need anything else.',
                    'No problem! I\'m here to help.'
                ]
            },
            'how_are_you': {
                'patterns': ['how are you', 'how\'s it going', 'how do you do', 'how\'re you', 'what\'s up'],
                'responses': [
                    'I\'m doing great, thanks for asking! How about you?',
                    'I\'m good! Ready to help you with anything!',
                    'Doing well! What can I do for you?',
                    'All systems operational and ready to chat!'
                ]
            },
            'name': {
                'patterns': ['what\'s your name', 'who are you', 'your name', 'what do i call you'],
                'responses': [
                    f'I\'m {self.name} (v{self.version}), your advanced problem-solving assistant!',
                    f'You can call me {self.name}. I solve problems and teach programming!',
                    f'I\'m {self.name}, here to help you with coding and learning!'
                ]
            },
            'help': {
                'patterns': ['help', 'what can you do', 'capabilities', 'features', 'assist'],
                'responses': [
                    f'{self.name} can solve programming problems, analyze code, provide learning resources, and much more!',
                    f'I\'m {self.name}! I can help with debugging, performance optimization, code analysis, and learning Python.',
                    f'As {self.name}, I can assist with general conversations, solve coding problems, and teach programming!'
                ]
            },
            'joke': {
                'patterns': ['tell me a joke', 'make me laugh', 'joke', 'funny'],
                'responses': [
                    'Why did the programmer quit his job? Because he didn\'t get arrays!',
                    'Why do programmers prefer dark mode? Because light attracts bugs!',
                    'How many programmers does it take to change a light bulb? None, that\'s a hardware problem!',
                    'Why did Python go to the gym? To get more fit in the fit() function!'
                ]
            },
            'time': {
                'patterns': ['what time is it', 'current time', 'tell me the time', 'what\'s the time'],
                'responses': [
                    f'The current time is {datetime.now().strftime("%H:%M:%S")}',
                    f'It\'s {datetime.now().strftime("%I:%M %p")} right now.',
                    f'According to my clock, it\'s {datetime.now().strftime("%H:%M")}'
                ]
            },
            'date': {
                'patterns': ['what\'s the date', 'today\'s date', 'what date is it', 'today is'],
                'responses': [
                    f'Today is {datetime.now().strftime("%A, %B %d, %Y")}',
                    f'The date is {datetime.now().strftime("%m/%d/%Y")}',
                    f'It\'s {datetime.now().strftime("%A, %B %d")}'
                ]
            },
            'default': {
                'patterns': [],
                'responses': [
                    'That\'s interesting! Tell me more.',
                    'I see. Could you elaborate?',
                    'Interesting point! How does that relate to what you\'re working on?',
                    'I understand. What else would you like to know?',
                    'Got it! Is there anything else I can help you with?',
                    'That\'s great! Do you have any other questions?'
                ]
            }
        }
    
    def _get_intent(self, user_input):
        user_input_lower = user_input.lower().strip()
        
        for intent, data in self.responses.items():
            for pattern in data['patterns']:
                if pattern.lower() in user_input_lower:
                    return intent
        
        return 'default'
    
    def get_response(self, user_input):
        if not user_input or not isinstance(user_input, str):
            return "I didn't catch that. Could you please rephrase?"
        
        self.conversation_count += 1
        user_input_lower = user_input.lower()
        
        if any(word in user_input_lower for word in ['help with', 'error', 'issue', 'problem', 'fix', 'debug']):
            if 'error' in user_input_lower or 'exception' in user_input_lower:
                return self.problem_solver.solve_problem(user_input)
        
        if 'analyze' in user_input_lower or 'check code' in user_input_lower or 'review' in user_input_lower:
            return "I can analyze your code. Please share the code snippet and I'll provide detailed feedback."
        
        if any(word in user_input_lower for word in ['learn', 'teach', 'resource', 'course', 'tutorial']):
            if 'learning path' in user_input_lower or 'path for' in user_input_lower:
                topic = user_input.replace('learning path for', '').replace('path for', '').strip()
                return self.learning_resources.get_learning_path(topic)
            elif 'resources' in user_input_lower:
                return self.learning_resources.list_all_resources()
            else:
                topic = user_input.replace('learn about', '').replace('teach me', '').strip()
                return self.learning_resources.get_resource(topic)
        
        if 'example' in user_input_lower or 'show me' in user_input_lower:
            topic = user_input.replace('example of', '').replace('show me', '').strip()
            return self.problem_solver.get_code_example(topic)
        
        if any(word in user_input_lower for word in ['about', 'version', 'features', 'capabilities']):
            if 'version' in user_input_lower:
                return f"I'm {self.name} version {self.version}, created to help with programming problems and learning!"
            elif 'features' in user_input_lower:
                info = self.utils.get_chatbot_info()
                features = ', '.join(info['features'])
                return f"**{self.name} Features:**\n• {features.replace(', ', '\n• ')}"
            else:
                return f"I'm {self.name} - an advanced chatbot designed to solve programming problems, analyze code, and provide learning resources."
        
        if 'tips' in user_input_lower or 'advice' in user_input_lower:
            if 'learning' in user_input_lower:
                return self.learning_resources.get_tips_for_learning()
            elif 'debugging' in user_input_lower:
                solutions = self.problem_solver.solutions['debugging']
                tips = '\n'.join([f"• {tip}" for tip in solutions['tips']])
                return f"**Debugging Tips:**\n{tips}"
            elif 'performance' in user_input_lower or 'optimization' in user_input_lower:
                solutions = self.problem_solver.solutions['performance']
                tips = '\n'.join([f"• {tip}" for tip in solutions['tips']])
                return f"**Performance Optimization Tips:**\n{tips}"
        
        if 'menu' in user_input_lower or ('help' in user_input_lower and 'command' in user_input_lower):
            return self.utils.get_help_menu()
        
        intent = self._get_intent(user_input)
        responses = self.responses[intent]['responses']
        
        return random.choice(responses)


if __name__ == '__main__':
    bot = Chatbot()
    
    test_inputs = [
        'Hello',
        'How are you?',
        'Tell me a joke',
        'What\'s the time?',
        'Goodbye'
    ]
    
    print(f"{bot.name} is online!\n")
    
    for user_input in test_inputs:
        response = bot.get_response(user_input)
        print(f"User: {user_input}")
        print(f"Bot: {response}\n")
