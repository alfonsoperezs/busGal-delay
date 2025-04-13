from __future__ import annotations

from sqlmodel import Session, select
from models import Delay

def insert_delay(session: Session, delay: Delay) -> Delay | None:
    statement = select(Delay).where(Delay.id == delay.id)
    result = session.exec(statement).first()
    if result is None:
        session.add(delay)
        session.commit()
        session.refresh(delay)
        return delay
    else:
        return None

def find_delays(session: Session) -> list[Delay] | None:
    statement = select(Delay)
    result = session.exec(statement).all()
    return result if result else None