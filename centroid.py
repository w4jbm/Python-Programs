# Find the Centroid of a triangle by finding the intercept
# of two of the three "point to midpoint-of-side" lines.
#
# Problem posed by Lee Bradley in the Facebook "not just tiny-c
# Programming Group".
#
# This solution coded by Jim McClanahan W4JBM (Jan 2023)
#
# Figure below is for reference:
#
# Points do not need to be in any particular order as
# long as they form a triangle.
#
#             ^ (Point 2)
#            / \
#    Side 1 /   \ Side 0
#          /     \
# Point 0 +-------+ Point 1
#           Side 2
#
# Side 0 is across the Angle formed at Point 0, etc.

from sympy import symbols, Eq, solve

def line_between_points(P1, P2):
    # print(P1)
    # print(P2)
    # Calculate Slop
    y_delta = P2[1] - P1[1]
    x_delta = P2[0] - P1[0]
    slope = y_delta / x_delta
    
    # Y = Slope*X + Intercept
    # Intercept = Y - Slope*X
    intercept = P1[1] - slope*P1[0]
 
    print("Line through Point 1 and Point 2 is:",
           "y = ", slope, "* x + ", intercept)
    return(slope,intercept)

# Definition of the three original points
x_given = [0, 4, 10]
y_given = [0, 0, 6]

x_mid_side0 = (x_given[1] + x_given[2]) / 2.0
y_mid_side0 = (y_given[1] + y_given[2]) / 2.0

x_mid_side1 = (x_given[0] + x_given[2]) / 2.0
y_mid_side1 = (y_given[0] + y_given[2]) / 2.0

print("Evaluating Point 0 to Mid-Point of Side 0...")
slope0, intercept0 = line_between_points([x_given[0], y_given[0]], [x_mid_side0, y_mid_side0])
print("\nEvaluating Point 1 to Mid-Point of Side 1...")
slope1, intercept1 = line_between_points([x_given[1], y_given[1]], [x_mid_side1, y_mid_side1])
print()

x, y = symbols('x,y')

# Y = Slope*X + Intercept
# Y - Slope*X = Intercept
equation0 = Eq((y-slope0*x), intercept0)
# print(equation0)
equation1 = Eq((y-slope1*x), intercept1)
# print(equation1)

print("Soluton for unknowns...")
print(solve((equation0, equation1), (x, y)))
