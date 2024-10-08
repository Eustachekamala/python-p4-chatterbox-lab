#!/usr/bin/env python3

from random import choice as rc

from faker import Faker # type: ignore

from app import app
from models import db, Message,User

fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    # Clear existing messages
    Message.query.delete()
    
    messages = []
    
    # Create a Faker instance
    fake = Faker()

    # Generate usernames
    usernames = [fake.first_name() for _ in range(4)]
    if "Duane" not in usernames:
        usernames.append("Duane")

    # Create messages with random users
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