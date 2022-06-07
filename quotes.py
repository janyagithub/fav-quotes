from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgresql123@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://lzalsusjjexoqs:d09d1e66ae9116f9679bd2fd32652ea7bd4b289fb4a5b6f03e50ea96082a1d24@ec2-34-247-172-149.eu-west-1.compute.amazonaws.com:5432/d6dqah5i1m6lt1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db=SQLAlchemy(app)

class Favquotes(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    author=db.Column(db.String(30))
    quote=db.Column(db.String(2000))


@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author, quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))
