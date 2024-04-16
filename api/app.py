from flask import Flask, render_template, request, redirect, url_for, Blueprint

app = Flask(__name__)

main_bp = Blueprint('main', __name__)
upload_bp = Blueprint('upload', __name__)
options_bp = Blueprint('options', __name__)

@main_bp.route('/')
def main():
    return render_template('main.html')

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        dataset = request.get_data("file")
        print(dataset)
        return redirect(url_for('options.options'))
    return render_template('upload.html')

@options_bp.route('/options')
def options():
    return render_template('options.html')

app.register_blueprint(main_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(options_bp)

if __name__ == '__main__':
    app.run(debug=True)