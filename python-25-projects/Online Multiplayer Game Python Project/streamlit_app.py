import streamlit as st
from client import Network

st.set_page_config(page_title="Online Multiplayer Game", layout="centered")

# Initialize connection
if 'network' not in st.session_state:
    st.session_state.network = Network()
    st.session_state.x = 50
    st.session_state.y = 50

st.title("🎮 Streamlit Multiplayer Game")
st.write(f"🧍 You are Player {st.session_state.network.id}")

# Controls
col1, col2 = st.columns(2)
with col1:
    st.session_state.x = st.slider("Move X", 0, 500, st.session_state.x, step=10)
with col2:
    st.session_state.y = st.slider("Move Y", 0, 500, st.session_state.y, step=10)

# Send and Receive
player_pos = {"x": st.session_state.x, "y": st.session_state.y}
positions = st.session_state.network.send(player_pos)

# Display All Players
st.subheader("🧑 Players Online:")
for pid, pos in positions.items():
    st.write(f"Player {pid}: X = {pos['x']}, Y = {pos['y']}")
