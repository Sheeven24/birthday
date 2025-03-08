#pip install streamlit

import os
os.system("pip install matplotlib")
import matplotlib.pyplot as plt

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create pixelated heart animation
def draw_pixelated_heart():
    t = np.linspace(0, 2 * np.pi, 200)  # Reduce points for pixel effect
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    # Round coordinates to create pixelation
    x_pixelated = np.round(x)
    y_pixelated = np.round(y)

    # Create figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-18, 18)
    ax.set_ylim(-15, 15)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Happy Birthday bachu", fontsize=14, color='red')

    # Create scatter plot for pixel effect
    scatter = ax.scatter([], [], color='red', s=100, marker='s')

    # Animation function
    def animate(i):
        scatter.set_offsets(np.c_[x_pixelated[:i], y_pixelated[:i]])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)

    st.pyplot(fig)  # Display in Streamlit

# Streamlit App UI
st.title("Authentication Required!")

st.subheader("1+1? ")

col1, col2 = st.columns(2)

with col1:
    if st.button("2"):
        st.success("Correct!")
        draw_pixelated_heart()

with col2:
    if st.button("10"):
        st.error("Aww trynna be a coder? i loved that you tried")
