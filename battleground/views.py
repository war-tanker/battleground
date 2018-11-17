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
    # base data 
    base_data = {'labels': [], 'base16': [], 'base32': [], 'base64': [], 'base-error': []}
    base_data['labels'] = list(reversed([(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, 7)]))
    for label in base_data['labels']:
        for topic in ['base16', 'base32', 'base64', 'base-error']:
            base_data[topic].append(len(Log.query.filter_by(
                timestamp=label, 
                type=topic
            ).all()))
    return render_template('index.html', base_data=base_data)

@app.route('/api/encode/base', methods=['POST'])
def base_encode():
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

@app.route('/api/decode/base', methods=['POST'])  
def base_decode():
    try:
        query = request.form.get('enc')
        result, base = crypto.base_decode(query, question_base=True)
    except crypto.UnknownBaseError:
        newlog = Log(
            type='base-error',
            timestamp=datetime.now().strftime('%Y-%m-%d'),
            json={ 'query': query }
        )
        db.session.add(newlog)
        db.session.commit()
        return 'Unknown base'
    newlog = Log(
        type='base' + str(base),
        timestamp=datetime.now().strftime('%Y-%m-%d'),
        json={ 'query': query, 'result': result }
    )
    db.session.add(newlog)
    db.session.commit()
    return str((result, base))

@app.route('/api/encrypt/hash', methods=['POST'])
def hash_encrypt():
    hashfunc = request.form.get('hash')
    plain = request.form.get('plain')
    if hashfunc == 'md5':
        result = hash.md5encode(plain)  
    elif hashfunc in ['sha1', 'sha256', 'sha384', 'sha512']:
        result = hash.sha_encode(int(hashfunc.replace('sha', '')), plain)
    else:
        return 'Unknown hash function'            
    
    newlog = Log(
        type=hashfunc,
        timestamp=datetime.now().strftime('%Y-%m-%d'),
        json={ 'query': plain, 'result': result }
    )
    db.session.add(newlog)
    db.session.commit()
    
    newhash = Hash(plain=plain, hash=result, func=hashfunc)
    db.session.add(newhash)
    db.session.commit()
    return result

@app.route('/api/decrypt/hash', methods=['POST'])
def hash_decrypt():
    q_func = request.form.get('func')
    if q_func not in ['sha1', 'sha256', 'sha384', 'sha512' ,'md5']:
        return 'Unknown hash function'
    q_hash = request.form.get('hash')
    # query plaintext with func, hash
    result = Hash.query.filter_by(func=q_func, hash=q_hash).first()
    if not result:
        return 'Not in DB'
    return result.plain

@app.route('/api/web/post', methods=['POST'])
def post_data():
    return web.post(
        url=request.form.get('url'), 
        json=request.form.get('json'), 
        data=request.form.get('data')
    )

@app.route('/api/pwn/terminal', methods=['POST'])
def terminal_run():
    command = request.form.get('cmd')
    print (pwnable.terminal(command))
    return pwnable.terminal(command)

@app.route('/<cate>/<menu>')
def show_form(cate=None, menu=None):
    return render_template('form.html', title=cate+'-'+menu)
