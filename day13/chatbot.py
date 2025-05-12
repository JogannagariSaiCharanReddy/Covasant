from flask import Flask, render_template, request
from chatbot_langchain import conversation

app = Flask(__name__)

history=[]
@app.route("/", methods=["GET", "POST"])
def chat():
    result = ""
    query=''
    if request.method == "POST":
        query = request.form["query"]
        if query:
            result=conversation.run(query)

            history.append(dict(human=query,AI=result))
               
    return render_template("index.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)
