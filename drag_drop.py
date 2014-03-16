
import wx

class MyFileDropTarget(wx.FileDropTarget):
	
	def __init__(self, window):
		wx.FileDropTarget.__init__(self)
		self.window = window
	
	def OnDropFiles(self, x, y, filenames):
		self.window.SetInsertionPointEnd()
		# self.window.WriteText("\n%d file(s) dropped at %d,%d:\n" %(len(filenames), x, y))
		print "\n%d file(s) dropped at %d,%d:\n" %(len(filenames), x, y)

		for filepath in filenames:
			self.window.updateText(filepath + '\n')


class DnDPanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		file_drop_target = MyFileDropTarget(self)
		lbl = wx.StaticText(self, label="Drag some files here:")
		self.fileTextCtrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
		self.fileTextCtrl.SetDropTarget(file_drop_target)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(lbl, 0, wx.ALL, 5)
		sizer.Add(self.fileTextCtrl, 1, wx.EXPAND|wx.ALL, 5)
		self.SetSizer(sizer)
	
	def SetInsertionPointEnd(self):
		self.fileTextCtrl.SetInsertionPointEnd()
	
	def updateText(self, text):
		self.fileTextCtrl.WriteText(text)
	
class DnDFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self, parent=None, title="DnD Tutorial")
		panel = DnDPanel(self)
		self.Show()


if __name__ == "__main__":
	app = wx.App(False)
	frame = DnDFrame()
	app.MainLoop()

