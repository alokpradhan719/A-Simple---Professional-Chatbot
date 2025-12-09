import json
from datetime import datetime
from typing import Dict, List, Tuple

class ProblemSolver:
    
    def __init__(self):
        self.name = "Alok Pradhan Chatbot"
        self.problems_solved = 0
        self.solutions = self._load_solutions()
    
    def _load_solutions(self) -> Dict:
        return {
            'python': {
                'category': 'Python Programming',
                'problems': {
                    'error': [
                        'AttributeError', 'TypeError', 'ValueError', 
                        'KeyError', 'IndexError', 'NameError'
                    ],
                    'solutions': {
                        'AttributeError': 'This error occurs when trying to access an attribute that doesn\'t exist. Check if the object has that attribute or if you misspelled it.',
                        'TypeError': 'This error means you\'re performing an operation on incompatible data types. Ensure types match (e.g., int + str).',
                        'ValueError': 'This error occurs when a function receives an argument of correct type but inappropriate value. Check your input values.',
                        'KeyError': 'This error occurs when trying to access a dictionary key that doesn\'t exist. Use .get() method instead.',
                        'IndexError': 'This error occurs when trying to access a list index that doesn\'t exist. Check your list length.',
                        'NameError': 'This error occurs when using a variable that hasn\'t been defined. Define the variable first.'
                    }
                }
            },
            'debugging': {
                'category': 'Debugging Techniques',
                'tips': [
                    'Use print() statements to track variable values',
                    'Use debugger: import pdb; pdb.set_trace()',
                    'Check for typos in variable names',
                    'Verify data types are correct',
                    'Test functions with different inputs',
                    'Use try-except blocks for error handling'
                ]
            },
            'performance': {
                'category': 'Performance Optimization',
                'tips': [
                    'Use list comprehensions instead of loops',
                    'Use set for O(1) lookup instead of list',
                    'Avoid nested loops when possible',
                    'Cache results with functools.lru_cache',
                    'Use generators for large datasets',
                    'Profile code with cProfile module'
                ]
            },
            'web': {
                'category': 'Web Development Issues',
                'problems': {
                    'CORS': 'Cross-Origin Resource Sharing error. Add CORS headers or use Flask-CORS.',
                    '404': 'Resource not found. Check URL path and API endpoint.',
                    '500': 'Server error. Check server logs for details.',
                    'timeout': 'Request timeout. Increase timeout duration or optimize code.'
                }
            },
            'database': {
                'category': 'Database Issues',
                'problems': {
                    'connection': 'Can\'t connect to database. Check credentials, host, and port.',
                    'syntax': 'SQL syntax error. Check your SQL query for typos.',
                    'constraint': 'Constraint violation. Check unique/foreign key constraints.',
                    'transaction': 'Transaction error. Use ROLLBACK and retry.'
                }
            }
        }
    
    def solve_problem(self, problem: str, domain: str = None) -> str:
        problem_lower = problem.lower().strip()
        
        if not domain:
            domain = self._detect_domain(problem_lower)
        
        if domain not in self.solutions:
            return f"Sorry, I don't have solutions for the '{domain}' domain yet. Try asking about: Python, Debugging, Performance, Web, or Database."
        
        solution = self._get_solution(problem_lower, domain)
        self.problems_solved += 1
        
        return solution
    
    def _detect_domain(self, problem: str) -> str:
        keywords = {
            'python': ['python', 'error', 'code', 'script', 'function'],
            'debugging': ['debug', 'bug', 'fix', 'wrong', 'issue'],
            'performance': ['slow', 'fast', 'optimize', 'performance'],
            'web': ['api', 'web', 'cors', 'http', 'request'],
            'database': ['database', 'sql', 'data', 'query']
        }
        
        for domain, keywords_list in keywords.items():
            for keyword in keywords_list:
                if keyword in problem:
                    return domain
        
        return 'python'
    
    def _get_solution(self, problem: str, domain: str) -> str:
        domain_data = self.solutions[domain]
        
        if domain == 'python':
            for error_type, solution in domain_data['problems']['solutions'].items():
                if error_type.lower() in problem:
                    return f"**{error_type} Solution:**\n{solution}"
            
            return f"I can help with these Python errors: {', '.join(domain_data['problems']['solutions'].keys())}"
        
        elif domain == 'debugging':
            tips = '\n'.join([f"• {tip}" for tip in domain_data['tips']])
            return f"**Debugging Tips:**\n{tips}"
        
        elif domain == 'performance':
            tips = '\n'.join([f"• {tip}" for tip in domain_data['tips']])
            return f"**Performance Optimization Tips:**\n{tips}"
        
        elif domain == 'web':
            for error, solution in domain_data['problems'].items():
                if error.lower() in problem:
                    return f"**{error} Error Solution:**\n{solution}"
            
            return f"I can help with: {', '.join(domain_data['problems'].keys())}"
        
        elif domain == 'database':
            for error, solution in domain_data['problems'].items():
                if error.lower() in problem:
                    return f"**{error} Issue Solution:**\n{solution}"
            
            return f"I can help with: {', '.join(domain_data['problems'].keys())}"
        
        return "I can't find a solution for that problem."
    
    def get_code_example(self, topic: str) -> str:
        examples = {
            'list_comprehension': "numbers = [1, 2, 3, 4, 5]\nsquared = [x**2 for x in numbers]\nprint(squared)",
            'try_except': "try:\n    value = int('abc')\nexcept ValueError:\n    print('Invalid input')",
            'lambda': "square = lambda x: x ** 2\nprint(square(5))",
            'decorator': "def my_decorator(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__}')\n        return func(*args, **kwargs)\n    return wrapper"
        }
        
        if topic.lower() in examples:
            return f"**{topic.title()} Example:**\n```python\n{examples[topic.lower()]}\n```"
        
        return f"I don't have an example for '{topic}' yet."
    
    def get_stats(self) -> Dict:
        return {
            'chatbot_name': self.name,
            'problems_solved': self.problems_solved,
            'domains_available': list(self.solutions.keys()),
            'timestamp': datetime.now().isoformat()
        }
