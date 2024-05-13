from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
basedir = os.path.abspath(os.path.dirname(__file__))
# 絶対パスを使用してデータベースURIを設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'reservations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    __tablename__ = 'reservation'  # 明示的にテーブル名を指定
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)

@app.route('/')
def index():
    # テーブルが存在しない場合、作成
    db.create_all()
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    date = request.form['date']
    new_reservation = Reservation(name=name, date=date)
    db.session.add(new_reservation)
    db.session.commit()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return '予約が完了しました！'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)


