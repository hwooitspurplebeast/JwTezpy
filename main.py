from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.form['input_data']
    with open('test.txt', 'w') as file:
        file.write(data)
    return 'Data saved successfully!'

if __name__ == '__main__':
    app.run(debug=True)
