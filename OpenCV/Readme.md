# Yellow Volleyball Tracker using OpenCV
Date: 17/06/2025<br>
This script detects and tracks a volleyball in a video using OpenCV. The ball is identified using color thresholding in HSV space and shape filtering using circularity. A motion trail follows the ball as it moves.

## Features
- Detects yellow objects based on HSV color range
- Filters out non-circular objects using contour circularity
- Tracks ball motion with trail

## Modules Used
1. OpenCV (cv2)
2. Numpy (numpy)
3. Time (Time)

## Output
- A green circle marks the ball
- A red trail shows recent motion path<br>
Youtube Video: https://youtu.be/SjksOvPpZyA
