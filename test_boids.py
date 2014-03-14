from boids import update_boids, move_boids, Boid
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    repulsion = 100
    attraction = 0.01
    speed_threshold = 10000
    acceleration = 0.125
    update_boids(boid_data, repulsion, attraction, speed_threshold, acceleration)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)

def test_move_boids():
    """
    Boids move towards middle
    """
    centre_attraction = 0.01
    boids_x = [-450,20]
    boid_x_velocities = [5,4]
    move_boids(boid_x_velocities, boids_x, centre_attraction)
    expected = [7.35, 1.65]
    assert_equal(expected, boid_x_velocities)

def test_Boid_class():
    """
    Tests that the number of boids is calculated correctly
    """
    boids = []
    for i in range(1,10):
        boids.append(Boid())
        assert_equal(Boid.get_number_of_boids(),i)

def test_update_boids():
    pass
