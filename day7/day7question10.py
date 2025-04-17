from flask import Flask,jsonify
from flask import render_template, request 
import os

app = Flask(__name__)

@app.route("/")         
def index():
    return share()
    
@app.route("/updatefortoday", methods=['GET','POST'])    
def notepad():
    if request.method == 'POST':
        content = request.form.get("content", "ALL")
        with open("notepad.txt","a") as f:
            f.writelines(content+"\n")
        
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
    <html><head>
    <title>Give Env</title>
    </head>
    <body>
        <form action="/updatefortoday" method="post">
        Enter text:
        <br/>
        <textarea name="content" cols="40" rows="5"></textarea>
        <br/>
        <input type="submit" value="update" />
        </form>
        <br/>
        <a href="/share">share<a/>
        <br/>
        <a href="/clearnotepad">clear notepad<a/>
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