import os
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    print(os.getenv('APP_LOCALE'))
    user = {'username': 'Germán'}
    files = [
        {
            'properties': {'hash': '1234123412341234'},
            'name': 'try.txt'
        },
        {
            'properties': {'hash': '1234123412341234'},
            'name': 'try2.txt'
        }
    ]
    return render_template('index.html', title='Index', user=user, files=files)
