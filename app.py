from flask import Flask , render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index2.html')
def index2():
    return render_template('index2.html')

@app.route('/final_index.html')
def final_index():
    return render_template('final_index.html')
@app.route('/index3.html')
def index3():
    return render_template('index3.html')
@app.route('/index4.html')
def index4():
    return render_template('index4.html')
@app.route('/final_final_index.html')
def final_final_index():
    return render_template('final_final_index.html')

@app.route('/final_achi_index.html')
def final_achi_index():
    return render_template('final_achi_index.html')

@app.route('/final_final_final_index.html')
def final_final_final_index():
    return render_template('final_final_final_index.html')

# Run the app only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
