from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boids

# Deliberately terrible code for teaching purposes
repulsion = 100
attraction = 0.01
speed = 10000
acceleration = 0.125
model = Boids(50, repulsion, attraction, speed, acceleration)
model.initialise_random()

figure = plt.figure()
axes = plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter = axes.scatter( [boid.x for boid in model.boids],\
                        [boid.y for boid in model.boids] )

def animate(frame):
    model.update_boids()
    scatter.set_offsets(zip([boid.x for boid in model.boids], \
                            [boid.y for boid in model.boids]))

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
