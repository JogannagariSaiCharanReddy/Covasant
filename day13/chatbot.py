from flask import Flask, render_template, request
from chatbot_langchain import conversation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    result = ""
    history = []
    if request.method == "POST":
        query = request.form["query"]
        result = conversation.predict(input=query)
        history = conversation.memory.buffer.split("\n")
    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    app.run(debug=True)
