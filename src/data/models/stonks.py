from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime, Float

from ..database import db
from ..mixins import CRUDModel

class Stonks(CRUDModel):
    __tablename__ = 'stonks'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    company = Column(String(60), nullable=False, index=False)
    short = Column(String(8), nullable=False, index=True)
    value = Column(Float, default = False)
    last_value = Column(Float, default = False)
    datum_insertu = Column(DateTime)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def find_by_prijmeni(prijmeni):
        return db.session.query(Stonks).filter_by(prijmeni = prijmeni).all()

