import uuid

from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import select, delete

from backend.api.dependencies.db import Session_dp


class PGBase(AsyncAttrs, DeclarativeBase):
    '''
    Base class for all the `PostgreSQL` database tables.

    Include basic fields and methods.
    '''

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


    @classmethod
    async def create(cls, session: Session_dp, **kwargs):
        instance = cls(**kwargs)

        session.add(instance)
        await session.commit()

        return instance


    @classmethod
    async def all(cls, session: Session_dp):
        elems = await session.execute(select(cls))
        elems = elems.scalars().all()

        return elems
    
    @classmethod
    async def get(cls, session: Session_dp, field, value):
        stmt = select(cls).where(field == value)
        elem = await session.execute(stmt)

        elem = elem.scalars().first()

        return elem
    

    @classmethod
    async def delete(cls, session: Session_dp, id: uuid.UUID):
        stmt = delete(cls).where(cls.id == id)
        await session.execute(stmt)
        await session.commit()

        return 204
