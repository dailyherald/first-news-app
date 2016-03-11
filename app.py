import csv
from flask import Flask
from flask import render_template # combines data with html to make a webpage
#---------
app = Flask(__name__) # variable app = Flask(name of file)


# loads data source
def get_csv(csv_path):
	# period in a path says start where you currently are
    csv_file = open(csv_path, 'rb') # opens the the data r = read; rb = read binary (windows)
    csv_obj = csv.DictReader(csv_file) # parses the csv into a python object, if data has headers
    csv_list = list(csv_obj) # reads that into a list, which makes it permenant
    return csv_list


@app.route("/") # tells variable app to set root route for the app

# Function that returns a rendered index.html (must have an index.html to return)
def index():
	# variable template equals index.html
    template = 'index.html'
    # Below grabs the get csv and includes it in the html
    object_list = get_csv('./static/la-riots-deaths.csv')
    return render_template(template, object_list=object_list)

# Sets up the server on localhost:5000
if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)