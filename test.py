import wx

app = wx.App()

frame = wx.Frame(None, -1, 'x')

statusBar = frame.CreateStatusBar()
statusBar.SetStatusText('current status')

menuBar = wx.MenuBar()
menu = wx.Menu()
menu.Append(wx.ID_EXIT, 'E&xit\tAlt-X', 'Exit Program')
menu.Append(200, 'Test', 'Test')
menuBar.Append(menu, '&File')
frame.SetMenuBar(menuBar)


frame.Show()
app.MainLoop()

