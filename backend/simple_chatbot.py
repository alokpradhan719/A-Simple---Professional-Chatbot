import random
import math
from datetime import datetime

class SimpleChatbot:
    def __init__(self):
        self.name = "Alok Pradhan Chatbot"
        self.version = "1.0"
        self.author = "Alok Pradhan"
        self.created = "December 9, 2024"
    
    def get_response(self, user_input):
        user_input_lower = user_input.lower().strip()
        
        if not user_input:
            return "Please say something!"
        
        if any(word in user_input_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return f"Hello! I'm {self.name}. How can I help you today?"
        
        if any(word in user_input_lower for word in ['bye', 'goodbye', 'see you', 'farewell']):
            return "Goodbye! Have a great day!"
        
        if 'joke' in user_input_lower or 'funny' in user_input_lower or 'laugh' in user_input_lower:
            return self.tell_joke()
        
        if any(word in user_input_lower for word in ['math', 'calculate', 'solve', 'add', 'subtract', 'multiply', 'divide']):
            return self.handle_math(user_input)
        
        if 'definition' in user_input_lower or 'mean' in user_input_lower or 'dictionary' in user_input_lower or 'word' in user_input_lower:
            return self.handle_dictionary(user_input)
        
        if 'time' in user_input_lower or 'what time' in user_input_lower:
            return f"Current time: {datetime.now().strftime('%H:%M:%S')}"
        
        if 'date' in user_input_lower or 'today' in user_input_lower:
            return f"Today is: {datetime.now().strftime('%A, %B %d, %Y')}"
        
        if any(word in user_input_lower for word in ['name', 'who are you', 'your name', 'creator', 'author']):
            return f"I'm {self.name} v{self.version}\nCreated by {self.author}\nDate: {self.created}\nA professional AI assistant by Alok Pradhan"
        
        if 'help' in user_input_lower or 'what can you do' in user_input_lower:
            return self.get_help()
        
        return self.get_default_response()
    
    def tell_joke(self):
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Why did Python go to the gym? To get more fit!",
            "What do you call a programmer from Finland? Nerdic!",
            "Why do Java developers wear glasses? Because they don't C#!",
            "How many MySQL developers does it take to change a light bulb? None, that's a database problem!",
            "What's the object-oriented way to become wealthy? Inheritance!"
        ]
        return random.choice(jokes)
    
    def handle_math(self, user_input):
        try:
            if '+' in user_input:
                numbers = user_input.replace('+', ' ').split()
                result = sum(float(n) for n in numbers if self.is_number(n))
                return f"Result: {result}"
            
            elif '-' in user_input and user_input.count('-') == 1:
                parts = user_input.split('-')
                if self.is_number(parts[0].strip()) and self.is_number(parts[1].strip()):
                    result = float(parts[0].strip()) - float(parts[1].strip())
                    return f"Result: {result}"
            
            elif '*' in user_input or 'multiply' in user_input:
                if '*' in user_input:
                    parts = user_input.split('*')
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        return f"Result: {a * b}"
            
            elif '/' in user_input or 'divide' in user_input:
                if '/' in user_input:
                    parts = user_input.split('/')
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        if b != 0:
                            return f"Result: {a / b}"
                        else:
                            return "Cannot divide by zero!"
            
            elif 'square' in user_input:
                for word in user_input.split():
                    if self.is_number(word):
                        num = float(word)
                        return f"Square of {num} is {num**2}"
            
            elif 'sqrt' in user_input or 'square root' in user_input:
                for word in user_input.split():
                    if self.is_number(word):
                        num = float(word)
                        if num >= 0:
                            return f"Square root of {num} is {math.sqrt(num)}"
                        else:
                            return "Cannot find square root of negative number!"
            
            return "I can help with: addition (+), subtraction (-), multiplication (*), division (/), square, square root. Example: '5 + 3'"
        
        except:
            return "Sorry, I couldn't solve that. Try: '5 + 3' or '10 * 2'"
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except:
            return False
    
    def handle_dictionary(self, user_input):
        dictionary = {
            'python': 'A high-level programming language known for its simplicity.',
            'algorithm': 'A step-by-step procedure for solving a problem.',
            'variable': 'A named location in memory that stores a value.',
            'function': 'A reusable block of code that performs a specific task.',
            'loop': 'A control structure that repeats a block of code.',
            'data': 'Information or facts collected for analysis.',
            'database': 'An organized collection of structured data.',
            'api': 'Application Programming Interface - a way for software to communicate.',
            'bug': 'An error or flaw in a program.',
            'debug': 'The process of finding and fixing errors in code.',
            'array': 'A collection of elements stored in a single variable.',
            'dictionary': 'A collection of key-value pairs.',
            'string': 'A sequence of characters.',
            'integer': 'A whole number without decimal points.',
            'boolean': 'A data type with only two values: True or False.',
            'cloud': 'Remote servers accessed over the internet.',
            'server': 'A computer that provides resources or services to other computers.',
            'client': 'A computer or software that requests services from a server.',
            'cache': 'Fast storage used to reduce access time to data.',
            'encryption': 'The process of converting data into a code to prevent unauthorized access.'
        }
        
        word_to_find = None
        for word in user_input.lower().split():
            if word in dictionary:
                word_to_find = word
                break
        
        if word_to_find:
            return f"**{word_to_find.capitalize()}**: {dictionary[word_to_find]}"
        
        available = ', '.join(list(dictionary.keys())[:10]) + '...'
        return f"Available words: {available}\nTry asking 'definition of python' or 'what is algorithm'"
    
    def get_help(self):
        return f"""
╔══════════════════════════════════════════════════════════╗
║     {self.name} - Help Menu
║     Created by {self.author}
╚══════════════════════════════════════════════════════════╝

📚 AVAILABLE FEATURES:

1️⃣ JOKES & FUN
   - "Tell me a joke"
   - "Make me laugh"
   - "Funny"

2️⃣ MATHEMATICS
   - Addition: "5 + 3"
   - Subtraction: "10 - 2"
   - Multiplication: "5 * 4"
   - Division: "20 / 4"
   - Square: "square 9"
   - Square Root: "sqrt 16"

3️⃣ DICTIONARY & DEFINITIONS
   - "definition of python"
   - "what is algorithm"
   - "meaning of api"
   - "what does database mean"

4️⃣ TIME & DATE
   - "what time is it"
   - "what's the date"
   - "current time"
   - "today"

5️⃣ INFORMATION
   - "who are you"
   - "what can you do"
   - "help"
   - "features"

6️⃣ GREETINGS
   - "hello" / "hi"
   - "goodbye" / "bye"
   - "good morning"

💡 EXAMPLE CONVERSATIONS:
   • User: "Tell me a joke" → Bot tells a programming joke
   • User: "5 + 3" → Bot: "Result: 8"
   • User: "definition of python" → Bot: Shows definition
   • User: "square 7" → Bot: "Square of 7 is 49"
   • User: "what time is it" → Bot: Shows current time

Need help? Just type "help" anytime!
        """
    
    def get_default_response(self):
        responses = [
            "That's interesting! Tell me more.",
            "I see. Could you elaborate?",
            "Interesting! Do you need help with anything?",
            "I'm here to help! Ask me about math, jokes, or definitions.",
            "Can you rephrase that? Or try asking me a joke!",
            "Got it! Do you want help with math or a joke?"
        ]
        return random.choice(responses)
