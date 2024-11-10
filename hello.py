from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def greet( name = None):
    return render_template('greet.html', name=name)

@app.route("/products/<id>/")
def products(id):
    return render_template('products.html', id=id)

# @app.route("/products/<id>/", methods=['GET', 'POST', 'PUT'])
# def products(id):
#     if request.method=='POST':
#         return "This is POST call"
    
#     elif request.method=='PUT':
#         return "This is PUT call"
    
#     else:
#         return render_template('products.html')

@app.route("/about-us/")
def aboutUs():
    return "<p> About Us </p>"

@app.route("/users/<username>/")
def userDetail(username):
    return f"<p> User {escape(username)}</p>"