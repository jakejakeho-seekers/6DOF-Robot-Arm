from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from fk import fk
from ik import ik
from matplotlib.widgets import Slider, Button, RadioButtons

def fkplot(valupdateSlider):
    points = fk(getCurrentAngles())
    enpoints = points[:,8]
    # sliderX.set_val(enpoints[0])
    # sliderY.set_val(enpoints[1])
    # sliderZ.set_val(enpoints[2])
    plotByAngles(points)

def plotByAngles(points):
    ax.clear()
    ax.set_xlim([-2000, 2000])
    ax.set_ylim([-2000, 2000])
    ax.set_zlim([-2000, 2000])
    for i in range(len(points[0]) - 1):
        ax.plot([points[0][i], points[0][i + 1]], [points[1][i], points[1][i + 1]],zs=[points[2][i], points[2][i + 1]])    

def getCurrentAngles():
    theta1 = sliderT1.val
    theta2 = sliderT2.val
    theta3 = sliderT3.val
    theta4 = sliderT4.val
    theta5 = sliderT5.val
    theta6 = sliderT6.val
    theta7 = sliderT7.val
    return [theta1, theta2, theta3, theta4, theta5, theta6, theta7]

def ikplot(val):
    x = sliderX.val
    y = sliderY.val
    z = sliderZ.val

    angles = ik([x, y, z], getCurrentAngles())
    sliderT1.set_val(angles[0])
    sliderT2.set_val(angles[1])
    sliderT3.set_val(angles[2])
    sliderT4.set_val(angles[3])
    sliderT5.set_val(angles[4])
    sliderT6.set_val(angles[5])
    sliderT7.set_val(angles[6])

    fkplot(None)

fig = plt.figure()
ax = plt.axes(projection="3d")

axcolor = 'lightgoldenrodyellow'
axT1 = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor=axcolor)
axT2 = plt.axes([0.25, 0.04, 0.65, 0.03], facecolor=axcolor)
axT3 = plt.axes([0.25, 0.08, 0.65, 0.03], facecolor=axcolor)
axT4 = plt.axes([0.25, 0.12, 0.65, 0.03], facecolor=axcolor)
axT5 = plt.axes([0.25, 0.16, 0.65, 0.03], facecolor=axcolor)
axT6 = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
axT7 = plt.axes([0.25, 0.24, 0.65, 0.03], facecolor=axcolor)
axX = plt.axes([0.25, 0.28, 0.65, 0.03], facecolor=axcolor)
axY = plt.axes([0.25, 0.32, 0.65, 0.03], facecolor=axcolor)
axZ = plt.axes([0.25, 0.36, 0.65, 0.03], facecolor=axcolor)

sliderT1 = Slider(axT1, 'T1', -141.0, 51.0, valinit=0)
sliderT2 = Slider(axT2, 'T2', -123.0, 60.0, valinit=0)
sliderT3 = Slider(axT3, 'T3', -173.0, 173.0, valinit=0)
sliderT4 = Slider(axT4, 'T4', -3.0, 150.0, valinit=0)
sliderT5 = Slider(axT5, 'T5', -175.0, 175.0, valinit=0)
sliderT6 = Slider(axT6, 'T6', -90.0, 120.0, valinit=0)
sliderT7 = Slider(axT7, 'T7', -175.0, 175.0, valinit=0)
sliderX = Slider(axX, 'X', -2000.0, 2000.0, valinit=0)
sliderY = Slider(axY, 'Y', -2000.0, 2000.0, valinit=0)
sliderZ = Slider(axZ, 'Z', -2000.0, 2000.0, valinit=0)

sliderT1.on_changed(fkplot)
sliderT2.on_changed(fkplot)
sliderT3.on_changed(fkplot)
sliderT4.on_changed(fkplot)
sliderT5.on_changed(fkplot)
sliderT6.on_changed(fkplot)
sliderT7.on_changed(fkplot)
fkplot(None)
sliderX.on_changed(ikplot)
sliderY.on_changed(ikplot)
sliderZ.on_changed(ikplot)


plt.show()