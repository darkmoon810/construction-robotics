import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add project root to Python path
root_dir = Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

from app.services.ros_client import ROSClient
from app.models.robot import RobotState, JointStates, JointState

# Initialize ROS connection
ros_client = ROSClient()

def update_robot_state(state: RobotState):
    """Callback for ROS odometry updates"""
    st.session_state['robot_state'] = state

if 'ros_connected' not in st.session_state:
    try:
        if ros_client.connect(host='localhost', port=9090):
            ros_client.register_callback('odometry', update_robot_state)
            st.session_state['ros_connected'] = True
    except Exception as e:
        st.error(f"Failed to connect to ROS: {e}")

# Dashboard UI
st.title("ROS-Integrated Construction Robot Dashboard")

if st.session_state.get('ros_connected'):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Live Robot State")
        if 'robot_state' in st.session_state:
            state = st.session_state['robot_state']
            st.write(f"Position: ({state.x:.2f}, {state.y:.2f})")
            st.write(f"Heading: {state.orientation:.2f} rad")
            
            # Plot trajectory
            if 'trajectory' not in st.session_state:
                st.session_state['trajectory'] = []
            st.session_state['trajectory'].append((state.x, state.y))
            
            df = pd.DataFrame(st.session_state['trajectory'], columns=['x', 'y'])
            st.line_chart(df)
    
    with col2:
        st.subheader("ROS Control")
        if st.button("Emergency Stop"):
            # Implement ROS service call
            st.error("STOP command sent to robot")
        
        speed = st.slider("Speed %", 0, 100, 50)
        # Would publish to /cmd_vel in real implementation
else:
    st.error("Not connected to ROS bridge")