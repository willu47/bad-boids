from boids import update_boids, move_boids
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
def test_move_boids():
    """
    Boids move towards middle    
    """
    boids_x = [-450,20]
    boid_x_velocities = [5,4]
    move_boids(boid_x_velocities,boids_x)
    expected = [7.35, 1.65]
    assert_equal(expected, boid_x_velocities)
    
    