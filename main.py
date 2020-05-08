from flask import Flask, render_template
from data import db_session
from data.users import User
import os
from data.jobs import Jobs

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = "First task"
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    title = 'Second task'
    return render_template('base2.html', title=title, prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    title = 'Third task'
    return render_template('base3.html', title=title, list=list)


if __name__ == '__main__':

    db_session.global_init()
    session = db_session.create_session()
    if not session.query(User).first():
        import fill_base

    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
