# 5.6 Modify exercise 3.2 to complete this exercise. Using the current
# location (x1,y1) and the destination location (x2,y2) the software should also be able
# to identify direction of the movement. For example, if the robot is moving to the
# Bottom, Top, Right, Left or combination of them e.g. Top Right or Bottom Left.
# As in exercise 3.2, when the user inputs a special number/character, the software
# should print all previous movements by showing a combination of the moved
# distance and the direction of each step. The trace function also displays the total
# distance travelled by the robot.
# The trace of robot movement is shown as the following:

import math

def get_next_point(step):
    x = int(input(f"please insert destination X value:"))
    y = int(input(f"please insert destination Y value:"))
    return (x, y)

def get_direction(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    direction = ""
    if dy > 0:
        direction += "Top"
    elif dy < 0:
        direction += "Bottom"
    if dx > 0:
        direction += " Right" if direction else "Right"
    elif dx < 0:
        direction += " Left" if direction else "Left"
    return direction.strip()

def cal_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def main():
    print("------ Robot Program ------")
    current_point = (0, 0)
    movements = []
    step = 1

    while True:
        next_point = get_next_point(step)
        if next_point == (999, 999):
            break
        distance = cal_distance(current_point, next_point)
        direction = get_direction(current_point, next_point)
        movements.append((round(distance), direction))
        current_point = next_point
        step += 1


    print("-----------------")
    for i, (d, direction) in enumerate(movements, start=1):
        print(f"Step {i}: {d} meter to {direction}")

    print(f"Total distance travellled by the robot is :{sum(d for d, _ in movements)}")
if __name__ == "__main__":
    main()