from dataclasses import dataclass
from typing import Optional

@dataclass
class SimulationMetrics:
    stability: float
    power_usage: float
    collision_status: bool
    timestamp: float = 0.0