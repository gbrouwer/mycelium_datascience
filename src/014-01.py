import math
import numpy as np

def rotate(P):

	#Rotate
	degrees = 45
	alpha = degrees / 180 * math.pi
	P_rotated = []
	for i in range(len(P)):
		x = P[i,0]
		y = P[i,1]
		x_rot = x * math.cos(alpha) + y * math.sin(alpha)
		y_rot = x * -math.sin(alpha) + y * math.cos(alpha)
	P_rotated.append((y_rot,x_rot))

	#Return
	return np.array(P_rotated)

if __name__ == '__main__':

	P = np.randon.random((10,2))
	rotate(P)





