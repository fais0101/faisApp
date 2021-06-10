
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/Dude')
def hello_world():
   print("Im printing..", flush=True)
   return render_template('learningjs.html')

@app.route('/Dudett')
def hello_dudett():
   return 'Hello Dudett'

if __name__ == '__main__':
   app.run()