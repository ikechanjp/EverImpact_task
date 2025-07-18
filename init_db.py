from app import app
from models import db, User, Checklist, Task, Comment

# Create database tables
def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
