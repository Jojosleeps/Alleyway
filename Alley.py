from flask import Flask, render_template, request, url_for

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])

@app.route('/',methods = ['GET','POST'])
def main():
    if request.method == 'GET':
       return render_template(".html")
       return render_template(".html")
    else:
        return GetInfo()
        return render_template('', , )
    

def GetInfo():
    global mylist
    global headings, data
    headings = ("","","","")
    period1 = request.form.get('' )
    course1 = request.form.get('' )
    teacher1 = request.form.get('')
    room1 = request.form.get('')
    period2 = request.form.get('')
    course2 = request.form.get('')
    teacher2 = request.form.get('')
    room2 = request.form.get('')
    period3 = request.form.get('')
    course3 = request.form.get('')
    teacher3 = request.form.get('')
    room3 = request.form.get('')
    period4 = request.form.get('')
    course4 = request.form.get('')
    teacher4 = request.form.get('')
    room4 = request.form.get('')

        data = (
        (, , , ),
        (, , , ),
        (, , , ),
        (, , , ),
        (, , , ),
        (, , , ),
        (, , , ),
        (, , , )
        )
    
    
  




if __name__ == "__main__":
    app.run();
