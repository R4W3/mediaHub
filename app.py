from flask import Flask, render_template
from flask_compress import Compress
from music_lib import music

app = Flask(__name__)
app.secret_key = "dfsgjl646385sädjkgjhhöalosdhhtas"
Compress(app)


@app.route("/")
def homepage():
    m_lib = music

    return render_template("/index/index.html", m_lib=m_lib)


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
