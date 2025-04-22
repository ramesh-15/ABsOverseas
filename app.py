from flask import Flask, send_from_directory

app = Flask(__name__,static_folder='abs')

@app.route('/')
def home():
    return send_from_directory(app.static_folder,'index.html')

@app.route('/about.html')
def about():
    return send_from_directory(app.static_folder,'about.html')

@app.route('/contact.html')
def contact():
    return send_from_directory(app.static_folder, 'contact.html')

@app.route('/services.html')
def services():
    return send_from_directory(app.static_folder, 'services.html')

@app.route('/blogs.html')
def blogs():
    return send_from_directory(app.static_folder, 'blogs.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

