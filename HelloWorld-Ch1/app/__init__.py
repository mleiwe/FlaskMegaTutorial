# This script creates the application object as an instance of class 'Flask' imported from the flask package.
# __name__ - a variable passed to the Flask class as a Python pre-defined variable, which is set to the name of the module used
# Flask uses the location module passed here as a starting point when it needs to load associated resources such as template files


from flask import Flask

app = Flask(__name__)

from app import routes 
#the app then imports the routes module which doesn't exist yet
#This is done as a workaround to circular imports (a common problem in Flask applications)
#routes is a module which are the different URLs the application implements.
#In Flask, handlers for application routes are written as Python functions, known as "view functions"
#View functions are mapped onto one or more route URLs so Flask knows what logic to execute when a client requests a given URL
