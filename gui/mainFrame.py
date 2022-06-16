import wx

from file import file
from constants import titles

class MainFrame(wx.Frame):
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

	def shutdown(self, evt):
		"""It's all ending. I can feel it slipping away...
		But what if the user hasn't saved yet?
		"""
		dlg = wx.MessageDialog(self, message="Are you sure you want to quit?", caption="Caption", style=wx.YES_NO, pos=wx.DefaultPosition)
		resp = dlg.ShowModal()
		if resp == wx.ID_YES:
			super().Close()
		else:
			evt..StopPropagation()
