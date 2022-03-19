import numpy as np
import ahrs
def distance_between_2_gps_points(coords_1, coords_2):
    return distance_between_2_xyz_points(llh2ecef(*coords_1), llh2ecef(*coords_2))


def distance_between_2_xyz_points(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))
coor1 = [32.66541741500552, 35.10366327655712, 0]
coor2 = [32.66541741500552, 35.10360, 0]
coor3 = [32.66540, 35.10366327655712, 0]
distance = 100  # m

print(f"dlon: {coor1[1] - coor2[1]}, distance: {distance_between_2_gps_points(coor1, coor2)}")
print(f"dlat: {coor1[0] - coor3[0]}, distance: {distance_between_2_gps_points(coor1, coor3)}")

convert = {"dlon2dx": (coor1[1] - coor2[1]) / distance_between_2_gps_points(coor1, coor2),
               "dlat2dy": (coor1[0] - coor3[0]) / distance_between_2_gps_points(coor1, coor3)}

