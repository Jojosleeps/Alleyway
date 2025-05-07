from flask import Flask, render_template, request, redirect, url_for

msg = ("Welcome to the Kids Books selection!","Welcome to the Student Books selection!")  

def main():
    AskInfo();

def AskInfo():
    checkpoint = "askinfo";
    whichoption = str(input("1 - Kids Books\n"
                            "2 -  Students Books\n"
                            "3 - Exit \n"
                            "Select an option by typing 1,2 or 3: "));
    CheckInfo(whichoption,checkpoint);

def CheckInfo(optionwhich,pointcheck):
    global whichfilename;
    match(pointcheck):
        case"askinfo":
           optwhich=ord(optionwhich);
           if(optwhich < 49 or optwhich > 51):
              print("Incorrrect response.");
              AskInfo();
           else:
               match(optionwhich):
                case "1":
                    whichfilename = str(input(msg[0]));
                case "2":
                    whichfilename = str(input(msg[1]));
                case "3":
                    print("Thank you");
                    sys.exit();

               whichfilename = whichfilename + ".doc";
               
        case default:
          print("We have a problem");
          sys.exit();



    
if __name__ == "__main__":
    main();
