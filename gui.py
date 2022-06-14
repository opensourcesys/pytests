import wx

import misc
from constants import titles
from file import file

# Module level variables
mainFrame = None
menuBar = None

menus = [
	Menu(
		"&File",
		(wx.ID_NEW, "", "Creates a new project", None),
		(wx.ID_OPEN, "Open", "Open an existing project", None),
		(wx.ID_SEPARATOR, "", "", None),
		(wx.ID_EXIT, "Exit", "Close application", misc.quit)
	),
	Menu(
		"&Help",
		(wx.ID_ABOUT, "", "", None)
	)
]


def setup() -> None:
	"""Configures the GUI."""
	global mainFrame, menuBar
	# Mild sanity check
	if mainFrame is not None or menuBar is not None:
		raise RuntimeError("gui.setup() seems to have been called more than once!")
	mainFrame = MainFrame()
	# FixMe: do we need this?
	#wx.GetApp().SetTopWindow(mainFrame)
	# Create a menu bar, and add menus to it
	menuBar = wx.MenuBar()
	for menu in menus:
		menuBar.Append(menu, menu.Title)
	# Add the just-created menuBar to the mainFrame
	mainFrame.SetMenuBar(menuBar)


class MainFrame(wx.frame):
	"""The primary program frame. This is the base for the main program window. Virtual singleton."""

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


class Menu(wx.Menu):
	"""Manages a wx Menu.
	Create the menu with the menu title, including optional shortkey indicator (&).
	Provide all menu items as four-tuples in the following args.
	Example: (wx.ID_XXXX, "&Name", "helpString", event_callable)
	super().__init__() receives any kwargs.
	"""

	def __init__(self, title, *args):
		super().__init__(title, style=0)
		# Process each menu item, presented as a tuple in args
		for id, name, helpString, toCall in args:
			if id != wx.ID_SEPARATOR:
				thisItem = self.Append(id, name, helpString)
				if callable(toCall):
					self.Bind(wx.EVT_MENU, toCall, thisItem)
			else:  # It's a separator, not a real item
				self.Append(wx.ID_SEPARATOR, kind=wx.ITEM_SEPARATOR)
