# Boids Algorithm Visualizer

> **Archived project:** This repository contains my first attempt at implementing and visualizing the Boids algorithm. It is an older experiment and is no longer being developed or maintained.

A newer approach to the same problem is available here:

**[View the newer Boids implementation](https://github.com/Rejman333/FlockingAlgorithm)**

## Demo

![Boids Algorithm Visualizer](https://github.com/Rejman333/Boids-Algorithm-Visualizer/blob/main/media/Boids.gif)

## About

This project is a personal experiment created to visualize the **Boids algorithm**, which simulates flocking behavior in a two-dimensional space.

Each boid follows a small set of local rules. When those rules are applied across the group, they produce collective movement resembling flocking, schooling, or herding.

## Features

* Real-time visualization of boid movement in 2D space.
* Adjustable cohesion, alignment, and separation parameters.
* A simple demonstration of how local behavior can produce complex group movement.

## How It Works

The Boids algorithm is based on three primary rules:

1. **Cohesion** — Boids move toward the average position of their nearby neighbors.
2. **Alignment** — Boids adjust their direction to match the average heading of nearby neighbors.
3. **Separation** — Boids steer away from nearby neighbors to avoid overcrowding.

Combining these rules creates natural-looking flocking behavior. Adjusting their relative weights changes how the flock moves and groups together.

## Getting Started

### Prerequisites

* Python 3.x
* The dependencies listed in `requirements.txt`

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application using the appropriate entry-point script for the project.

## Project Status

This repository is preserved as a record of my first Boids implementation. It reflects an early approach to the problem and is not intended for further development.

For the newer implementation, architecture, and ongoing version of the project, visit:

**[New Boids repository](https://github.com/Rejman333/FlockingAlgorithm)**
