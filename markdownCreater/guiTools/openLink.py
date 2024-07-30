import webbrowser
import pyperclip
import wx
import settings
settings.language.init_translation()
class openLink(wx.Dialog):
    def __init__(self,p,link):
        super().__init__(p,-1,title=_("open link"))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer()
        sizer.Add(wx.StaticText(panel,-1,_("link")))
        self.link=wx.TextCtrl(panel,-1,style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)
        self.link.SetValue(link)
        sizer.Add(self.link)
        self.open=wx.Button(panel,-1,_("open link"))
        self.Bind(wx.EVT_BUTTON,self.OOpen,self.open)
        sizer.Add(self.open)
        self.copy=wx.Button(panel,-1,_("copy link"))
        self.Bind(wx.EVT_BUTTON,self.Ocopy,self.copy)
        sizer.Add(self.copy)
        panel.SetSizer(sizer)
    def OOpen(self,e):
        webbrowser.open(self.link.Value)
        self.Close()
    def Ocopy(self,e):
        pyperclip.copy(self.link.Value)
        self.Close()
def OpenLink(p,link):
    openLink(p,link).Show()