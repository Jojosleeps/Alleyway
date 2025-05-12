from flask import Flask, render_template, request, redirect, url_for
import sys

msg = ("Welcome to the Book Selection!","Welcome to the Book Selection!")  

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
           optwhich=ord(int(optionwhich));
           if int(optwhich < 49 or optwhich > 53):
              print("Incorrrect response.");
              AskInfo();
           else:
               match(optionwhich):
                case "1":
                    whichfilename = str(input(msg[0]));
                case "2":
                    whichfilename = str(input(msg[1]));
                case "3":
                    whichfilename = str(input(msg[0]));
                case "4":
                    whichfilename = str(input(msg[1]));
                case "5":
                    print("Thank you");
                    sys.exit();

               whichfilename = whichfilename + ".doc";
               
        case default:
          print("We have a problem");
          sys.exit();

    
if __name__ == "__main__":
    main();
