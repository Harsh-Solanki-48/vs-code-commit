from flask import Flask, render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db = SQLAlchemy(app)

class Donation(db.Model):
   id = db.Column(db.Integer,primary_key=True)
   fname = db.Column(db.String(100) , nullable = False)
   lname = db.Column(db.String(100) , nullable = False)
   email = db.Column(db.String(100) , nullable = False)
   city = db.Column(db.String(100) , nullable = False)
   number = db.Column(db.INTEGER() , nullable = False)
   state = db.Column(db.String(100) , nullable = False)
   pincode = db.Column(db.INTEGER() , nullable = False)
   address = db.Column(db.String(100) , nullable = False)
   items = db.Column(db.String(500) , nullable = False)
   date_posted = db.Column(db.DateTime ,nullable=False,default=datetime.utcnow)

   def __repr__(self):
      return 'Donation '+str(self.id)

db.create_all()

#for index
@app.route('/')
def index():
   return render_template('index.html')

#for direct
@app.route('/direct.html', methods=['GET','POST'])
def direct():
   if request.method=='POST':
      post_fname = request.form['fname']
      post_lname = request.form['lname']
      post_email = request.form['email']
      post_city = request.form['city']
      post_number = request.form['number']
      post_state = request.form['state']
      post_pincode = request.form['pincode']
      post_address = request.form['address']
      post_items = request.form['items']
      new_post =Donation(fname=post_fname,lname=post_lname,email=post_email,city=post_city,number=post_number,state=post_state,pincode=post_pincode,address=post_address,items=post_items)
      db.session.add(new_post)
      db.session.commit()
      return redirect('/direct.html')
   else:
      # return render_template('posts.html',posts=all_posts)
      return render_template('direct.html')


#for indirect
@app.route('/indirect.html')
def indirect():
   return render_template('indirect.html')

#for games
@app.route('/games.html')
def games():
   return render_template('games.html')

#for frj
@app.route('/frj.html')
def frj():
   return render_template('frj.html')

#for facts
@app.route('/facts.html')
def facts():
   return render_template('facts.html')

#for riddles
@app.route('/riddles.html')
def riddles():
   return render_template('riddles.html')

#for jokes
@app.route('/jokes.html')
def jokes():
   return render_template('jokes.html')


#for articles
@app.route('/articles.html')
def articles():
   return render_template('articles.html')

#for game1
@app.route('/1.html')
def game1():
   return render_template('1.html')

#for game2
@app.route('/2.html')
def game2():
   return render_template('2.html')

#for game3
@app.route('/3.html')
def game3():
   return render_template('3.html')

#for game4
@app.route('/4.html')
def game4():
   return render_template('4.html')

#for game5
@app.route('/5.html')
def game5():
   return render_template('5.html')

#for game6
@app.route('/6.html')
def game6():
   return render_template('6.html')


#for game7
@app.route('/7.html')
def game7():
   return render_template('7.html')

#for game8
@app.route('/8.html')
def game8():
   return render_template('8.html')

#for game9
@app.route('/9.html')
def game9():
   return render_template('9.html')

@app.route('/admin@1907')
def admin():
   all_posts=Donation.query.order_by(Donation.date_posted).all()
   return render_template('admin.html',posts=all_posts)


if __name__ == "__main__" :
   app.run()