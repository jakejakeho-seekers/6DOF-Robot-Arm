from fk import fk
import numpy as np
from scipy.optimize import fsolve, root
def distance(angles, targetEndPoint):
    currentEndPoint = np.array(fk(angles)[:,8])
    result = np.subtract(targetEndPoint, currentEndPoint)
    return np.append(result, [0, 0, 0, 0])

def ik(targetEndPoint, angles):
    result = root(distance, np.array(angles), np.array(targetEndPoint))
    return result.x