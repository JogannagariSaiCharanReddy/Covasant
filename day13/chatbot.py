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
        
        history = []
        for msg in conversation.memory.chat_memory.messages:
            current_conv={}
            if msg.type == "human":
                current_conv["User"]= msg.content
            elif msg.type == "ai":
                lines = msg.content.strip().split('\n')
                for line in lines:
                    if "AI" not in current_conv:
                        current_conv["AI"]=[line.strip()]
                    else:
                        current_conv["AI"].append(line.strip())
            history.append(current_conv)

        print(history)

    return render_template("index.html", result=result, history=history)

if __name__ == "__main__":
    app.run(debug=True)
