from flask import Flask, render_template, url_for, request

app = Flask('__name__')


@app.route('/index')
@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('contact.html')
    return render_template('index.html')


@app.route('/contact')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('contact.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
