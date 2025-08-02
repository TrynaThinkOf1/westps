"""
GNU GPL license located at top level "westps/LICENSE"
"""



# Exception classes
class PlottingError(Exception):
    def __init__(msg: str, cause: str):
        super().__init__(f"Plotting failed: {msg} from {cause}")
