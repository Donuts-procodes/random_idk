from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')

@app.route("/main")
def main():
    return render_template('main.html')

if __name__ == '__main__':
	#DEBUG is SET to TRUE. CHANGE FOR PROD
	app.run(port=5000,debug=True)