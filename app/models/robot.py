from dataclasses import dataclass
from typing import List, Optional

@dataclass
class RobotState:
    x: float
    y: float
    orientation: float
    timestamp: float = 0.0

@dataclass
class JointState:
    name: str
    position: float
    velocity: float = 0.0
    effort: float = 0.0

@dataclass
class JointStates:
    names: List[str]
    positions: List[float]
    velocities: List[float]
    timestamp: float = 0.0

    @classmethod
    def from_joint_states(cls, joints: List[JointState]) -> 'JointStates':
        return cls(
            names=[j.name for j in joints],
            positions=[j.position for j in joints],
            velocities=[j.velocity for j in joints],
            timestamp=0.0
        )