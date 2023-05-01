from flask import Flask, render_template, request 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form['number1'])
        num2 = int(request.form['number2'])
        operation = request.form.get('operation')
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        return render_template('result.html', result=result)
    return render_template('calculator.html')


@app.route('/result')
def res():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
