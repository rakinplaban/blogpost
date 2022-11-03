from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'title' : "Blogpost 1",
        'author' : "Jhon Doe",
        'date_posted' : "20 April, 2022",
        'content' : "First Blog post" 
    },
    {
        'title' : "Blogpost 2",
        'author' : "Alice Chan",
        'date_posted' : "25 April, 2022",
        'content' : "Second Blog post" 
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/new_route")
def new_route():
    return render_template('about.html',title='About')


if __name__ == '__main__':
    app.run(debug=True)