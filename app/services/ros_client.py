import json
import time
from typing import Callable, Optional
import roslibpy
from app.models.robot import RobotState, JointStates, JointState
from app.models.simulation import SimulationMetrics

class ROSClient:
    def __init__(self):
        self.client = None
        self._connected = False
        self._callbacks = {
            'odometry': [],
            'joint_states': [],
            'sim_metrics': []
        }
        self.subscribers = {}

    def connect(self, host: str = 'localhost', port: int = 9090) -> bool:
        """Establish connection to ROS bridge"""
        try:
            self.client = roslibpy.Ros(host=host, port=port)
            self.client.run()
            if self.client.is_connected:
                self._connected = True
                print("Successfully connected to ROS")
                self._setup_subscribers()
            return self.client.is_connected
        except Exception as e:
            print(f"Failed to connect to ROS: {e}")
            return False

    def _setup_subscribers(self):
        """Initialize all ROS subscribers"""
        # Odometry subscriber
        self.odom_sub = roslibpy.Topic(
            self.client,
            '/robot/odometry',
            'nav_msgs/Odometry'
        )
        self.odom_sub.subscribe(self._handle_odometry)

        # Joint states subscriber
        self.joint_sub = roslibpy.Topic(
            self.client,
            '/robot/joint_states',
            'sensor_msgs/JointState'
        )
        self.joint_sub.subscribe(self._handle_joint_states)

        # Simulation metrics subscriber (custom message)
        self.sim_sub = roslibpy.Topic(
            self.client,
            '/simulation/metrics',
            'construction_msgs/SimMetrics'
        )
        self.sim_sub.subscribe(self._handle_sim_metrics)

    def register_callback(self, topic: str, callback: Callable):
        """Register external callback for ROS data"""
        if topic in self._callbacks:
            self._callbacks[topic].append(callback)
        if topic == 'odometry':
            subscriber = roslibpy.Topic(
                self.client,
                '/robot/odometry',
                'nav_msgs/Odometry'
            )
            
            def on_message(msg):
                state = RobotState(
                    x=msg['pose']['pose']['position']['x'],
                    y=msg['pose']['pose']['position']['y'],
                    orientation=msg['pose']['pose']['orientation']['z']
                )
                callback(state)
                
            subscriber.subscribe(on_message)
            self.subscribers[topic] = subscriber

    # --- Message Handlers ---
    def _handle_odometry(self, msg):
        robot_state = RobotState(
            x=msg['pose']['pose']['position']['x'],
            y=msg['pose']['pose']['position']['y'],
            orientation=msg['pose']['pose']['orientation']['z'],
            timestamp=time.time()
        )
        for cb in self._callbacks['odometry']:
            cb(robot_state)

    def _handle_joint_states(self, msg):
        joints = JointStates(
            names=msg['name'],
            positions=msg['position'],
            velocities=msg['velocity'],
            timestamp=time.time()
        )
        for cb in self._callbacks['joint_states']:
            cb(joints)

    def _handle_sim_metrics(self, msg):
        metrics = SimulationMetrics(
            stability=msg['stability_score'],
            power_usage=msg['power_usage'],
            collision_status=msg['in_collision'],
            timestamp=time.time()
        )
        for cb in self._callbacks['sim_metrics']:
            cb(metrics)

    def disconnect(self):
        """Cleanly shutdown ROS connection"""
        if self.client and self._connected:
            self.odom_sub.unsubscribe()
            self.joint_sub.unsubscribe()
            self.sim_sub.unsubscribe()
            self.client.terminate()
            self._connected = False