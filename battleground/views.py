from battleground import app
from battleground.database import *
from flask import (
    render_template,
    redirect,
    request,
    url_for
)
from wartanker import *

@app.route('/')
def home():
    return redirect(url_for('base_decode'))

@app.route('/decode/base', methods=['GET', 'POST'])  
def base_decode():
    if request.method == 'POST':
        try:
            result, base = crypto.base_decode(request.form.get('enc'), question_base=True)
        except crypto.UnknownBaseError:
            return 'Unknown base'
        return str((result, base))
    return render_template('decode/base.html')
