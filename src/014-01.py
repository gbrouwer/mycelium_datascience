import math

def rotate(P):
	degrees = 45
	alpha = degrees / 180 * math.pi
	P_rotated = []
	for i in range(len(P)):
		x = P[i,0]
		y = P[i,1]
		x_rot = x * math.cos(alpha) + y * math.sin(alpha)
		y_rot = x * -math.sin(alpha) + y * math.cos(alpha)
		P_rotated.append((x_rot,y_rot))






