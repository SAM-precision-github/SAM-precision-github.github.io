from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='', 
            )

@app.route('/')
def home():
   return render_template('index.html')

from flask import send_from_directory

@app.route('/')
def send_report(path):
    return send_from_directory('reports', path)

if __name__ == '__main__':
   app.run(debug=True)