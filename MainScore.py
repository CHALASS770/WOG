from flask import Flask, render_template

class  MainScore :


    app = Flask(__name__)
    @app.route('/')

    def content():
        with open("score.txt", "r+") as f:
            content = f.read()
        return render_template("score.html", content=content)

    if __name__ == '__main__':
        app.run(debug = True,  host='0.0.0.0')