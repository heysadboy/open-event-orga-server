from . import db


class CallForPaper(db.Model):
    """call for paper model class"""
    __tablename__ = 'call_for_papers'
    id = db.Column(db.Integer, primary_key=True)
    announcement = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, announcement=None, start_date=None, end_date=None):
        self.announcement = announcement
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return '<call_for_papers %r>' % self.announcement

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return self.name

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {'id': self.id,
                'announcement': self.announcement,
                'start_date':self.start_date,
                'end_date':self.end_date}