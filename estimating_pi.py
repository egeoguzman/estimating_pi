import random

def estimate_pi(n):
	num_point_in_circle = 0
	num_point_in_square = 0
	for i in range(n):
		point_x = random.uniform(0,1)
		point_y = random.uniform(0,1)
		distance = point_x**2 + point_y**2
		
		if distance <= 1:
			num_point_in_circle += 1
		num_point_in_square += 1

	return 4 * num_point_in_circle/num_point_in_square 

k=estimate_pi(100000000)
print(k)
