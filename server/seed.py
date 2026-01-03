from app import app, db
from models import Message

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

        
        m1 = Message(username="Alice", body="Hello World!")
        m2 = Message(username="Bob", body="Hi there!")
        db.session.add_all([m1, m2])
        db.session.commit()

        print(" Database seeded with messages!")
