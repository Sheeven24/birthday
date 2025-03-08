import os
os.system("pip install matplotlib pillow numpy streamlit")

import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import matplotlib.animation as animation

# Function to create pixelated heart animation
def draw_pixelated_heart():
    t = np.linspace(0, 2 * np.pi, 200)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    x_pixelated = np.round(x)
    y_pixelated = np.round(y)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-18, 18)
    ax.set_ylim(-15, 15)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add Happy Birthday background text
    ax.text(0, 0, "HAPPY BIRTHDAY", fontsize=30, color='pink',
            ha='center', va='center', alpha=0.3, fontweight='bold')

    scatter = ax.scatter([], [], color='red', s=100, marker='s')

    def animate(i):
        scatter.set_offsets(np.c_[x_pixelated[:i], y_pixelated[:i]])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)

    ani.save("heart.gif", writer="pillow")
    st.image("heart.gif")

# Function to create blooming rose animation
def draw_blooming_rose():
    t = np.linspace(0, 2 * np.pi, 200)
    
    # Rose parametric equations
    r = 8 * np.sin(4 * t)  # Petal shape
    x = r * np.cos(t)
    y = r * np.sin(t)

    x_pixelated = np.round(x)
    y_pixelated = np.round(y)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks([])
    ax.set_yticks([])

    # Add Happy Birthday background text
    ax.text(0, 0, "HAPPY BIRTHDAY BABY", fontsize=30, color='pink',
            ha='center', va='center', alpha=0.3, fontweight='bold')

    scatter = ax.scatter([], [], color='red', s=100, marker='s')

    def animate(i):
        scatter.set_offsets(np.c_[x_pixelated[:i], y_pixelated[:i]])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)

    ani.save("rose.gif", writer="pillow")
    st.image("rose.gif")

# Streamlit UI
st.title("🎉 Choose Your Surprise 🎉")

choice = st.radio("What would you like?", ("Heart", "Rose"))

if st.button("Show Animation"):
    if choice == "Heart":
        draw_pixelated_heart()
    elif choice == "Rose":
        draw_blooming_rose()
