from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def showUser(username):
        return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/euler/<int:max_value>')
def do_multiple(max_value):
	#mulitply of 3 & 5
	
	total = 0
	number = 0
	
	while (number < max_value):
		if(number % 5 == 0 or number % 3 == 0):
			total += number
			
		number+=1			
	#print (allValues)
	return ("Sum of all Values is: %d " % total)
	
@app.route('/palindrome/<word>')
def do_paledrome(word):
	#print str #test to show the word
   return (str(word[::-1]))
  

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
