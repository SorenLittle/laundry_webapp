import sqlalchemy.orm as orm
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy import (
    Column,
    Text,
)

from .meta import Base


class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'

    # COLUMNS

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    name = Column(
        Text, nullable=False, unique=True
    )

    # RELATIONSHIPS

    # one-many (users/appointments)
    appointments = orm.relationship(
        "Appointment",
        back_populates="user"
    )
