# (c) 2022 Open Source Systems, Ltd., all rights reserved.

import wx

import .gui


if __name__ == '__main__':
	app = wx.App()
	gui.setup()
	gui.mainFrame.Show()
	app.MainLoop()
