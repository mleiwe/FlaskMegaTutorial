from flask import render_template
from app import app #import app from __init__.py

#Decorator - something that modifies the function following it.  Used to register functions as callbacks for certain events.
@app.route('/') #Associates the given URL and the function.
@app.route('/index')
#So now whenever a web browser requests either of the URLs above Flask invokes this function and returns the value as a response.
def index():
    user = {'username': 'Marcus'} #dictionary of user names
    posts =[
        {
            'author': {'username':'Marcus'},
            'body': 'Advanced snuggles are my favourite'
        },
        {
            'author': {'username':'Caryn'},
            'body': 'My husband is the best husband ever'
        },
        {
            'author': {'username':'Marcus'},
            'body': 'I can make this say anything MUHAHAHAHAHA'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)