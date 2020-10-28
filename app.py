from flask import Flask, render_template
import os

app = Flask(__name__)


#def root_dir():  # maybe this sets the root directory?
    #return os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/static')
def secondary():
    return render_template('index.html')
app.run()

#app.run()
#if __name__=='__main__':
#app.run(host='127.0.0.1',port=5100)