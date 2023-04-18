import math

def calculateHeading(P):
    """
    This function takes a list of points representing the trajectory of a vehicle
    and returns its heading in degrees.
    """
    if len(P) < 2:
        return None
    x_diff = P[-1][0] - P[-2][0]
    y_diff = P[-1][1] - P[-2][1]
    return math.degrees(math.atan2(y_diff, x_diff))

def calculateBoundingBox(P, heading, H, W):
    """
    This function takes a list of points representing the trajectory of a vehicle,
    the heading of the vehicle, and its height and width, and returns the bounding box
    of the vehicle.
    """
    # Convert the heading to radians.
    theta = heading * math.pi / 180

    # Calculate the coordinates of the four corners of the vehicle.
    x1 = P[-1][0] - H/2 * math.cos(theta) - W/2 * math.sin(theta)
    y1 = P[-1][1] - H/2 * math.sin(theta) + W/2 * math.cos(theta)
    x2 = P[-1][0] + H/2 * math.cos(theta) - W/2 * math.sin(theta)
    y2 = P[-1][1] + H/2 * math.sin(theta) + W/2 * math.cos(theta)
    x3 = P[-1][0] + H/2 * math.cos(theta) + W/2 * math.sin(theta)
    y3 = P[-1][1] + H/2 * math.sin(theta) - W/2 * math.cos(theta)
    x4 = P[-1][0] - H/2 * math.cos(theta) + W/2 * math.sin(theta)
    y4 = P[-1][1] - H/2 * math.sin(theta) - W/2 * math.cos(theta)

    # Return the coordinates of the bounding box as a list of four points.
    return [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]


def doOverlap(B0, B1):
    """
    This function takes two bounding boxes B0 and B1, each represented as a list of
    four points, and returns True if the two boxes overlap and False otherwise.
    """
    # Check if any of the four points in box B0 is inside box B1.
    for point in B0:
        if (point[0] >= B1[0][0] and point[0] <= B1[1][0]) and \
           (point[1] >= B1[0][1] and point[1] <= B1[2][1]):
            return True

    # Check if any of the four points in box B1 is inside box

def doListsOverlap(L0, L1):
    """
    This function takes two lists of bounding boxes, L0 and L1, and returns True
    if any pair of boxes in the two lists overlap, and False otherwise.
    """
    # Iterate over all pairs of bounding boxes in L0 and L1.
    for t in range(len(L0)):
            # Check if the current pair of bounding boxes overlap.
            if doOverlap(L0[t], L1[t]):
                return t
    # If we reach this point, then no pairs of bounding boxes overlap.
    return -1


def collision_check(points0, points1, shape0, shape1):
    """
    This function takes two lists of points representing the trajectories of two vehicles,
    and the shapes of the vehicles, and returns True if the two vehicles collide and
    False otherwise.
    """
    # Calculate the headings of the two vehicles.
    heading0 = calculateHeading(points0)
    heading1 = calculateHeading(points1)

    # Calculate the bounding boxes of the two vehicles.
    bounding_boxes0 = [calculateBoundingBox(points0, heading0, shape0[0], shape0[1])]
    bounding_boxes1 = [calculateBoundingBox(points1, heading1, shape1[0], shape1[1])]

    # Check if the two vehicles collide.
    return doListsOverlap(bounding_boxes0, bounding_boxes1)

if __name__ == "__main__":
    points0 = [[0, 0], [1, 0], [2, 1], [2, 2], [1, 3], [0, 3], [-1, 2], [-1, 1], [-0.5, 1.5], [0, 2]]
    points1 = [[3, 3], [4, 3], [5, 4], [5, 5], [4, 6], [3, 6], [2, 5], [2, 4], [2.5, 4.5], [3, 5]]
    height = 2
    width = 1

    print(collision_check(points0, points1, (height, width), (height, width)))