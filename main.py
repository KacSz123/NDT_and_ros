import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

#im = Image.open('img/dd.png')

# Create figure and axes
fig, ax = plt.subplots()

# Display the image
#ax.imshow(im)

# Create a Rectangle patch
rect = patches.Rectangle((0, 0), 614, 614, linewidth=10, edgecolor='b', facecolor='none')
#ax.
# Add the patch to the Axes
ax.add_patch(rect)

plt.show()