from battleground import db

class Log(db.Model):
    __tablename__ = 'Log'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String, nullable=False)
    type = db.Column(db.String, unique=True, nullable=False)
    json = db.Column(db.PickleType())    

    def __repr__(self):
        return '<Log %r>' % self.timestamp        

db.create_all()
