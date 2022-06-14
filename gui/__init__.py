import wx

import misc
from .mainFrame import MainFrame
from .menu import Menu

# Module level variables
mainFrame = None
menuBar = None


def makeMenus() -> list:
	"""Returns a list containing all of the generated menus for the menubar."""
	return [Menu(
		"&File",
		(wx.ID_NEW, "", "Creates a new project", None),
		(wx.ID_OPEN, "Open", "Open an existing project", None),
		(wx.ID_SEPARATOR, "", "", None),
		(wx.ID_EXIT, "Exit", "Close application", misc.quit)
	),
	Menu(
		"&Help",
		(wx.ID_ABOUT, "", "", None)
	)]


def setup() -> None:
	"""Configures the GUI."""
	global mainFrame, menuBar
	# Mild sanity check
	if mainFrame is not None or menuBar is not None:
		raise RuntimeError("gui.setup() seems to have been called more than once!")
	mainFrame = MainFrame()
	wx.GetApp().SetTopWindow(mainFrame)
	# Create a menu bar, and add menus to it
	menuBar = wx.MenuBar()
	for menu in makeMenus():
		menuBar.Append(menu, menu.Title)
	# Add the just-created menuBar to the mainFrame
	mainFrame.SetMenuBar(menuBar)
