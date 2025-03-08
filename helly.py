import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# ---- Function to Draw Pixelated Heart ----
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
    ax.set_title("🎉 HAPPY BIRTHDAY BABY 🎉", fontsize=20, color='purple', alpha=0.3)

    scatter = ax.scatter([], [], color='red', s=100, marker='s')

    def animate(i):
        scatter.set_offsets(np.c_[x_pixelated[:i], y_pixelated[:i]])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)
    st.pyplot(fig)

# ---- Function to Draw Pixelated Rose ----
def draw_pixelated_rose():
    t = np.linspace(0, 2 * np.pi, 200)
    x = 10 * np.sin(t) * np.cos(t)
    y = 10 * np.cos(t) - 2 * np.cos(2 * t) - np.cos(3 * t)

    x_pixelated = np.round(x)
    y_pixelated = np.round(y)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("🎉 HAPPY BIRTHDAY BABY 🎉", fontsize=20, color='pink', alpha=0.3)

    scatter = ax.scatter([], [], color='red', s=100, marker='s')

    def animate(i):
        scatter.set_offsets(np.c_[x_pixelated[:i], y_pixelated[:i]])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)
    st.pyplot(fig)

# ---- Function for Animated Confetti ----
def draw_animated_confetti():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("🎉 HAPPY BIRTHDAY BABY 🎉", fontsize=20, color='gold', alpha=0.3)

    confetti_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    num_confetti = 30
    confetti_x = np.random.uniform(-9, 9, num_confetti)
    confetti_y = np.random.uniform(5, 10, num_confetti)  # Start from top

    scatter = ax.scatter(confetti_x, confetti_y, c=random.choices(confetti_colors, k=num_confetti), s=100, alpha=0.8)

    def animate(i):
        new_y = confetti_y - i * 0.1  # Move confetti downwards
        new_y[new_y < -9] = random.uniform(5, 10)  # Reset confetti that falls below screen
        scatter.set_offsets(np.c_[confetti_x, new_y])
        return scatter,

    ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
    st.pyplot(fig)

# ---- Streamlit UI ----
st.title("🎈 Surprise Gift! 🎈")

st.subheader("What do you want?")
choice = st.radio("", ["❤ A Heart", "🌹 A Rose"])

if st.button("Show Animation"):
    draw_animated_confetti()  # Play confetti animation first
    if choice == "❤ A Heart":
        draw_pixelated_heart()
    elif choice == "🌹 A Rose":
        draw_pixelated_rose()
