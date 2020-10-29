from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import tkinter.messagebox
import requests
import threading
import json




class Convert:
    def __init__(self,root):
        self.root=root
        self.root.title("Currency Converter")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo950.ico")
        self.root.resizable(0,0)

        froms=StringVar()
        to=StringVar()


        def on_enter1(e):
            but_convert['background']="black"
            but_convert['foreground']="cyan"  
        def on_leave1(e):
            but_convert['background']="SystemButtonFace"
            but_convert['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"







        def clear():
            text.delete('1.0',"end")
            froms.set("select Currency From")
            to.set("select Currency To")






        def convert():
            try:
                with open("convert.json","w") as f:
                    if froms.get()!="select Currency From":
                        if to.get()!="select Currency To":
                            url='https://free.currconv.com/api/v7/convert?apiKey=[your_api_key]&q={0}_{1},{1}_{0}'.format(froms.get(),to.get())
                            response=requests.get(url).text.encode('utf8').decode('ascii', 'ignore')
                            details=response
                            json_obj = json.loads(details)
                            #print(json.dumps(json_obj, indent=4, sort_keys=True))
                            f.write(json.dumps(json_obj, indent=4, sort_keys=True))                       
                        else:
                            tkinter.messagebox.showerror("Error","Please Select 'To' Currency")
                    else:
                        tkinter.messagebox.showerror("Error","Please Select 'From' Currency")
                with open('convert.json', encoding='utf-8') as data_file:
                    data = json.loads(data_file.read())
                    text.insert("end",json.dumps(data, indent=4, sort_keys=True))

            except Exception as e:
                print(e)





        def convert_thread():
            t1=threading.Thread(target=convert)
            t1.start()





#====================frame======================================#
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=170,relief="ridge",bd=3,bg="darkblue")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=223,relief="ridge",bd=3)
        secondframe.place(x=0,y=170)

#=========================firstframe==========================================
        lab_from=Label(firstframe,text="From",font=('times new roman',12),bg="darkblue",fg="white")
        lab_from.place(x=100,y=10)

        lab_to=Label(firstframe,text="To",font=('times new roman',12),bg="darkblue",fg="white")
        lab_to.place(x=350,y=10)


        list_currency_from=['AFA','ALL','DZD','AOR','ARS','AMD','AWG','AUD','AZN','BSD','BHD',\
                            'BDT','BBD','BYN','BZD','BMD','BTN','BOB','BWP','BRL','GBP','BND','BGN'\
                            ,'BIF','KHR','CAD','CVE','KYD','XOF','XAF','XPF','CLP','CNY','COP','KMF'\
                            ,'CDF','CRC','HRK','CUP','CZK','DKK','DJF','DOP','XCD','EGP','SVC','ERN',\
                            'EEK','ETB','EUR','FKP','FJD','GMD','GEL','GHS','GIP','XAU','XFO','GTQ','GNF'\
                            ,'GYD','HTG','HNL','HKD','HUF','ISK','XDR','INR','IDR','IRR','IQD','ILS','JMD',\
                            'JPY','JOD','KZT','KES','KWD','KGS','LAK','LVL','LBP','LSL','LRD','LYD','LTL',\
                            'MOP','MKD','MGA','MWK','MYR','MVR','MRO','MUR','MXN','MDL','MNT','MAD','MZN','MMK',\
                            'NAD','NPR','ANG','NZD','NIO','NGN','KPW','NOK','OMR','PKR','XPD','PAB','PGK','PYG',\
                            'PEN','PHP','XPT','PLN','QAR','RON','RUB','RWF','SHP','WST','STD','SAR','RSD','SCR','SLL'\
                            ,'XAG','SGD','SBD','SOS','ZAR','KRW','LKR','SDG','SRD','SZL','SEK','CHF','SYP','TWD','TJS',\
                            'TZS','THB','TOP','TTD','TND','TRY','TMT','AED','UGX','XFU','UAH','UYU','USD','UZS','VUV',\
                            'VEF','VND','YER','ZMK','ZWL']
        list_currency_from_combo=Combobox(firstframe,values=list_currency_from,font=('arial',12),width=17,state="readonly",textvariable=froms)
        list_currency_from_combo.set("select Currency From")
        list_currency_from_combo.place(x=35,y=60)


        list_currency_to=['AFA','ALL','DZD','AOR','ARS','AMD','AWG','AUD','AZN','BSD','BHD',\
                            'BDT','BBD','BYN','BZD','BMD','BTN','BOB','BWP','BRL','GBP','BND','BGN'\
                            ,'BIF','KHR','CAD','CVE','KYD','XOF','XAF','XPF','CLP','CNY','COP','KMF'\
                            ,'CDF','CRC','HRK','CUP','CZK','DKK','DJF','DOP','XCD','EGP','SVC','ERN',\
                            'EEK','ETB','EUR','FKP','FJD','GMD','GEL','GHS','GIP','XAU','XFO','GTQ','GNF'\
                            ,'GYD','HTG','HNL','HKD','HUF','ISK','XDR','INR','IDR','IRR','IQD','ILS','JMD',\
                            'JPY','JOD','KZT','KES','KWD','KGS','LAK','LVL','LBP','LSL','LRD','LYD','LTL',\
                            'MOP','MKD','MGA','MWK','MYR','MVR','MRO','MUR','MXN','MDL','MNT','MAD','MZN','MMK',\
                            'NAD','NPR','ANG','NZD','NIO','NGN','KPW','NOK','OMR','PKR','XPD','PAB','PGK','PYG',\
                            'PEN','PHP','XPT','PLN','QAR','RON','RUB','RWF','SHP','WST','STD','SAR','RSD','SCR','SLL'\
                            ,'XAG','SGD','SBD','SOS','ZAR','KRW','LKR','SDG','SRD','SZL','SEK','CHF','SYP','TWD','TJS',\
                            'TZS','THB','TOP','TTD','TND','TRY','TMT','AED','UGX','XFU','UAH','UYU','USD','UZS','VUV',\
                            'VEF','VND','YER','ZMK','ZWL']
        list_currency_to_combo=Combobox(firstframe,values=list_currency_to,font=('arial',12),width=17,state="readonly",textvariable=to)
        list_currency_to_combo.set("select Currency To")
        list_currency_to_combo.place(x=275,y=60)


        but_convert=Button(firstframe,text="Convert",font=('times new roman',12),width=15,cursor="hand2",command=convert_thread)
        but_convert.place(x=50,y=120)
        but_convert.bind("<Enter>",on_enter1)
        but_convert.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,text="Clear",font=('times new roman',12),width=15,cursor="hand2",command=clear)
        but_clear.place(x=290,y=120)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#==========================secondframe========================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=11,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3)      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Convert(root)
    root.mainloop()