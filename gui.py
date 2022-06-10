import wx

import .globalVars
from .constants import titles
from .file import file

def startup() -> None:
	if not globalVars.mainFrame:
		globalVars.mainFrame = MainFrame()
	# FixMe: do we need this?
	#wx.GetApp().SetTopWindow(mainFrame)
	menubar = wx.MenuBar()


class MainFrame(wx.frame):
	"""The primary program frame. This is the base for the main program window."""

	def __init__(self, titlePrepend: str=""):
		# A star goes in the title if we have unsaved changes
		fileStatusMarker = "*" if file.isUnsaved else ""
		# If we have an open file, its name should appear as part of the title
		if file.name is not None:
			title = f"{fileStatusMarker}{file.name} - {titles.displayName}"
		else:
			title = titles.displayName
		super().__init__(
			None,
			style=wx.DEFAULT_FRAME_STYLE,
			title=title
		)
		# FixMe: this can max and restore
		self.Maximize()


class 
