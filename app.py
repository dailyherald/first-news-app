from flask import Flask
from flask import render_template # combines data with html to make a webpage

#---------
app = Flask(__name__) # variable app = Flask(name of file)

@app.route("/") # tells variable app to set root route for the app

# Function that returns a rendered index.html (must have an index.html to return)
def index():
	# variable template equals index.html
    template = 'index.html'
    # tell function to read that file with render_template
    return render_template(template)

# Sets up the server on localhost:5000
if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)