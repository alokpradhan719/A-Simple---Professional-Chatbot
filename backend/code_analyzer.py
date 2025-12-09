import re
from typing import Dict, List, Tuple

class CodeAnalyzer:
    
    def __init__(self):
        self.chatbot_name = "Alok Pradhan Chatbot"
        self.issues_found = 0
    
    def analyze_code(self, code: str) -> Dict:
        issues = {
            'syntax_errors': [],
            'style_issues': [],
            'performance_issues': [],
            'security_issues': []
        }
        
        issues['syntax_errors'] = self._check_syntax(code)
        issues['style_issues'] = self._check_style(code)
        issues['performance_issues'] = self._check_performance(code)
        issues['security_issues'] = self._check_security(code)
        
        self.issues_found += len([i for issue_list in issues.values() for i in issue_list])
        
        return issues
    
    def _check_syntax(self, code: str) -> List[str]:
        issues = []
        
        if re.search(r'(if|for|while|def|class)\s+.*[^:]$', code, re.MULTILINE):
            issues.append("Missing colon ':' after control statement")
        
        # Check for unmatched parentheses
        if code.count('(') != code.count(')'):
            issues.append("Unmatched parentheses")
        
        if code.count('[') != code.count(']'):
            issues.append("Unmatched brackets")
        
        return issues
    
    def _check_style(self, code: str) -> List[str]:
        issues = []
        
        if re.search(r'[a-z]\w*[A-Z]', code):
            issues.append("Use snake_case for variable names (e.g., my_var not myVar)")
        
        # Check for multiple statements on one line
        if code.count(';') > 0:
            issues.append("Avoid multiple statements on one line (semicolons)")
        
        lines = code.split('\n')
        for i, line in enumerate(lines):
            if len(line) > 79:
                issues.append(f"Line {i+1} is too long ({len(line)} > 79 characters)")
        
        return issues
    
    def _check_performance(self, code: str) -> List[str]:
        issues = []
        
        if code.count('for') > 1 and 'for' in code:
            issues.append("Consider if nested loops can be optimized")
        
        # Check for repeated string concatenation
        if code.count('+') > 3 and '"' in code:
            issues.append("Use str.join() instead of repeated '+' concatenation")
        
        if 'list(' in code:
            issues.append("Consider if list() conversion is necessary")
        
        return issues
    
    def _check_security(self, code: str) -> List[str]:
        issues = []
        
        if 'eval(' in code:
            issues.append("SECURITY: Avoid eval() - it's dangerous!")
        
        # Check for exec usage
        if 'exec(' in code:
            issues.append("SECURITY: Avoid exec() - it's dangerous!")
        
        if 'query' in code and '+' in code:
            issues.append("SECURITY: Check for SQL injection vulnerabilities")
        
        return issues
    
    def get_suggestions(self, code: str) -> List[str]:
        suggestions = []
        
        if 'def ' in code and '"""' not in code:
            suggestions.append("Add docstrings to functions")
        
        # Check for type hints
        if 'def ' in code and '->' not in code:
            suggestions.append("Add type hints to function signatures")
        
        if 'open(' in code and 'try:' not in code:
            suggestions.append("Add try-except block for file operations")
        
        return suggestions
    
    def format_report(self, issues: Dict) -> str:
        report = f"**{self.chatbot_name} - Code Analysis Report**\n\n"
        
        total_issues = sum(len(v) for v in issues.values() if isinstance(v, list))
        
        if total_issues == 0:
            report += "✅ No issues found! Your code looks good.\n"
            return report
        
        if issues['syntax_errors']:
            report += "🔴 **Syntax Errors:**\n"
            for error in issues['syntax_errors']:
                report += f"  • {error}\n"
            report += "\n"
        
        if issues['style_issues']:
            report += "🟡 **Style Issues:**\n"
            for issue in issues['style_issues']:
                report += f"  • {issue}\n"
            report += "\n"
        
        if issues['performance_issues']:
            report += "🟠 **Performance Issues:**\n"
            for issue in issues['performance_issues']:
                report += f"  • {issue}\n"
            report += "\n"
        
        if issues['security_issues']:
            report += "🔴 **Security Issues:**\n"
            for issue in issues['security_issues']:
                report += f"  • {issue}\n"
            report += "\n"
        
        report += f"**Total Issues: {total_issues}**\n"
        return report
