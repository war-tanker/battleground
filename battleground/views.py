from battleground import app
from battleground.database import *
from flask import (
    render_template,
    redirect,
    request,
    url_for
)
from wartanker import *
from datetime import date, datetime, timedelta

@app.route('/')
def home():
    today = date.today()
    base_data = {'labels': [], 'base16': [], 'base32': [], 'base64': []}
    base_data['labels'] = list(reversed([(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, 7)]))
    for label in base_data['labels']:
        for topic in ['base16', 'base32', 'base64']:
            base_data[topic].append(len(Log.query.filter_by(
                timestamp=label, 
                type=topic
            ).all()))
    return render_template('main.html', base_data=base_data)

@app.route('/decode/base', methods=['GET', 'POST'])  
def base_decode():
    if request.method == 'POST':
        try:
            query = request.form.get('enc')
            result, base = crypto.base_decode(query, question_base=True)
        except crypto.UnknownBaseError:
            return 'Unknown base'
        newlog = Log(
            type='base' + str(base),
            timestamp=datetime.now().strftime('%Y-%m-%d'),
            json={ 'query': query, 'result': result }
        )
        db.session.add(newlog)
        db.session.commit()
        return str((result, base))
    return render_template('decode/base.html')

@app.route('encode/base', methods=['GET', 'POST'])
def base_encode():
    if request.method == 'POST':
        base = int(request.form.get('base'))
        plain = request.form.get('plain')
        result = crypto.base_encode(base, plain)

        newlog = Log(
            type='base' + str(base),
            timestamp=datetime.now().strftime('%Y-%m-%d'),
            json={ 'query': plain, 'result': result }
        )
        db.session.add(newlog)
        db.session.commit()

        return result
    return render_template('encode/base.html')

@app.route('encrypt/hash', methods=['GET', 'POST'])
def hash_encrypt():
    if request.method == 'POST':
        hashfunc = request.form.get('hash')
        plain = request.form.get('plain')
        if hashfunc not in []:
            return 'No'
        else: 
            result = ''
        newlog = Log(
            type=hashfunc,
            timestamp=datetime.now().strftime('%Y-%m-%d'),
            json={ 'query': plain, 'result': result }
        )
        db.session.add(newlog)
        db.session.commit()
        
        newhash = Hash(plain=plain, hash=result)
        db.session.add(newhash)
        db.session.commit()
        return result
    return render_template('encrypt/hash')
    