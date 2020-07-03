from flask import Flask , render_template,url_for
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None,post_id=None):
    # print(url_for('static',filename = 'grunt.ico'))
    return render_template("index.html",name=username,post_id=post_id)

# @app.route('/')
# def hello():
#     return "hello"

@app.route('/about')
def about():
    return render_template("about.html")    

@app.route('/blog')
def myblog():
    return "Welcome to my Blog"   

@app.route('/football')
def laliga():
    return "34 times Champions"     

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
    app.debug=True    