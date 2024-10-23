# Boids Algorithm Visualizer

This project is a personal experiment aimed at visualizing the **Boids algorithm**, which simulates the flocking
behavior of birds in 2D space. The algorithm is based on a simple set of rules that dictate how individual "boids"
(bird-objects) interact with each other to create collective motion, resembling flocking, schooling, or herding
behavior.

*Unfortunately it is not yet finished, and I steal consider it work in progress.*

## Features

- **Real-time visualization** of the Boids algorithm, simulating natural flocking behavior in 2D space.
- **Dynamic parameter adjustments**: Tune flocking parameters like cohesion, alignment, and separation to see how they
  affect the behavior of the boids.

## How it Works

The Boids algorithm works by simulating individual boids (agents) that follow three basic rules:

1. **Coherence**: Boids move towards the average position of their neighbors.
2. **Alignment**: Boids align their direction with the average heading of their neighbors.
3. **Separation**: Boids steer to avoid crowding their neighbors.

By combining these rules, the boids can create complex and realistic flocking behavior. This visualization allows users
to see how different weights on these rules influence the overall movement of the flock.

## Getting Started

### Prerequisites

- **Python 3.x** is required to run the project.
- You may need to install additional Python packages. Run the following to install all dependencies:


```bash
pip install -r requirements.txt
```

# ToDo

- [ ] Code refactor.
- [ ] Implementing Spatial Partition.
- [ ] Smoothing boids movement.
- [ ] Adding feathers that enhance the project's aesthetics.
