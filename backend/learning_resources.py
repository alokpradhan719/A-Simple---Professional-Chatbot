from typing import Dict, List
from datetime import datetime

class LearningResources:
    
    def __init__(self):
        self.chatbot_name = "Alok Pradhan Chatbot"
        self.resources = self._load_resources()
    
    def _load_resources(self) -> Dict:
        return {
            'python_basics': {
                'title': 'Python Basics',
                'topics': ['variables', 'data types', 'operators', 'conditionals', 'loops'],
                'difficulty': 'Beginner',
                'duration': '2-3 hours'
            },
            'functions': {
                'title': 'Functions and Scope',
                'topics': ['function definition', 'parameters', 'return values', 'scope', 'lambda'],
                'difficulty': 'Beginner',
                'duration': '2 hours'
            },
            'data_structures': {
                'title': 'Data Structures',
                'topics': ['lists', 'tuples', 'dictionaries', 'sets', 'comprehensions'],
                'difficulty': 'Intermediate',
                'duration': '3 hours'
            },
            'oop': {
                'title': 'Object-Oriented Programming',
                'topics': ['classes', 'objects', 'inheritance', 'polymorphism', 'encapsulation'],
                'difficulty': 'Intermediate',
                'duration': '4 hours'
            },
            'error_handling': {
                'title': 'Error Handling and Debugging',
                'topics': ['try-except', 'custom exceptions', 'debugging', 'logging'],
                'difficulty': 'Intermediate',
                'duration': '2.5 hours'
            },
            'file_io': {
                'title': 'File I/O and JSON',
                'topics': ['reading files', 'writing files', 'JSON', 'CSV', 'serialization'],
                'difficulty': 'Beginner',
                'duration': '2 hours'
            },
            'apis': {
                'title': 'Working with APIs',
                'topics': ['HTTP requests', 'REST', 'API design', 'requests library', 'response handling'],
                'difficulty': 'Intermediate',
                'duration': '3 hours'
            },
            'databases': {
                'title': 'Databases and SQL',
                'topics': ['SQL basics', 'CRUD operations', 'relationships', 'joins', 'indexing'],
                'difficulty': 'Intermediate',
                'duration': '4 hours'
            }
        }
    
    def get_resource(self, topic: str) -> str:
        topic_lower = topic.lower().replace(' ', '_')
        
        if topic_lower in self.resources:
            resource = self.resources[topic_lower]
            return self._format_resource(resource)
        
        return f"Sorry, I don't have a resource for '{topic}'. Available resources: {', '.join(self.resources.keys())}"
    
    def _format_resource(self, resource: Dict) -> str:
        topics = ', '.join(resource['topics'])
        return f"""
**{resource['title']}**
📚 Topics: {topics}
🎓 Difficulty: {resource['difficulty']}
⏱️ Duration: {resource['duration']}

This course covers all essential concepts you need to master {resource['title'].lower()}.
        """.strip()
    
    def list_all_resources(self) -> str:
        report = f"**{self.chatbot_name} - Available Learning Resources**\n\n"
        
        for key, resource in self.resources.items():
            report += f"📚 **{resource['title']}** ({resource['difficulty']})\n"
            report += f"   ⏱️ {resource['duration']}\n"
            report += f"   Topics: {', '.join(resource['topics'][:3])}...\n\n"
        
        return report
    
    def get_learning_path(self, goal: str) -> str:
        """Suggest learning path based on goal"""
        paths = {
            'web development': ['python_basics', 'functions', 'data_structures', 'apis', 'databases'],
            'data science': ['python_basics', 'data_structures', 'error_handling', 'file_io'],
            'backend': ['python_basics', 'oop', 'apis', 'databases', 'error_handling'],
            'automation': ['python_basics', 'functions', 'file_io', 'error_handling']
        }
        
        goal_lower = goal.lower()
        
        # Find matching path
        matching_path = None
        for key in paths:
            if key in goal_lower or goal_lower in key:
                matching_path = key
                break
        
        if not matching_path:
            return f"I don't have a learning path for '{goal}'. Try: {', '.join(paths.keys())}"
        
        course_list = paths[matching_path]
        report = f"**{self.chatbot_name} - Learning Path for {matching_path.title()}**\n\n"
        
        for i, course_key in enumerate(course_list, 1):
            if course_key in self.resources:
                course = self.resources[course_key]
                report += f"{i}. **{course['title']}** ({course['duration']})\n"
        
        return report
    
    def get_tips_for_learning(self) -> str:
        """Get tips for effective learning"""
        tips = [
            "Practice coding every day, even if just for 15 minutes",
            "Build projects to apply what you've learned",
            "Read other people's code to improve your understanding",
            "Join coding communities and participate in discussions",
            "Use version control (Git) from the start",
            "Write clean, readable code with comments",
            "Test your code thoroughly before deployment",
            "Don't just watch tutorials - write code along with them",
            "Solve coding challenges and problems regularly",
            "Teach others what you've learned"
        ]
        
        report = f"**{self.chatbot_name} - Tips for Effective Learning**\n\n"
        for i, tip in enumerate(tips, 1):
            report += f"{i}. {tip}\n"
        
        return report
