from app import app #import app from __init__.py

#Decorator - something that modifies the function following it.  Used to register functions as callbacks for certain events.
@app.route('/') #Associates the given URL and the function.
@app.route('/index')
#So now whenever a web browser requests either of the URLs above Flask invokes this function and returns the value as a response.
def index():
    user = {'username': 'Marcus'} #dictionary of user names
    return '''

#Now complete the webpage with some HTML
<HTML>
    <head>
        <title> Home Page - Microblog</title>
    </head>
    <body>
        <h1> Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''