#!/usr/bin/env python3

from random import choice as rc
from faker import Faker  # type: ignore
from app import app
from models import db, Message, User

# Initialize Faker
fake = Faker()

def make_messages():
    # Clear existing messages
    Message.query.delete()
    
    messages = []

    # Ensure 'Duane' is always included
    usernames = [fake.first_name() for _ in range(4)]
    if "Duane" not in usernames:
        usernames.append("Duane")

    # Create users if they don't exist
    for name in usernames:
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)

    # Commit users to the database
    db.session.commit()

    # Generate messages
    for _ in range(20):
        user_name = rc(usernames)
        user = User.query.filter_by(name=user_name).first()
        
        # Ensure the user exists before creating a message
        if user:
            message = Message(
                text=fake.sentence(),
                user_id=user.id,
            )
            messages.append(message)

    # Add and commit the new messages to the session
    db.session.add_all(messages)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_messages()
