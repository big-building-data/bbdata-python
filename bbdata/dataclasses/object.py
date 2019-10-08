from dataclasses import dataclass
from .owner import Owner
from .tags import Tags
from .unit import Unit


@dataclass
class Object:
    creation_date: str
    description: str
    id: int
    name: str
    owner: Owner
    tags: Tags
    unit: Unit



