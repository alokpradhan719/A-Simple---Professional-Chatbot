from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
from chatbot import Chatbot
from problem_solver import ProblemSolver
from code_analyzer import CodeAnalyzer
from learning_resources import LearningResources

app = Flask(__name__)
CORS(app)

chatbot = Chatbot()
problem_solver = ProblemSolver()
code_analyzer = CodeAnalyzer()
learning_resources = LearningResources()

conversation_history = []

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'success',
        'message': 'Chatbot API is running',
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Message field is required'
            }), 400
        
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'status': 'error',
                'message': 'Message cannot be empty'
            }), 400
        
        bot_response = chatbot.get_response(user_message)
        
        conversation_history.append({
            'user': user_message,
            'bot': bot_response,
            'timestamp': datetime.now().isoformat()
        })
        
        return jsonify({
            'status': 'success',
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        limit = request.args.get('limit', default=50, type=int)
        history = conversation_history[-limit:]
        
        return jsonify({
            'status': 'success',
            'history': history,
            'total': len(conversation_history)
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/clear', methods=['POST'])
def clear_history():
    try:
        global conversation_history
        conversation_history = []
        
        return jsonify({
            'status': 'success',
            'message': 'Conversation history cleared'
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/suggestions', methods=['GET'])
def get_suggestions():
    suggestions = [
        "Help with Python errors",
        "Analyze my code",
        "Learning resources for web development",
        "Show me a code example",
        "Debugging tips",
        "Performance optimization",
        "Tell me about your features"
    ]
    
    return jsonify({
        'status': 'success',
        'suggestions': suggestions
    }), 200


@app.route('/api/chatbot-info', methods=['GET'])
def get_chatbot_info():
    try:
        info = {
            'name': chatbot.name,
            'version': chatbot.version,
            'features': [
                'Problem solving (Python, Debugging, Performance, Web, Database)',
                'Code analysis and feedback',
                'Learning resources and tutorials',
                'Code examples and best practices',
                'Performance optimization tips',
                'Error diagnosis and solutions'
            ],
            'domains': list(problem_solver.solutions.keys()),
            'total_messages': chatbot.conversation_count
        }
        
        return jsonify({
            'status': 'success',
            'info': info,
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/solve-problem', methods=['POST'])
def solve_problem():
    try:
        data = request.get_json()
        
        if not data or 'problem' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Problem field is required'
            }), 400
        
        problem = data.get('problem', '').strip()
        domain = data.get('domain', None)
        
        if not problem:
            return jsonify({
                'status': 'error',
                'message': 'Problem cannot be empty'
            }), 400
        
        solution = problem_solver.solve_problem(problem, domain)
        
        return jsonify({
            'status': 'success',
            'problem': problem,
            'solution': solution,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/analyze-code', methods=['POST'])
def analyze_code():
    try:
        data = request.get_json()
        
        if not data or 'code' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Code field is required'
            }), 400
        
        code = data.get('code', '').strip()
        
        if not code:
            return jsonify({
                'status': 'error',
                'message': 'Code cannot be empty'
            }), 400
        
        issues = code_analyzer.analyze_code(code)
        report = code_analyzer.format_report(issues)
        suggestions = code_analyzer.get_suggestions(code)
        
        return jsonify({
            'status': 'success',
            'issues': issues,
            'report': report,
            'suggestions': suggestions,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/learning-resources', methods=['GET'])
def get_learning_resources():
    try:
        resource_list = learning_resources.list_all_resources()
        
        return jsonify({
            'status': 'success',
            'resources': resource_list,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/learning-path', methods=['POST'])
def get_learning_path():
    try:
        data = request.get_json()
        
        if not data or 'goal' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Goal field is required'
            }), 400
        
        goal = data.get('goal', '').strip()
        path = learning_resources.get_learning_path(goal)
        
        return jsonify({
            'status': 'success',
            'goal': goal,
            'learning_path': path,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/code-example', methods=['POST'])
def get_code_example():
    try:
        data = request.get_json()
        
        if not data or 'topic' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Topic field is required'
            }), 400
        
        topic = data.get('topic', '').strip()
        example = problem_solver.get_code_example(topic)
        
        return jsonify({
            'status': 'success',
            'topic': topic,
            'example': example,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    try:
        stats = {
            'chatbot_name': chatbot.name,
            'chatbot_version': chatbot.version,
            'total_conversations': chatbot.conversation_count,
            'problems_solved': problem_solver.problems_solved,
            'code_analyses': code_analyzer.issues_found,
            'available_domains': list(problem_solver.solutions.keys())
        }
        
        return jsonify({
            'status': 'success',
            'stats': stats,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500


if __name__ == '__main__':
    print(f"Starting {chatbot.name} (v{chatbot.version}) on http://localhost:5000")
    print("Features: Problem Solving, Code Analysis, Learning Resources, Error Detection")
    app.run(debug=True, host='0.0.0.0', port=5000)
