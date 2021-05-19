from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
# print(__name__)

def write_to_file(data):
	with open('contactdb.txt', mode='a') as filedb:
		email = data['email']
		subject = data['subject']
		message = data['message']
		filedb.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('contactdb.csv', 'a', newline='') as csvdb:
		email=data['email']
		subject=data['subject']
		message=data['message']
		csv_writer = csv.writer(csvdb,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/')
def hello_world():
    # return "Hello World"
    return render_template("index.html")

@app.route('/')
def home():
    # return "Hello World"
    return render_template("index.html")
    print("Test")

@app.route('/<string:page_name>')
def html_pages(page_name):
	return render_template(page_name)

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		write_to_file(data)
		write_to_csv(data)
		print (data)
	return redirect('/thanks.html')

# @app.route('/works.html')
# def works():
#     return render_template("works.html")

# @app.route('/work.html')
# def work():
#     return render_template("work.html")

# @app.route('/index.html')
# def index():
#     # return "Hello World"
#     return render_template("index.html")
#     print("Test")

# @app.route('/about.html')
# def about():
#     # return "Hello World"
#     return render_template("about.html")
#     print("Test")

# @app.route('/contact.html')
# def contact():
#     # return "Hello World"
#     return render_template("contact.html")
#     print("Test")

# @app.route('/components.html')
# def components():
#     # return "Hello World"
#     return render_template("components.html")
#     print("Test")