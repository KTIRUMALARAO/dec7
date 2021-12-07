from os import name
from flask import Flask,redirect,url_for
app = Flask(__name__)

# @app.route('/')
def hello():
    return 'Hello_world'
app.add_url_rule('/', 'home',hello)

def hello_a():
    return 'Hello_world good morning'
app.add_url_rule('/a','a',hello_a)


@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s' % name
# app.add_url_rule('/hello/<name>','name',hello_name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    if type(postID):
        return 'Blog Number %d' % postID
    else:
        return 'Invalid type'
    
# @app.route('/python')
# def hello_python():
#    return 'Hello Python'

@app.route('/python/')
def hello_python_pro():
   return 'Hello Python  m'

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello %s as guest ' % guest


if __name__  =='__main__':
    app.run(debug=True)