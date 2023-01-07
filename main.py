import json
from os.path import basename, splitext
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog
import threading


from PIL import Image
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gameb\AppData\Local\Tesseract-OCR\tesseract.exe'


class ARC(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ARC"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        
        self.var_source = tk.StringVar()
    
        self.btn_source = tk.Button(self, text = "Vybrat Soubor", command = self.ask_dir, width = 30, border = 3, background = "#D3D3D3")
        self.btn_source.pack(side = tk.TOP, anchor = tk.S, padx = 5, pady = 5)
        self.btn_convert = tk.Button(self, text = "Konvertovat", command = self.convert, width = 10, border = 3, background = "#75d060")
        self.btn_convert.pack(side = tk.TOP, anchor = tk.S, padx = 5, pady = 5)
        self.btn_export = tk.Button(self, text = "export", command = self.write_json, width = 10, border = 3, background = "#75d060")
        self.btn_export.pack(side = tk.TOP, anchor = tk.S, padx = 5, pady = 5)
        self.btn_tess = tk.Button(self, text = "tess", command = self.tess, width = 10, border = 3, background = "#75d060")
        self.btn_tess.pack(side = tk.TOP, anchor = tk.S, padx = 5, pady = 5)

        self.data = {}

    def ask_dir(self):
        adress = filedialog.askopenfilename()
        self.var_source.set(adress)
        print(f"Byl vybrán: {adress} .")


    def convert(self):
        threading.Thread(target=self.convert_thread).start() #aby aplikace nepřestala odpovídat tak to spustí konverzi jako nové vlákno a UI se nezasekne. Problém by mohl být u velkých PDF souborů



    def convert_thread(self):
        images = convert_from_path("mech.pdf")
 
        for i in range(len(images)):
            print(f"Uložil jsem stránku: {i} ")
            images[i].save('page'+ str(i) +'.jpg', 'JPEG')
    

    def write_json(self):
        name = filedialog.asksaveasfilename(filetypes=(("json", "*.json"),))
        with open(f"{name}", "w") as file:
            json.dump(self.data, file, indent = 4)


    def tess(self):
        filename = "page5.jpg"
        img1 = np.array(Image.open(filename))
        with open(f"pdf.pdf", "wb") as file:
            
            text = pytesseract.image_to_string(img1, lang="ces")
            
        print(text)


    def quit(self, event = None):
        super().quit()



app = ARC()
app.mainloop()

###################### možná se někdy šikne #######################
#pohřebiště vykradnu---- ehm výpůjčeného kódu :-)

"""
    def join(self): #tahle funkce by se mohla někdy hodit ale není funkční jen sem ji napsal abych věděl
        join = json.load(f"prvni")
        join2 = json.load(f"druhy")
        with open(f"joined", 'w') as file:
            joined = join + join2 # pochybuju že tohle bude fungovat XD 
            json.dump(joined, file, indent=4)
####################
        
        
        export = self.var_source.get()
        export = os.path.split(export)
        for i in export:
            if i.endswith(".pdf"):
                i = i.split(".") # [:4]
                name = i[0]
################################################

        self.var_base_folder = tk.StringVar()
        self.var_sub_folder = tk.StringVar()
        self.var_external_folder = tk.StringVar()
        self.var_file_extensions = tk.StringVar()
        self.var_smazat = tk.IntVar()
        self.var_name_conf = tk.StringVar()
        
        self.lbl_sub_folder = tk.Label(self, text = "Sub folder: ")
        self.lbl_sub_folder.grid(row = 1, column = 1, sticky = "w")
        self.entry_sub_folder = tk.Entry(self, textvariable = self.var_sub_folder, width = 50)
        self.entry_sub_folder.grid(row = 1, column = 2)
        
        self.lbl_base_folder = tk.Label(self, text = "Base folder: ")
        self.lbl_base_folder.grid(row = 2, column = 1, sticky = "w")
        self.entry_base_folder = tk.Entry(self, textvariable = self.var_base_folder, width = 50)
        self.entry_base_folder.grid(row = 2, column = 2)
        self.btn_base_folder = tk.Button(self, text = "Open", command = self.ask_dir1, width = 10)
        self.btn_base_folder.grid(row = 2, column = 3)


        self.lbl_external_folder = tk.Label(self, text = "External folder: ")
        self.lbl_external_folder.grid(row = 3, column = 1, sticky = "w")
        self.entry_external_folder = tk.Entry(self, textvariable = self.var_external_folder, width = 50)
        self.entry_external_folder.grid(row = 3, column = 2)
        self.btn_external_folder = tk.Button(self, text = "Open", command = self.ask_dir2, width = 10)
        self.btn_external_folder.grid(row = 3, column = 3)

        self.lbl_name_conf = tk.Label(self, text = "Preset name: ")
        self.lbl_name_conf.grid(row = 5, column = 1, sticky = "w")
        self.entry_name_conf = tk.Entry(self, textvariable = self.var_name_conf, width = 50)
        self.entry_name_conf.grid(row = 5, column = 2)
    
        self.lbl_file_extensions = tk.Label(self, text = "typy: ")
        self.lbl_file_extensions.grid(row = 4, column = 1, sticky = "w")
        self.entry_file_extensions = tk.Entry(self, textvariable = self.var_file_extensions, width = 50)
        self.entry_file_extensions.grid(row = 4, column = 2)


        self.check_btn_smazat = Checkbutton(self, onvalue = 1, offvalue = 0, variable = self.var_smazat, text = "Aut smazání")
        self.check_btn_smazat.grid(row = 1, column = 3)
        
        self.frame = Frame(self)
        self.frame.grid(row = 6, column = 3)
        self.btn_load = tk.Button(self.frame, text = "Load", command = self.load_conf, width = 10, border = 3)
        self.btn_load.grid(row = 1, column = 1)

        self.btn_add = tk.Button(self.frame, text = "Add/Save", command = self.add_conf, width = 10, border = 3)
        self.btn_add.grid(row = 2, column = 1)
        
        self.btn_del = tk.Button(self.frame, text = "Delete", command = self.del_conf, width = 10, border = 3)
        self.btn_del.grid(row = 3, column = 1)
        
        self.btn_ingest = tk.Button(self.frame, text = "Ingest", command = self.ingest, width = 10, border = 3, background = "#75d060")
        self.btn_ingest.grid(row = 4, column = 1)
        
        self.btn_quit = tk.Button(self, text = "Quit", command = self.quit)
        self.btn_quit.grid(row = 8, column = 2)

        self.listbox = Listbox(self, width = 50)
        self.listbox.grid(row = 6, column = 2, pady = 10)
        for item in self.data.keys():
            self.listbox.insert(END, item)

        self.bar = ttk.Progressbar(self, orient = "horizontal", mode = "determinate", length = 300)
        self.bar.grid(row = 7, column = 2)
        

    def ask_dir1(self):
        adress = filedialog.askdirectory()
        self.var_base_folder.set(adress)
    

    def ask_dir2(self):
        adress = filedialog.askdirectory()
        self.var_external_folder.set(adress)

        
    def load_conf(self):
        self.name_conf = self.listbox.get(ANCHOR)
        self.var_name_conf.set(self.name_conf)
        try:
            self.var_sub_folder.set(self.data[f"{self.name_conf}"]["device_sub_folder"])
            self.var_base_folder.set(self.data[f"{self.name_conf}"]["base_folder"])
            self.var_external_folder.set(self.data[f"{self.name_conf}"]["external_folder"])
            self.var_smazat.set(self.data[f"{self.name_conf}"]["smazat"])

            self.file_extensions = self.data[f"{self.name_conf}"]["file_extensions"][0]
            for i in range(1, len(self.data[f"{self.name_conf}"]["file_extensions"])):
                self.file_extensions = self.file_extensions + "," + self.data[f"{self.name_conf}"]["file_extensions"][i] 
            self.var_file_extensions.set(self.file_extensions)
        except:
            messagebox.showerror("Preset", "Zvolený preset neexistuje!")


    def load_json(self):
        if not os.path.exists(f"data.json"):
            f = open(f"data.json", "w")
            f.close()  
        
        with open(f"data.json", "r") as file:
            try:
                self.data = json.load(file)
            except:
                self.data = {}
                self.data["Caddx"] = {  "device_sub_folder": "dron",
                                        "base_folder": "\\\\PLEXOS\plexos\lety",
                                        "external_folder": "D:/DCIM/100MEDIA",
                                        "smazat": 1,
                                        "file_extensions": [".mp4"]
                                        }
        

    def add_conf(self):
        self.name_conf = self.var_name_conf.get()
        self.base_folder = self.var_base_folder.get()
        self.sub_folder = self.var_sub_folder.get()
        self.external_folder = self.var_external_folder.get()
        self.file_extensions = self.var_file_extensions.get().split(",")
        self.smazat = self.var_smazat.get()

        self.data[f"{self.name_conf}"] = {"device_sub_folder": f"{self.sub_folder}",
                                "base_folder": f"{self.base_folder}",
                                "external_folder": f"{self.external_folder}",
                                "smazat": self.smazat,
                                "file_extensions": self.file_extensions
                                }
        self.listbox_reload()


    def listbox_reload(self):
        self.listbox.delete(0, END)
        for item in self.data.keys():
            self.listbox.insert(END, item)


    def del_conf(self):
        self.name_conf = self.listbox.get(ANCHOR)
        if self.name_conf == "":
            self.name_conf = self.var_name_conf.get()

        try:
            self.data.pop(f"{self.name_conf}")
            self.listbox_reload()
        except:
            messagebox.showerror("Preset", "Zvolený preset neexistuje!")

    
    def save_conf(self):
        os.remove(f"data.json")
        with open(f"data.json", "w") as file:
            json.dump(self.data, file, indent = 4)
    

    def ingest(self):
        self.bar["value"] = 0
        self.base_folder = self.var_base_folder.get()
        self.sub_folder = self.var_sub_folder.get()
        self.external_folder = self.var_external_folder.get()
        self.file_extensions = self.var_file_extensions.get().lower()
        self.file_extensions = self.file_extensions.split(",")
        #print(type(self.file_extensions))
        self.smazat = self.var_smazat.get()
        
        dneska = datetime.now()
        rok = str(dneska.year)
        datum = dneska.strftime("%Y-%m-%d") + " " + " "
        datum = datum.strip()
        self.output_folder = os.path.join(self.base_folder, rok, datum, self.sub_folder)

        try:
            os.makedirs(self.output_folder)
        except FileExistsError as exists:
            print("Složka existuje", exists.filename)
            print("Používám již vytvořenou složku")
        
        sd_files = os.listdir(self.external_folder)
        for i in range(0, len(self.file_extensions)):
            print(self.file_extensions[i])
            self.selected_files = [k for k in sd_files if k.endswith(self.file_extensions[i])]
        self.n_files = len(self.selected_files)
        
        threading.Thread(target=self.copy_thread).start()
       

    def copy_thread(self):
        print(f"Kopíruju {self.n_files} {self.file_extensions} Souborů do: {self.output_folder}")

        for i, file_name in enumerate(self.selected_files):
            try:
                shutil.copy2(os.path.join(self.external_folder, file_name), self.output_folder)
                self.bar["value"] = 100 * i / len(self.selected_files)
                time.sleep(1)
            except:
                print("cosi") 
        self.bar["value"] = 100
        
        if self.n_files > 0 and self.smazat == 1:
            shutil.rmtree(self.external_folder)



"""