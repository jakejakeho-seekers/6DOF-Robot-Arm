import numpy as np
import math

def fk(angles):
    # Length of links
    L0 = 270.35
    L1 = 69.00
    L2 = 365.35
    L3 = 69.00
    L4 = 374.29
    L5 = 10.00
    L6 = 368.3

    # Reference frame for 0 & 7
    T0 = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, L0],
        [0, 0, 0, 1]
    ])

    T7 = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, L6],
        [0, 0, 0, 1]
    ])

    # Reference frame for T0_1, T1_2... T6_7
    index = 0
    T0_1 = np.array([
        [np.cos(np.deg2rad(angles[index])), -np.sin(np.deg2rad(angles[index])), 0, 0],
        [np.sin(np.deg2rad(angles[index])), np.cos(np.deg2rad(angles[index])), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ])

    index = 1
    T1_2 = np.array([
        [-np.sin(np.deg2rad(angles[index])), -np.cos(np.deg2rad(angles[index])), 0, L1],
        [0, 0, 1, 0],        
        [np.cos(np.deg2rad(angles[index])), np.sin(np.deg2rad(angles[index])), 0, 0],
        [0, 0, 0, 1],
    ])

        
    index = 2
    T2_3 = np.array([
        [np.cos(np.deg2rad(angles[index])), -np.sin(np.deg2rad(angles[index])), 0, 0],
        [0, 0, -1, -L2],        
        [np.sin(np.deg2rad(angles[index])), np.cos(np.deg2rad(angles[index])), 0, 0],
        [0, 0, 0, 1],
    ])

    index = 3
    T3_4 = np.array([
        [np.cos(np.deg2rad(angles[index])), -np.sin(np.deg2rad(angles[index])), 0, L3],
        [0, 0, 1, 0],        
        [-np.sin(np.deg2rad(angles[index])), -np.cos(np.deg2rad(angles[index])), 1, 0],
        [0, 0, 0, 1],
    ])

    index = 4
    T4_5 = np.array([
        [np.cos(np.deg2rad(angles[index])), -np.sin(np.deg2rad(angles[index])), 0, 0],
        [0, 0, -1, -L4],        
        [np.sin(np.deg2rad(angles[index])), np.cos(np.deg2rad(angles[index])), 0, 0],
        [0, 0, 0, 1],
    ])

    index = 5
    T5_6 = np.array([
        [np.cos(np.deg2rad(angles[index])), -np.sin(np.deg2rad(angles[index])), 0, L5],
        [0, 0, 1, 0],        
        [-np.sin(np.deg2rad(angles[index])), -np.cos(np.deg2rad(angles[index])), 0, 0],
        [0, 0, 0, 1],
    ])

    index = 6
    T6_7 = np.array([
        [np.cos(np.deg2rad(angles[index])), -np.sin(np.deg2rad(angles[index])), 0, 0],
        [0, 0, -1, 0],        
        [np.sin(np.deg2rad(angles[index])), np.cos(np.deg2rad(angles[index])), 0, 0],
        [0, 0, 0, 1],
    ])


    points = np.array([[0], [0], [0]])
    
    P1 = np.dot(T0, T0_1)
    points = np.hstack((points, P1[:3,[3]]))

    P2 = np.dot(P1, T1_2)
    points = np.hstack((points, P2[:3,[3]]))

    P3 = np.dot(P2, T2_3)
    points = np.hstack((points, P3[:3,[3]]))

    P4 = np.dot(P3, T3_4)
    points = np.hstack((points, P4[:3,[3]]))

    P5 = np.dot(P4, T4_5)
    points = np.hstack((points, P5[:3,[3]]))

    P6 = np.dot(P5, T5_6)
    points = np.hstack((points, P6[:3,[3]]))

    P7 = np.dot(P6, T6_7)
    points = np.hstack((points, P7[:3,[3]]))

    P = np.dot(P7, T7)
    points = np.hstack((points, P[:3,[3]]))
    return points
