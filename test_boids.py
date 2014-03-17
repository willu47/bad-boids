from boids import Boid, Boids
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml
import random

def test_class_boids_regression():
    """
    Regression test - ensures that given a fixed set of parameters
    the boids algorithm remains the same across changes to the program

    Data is stored in a yaml file called 'fixtures.py'
    """
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data = regression_data["before"]
    model = Boids(50,100,0.01,10000,0.125)
    model.initialise_from_data(boid_data)
    model.update_boids()
    model_after = [
                    [ boid.x for boid in model.boids ], \
                    [ boid.y for boid in model.boids ], \
                    [ boid.xv for boid in model.boids ], \
                    [ boid.yv for boid in model.boids ]
                ]
    for after,before in zip(regression_data["after"],model_after):
        for after_value,before_value in zip(after,before):
            assert_almost_equal(after_value,before_value,delta=0.01)

def test_initialise_one_from_data():
    model = Boids(50,100,0.01,10000,0.125)
    data = [[50],[600],[10],[20]]
    model.initialise_from_data(data)
    for boid,x,y,xv,yv in zip(model.boids,data[0],data[1],data[2],data[3]):
        assert_equal(boid.x, x)
        assert_equal(boid.y, y)
        assert_equal(boid.xv, xv)
        assert_equal(boid.yv, yv)

def test_initialise_mult_from_data():
    model = Boids(50,100,0.01,10000,0.125)
    data = [[50,-450],[600,300],[10,0],[20,-20]]
    model.initialise_from_data(data)
    for boid,x,y,xv,yv in zip(model.boids,data[0],data[1],data[2],data[3]):
        assert_equal(boid.x, x)
        assert_equal(boid.y, y)
        assert_equal(boid.xv, xv)
        assert_equal(boid.yv, yv)

def test_Boid_class():
    """
    Tests that the number of boids is calculated correctly
    """
    boids = []
    for i in range(1,10):
        boids.append(Boid(
                        random.uniform(-450,50.0), \
                        random.uniform(300.0,600.0), \
                        random.uniform(0,10.0), \
                        random.uniform(-20.0,20.0)
                        ))
        assert_equal(Boid.get_number_of_boids(),i)

def test_Boids_class():
    """
    Tests instantiation of Boids class
    """
    model = Boids(10,100,0.01,10000,0.125)
    assert_equal(model.number_of_boids,10)

def test_Boids_class_move_middle():
    """
    Tests move middle methods of Boids class
    """
    model = Boids(1,100,0.01,10000,0.125)
    data = [[5],[0],[4],[0]]
    model.initialise_from_data(data)
    model.move_boids_middle()
    expected = [7.35, 1.65]
    actual = [model.boids[0].x,model.boids[0].xv]
    assert_equal(actual, expected)
