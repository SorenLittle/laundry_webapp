from sqlalchemy import (
    Column,
    Text,
    Date,
)

from .meta import Base


class RightAppt(Base):
    """ The SQLAlchemy declarative model class for a RightAppt object. """
    __tablename__ = 'right_appts'

    # COLUMNS

    date = Column(
        Date,
        primary_key=True,
    )

    seven = Column(
        Text
    )
    eight = Column(
        Text
    )
    nine = Column(
        Text
    )
    ten = Column(
        Text
    )
    eleven = Column(
        Text
    )
    twelve = Column(
        Text
    )
    thirteen = Column(
        Text
    )
    fourteen = Column(
        Text
    )
    fifteen = Column(
        Text
    )
    sixteen = Column(
        Text
    )
    seveteen = Column(
        Text
    )
    eighteen = Column(
        Text
    )
    nineteen = Column(
        Text
    )
    twenty = Column(
        Text
    )
    twentyone = Column(
        Text
    )
    twentytwo = Column(
        Text
    )
    twentythree = Column(
        Text
    )
