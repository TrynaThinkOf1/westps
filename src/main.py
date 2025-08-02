"""
GNU GPL license located at top level "westps/LICENSE"
"""

# Python imports

# External imports
from starlette.responses import Response
# Local imports
from globl import globl
import plotr

globl = globl()

app = globl.APP
valid_positions = globl.VALID_POSITIONS
bg_img = globl.BG_IMG


@app.get("/map/show")
async def show_map():
    bytes = plotr.plot((1, 5), (2.35, 9.1), bg_img)

    return Response(bytes, media_type="image/png")
