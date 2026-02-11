# 🚗 Self-Learning Car using Reinforcement Learning (Deep Q-Learning)

This project implements a **self-learning autonomous car simulation** using **Reinforcement Learning**.  
The car learns how to drive within a constrained 2D environment by interacting with it and receiving rewards and penalties — **without any predefined driving rules**.

The learning is achieved using **Deep Q-Learning (DQN)** with a neural network implemented in **TensorFlow & Keras**, and the environment is visualized using **Pygame**.

---

## 🔍 Project Overview

- The car acts as an **RL agent**
- The road acts as the **environment**
- The agent observes its **state (position)**
- It chooses actions: **Left, Right, Forward**
- It receives **rewards for safe driving** and **penalties for crashes**
- Over time, the agent learns an optimal driving strategy

This project demonstrates how reinforcement learning can be applied to autonomous systems in a simplified simulation.

---

## 🧠 Key Concepts Used

- Reinforcement Learning (RL)
- Deep Q-Network (DQN)
- Exploration vs Exploitation
- Reward Shaping
- Neural Networks
- Simulation-based Learning

---

## 🏗️ Project Structure
Self-Learning-Car-Reinforcement-Learning/
│
├── environment.py # Simulation environment (road, car, rewards)
├── dqn_model.py # Deep Q-Network (car's brain)
├── train.py # Training loop
├── test_env.py # Environment testing (random actions)
├── requirements.txt # Required dependencies
└── README.md


---

## ⚙️ Technologies Used

- **Python**
- **TensorFlow**
- **Keras**
- **Pygame**
- **NumPy**
- **Matplotlib**

---

📊 Results & Observations

Initially, the car moves randomly and crashes frequently

As training progresses:

Crashes reduce

Movement becomes more stable

The car stays closer to the center of the road

Learning is validated visually and through improved reward values.

🚀 Future Enhancements

Add distance-based sensors (ray casting)

Introduce obstacles and traffic

Implement experience replay buffer

Save and load trained models

Extend to 3D simulation or robotics platforms.

🎓 Academic Use

This project is suitable for:

Machine Learning projects

Reinforcement Learning demonstrations

AI / Autonomous Systems coursework.

Final-year / major projects.



## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Self-Learning-Car-Reinforcement-Learning.git
cd Self-Learning-Car-Reinforcement-Learning

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Test the environment (random behavior)
python test_env.py

4️⃣ Train the self-learning car
python train.py

A Pygame window will open showing the car learning over multiple episodes.
