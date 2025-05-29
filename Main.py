from flask import Flask, render_template, request, redirect, url_for
import os.path
from os import path

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def file():
    if request.method == "GET":
        return render_template("Main.html")
    else:
        main()
    

msg =["Welcome!","Bye Bye!"]
def main(): 
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption = str(input("1 -  Science Books\n"
                            "2 -  Mathematic Books\n"
                            "3 -  History Books\n"
                            "4 -  English Books \n"
                            "5 - Exit \n"
                            "Select an option by typing 1,2,3,4 or 5: "));
    CheckInfo(whichoption,checkpoint);

def CheckInfo(optionwhich,pointcheck):
    global whichfilename;
    match(pointcheck):
        case"askinfo":
           optwhich = ord(str(optionwhich));
           if (int(optwhich)) < int(49) or int((optwhich) > int(53)):
              print("Incorrrect response. Type 1 to 5");
              AskInfo();
           else:
               if(optwhich == 1):
                   whichfilename = str(input(msg[1]));
                   print("You have selected wise!");
               else:
                   whichfilename = str(input(msg[0]));
        case default:
            print("We have a problem");

    whichfilename = whichfilename + ".doc";
    FileConnectivity();

    
def FileConnectivity():
    flieDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));

    if(fileexist == True):
        adminfile = open(whichfilename,"r");
    else:
        adminfile = open(whichfilename,"x");

    adminfile.close();

if __name__ == "__main__":
    main();
    app.run()
