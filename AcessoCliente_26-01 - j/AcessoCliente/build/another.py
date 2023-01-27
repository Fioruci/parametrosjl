import tkinter
import tkinter.messagebox
import customtkinter
import main, setup, run_processo, ctypes, updater

myappid = 'FYSoluções.ParametrosJL.subproduct.1.0.23.1b' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

updater.pegaChave("MAIN")
updater.pegaChave("SETUP")
updater.pegaChave("RUN_PROCESSO")
print("\nSistema atualizado na versão mais recente.")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("FY Soluções - Parâmetros")
        self.geometry(f"{290}x{320}")
        self.iconbitmap("build\\assets\\jlsoft.ico")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=80)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=(20,20), pady=(10,0))
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Sistemas: JLSoft Gestão - ME", font=customtkinter.CTkFont(size=14, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        global appearance_mode_optionemenu, appearance_mode_optionemenu2, appearance_mode_optionemenu3, appearance_mode_optionemenu4

        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["LOCALIZAÇÃO", "CM BAURU", "CM IGARATA", "CM IPERO/EXTERNO", "CM ITAPETININGA", "CM LUCELIA", "CM MANDURI", "CM PARANAPANEMA", "IPESPEN PARANAPANEMA", "PM IGARATA", "PM ILHA COMPRIDA", "PM IPERO", "PM ITAPETININGA", "PM NOVA INDEPENDENCIA", "PM UCHOA"])
        appearance_mode_optionemenu.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        appearance_mode_optionemenu2 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["SISTEMA", "Acesso", "Agua", "Almoxarifado", "Cemiterio", "Compras", "Contabilidade", "Controle Interno", "Folha", "Frota", "IPTU", "ISS", "Legislativo", "Procuradoria", "Protocolo", "Ponto", "Social", "Tesouraria"])
        appearance_mode_optionemenu2.grid(row=2, column=0, padx=20, pady=(10, 10))
        
        appearance_mode_optionemenu3 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["EXERCÍCIO", "2023", "2022", "2021"])
        appearance_mode_optionemenu3.grid(row=3, column=0, padx=20, pady=(10, 10))
        
        appearance_mode_optionemenu4 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["EMPRESA", "JLSOFT"])
        appearance_mode_optionemenu4.grid(row=4, column=0, padx=20, pady=(10, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=pegaCoisas)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=10)

        self.sidebar_button_1.configure(text="Salvar Alterações", fg_color="transparent", border_width=2, text_color=("gray10", "white"))




def pegaCoisas():
    aip = appearance_mode_optionemenu.get()
    ip = main.getKey(aip)
    
    sistema = appearance_mode_optionemenu2.get()
    exer = appearance_mode_optionemenu3.get()
    empresa = appearance_mode_optionemenu4.get()

    key = setup.setupKey(empresa)
    main.main(ip, key, exer, empresa)
    run_processo.subprocesso(sistema, exer, empresa)


def verify():
    pass

if __name__ == "__main__":
    app = App()
    app.iconbitmap(default="build\\assets\\jlsoft.ico")
    app.mainloop()