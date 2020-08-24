import sqlalchemy.orm as orm
from sqlalchemy import (
    Column,
    Text,
)

from .meta import Base


class Machine(Base):
    """ The SQLAlchemy declarative model class for a Machine object. """
    __tablename__ = 'machines'

    # COLUMNS

    side = Column(
        Text,
        primary_key=True,
    )

    accepts = Column(
        Text,
        nullable=False
    )

    # RELATIONSHIPS

    # one-many (machines/appointments)
    appointments = orm.relationship(
        "Appointment",
        back_populates="machine"
    )
