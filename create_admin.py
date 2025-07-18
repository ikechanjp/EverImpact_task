from app import app
from models import db, User
from werkzeug.security import generate_password_hash

ADMIN_EMAIL = "noriyoshi.ikeda@gmail.com"
ADMIN_PASSWORD = "nori5592"

with app.app_context():
    if not User.query.filter_by(email=ADMIN_EMAIL).first():
        admin = User(
            username="admin",
            email=ADMIN_EMAIL,
            password=generate_password_hash(ADMIN_PASSWORD),
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("管理者ユーザーを作成しました")
    else:
        print("すでに管理者ユーザーは存在します")
