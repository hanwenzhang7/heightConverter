import wx

class heightConverter(wx.Frame):
	
	def __init__(self,parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY,"This is height converter.")
		self.panel = wx.Panel(self)
		self.prompt = wx.StaticText(self.panel, label="Enter your height in feet and inches:", pos=(40, 10))
		self.response = wx.StaticText(self.panel, pos=(40, 80))
		
		self.feet = wx.StaticText(self.panel, label="Feet", pos=(160, 50))
		self.inch = wx.StaticText(self.panel, label="Inch", pos=(320, 50))
		self.feetBox = wx.TextCtrl(self.panel, pos=(40, 50))
		self.inchBox = wx.TextCtrl(self.panel, pos=(200, 50))
		
		self.btnSubmit = wx.Button(self.panel, label="Submit", pos=(150, 100))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)
		
		self.btnRoundNumber = wx.Button(self.panel, label="RoundNumber", pos=(150, 150))
		self.btnRoundNumber.Bind(wx.EVT_BUTTON, self.OnRoundNumber)
		
	def OnSubmit(self, e):
		feet = float(self.feetBox.GetValue())
		inch = float(self.inchBox.GetValue())
		
		try:
			height=30.48*feet + 2.54*inch
			self.response.SetLabel("You are " +str(height)+" cm tall.")
		except:
			wx.MessageBox("Please enter a number", "Info", wx.OK)
			
	def OnRoundNumber(self,e):
		feet = float(self.feetBox.GetValue())
		inch = float(self.inchBox.GetValue())
		height=30.48*feet + 2.54*inch
		height = int(height)
		self.response.SetLabel("You are " + str(height) + " cm tall.")

#-----------------------------------Main Program-------------------------------------------

heightConverterApp = wx.App(False)
frame = heightConverter(None)
frame.Show()
heightConverterApp.MainLoop()
