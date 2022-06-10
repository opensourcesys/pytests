# (c) 2022 Open Source Systems, Ltd., all rights reserved.

import wx

import .globalVars
import .gui


if __name__ == '__main__':
	app = wx.App()
	gui.startup()
	app.MainLoop()
