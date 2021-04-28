from typing import ClassVar
from flask import Flask,render_template,request,redirect


app=Flask(__name__)
persons=[]
class Person():
    def __init__(self,_name,_surname,_email):
        self.ad=_name
        self.soyad=_surname
        self.email=_email


showData='show page data'
addData={
    'title':'Add Page',
    'content':'Lorem ipsum dolor sit amet',
}
contactData='contact page data'
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        _ad=request.form['ad']
        _soyad=request.form['soyad']
        _email=request.form['email']
        user=Person(_ad,_soyad,_email)
        return redirect('/add')
        return render_template('show.html',person=persons)

if __name__=='__main__':
    app.run(debug=True)