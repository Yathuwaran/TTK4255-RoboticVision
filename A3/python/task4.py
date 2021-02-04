import numpy as np
import matplotlib.pyplot as plt
from common import *

# Tip: Use np.loadtxt to load data into an array
K = np.loadtxt('../data/heli_K.txt')
T_platform_cam = np.loadtxt('../data/platform_to_camera.txt')

screw_dist = 0.1145


screw_holes = np.array([[0,0,0,1], [screw_dist,0,0,1], [screw_dist,screw_dist,0,1], [0,screw_dist,0,1]])

screw_holes = T_platform_cam@screw_holes.T


width,height = 600,400

u,v = project(K, screw_holes)


img = plt.imread("../data/quanser.jpg")
plt.imshow(img)
h, w = img.shape[0:2]
#plt.xlim([100,600])
#plt.ylim([600,300])

draw_frame(K,T_platform_cam, scale=screw_dist)
plt.scatter(u, v, c='cyan', marker='.', s=20)
plt.savefig("t42")


#4.3
def t_base_platform(T_platform_cam,psi):
    return T_platform_cam@T_y(screw_dist/2)@T_x(screw_dist/2)@R_z(psi)

#4.4
def t_hinge_base(T_base_platform,theta):
    return T_base_platform@T_z(0.325)@R_y(theta)

#4.5
def t_arm_hinge(T_hinge_base):
    return T_hinge_base@T_z(-0.05)
#4.6
def t_rotor_arm(T_arm_hinge, phi):
    return T_arm_hinge@T_x(0.65)@T_z(-0.03)@R_x(phi)


T_base_platform = t_base_platform(T_platform_cam,11.6)

T_hinge_base = t_hinge_base(T_base_platform,28.9)

T_arm_hinge = t_arm_hinge(T_hinge_base)

T_rotor_arm = t_rotor_arm(T_arm_hinge, 0)

draw_frame(K,T_base_platform,0.05)
draw_frame(K,T_hinge_base,0.05)
draw_frame(K,T_arm_hinge,0.05)
draw_frame(K,T_rotor_arm,0.05)

plt.savefig("t43")

X =np.loadtxt('../data/heli_points.txt')

#4.7
arm = T_arm_hinge@X[:3,:4].T
u,v = project(K, arm)
plt.scatter(u,v, c='yellow', marker='.', s=30)

rotor = T_rotor_arm@X[3:,:4].T
u,v = project(K, rotor)
plt.scatter(u,v, c='red', marker='.', s=30)
plt.savefig("t47")
plt.show()
