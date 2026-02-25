
from dataclasses import dataclass
from mathutils import Vector, Quaternion, Matrix

@dataclass(slots=True)
class Inertial:
    mass: float
    pos: Vector
    quat: Quaternion
    diaginertia: Vector
    fullinertia: Matrix