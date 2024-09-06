import math

# Function to calculate distance between two points
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Input coordinates for two points
x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

# Calculate the distance
distance = calculate_distance(x1, y1, x2, y2)

# Output the result
print(f"The distance between the two points is: {distance:.2f}")
