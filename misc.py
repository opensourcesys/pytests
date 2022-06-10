"""Functions that just didn't fit anywhere else."""

import .globalVars

def quit() -> None:
	"""End of the world. Closes the program."""
	globalVars.mainFrame.Close()
