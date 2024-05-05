from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 絶対パスでデータベースを指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hide/Desktop/App/20240501_ReservationSite/reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)

@app.route('/')
def index():
    # テーブルが存在しない場合、作成
    db.create_all()
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)


