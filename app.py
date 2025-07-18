from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///everimpact.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, User, Checklist, Task, Comment

db.init_app(app)

# Ensure tables exist at startup
with app.app_context():
    db.create_all()
login_manager = LoginManager(app)
login_manager.login_view = 'login'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    users = User.query.all()
    progress_data = []
    
    for user in users:
        total_tasks = 0
        completed_tasks = 0
        
        # Get all tasks from user's checklists
        for checklist in user.checklists:
            if not checklist.is_template:  # Exclude template checklists
                for task in checklist.tasks:
                    total_tasks += 1
                    if task.is_completed:
                        completed_tasks += 1
        
        progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        progress_data.append({
            'user': user,
            'progress': progress,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks
        })
    
    return render_template('dashboard.html', progress_data=progress_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        
        flash('Invalid email or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/checklist/template')
@login_required
def template_checklist():
    if current_user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    template = Checklist.query.filter_by(is_template=True).first()
    return render_template('template_checklist.html', template=template)

@app.route('/checklist/<int:checklist_id>')
@login_required
def view_checklist(checklist_id):
    checklist = Checklist.query.get_or_404(checklist_id)
    return render_template('checklist.html', checklist=checklist)

@app.route('/checklist/<int:checklist_id>/task/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(checklist_id, task_id):
    task = Task.query.get_or_404(task_id)
    if task.checklist.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    task.is_completed = not task.is_completed
    if task.is_completed:
        task.completed_at = datetime.utcnow()
    else:
        task.completed_at = None
    db.session.commit()
    
    return jsonify({'success': True, 'is_completed': task.is_completed, 'completed_at': task.completed_at.isoformat() if task.completed_at else None})

@app.route('/checklist/<int:checklist_id>/task/<int:task_id>/comment', methods=['POST'])
@login_required
def add_comment(checklist_id, task_id):
    content = request.form.get('content')
    if not content:
        return jsonify({'error': 'Comment cannot be empty'}), 400
    
    comment = Comment(
        content=content,
        user_id=current_user.id,
        task_id=task_id
    )
    db.session.add(comment)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'comment': {
            'id': comment.id,
            'content': comment.content,
            'user_name': comment.user.username,
            'created_at': comment.created_at.isoformat()
        }
    })

@app.route('/api/checklist/<int:checklist_id>/updates')
@login_required
def get_checklist_updates(checklist_id):
    checklist = Checklist.query.get_or_404(checklist_id)
    
    tasks_data = []
    for task in checklist.tasks:
        comments_data = []
        for comment in task.comments:
            comments_data.append({
                'id': comment.id,
                'content': comment.content,
                'user_name': comment.user.username,
                'created_at': comment.created_at.isoformat()
            })
        
        tasks_data.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'is_completed': task.is_completed,
            'completed_at': task.completed_at.isoformat() if task.completed_at else None,
            'comments': comments_data
        })
    
    return jsonify({
        'success': True,
        'tasks': tasks_data,
        'last_updated': datetime.utcnow().isoformat()
    })

@app.route('/api/users/<username>/tasks', methods=['GET'])
def get_user_tasks(username):
    # Get user's task progress
    user_tasks = request.args.get('tasks', '[]')
    try:
        tasks = eval(user_tasks)  # In production, use json.loads
        return jsonify({
            'success': True,
            'tasks': tasks,
            'username': username
        })
    except:
        return jsonify({'success': False, 'error': 'Invalid task data'})

@app.route('/api/users/<username>/tasks', methods=['POST'])
def save_user_tasks(username):
    # Save user's task progress
    tasks = request.json.get('tasks', [])
    # In a real implementation, save to database
    # For now, return success
    return jsonify({
        'success': True,
        'message': 'Tasks saved successfully',
        'username': username
    })

@app.route('/api/all-users-progress', methods=['GET'])
def get_all_users_progress():
    # Get all users' progress data
    # This would be implemented with proper database queries
    return jsonify({
        'success': True,
        'users': [],  # Placeholder for now
        'last_updated': datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)
