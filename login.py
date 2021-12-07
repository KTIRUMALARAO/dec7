# from os import name
from flask import Flask,redirect,url_for,request
# from flask.wrappers import Request
app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))
@app.route('/seccess/<name>')
def success(name):
    return 'Hello  %s' % name


if __name__  =='__main__':
    app.run(debug=True)