import guiTools
import sys
import os
from . import settings_handler
from . import language
import wx
language.init_translation()
class settings (wx.Dialog):
    def __init__(self,p):
        super().__init__(p,-1,title=_("settings"))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer()
        sizer_Genral=wx.BoxSizer()
        sizer.Add(wx.StaticText(panel,-1,_("select sectian")))
        self.sectian=wx.Listbook(panel,-1)
        sizer.Add(self.sectian)
        panel_general=wx.Panel(self.sectian)
        sizer_Genral.Add(wx.StaticText(panel_general,-1,_("language")))
        self.language=wx.Choice(panel_general,-1)
        self.language.Set(list(language.lang().keys()))
        languages = {index:language for language, index in enumerate(language.lang().values())}
        try:
            self.language.SetSelection(int(languages[settings_handler.get("g","lang")]))
        except Exception as e:
            self.language.SetSelection(0)
        sizer_Genral.Add(self.language)
        self.ExitDialog=wx.CheckBox(panel_general,-1,_("Show exit dialog when exiting the program"))
        self.ExitDialog.SetValue(self.cbts(settings_handler.get("g","exitDialog")))
        sizer_Genral.Add(self.ExitDialog)
        panel_general.SetSizer(sizer_Genral)
        self.sectian.AddPage(panel_general,_("general"))
        self.ok=wx.Button(panel,-1,_("OK"))
        self.Bind(wx.EVT_BUTTON,self.fok,self.ok)
        sizer.Add(self.ok)
        self.defolt=wx.Button(panel,-1,_("default"))
        self.Bind(wx.EVT_BUTTON,self.default,self.defolt)
        sizer.Add(self.defolt)
        self.cancel=wx.Button(panel,-1,_("cancel"))
        self.Bind(wx.EVT_BUTTON,self.fcancel,self.cancel)
        sizer.Add(self.cancel)
        panel.SetSizer(sizer)
    def fok(self,event):
        aa=0
        if settings_handler.get("g","lang")!=str(language.lang()[self.language.StringSelection]):
            aa=1
        settings_handler.set("g","lang",str(language.lang()[self.language.StringSelection]))
        settings_handler.set("g","exitDialog",str(self.ExitDialog.GetValue()))
        if aa==1:
            mb=wx.MessageDialog(self,_("you must restart the program to apply changes \n do you want to restart now?"),_("settings updated"),style=wx.YES_NO)
            mb.SetYesNoLabels(_("restart now"),_("restart later"))
            ex=mb.ShowModal()
            if ex==wx.ID_YES:
                os.execl(sys.executable, sys.executable, *sys.argv)
            elif ex==wx.ID_NO:
                self.Close()
        else:
            self.Close()
    def default(self,event):
        mb=wx.MessageDialog(self,_("do you wanna reset your settings ? \n if you click reset , the program will restart to complete reset."),_("alert"),style=wx.YES_NO)
        mb.SetYesNoLabels(_("reset and restart"),_("cancel"))
        ex=mb.ShowModal()
        if ex==wx.ID_YES:
            os.remove(settings_handler.cpath)
            os.execl(sys.executable, sys.executable, *sys.argv)

    def fcancel(self,event):
        self.Close()
    def cbts(self,string):
        if string=="True":
            return True
        else:
            return False


