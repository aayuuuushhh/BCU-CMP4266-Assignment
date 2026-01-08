# You are going to design a program which allows a robot to move in a 2D coordinate system
# starting from the original point (0, 0). The robot can move to the next point (x, y) specified by
# the user. If the next point is (999, 999), the program ends and prints out the distance moved at
# each step.
# Your program can be implemented in various ways as long as it has the below behavior/display
# format - user inputs are highlighted in yellow:

import math

def get_next_point(step):
    x = int(input(f"Enter x{step} corrdinates:"))
    y = int(input(f"Enter y{step} corrdinates:"))
    return (x, y)

def cal_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def main():
    print("------ Robot Program ------")
    current_point = (0, 0)
    distances = []
    step = 1

    while True:
        next_point = get_next_point(step)
        if next_point == (999, 999):
            break
        distance = cal_distance(current_point, next_point)
        distances.append(distance)
        current_point = next_point
        step += 1

    print("-----------------")
    total_distance = 0
    for i, d in enumerate(distances, start = 1):
        print(f"Step {i}: Moved distance {d:.2f}")
        total_distance += d
    print(f"Total distance travellled by the robot is :{total_distance:.2f}")
if __name__ == "__main__":
    main()