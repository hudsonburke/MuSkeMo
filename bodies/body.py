
from dataclasses import dataclass
from mathutils import Vector
from ..inertial import Inertial

@dataclass(slots=True)
class Body:
    name: str
    inertial: Inertial
    collection: str | None = None
    scale: Vector = Vector((1.0, 1.0, 1.0))
    

