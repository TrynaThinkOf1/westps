"""
GNU GPL license located at top level "westps/LICENSE"
"""

# Python imports
from typing import Tuple, Any
from io import BytesIO
# External imports
import matplotlib.pyplot as plt
# Local imports
from Classes import PlottingError


def plot(starting_position: Tuple[float, float], ending_position: Tuple[float, float], bg_img: Tuple[Any, int, int]):
    """
    Function to use the C++ implemented Djikstra's algorithm to create an image
      with the guide path that the user should take in red dots.

    Params:
        starting_position: Tuple[float, float]  user's starting X and Y position values
        ending_position: Tuple[float, float]  X and Y position values of where the user wants to go

    Returns:
        A matplotlib plot object that should be turned into an image and returned to the user

    Raises:
        If the plot fails to generate, it will raise a PlottingError
    """

    fig, ax = plt.subplots(figsize=(bg_img[1] / 100, bg_img[2] / 100))
    fig.suptitle("Follow Red Dots to Destination")

    ax.set(
        xlim=(0, bg_img[1]),
        ylim=(0, bg_img[2]),
        xticks=[],
        yticks=[]
    )

    ax.imshow(bg_img[0], extent=[0, bg_img[1], 0, bg_img[2]])
    
    xy = (starting_position[0] - 0.4, starting_position[1] + 0.2)
    ax.plot(*starting_position, marker="*", color="yellow", ms=12)
    ax.annotate("YOU ARE HERE", xy)

    xy = (ending_position[0] - 0.5, ending_position[1] + 0.3)
    ax.plot(*ending_position, marker="X", color="green", ms=15)
    ax.annotate("DESTINATION", xy)

    #ax.gca().invert_xaxis() # I DONT KNOW WHY THIS HAS TO HAPPEN BUT IF IT DOESNT IT REVERSES THE GRAPH
    #ax.gca().invert_yaxis() #   THIS TOO ^^

    buf = BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)

    buf.seek(0)
    return buf.getvalue()
