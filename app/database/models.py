from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Email(Base):

    __tablename__ = "emails"

    id = Column(
        Integer,
        primary_key=True
    )

    category = Column(String)

    raw_text = Column(Text)
    
class Tonnage(Base):

    __tablename__ = "tonnage"

    id = Column(
        Integer,
        primary_key=True
    )

    vessel_name = Column(String)

    vessel_size = Column(String)

    open_port = Column(String)

    open_date = Column(String)
    
class CargoVC(Base):

    __tablename__ = "cargo_vc"

    id = Column(
        Integer,
        primary_key=True
    )

    account_name = Column(String)

    cargo_name = Column(String)

    loading_port = Column(String)

    discharge_port = Column(String)

    laycan = Column(String)

    cargo_type = Column(String)
    
    
class CargoTC(Base):

    __tablename__ = "cargo_tc"

    id = Column(
        Integer,
        primary_key=True
    )

    account_name = Column(String)

    delivery_port = Column(String)

    redelivery_port = Column(String)

    duration = Column(String)

    laycan = Column(String)
    
class ReviewQueue(Base):

    __tablename__ = "review_queue"

    id = Column(
        Integer,
        primary_key=True
    )

    category = Column(String)

    confidence = Column(Integer)

    data = Column(Text)
    