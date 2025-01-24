from flask import Blueprint, render_template, request, redirect, url_for
import os
from app.utils import face_recognition, database_operations

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            file_path = os.path.join('data/faces', file.filename)
            file.save(file_path)
            face_recognition.add_face(file_path)
            return redirect(url_for('main.dashboard'))
    return render_template('upload.html')

@main.route('/dashboard')
def dashboard():
    attendance_logs = database_operations.get_attendance_logs()
    return render_template('dashboard.html', logs=attendance_logs)
