import os
os.system("pip install matplotlib pillow numpy")

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
    ax.set_title("❤ Happy Birthday ❤", fontsize=14, color='red')

    scatter = ax.scatter([], [], color='red', s=100, marker='s')

    def animate(i):
        scatter.set_offsets(np.c_[x_pixelated[:i], y_pixelated[:i]])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)
    
    ani.save("heart.gif", writer="pillow")
    st.image("heart.gif")

# Function to create flying pixelated balloons animation
def draw_flying_balloons():
    num_balloons = 10
    frames = 100

    x_positions = np.random.uniform(-10, 10, num_balloons)
    y_positions = np.random.uniform(-15, -5, num_balloons)

    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_xlim(-12, 12)
    ax.set_ylim(-15, 15)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("🎈 Happy Birthday 🎉", fontsize=14, color='red')

    scatter = ax.scatter(x_positions, y_positions, color='red', s=200, marker='o')

    def animate(i):
        new_y_positions = y_positions + (i * 0.1)
        scatter.set_offsets(np.c_[x_positions, new_y_positions])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

    ani.save("balloons.gif", writer="pillow")
    st.image("balloons.gif")

# Streamlit App UI
st.title("🎉 Welcome to the Birthday Surprise! 🎉")

# Ask user what they want
choice = st.radio("What do you want?", ("Balloons", "Heart"))

if st.button("Show Animation"):
    if choice == "Balloons":
        draw_flying_balloons()
    elif choice == "Heart":
        draw_pixelated_heart()
