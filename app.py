from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ravi')
def resume():
    return send_from_directory('.', 'ravi_resume.pdf')  # Replace 'your_resume.pdf' with your actual resume filename

if __name__ == '__main__':
    app.run(debug=True)
