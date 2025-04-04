import streamlit as st
import pandas as pd
import plotly.express as px
from ros_bridge import ROSBridge
from dataclasses import dataclass
from typing import Dict, List
import json

@dataclass
class RobotData:
    odometry: Dict = None
    joint_states: Dict = None
    metrics: Dict = None

# Initialize session state
if 'robot_data' not in st.session_state:
    st.session_state.robot_data = RobotData()
    
def update_odometry(msg):
    st.session_state.robot_data.odometry = msg

def update_joint_states(msg):
    st.session_state.robot_data.joint_states = msg

def update_metrics(msg):
    st.session_state.robot_data.metrics = msg

def main():
    st.title("Construction Robotics Dashboard")
    
    # ROS Bridge Connection
    ros_bridge = ROSBridge()
    
    if st.button("Connect to ROS"):
        if ros_bridge.connect():
            st.success("Connected to ROS Bridge")
            ros_bridge.subscribe_to_odometry(update_odometry)
            ros_bridge.subscribe_to_joint_states(update_joint_states)
            ros_bridge.subscribe_to_metrics(update_metrics)
        else:
            st.error("Failed to connect to ROS Bridge")

    # Display Data
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Robot Odometry")
        if st.session_state.robot_data.odometry:
            st.json(st.session_state.robot_data.odometry)
    
    with col2:
        st.subheader("Joint States")
        if st.session_state.robot_data.joint_states:
            st.json(st.session_state.robot_data.joint_states)
    
    st.subheader("Simulation Metrics")
    if st.session_state.robot_data.metrics:
        st.json(st.session_state.robot_data.metrics)

if __name__ == "__main__":
    main()