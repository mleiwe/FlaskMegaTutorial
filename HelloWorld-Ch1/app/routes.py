from app import app #import app from __init__.py

#Decorator - something that modifies the function following it.  Used to register functions as callbacks for certain events.
@app.route('/') #Associates the given URL and the function.
@app.route('/index')
#So now whenever a web browser requests either of the URLs above Flask invokes this function and returns the value as a response.
def index():
    return "Hello World!" #Returns a greeting as a string