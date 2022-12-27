from flask import *
import random
import string
import time
app = Flask(__name__)


@app.route("/")
def hello_result():
    return render_template("urlshort.html")

URl_dict={}
shorturl = str()
@app.route('/',methods = ['POST'])  
def generateurl():
    Value=request.form['Value']
    mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    global shorturl
    shorturl ="".join(random.choices(mylist,k=5))
    URl_dict[shorturl] =  Value   
    return  "127.0.0.1:5000/"+shorturl 


@app.route('/<name>')
def hello_user(name):
    if name == shorturl: 
        URL = URl_dict[shorturl]
        return redirect(URL,code=302)
    else:        
        return  " Invalid Key " 

if __name__ =="__main__":
   app.run(debug=True)