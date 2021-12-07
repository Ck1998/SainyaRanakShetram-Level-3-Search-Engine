from flask import Flask
from flask import request
from json import dumps
app = Flask(__name__)


@app.route("/search", methods=['POST'])
def search():
    query = request.form.get("Q")
    # call search api
    return {"count": 12132, "query": query}


if __name__ == "__main__":
    app.run()
