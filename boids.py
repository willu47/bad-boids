"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x = [random.uniform(-450, 50.0) for x in range(50)]
boids_y = [random.uniform(300.0, 600.0) for x in range(50)]
boid_x_velocities = [random.uniform(0, 10.0) for x in range(50)]
boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(50)]
boids=(boids_x, boids_y, boid_x_velocities, boid_y_velocities)

def move_boids(boid_velocities, boid_position):
    number_of_boids = len(boid_position)
    array_of_boids =  range(number_of_boids)
    for i in array_of_boids:
        for j in array_of_boids:
            boid_velocities[i] = boid_velocities[i] + \
                (boid_position[j] - boid_position[i]) * 0.01 / number_of_boids

def update_boids(boids):
    xs,ys,xvs,yvs = boids
    number_of_boids = len(xs)
    array_of_boids =  range(number_of_boids)
	
    # Fly towards the middle
    move_boids(xvs, xs)
    move_boids(yvs, ys)
    
    # Fly away from nearby boids
    for i in array_of_boids:
        for j in array_of_boids:
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 100:
                xvs[i] = xvs[i] + (xs[i] - xs[j])
                yvs[i] = yvs[i] + (ys[i] - ys[j])
    # Try to match speed with nearby boids
    for i in array_of_boids:
        for j in array_of_boids:
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 10000:
                xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * 0.125 / number_of_boids
                yvs[i] = yvs[i] + (yvs[j] - yvs[i]) * 0.125 / number_of_boids
    # Move according to velocities
    for i in array_of_boids:
        xs[i] = xs[i] + xvs[i]
        ys[i] = ys[i] + yvs[i]


figure = plt.figure()
axes = plt.axes(xlim = (-500,1500), ylim = (-500,1500))
scatter=axes.scatter(boids[0], boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0], boids[1]))


anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
