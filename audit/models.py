
from audit import db


class Record(db.Model):

    __tablename__ = 'records'
    
    # primary key
    rec_id = db.Column(db.Integer, primary_key=True)   # primary id field; unique id for each record

    isbn = db.Column(db.String(64), nullable=True)     # id field; unique id for each user
    
    name = db.Column(db.String(1024), nullable=True)       # email field

    units = db.Column(db.Integer, nullable=True, default=0)           # this field will store the password hash

    publisher = db.Column(db.String(1024), default='', nullable=True, unique=False)

    # object initialization method
    def __init__(self, isbn=None, name=None, units=0, publisher=''):

        self.isbn = isbn
        self.name = name
        self.units = units if units is not None else 0
        self.publisher = publisher
        
    # string representation for this object
    def __repr__(self):
        return '<Record [%r, %r; Publisher: %r] >' % (self.isbn, self.name, self.publisher)
