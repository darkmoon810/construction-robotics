import roslibpy
from typing import Optional

class ROSBridge:
    def __init__(self, host: str = 'localhost', port: int = 9090):
        self.client = roslibpy.Ros(host=host, port=port)
        self.odometry_listener = None
        self.joint_states_listener = None
        self.metrics_listener = None

    def connect(self) -> bool:
        self.client.run()
        return self.client.is_connected

    def disconnect(self):
        self.client.terminate()

    def subscribe_to_odometry(self, callback):
        self.odometry_listener = roslibpy.Topic(
            self.client,
            '/robot/odometry',
            'nav_msgs/Odometry'
        )
        self.odometry_listener.subscribe(callback)

    def subscribe_to_joint_states(self, callback):
        self.joint_states_listener = roslibpy.Topic(
            self.client,
            '/robot/joint_states',
            'sensor_msgs/JointState'
        )
        self.joint_states_listener.subscribe(callback)

    def subscribe_to_metrics(self, callback):
        self.metrics_listener = roslibpy.Topic(
            self.client,
            '/simulation/metrics',
            'construction_msgs/SimMetrics'
        )
        self.metrics_listener.subscribe(callback)