# (c) 2022 Open Source Systems, Ltd., all rights reserved.

import wx

app = wx.App()
window = wx.Frame(None, title="WX Test Frame", size=(300, 200))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
window.Show(True)

app.MainLoop()
