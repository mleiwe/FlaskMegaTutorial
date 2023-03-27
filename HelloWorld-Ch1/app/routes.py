from app import app #import app from __init__.py

@app.route('/')
@app.route('/index')

def index():
    return "Hello World!" #Returns a greeting as a string