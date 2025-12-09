from flask import Flask, request, jsonify
from flask_cors import CORS
from simple_chatbot import SimpleChatbot

app = Flask(__name__)
CORS(app)

chatbot = SimpleChatbot()
conversation_history = []

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'status': 'error', 'message': 'Message required'}), 400
        
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'status': 'error', 'message': 'Message cannot be empty'}), 400
        
        bot_response = chatbot.get_response(user_message)
        
        conversation_history.append({
            'user': user_message,
            'bot': bot_response,
            'timestamp': str(__import__('datetime').datetime.now())
        })
        
        return jsonify({
            'status': 'success',
            'user': user_message,
            'bot': bot_response
        }), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/help', methods=['GET'])
def get_help():
    return jsonify({
        'status': 'success',
        'help': chatbot.get_help()
    }), 200

@app.route('/api/joke', methods=['GET'])
def get_joke():
    return jsonify({
        'status': 'success',
        'joke': chatbot.tell_joke()
    }), 200

@app.route('/api/math', methods=['POST'])
def do_math():
    try:
        data = request.get_json()
        problem = data.get('problem', '')
        result = chatbot.handle_math(problem)
        return jsonify({'status': 'success', 'result': result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/dictionary', methods=['POST'])
def get_definition():
    try:
        data = request.get_json()
        word = data.get('word', '')
        result = chatbot.handle_dictionary(f"definition of {word}")
        return jsonify({'status': 'success', 'result': result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    return jsonify({
        'status': 'success',
        'history': conversation_history[-50:]
    }), 200

@app.route('/api/clear', methods=['POST'])
def clear_history():
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'success', 'message': 'History cleared'}), 200

if __name__ == '__main__':
    print(f"\n{'='*60}")
    print(f"  {chatbot.name}")
    print(f"  Version: {chatbot.version}")
    print(f"  Author: {chatbot.author}")
    print(f"  Created: {chatbot.created}")
    print(f"{'='*60}")
    print(f"Features: Math | Jokes | Dictionary | General Chat")
    print(f"Server: http://localhost:5000")
    print(f"Frontend: http://localhost:8000/simple_chat.html")
    print(f"{'='*60}\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
