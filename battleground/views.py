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
    pass
