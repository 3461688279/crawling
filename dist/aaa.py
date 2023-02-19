# coding=utf-8
import openai,os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
openai.api_key = "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"
class Application_ui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('聊天室')
        self.master.geometry('800x500')
        self.createWidgets()
    def createWidgets(self):
        self.top = self.winfo_toplevel()
        self.style = Style()
        self.style.configure('Tftitle.TLabelframe', font=('楷体', 12))
        self.style.configure('Tftitle.TLabelframe.Label', font=('楷体', 12))
        self.ftitle = LabelFrame(self.top, text='ai', style='Tftitle.TLabelframe')
        self.ftitle.place(relx=0.01, rely=0.02, relwidth=0.9, relheight=0.9)
        self.stext = Text(self.ftitle, font=('楷体', 22), wrap=NONE, )
        self.stext.place(relx=0.02, rely=0.035, relwidth=0.9, relheight=0.4)
        self.VScroll1 = Scrollbar(self.stext, orient='vertical')
        self.VScroll1.pack(side=RIGHT, fill=Y)
        self.VScroll1.config(command=self.stext.yview)
        self.stext.config(yscrollcommand=self.VScroll1.set)
        self.stextxscroll = Scrollbar(self.stext, orient=HORIZONTAL)
        self.stextxscroll.pack(side=BOTTOM, fill=X)
        self.stextxscroll.config(command=self.stext.xview)
        self.stext.config(xscrollcommand=self.stextxscroll.set)
        self.totext = Text(self.ftitle, font=('楷体', 12), wrap=NONE)
        self.totext.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.4)
        self.VScroll2 = Scrollbar(self.totext, orient='vertical')
        self.VScroll2.pack(side=RIGHT, fill=Y)
        self.VScroll2.config(command=self.totext.yview)
        self.totext.config(yscrollcommand=self.VScroll2.set)
        self.totextxscroll = Scrollbar(self.totext, orient=HORIZONTAL)
        self.totextxscroll.pack(side=BOTTOM, fill=X)
        self.totextxscroll.config(command=self.totext.xview)
        self.totext.config(xscrollcommand=self.totextxscroll.set)
        def cut(editor, event=None):
            editor.event_generate("<<Cut>>")
        def copy(editor, event=None):
            editor.event_generate("<<Copy>>")
        def paste(editor, event=None):
            editor.event_generate('<<Paste>>')
        def rightKey(event, editor):
            menubar.delete(0, END)
            menubar.add_command(label='剪切', command=lambda: cut(editor))
            menubar.add_command(label='复制', command=lambda: copy(editor))
            menubar.add_command(label='粘贴', command=lambda: paste(editor))
            menubar.post(event.x_root, event.y_root)
        menubar = Menu(self.top, tearoff=False)  # 创建一个菜单
        self.stext.bind("<Button-3>", lambda x: rightKey(x, self.stext))
        self.totext.bind("<Button-3>", lambda x: rightKey(x, self.totext))
        self.style.configure('Tcleartext.TButton', font=('楷体', 12))
        self.cleartext = Button(self.ftitle, text='清空', command=self.clear, style='Tcleartext.TButton')
        self.cleartext.place(relx=0.239, rely=0.463, relwidth=0.086, relheight=0.073)
        self.style.configure('Taddyh.TButton', font=('楷体', 12))
        self.addrs = Button(self.ftitle, text='点击查询', command=self.postrequest,style='Taddyh.TButton')
        self.addrs.place(relx=0.512, rely=0.463, relwidth=0.2, relheight=0.073)


class Appreturn(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
    def clear(self, event=None):
        self.stext.delete(1.0, "end")
        self.totext.delete(1.0, "end")
    def postrequest(self, event=None):
        cookiestext = self.stext.get(1.0, "end")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=cookiestext,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        answer = (response["choices"][0]["text"]).split(".")
        for i in answer:
            self.totext.insert(1.0, i)
            self.totext.update()
if __name__ == "__main__":
    top = Tk()
    Appreturn(top).mainloop()

