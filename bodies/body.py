from dataclasses import dataclass
from mathutils import Matrix, Vector
from ..inertial import Inertial
import bpy


@dataclass(slots=True)
class Body:
    name: str
    inertial: Inertial
    scale: Vector = Vector((1.0, 1.0, 1.0))


def body_from_object(obj: bpy.types.Object) -> Body:
    """Create a Body instance from a Blender object."""
    name = obj.name
    inertial = Inertial(
        mass=obj.rigid_body.mass if obj.rigid_body else 0.0,
        pos=obj.location.copy(),
        quat=obj.rotation_quaternion.copy(),
        diaginertia=obj.rigid_body.inertia
        if obj.rigid_body
        else Vector((0.0, 0.0, 0.0)),
        fullinertia=obj.rigid_body.inertia_tensor
        if obj.rigid_body
        else Matrix.Identity(3),
    )
    scale = obj.scale.copy()

    return Body(name=name, inertial=inertial, scale=scale)
