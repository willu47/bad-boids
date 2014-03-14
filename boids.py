"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

class Boid(object):
    """
    A class of object to represent the birds
    Parameters:
        number_of_boids -   class member variable which counts the
                            number of boids initialised


    """

    number_of_boids = 0

    def __init__(self):
        Boid.number_of_boids += 1

    @classmethod
    def get_number_of_boids(self):
        return Boid.number_of_boids

class Boids(object):
    """
    A flock of Boid objects
    Parameters:
        xs  -   Vector of x positions
        ys  -   Vector of y positions
        xvs -   Vector of x vectors
        yvs -   Vector of y vectors
    """

    def __init__(self,xs,ys,xvs,yvs):
        self.xs = xs
        self.ys = ys
        self.xvs = xvs
        self.yvs = yvs





from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def move_boids(boid_velocities, boid_position, centre_attraction):
    number_of_boids = len(boid_position)
    array_of_boids =  range(number_of_boids)
    for i in array_of_boids:
        for j in array_of_boids:
            boid_velocities[i] = boid_velocities[i] + \
                (boid_position[j] - boid_position[i]) * centre_attraction / number_of_boids

def update_boids(boids, bird_repulsion, centre_attraction, speed_threshold, acceleration):
    xs,ys,xvs,yvs = boids
    number_of_boids = len(xs)
    array_of_boids =  range(number_of_boids)

    # Fly towards the middle
    move_boids(xvs, xs, centre_attraction)
    move_boids(yvs, ys, centre_attraction)

    # Fly away from nearby boids
    for i in array_of_boids:
        for j in array_of_boids:
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < bird_repulsion:
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in array_of_boids:
        for j in array_of_boids:
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < speed_threshold:
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*acceleration/number_of_boids
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*acceleration/number_of_boids
    # Move according to velocities
    for i in array_of_boids:
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    repulsion = 100
    attraction = 0.01
    speed_threshold = 10000
    acceleration = 0.125
    update_boids(boids, repulsion, attraction, speed_threshold, acceleration)
    scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
