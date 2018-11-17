from battleground import db

class Log(db.Model):
    __tablename__ = 'Log'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    json = db.Column(db.PickleType())    

    def __repr__(self):
        return '<Log %r>' % self.timestamp        

class Hash(db.Model):
    __tablename__ = 'Hash'
    id = db.Column(db.Integer, primary_key=True)
    func = db.Column(db.String, nullable=False) # hash func
    plain = db.Column(db.String, nullable=False) # plaintext
    hash = db.Column(db.String, nullable=False) # hash

    def __repr__(self):
        return '<Hash %r>' % self.hash

db.create_all()
