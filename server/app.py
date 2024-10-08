from flask import Flask, request, jsonify, make_response  # type: ignore
from flask_cors import CORS  # type: ignore
from flask_migrate import Migrate  # type: ignore
from models import db, Message, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to the Chatterbox API</h1>'

@app.route('/messages', methods=['GET'])
def messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages]), 200

@app.route('/messages', methods=['POST'])
def messages_post():
    message_data = request.json
    if 'text' not in message_data or 'user_id' not in message_data:
        return make_response(jsonify({"error": "Invalid input"}), 400)
    
    new_message = Message(
        text=message_data['text'],
        user_id=message_data['user_id']
    )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201


@app.route('/messages/<int:id>', methods=['GET'])
def messages_by_id(id):
    message = Message.query.get(id)
    if message:
        return jsonify(message.to_dict()), 200
    return make_response(jsonify({"error": "Message not found"}), 404)

@app.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users', methods=['POST'])
def users_post():
    user = request.json
    if 'name' not in user:
        return make_response(jsonify({"error": "Invalid input"}), 400)
    new_user = User(name=user['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:id>', methods=['GET'])
def users_by_id(id):
    user = User.query.get(id)
    if user:
        return jsonify(user.to_dict()), 200
    return make_response(jsonify({"error": "User not found"}), 404)

@app.route('/messages/<int:id>', methods=['DELETE'])
def messages_by_id_delete(id):
    message = Message.query.get(id)
    if message:
        db.session.delete(message)
        db.session.commit()
        return jsonify({"message": "Message deleted"}), 200
    return make_response(jsonify({"error": "Message not found"}), 404)

@app.route('/messages/<int:id>', methods=['PATCH'])
def messages_by_id_patch(id):
    message = Message.query.get(id)
    if message:
        data = request.json
        if 'text' not in data:
            return make_response(jsonify({"error": "Invalid input"}), 400)
        message.text = data['text']
        db.session.commit()
        return jsonify(message.to_dict()), 200
    return make_response(jsonify({"error": "Message not found"}), 404)

@app.route('/users/<int:id>', methods=['DELETE'])
def users_by_id_delete(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    return make_response(jsonify({"error": "User not found"}), 404)

if __name__ == '__main__':
    app.run(port=5555)
