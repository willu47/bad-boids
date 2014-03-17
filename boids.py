"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
import random

class Boid(object):
    """
    A class of object to represent a bird
    Parameters:
        number_of_boids -   class member variable which counts the
                            number of boids initialised
        x               -   x position
        y               -   y position
        xv              -   x vector
        yv              -   y vector
    """

    number_of_boids = 0

    def __init__(self, x, y, xv, yv):
        Boid.number_of_boids += 1
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv

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

    def __init__(self,number_of_boids = 50,repulsion = 100, \
                    attraction = 0.01, speed_threshold = 10000, \
                    acceleration = 0.125):
        self.boids = []
        self.repulsion = repulsion
        self.attraction = attraction
        self.speed_threshold = speed_threshold
        self.acceleration = acceleration
        self.number_of_boids = number_of_boids

    def initialise_random(self):
        for i in range(1,self.number_of_boids):
            self.boids.append(Boid(
                        random.uniform(-450,50.0), \
                        random.uniform(300.0,600.0), \
                        random.uniform(0,10.0), \
                        random.uniform(-20.0,20.0)
                        ))

    def initialise_from_data(self, boid_data):
        self.number_of_boids = len(boid_data[0])
        for boid in range(self.number_of_boids):
            self.boids.append(Boid(boid_data[0][boid], \
                            boid_data[1][boid], \
                            boid_data[2][boid], \
                            boid_data[3][boid]))

    def move_boids_middle(self):
        for i in self.boids:
            for j in self.boids:
                i.xv = i.xv + \
                    (j.x - i.x) * self.attraction / self.number_of_boids
                i.yv = i.yv + \
                    (j.y - i.y) * self.attraction / self.number_of_boids

    def boids_avoid_others(self):
        for i in self.boids:
            for j in self.boids:
                if (j.x - i.x)**2 + (j.y - i.y)**2 < self.repulsion:
                    i.xv = i.xv + (i.x - j.x)
                    i.yv = i.yv + (i.y - j.y)

    def match_speed(self):
        for i in self.boids:
            for j in self.boids:
                if (j.x - i.x)**2 + (j.y - i.y)**2 < self.speed_threshold:
                    i.xv = i.xv + (j.xv - i.xv) * self.acceleration \
                                / self.number_of_boids
                    i.yv = i.yv + (j.yv - i.yv) * self.acceleration \
                                / self.number_of_boids

    def update_boids(self):
        self.move_boids_middle()
        self.boids_avoid_others()
        self.match_speed()
        # Move according to velocities
        for i in self.boids:
            i.x = i.x + i.xv
            i.y = i.y + i.yv



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
