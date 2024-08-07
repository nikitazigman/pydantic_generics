from dataclasses import dataclass
from datetime import datetime


@dataclass
class Subscription:
    id: str
    expiration: datetime