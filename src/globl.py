"""
GNU GPL license located at top level "westps/LICENSE"
"""

# Python imports
from typing import Tuple, Any
# External imports
from fastapi import FastAPI
import matplotlib.pyplot as plt

class globl:
    def __init__(self):
        self.APP = FastAPI(
            name="WestPS",
            version="0.0.4"
        )

        self.VALID_POSITIONS: list[Tuple[float, float]] = [
            (0.3, 1),
            (3.14, 5.8),
            (0, 4),
            (0, 4.7)
        ]

        img = plt.imread("assets/map.png")
        self.BG_IMG: Tuple[Any, int, int] = (img, img.shape[1], img.shape[0])
