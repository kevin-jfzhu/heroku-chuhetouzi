from root.utils import app, render_template


"""---------------------------------  Pages & Router Definition ---------------------------------"""


# @app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/dashboard', methods=['GET'])
@app.route('/dashboard.html', methods=['GET'])
def dashbaord():
    return render_template('dashboard.html')


@app.route('/register', methods=['GET'])
@app.route('/register.html', methods=['GET'])
def register():
    return render_template('register.html')


@app.route('/forgot-password', methods=['GET'])
@app.route('/forgot-password.html', methods=['GET'])
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/login', methods=['GET'])
@app.route('/login.html', methods=['GET'])
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
@app.route('/products', methods=['GET'])
@app.route('/products.html', methods=['GET'])
def products():
    return render_template('products.html')


@app.route('/strategies', methods=['GET'])
@app.route('/strategies.html', methods=['GET'])
def strategies():
    return render_template('strategies.html')
