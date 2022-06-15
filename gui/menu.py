import wx

class Menu(wx.Menu):
	"""Manages a wx Menu.
	Create the menu with the menu title, including optional shortkey indicator (&).
	Provide all menu items as four-tuples in the following args.
	Example: (wx.ID_XXXX, "&Name", "helpString", event_callable)
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
