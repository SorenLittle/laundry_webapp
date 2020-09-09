import sqlalchemy.orm as orm
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Text,
)

from .meta import Base


class Appointment(Base):
    """ The SQLAlchemy declarative model class for an Appointment object. """
    __tablename__ = 'appointments'

    # COLUMNS

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    date = Column(
        Date,
        nullable=False,
    )

    hour = Column(
        Integer,
        nullable=False
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )

    machine_id = Column(
        Text,
        ForeignKey("machines.side"),
    )

    # RELATIONSHIPS

    # many-one (appointments/users)
    user = orm.relationship(
        "User",
        back_populates="appointments",
    )

    # many-one (appointments/machines)
    machine = orm.relationship(
        "Machine",
        back_populates="appointments",
    )
