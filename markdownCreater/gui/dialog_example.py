import wx
import settings
settings.language.init_translation()
class dialog(wx.Dialog):
    def __init__(self,p):
        super().__init__(p,-1,title=_(""))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer()
        panel.SetSizer(sizer)