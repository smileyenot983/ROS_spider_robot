#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:44:31 2019

@author: ramil
"""

import unittest
import math
import numpy as np

def rot_x(angle):
    
    matrix = np.eye(3)
    matrix[1][1] = math.cos(angle)
    matrix[2][2] = math.cos(angle)
    matrix[1][2] = -math.sin(angle)
    matrix[2][1] = math.sin(angle)
    
    return matrix
    
def rot_y(angle):
    
    matrix = np.eye(3)
    
    matrix[0][0] = math.cos(angle)
    matrix[2][2] = math.cos(angle)
    
    matrix[2][0] = -math.sin(angle)
    matrix[0][2] = math.sin(angle)
    
    return matrix



def rot_z(angle):
    
    matrix = np.eye(3)
    
    matrix[0][0] = math.cos(angle)
    matrix[1][1] = math.cos(angle)
    
    matrix[0][1] = -math.sin(angle)
    matrix[1][0] = math.sin(angle)
    
    return matrix


def homogeneous_rot(axis,angle):
    matrix = np.eye(4)
    rot = np.zeros(3)
    
    if axis =='x':
        rot = rot_x(angle)
    elif axis=='y':
        rot=rot_y(angle)
    else:
        rot=rot_z(angle)

    matrix[:3,:3] = rot  
    
    return matrix

def homogeneous_translate(axis,length):
    matrix = np.eye(4)
    if axis =='x':
        matrix[0][3] = length
    elif axis=='y':
        matrix[1][3] = length
    else:
        matrix[2][3] = length
    return matrix






#list of joint parameters 

l1 = 2
l2 = 3
l3 = 4
theta1 = math.pi/6
theta2 = math.pi/2

def FK(l1,l2,l3,theta1,theta2):
    transform1 = np.dot(homogeneous_translate('z',l1),homogeneous_rot('x',theta1))
    transform2 = np.dot(homogeneous_translate('y',l2),homogeneous_rot('x',theta2))
    t12 = np.dot(transform1,transform2)
    end_effector = np.dot(t12,homogeneous_translate('y',l3))
    
    return end_effector




#HERE ARE TEST
    

class test_FK(unittest.TestCase):
    
    def test_FK1_simple(self):
        result = np.array([[ 1.        ,  0.        ,  0.        ,  0.        ],
           [ 0.        , -0.5       , -0.8660254 ,  0.59807621],
           [ 0.        ,  0.8660254 , -0.5       ,  6.96410162],
           [ 0.        ,  0.        ,  0.        ,  1.        ]])
        fk_answer = FK(2,3,4,math.pi/6,math.pi/2)
    
#        results = np.allclose(fk_answer,result)
        self.assertTrue(np.allclose(fk_answer,result))
        
    def test_FK2_simple(self):
        result = np.array([[  1.        ,   0.        ,   0.        ,   0.        ],
           [  0.        ,  -0.5       ,   0.8660254 , -10.        ],
           [  0.        ,  -0.8660254 ,  -0.5       ,  -3.66025404],
           [  0.        ,   0.        ,   0.        ,   1.        ]])
        fk_answer = FK(5,5,10,math.pi,math.pi/3)
        self.assertTrue(np.allclose(fk_answer,result))
            
    def test_FK3_zerotrans(self):
        result = np.array([[ 1.       ,  0.       ,  0.       ,  0.       ],
           [ 0.       , -0.5      ,  0.8660254,  0.       ],
           [ 0.       , -0.8660254, -0.5      ,  0.       ],
           [ 0.       ,  0.       ,  0.       ,  1.       ]])
        fk_answer = FK(0,0,0,math.pi,math.pi/3)
        self.assertTrue(np.allclose(fk_answer,result))
        

    def test_FK4_zeroangs(self):
        result = np.array([[1., 0., 0., 0.],
           [0., 1., 0., 8.],
           [0., 0., 1., 5.],
           [0., 0., 0., 1.]])
        fk_answer = FK(5,6,2,0,0)
        self.assertTrue(np.allclose(fk_answer,result))
            
            
    def test_FK5_zeroaall(self):
        result = np.array([[1., 0., 0., 0.],
           [0., 1., 0., 0.],
           [0., 0., 1., 0.],
           [0., 0., 0., 1.]])
        fk_answer = FK(0,0,0,0,0)
        self.assertTrue(np.allclose(fk_answer,result))
    
    
    def test_FK6_negtrans(self):
        result = np.array([[ 1.        ,  0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.33027906, -0.94388333, -3.86581297],
           [ 0.        ,  0.94388333,  0.33027906, -8.47941724],
           [ 0.        ,  0.        ,  0.        ,  1.        ]])
        fk_answer = FK(-4,-5,-1,math.pi/4,math.pi/7)
        self.assertTrue(np.allclose(fk_answer,result))
    
    
    def test_FK7_negangs(self):
        result = np.array([[ 1.        ,  0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.33027906,  0.94388333,  3.86581297],
           [ 0.        , -0.94388333,  0.33027906, -0.47941724],
           [ 0.        ,  0.        ,  0.        ,  1.        ]])
        fk_answer = FK(4,5,1,-math.pi/4,-math.pi/7)
        self.assertTrue(np.allclose(fk_answer,result))
            
    def test_FK8_negall(self):
        result = np.array([[ 1.        ,  0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.33027906,  0.94388333, -3.86581297],
           [ 0.        , -0.94388333,  0.33027906,  0.47941724],
           [ 0.        ,  0.        ,  0.        ,  1.        ]])
        fk_answer = FK(-4,-5,-1,-math.pi/4,-math.pi/7)
        self.assertTrue(np.allclose(fk_answer,result))
        


tests = test_FK()

tests.test_FK1_simple()
tests.test_FK2_simple()
tests.test_FK3_zerotrans()
tests.test_FK4_zeroangs()
tests.test_FK5_zeroaall()
tests.test_FK6_negtrans()
tests.test_FK7_negangs()
tests.test_FK8_negall()

    
    
    
    
