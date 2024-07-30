import sys,os
import wx
import settings
settings.language.init_translation()
class ExitDialog(wx.Dialog):
    def __init__(self,p):
        super().__init__(p,-1,title=_("exit {} dialog".format(settings.app.name)))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer()
        sizer.Add(wx.StaticText(panel,-1,_("what woud you like to do?")))
        self.choose=wx.Choice(panel,-1,choices=[_("exit"),_("restart")])
        self.choose.SetSelection(0)
        sizer.Add(self.choose)
        self.ok=wx.Button(panel,-1,_("OK"))
        self.Bind(wx.EVT_BUTTON,self.OKE,self.ok)
        self.ok.SetDefault()
        sizer.Add(self.ok)
        self.cancel=wx.Button(panel,-1,_("cancel"))
        self.Bind(wx.EVT_BUTTON,lambda event:self.Close(),self.cancel)
        sizer.Add(self.cancel)
        panel.SetSizer(sizer)
    def OKE(self,event):
        x=self.choose.GetSelection()
        if x==0:
            wx.Exit()
        elif x==1:
            os.execl(sys.executable, sys.executable, *sys.argv)