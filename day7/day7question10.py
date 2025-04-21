from flask import Flask,jsonify
from flask import render_template, request 
import os

app = Flask(__name__)

@app.route("/")         
def index():
    return share()
    
    
@app.route("/favicon.ico")  #http://localhost:5000/favicon.ico
def favicon():
    return app.send_static_file("favicon.ico")
    
    
@app.route("/updatefortoday", methods=['GET','POST'])    
def notepad():
    if request.method == 'POST':
        content = request.form.get("content", "ALL")
        with open("notepad.txt","a") as f:
            f.writelines(content)
        
        with open("notepad.txt","rt") as f:
            notepad=f.readlines()
            return  """
        <html>
            <head>
                <title>
                    clear
                </title>
                <a href="share">
                    share
                </a>
            </head>
            <body>
            
                <h3>
                    updated sucessfully
                </h3>
                
            </body>
        </html>
    
    
    """
            
        
        
    else:
        return """
  <!DOCTYPE html>
<html>
<head>
    <title>Give Env</title>
    <style>
        body {
            padding: 40px;
            text-align: center;
           }

        textarea {
            width: 80%;
            height: 300px;
            font-size: 16px;
            padding: 10px;
            resize: vertical;
        }

        input[type="submit"] {
            margin-top: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }

        a {
            display: block;
            margin-top: 20px;
            font-size: 16px;
            text-decoration: none;
            color: #3366cc;
        }
    </style>
</head>
<body>

    <form action="/updatefortoday" method="post">
        <textarea id="content" name="content" placeholder="Write something..."></textarea><br/>
        <input type="submit" value="Update" />
    </form>

    <a href="/share">Share</a>
    <a href="/clearnotepad">Clear Notepad</a>

</body>
</html>


        """
        
@app.route("/clearnotepad", methods=['GET'])        
def clearnotepad():
    with open("notepad.txt","w") as f:
        f.write("")
        
    return """
        <html>
            <head>
                <title>
                    clear
                </title>
                <a href="updatefortoday">
                    <-back
                </a>
            </head>
            <body>
            
                <h3>
                    cleared notepad
                </h3>
                
            </body>
        </html>
    
    
    """

@app.route("/share", methods=['GET'])        
def share():
    with open("notepad.txt","rt") as f:
        content=f.readlines()
        
        
    if content :
        return render_template("notepad.html",content=content)
    else:
        return """
                <html>
                    <head>
                        <title>
                            clear
                        </title>
                        <a href="updatefortoday">
                            click here to add something
                        </a>
                    </head>
                    <body>
                    
                        <h3>
                            nothing to show
                        </h3>
                        
                    </body>
                </html>
            
            
            """
               
        
    
    
    
    
if __name__=='__main__':
    app.run()