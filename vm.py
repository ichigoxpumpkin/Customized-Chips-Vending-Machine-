import tkinter as tk

class VendingMachine:

    transitions = {
        "q0": {"a": ("q1", 0), "b": ("q2", 0), "c": ("q3", 0)},
        "q1": {"d": ("q4", 5)},
        "q2": {"d": ("q4", 10)},
        "q3": {"d": ("q4", 20)},
        "q4": {"e": ("q4b", 0), "f": ("q5", 0)},
        "q5": {"g": ("q6", 0), "h": ("q7", 0), "i": ("q8", 0), "j": ("q9", 0), "k": ("q10", 0)},
        "q6": {"l": ("q11", 0), "m": ("q12", 0), "n": ("q13", 0), "o": ("q14", 0), "p": ("q15", 0)},
        "q7": {"l": ("q11", 0), "m": ("q12", 0), "n": ("q13", 0), "o": ("q14", 0), "p": ("q15", 0)},
        "q8": {"l": ("q11", 0), "m": ("q12", 0), "n": ("q13", 0), "o": ("q14", 0), "p": ("q15", 0)},
        "q9": {"l": ("q11", 0), "m": ("q12", 0), "n": ("q13", 0), "o": ("q14", 0), "p": ("q15", 0)},
        "q10": {"l": ("q11", 0), "m": ("q12", 0), "n": ("q13", 0), "o": ("q14", 0), "p": ("q15", 0)},
        "q11": {"q": ("q16", 1)},
        "q12": {"q": ("q16", 1)},
        "q13": {"q": ("q16", 1)},
        "q14": {"q": ("q16", 1)},
        "q15": {"q": ("q16", 1)},
        "q16": {},
        "q4b":{}
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")
        self.root.resizable(False, False)
        self.current_state = "q0"
        self.state = ['q0']
        
        self.create_size_menu()
        
    def create_size_menu(self):
        self.clear_frame() 
        self.set_bg()
        
        label = tk.Label(self.root, text="Select size:")
        label.pack(pady=115)
        
        self.small_img = tk.PhotoImage(file="assets/small.png")
        self.medium_img = tk.PhotoImage(file="assets/medium.png")
        self.large_img = tk.PhotoImage(file="assets/large.png")

        size_buttons = [
            ("Small", "a", self.small_img, 70, 190),
            ("Medium", "b", self.medium_img, 142, 165),
            ("Large", "c", self.large_img, 225, 155)
        ]

        for name, state, img, lx, ly in size_buttons:
            button = tk.Button(self.root, image=img, borderwidth=0, command=lambda name=name,state=state:self.confirm_menu(name, state))
            button.place(x=lx, y=ly)

    def confirm_menu(self, name, state):
        self.clear_frame() 
        self.set_bg()

        self.current_state, _ = self.update_state(state)

        label = tk.Label(self.root, text="Konfirmasi")
        label.pack(pady=115)

        label = tk.Label(self.root, text=f"Size: {name}")
        label.place(x=135,y=160)

        price = 5000 if name == "Small" else (10000 if name == "Medium" else 20000)

        label = tk.Label(self.root, text=f"Price: Rp. {price}")
        label.place(x=135,y=180)

        continue_button = tk.Button(self.root, text="Lanjutkan", command=self.display_payment_menu)
        continue_button.place(x=145,y=240)

    def display_payment_menu(self):
        self.clear_frame()
        self.set_bg()

        self.current_state, price = self.update_state("d")
        label = tk.Label(self.root, text="Total Harga:")
        label.pack(pady=115)
        
        details_label = tk.Label(self.root, text=f"Rp {5000 if price == 5 else (10000 if price == 10 else 20000)}")
        details_label.pack()
        
        confirm_button = tk.Button(self.root, text="Lanjut", command=self.create_type_menu)
        confirm_button.place(x=130,y=275)

        cancel_button = tk.Button(self.root, text="Batal", command=self.cancel_order)
        cancel_button.place(x=190,y=275)

        self.qr_img = tk.PhotoImage(file="assets/qr.png")
        qr =  tk.Label(self.root, image=self.qr_img)
        qr.place(x=130, y=150)

    def create_type_menu(self):
        self.clear_frame() 
        self.set_bg()

        self.current_state, _ = self.update_state("f")
        
        label = tk.Label(self.root, text="Pilih Jenis Keripik")
        label.pack(pady=115)
        
        self.tempe_img = tk.PhotoImage(file="assets/tempe.png")
        self.singkong_img = tk.PhotoImage(file="assets/singkong.png")
        self.kentang_img = tk.PhotoImage(file="assets/kentang.png")
        self.talas_img = tk.PhotoImage(file="assets/talas.png")
        self.ubi_img = tk.PhotoImage(file="assets/ubi.png")

        type_buttons = [
            ("Kentang", "g", self.kentang_img, 225, 135),
            ("Singkong", "h", self.singkong_img, 142, 135),
            ("Tempe", "i", self.tempe_img, 70, 135),
            ("Talas", "j", self.talas_img, 70, 225),
            ("Ubi Jalar", "k" , self.ubi_img, 142, 225)
        ]
        
        for name, state, img, lx, ly in type_buttons:
            button = tk.Button(self.root, image=img, borderwidth=0, command=lambda state=state,name=name: self.select_type(name,state))
            button.place(x=lx, y=ly)

    def select_type(self, name, state):
        self.type = name
        self.current_state, _ = self.update_state(state)
        self.create_seasoning_menu()

    def create_seasoning_menu(self):
        self.clear_frame() 
        self.set_bg()

        label = tk.Label(self.root, text="Pilih Bumbu")
        label.pack(pady=115)
        
        self.balado_img = tk.PhotoImage(file="assets/balado.png")
        self.bbq_img = tk.PhotoImage(file="assets/bbq.png")
        self.keju_img = tk.PhotoImage(file="assets/keju.png")
        self.jagung_img = tk.PhotoImage(file="assets/jagung.png")
        self.laut_img = tk.PhotoImage(file="assets/laut.png")

        seasoning_buttons = [
            ("Balado", "l", self.balado_img, 70, 135),
            ("BBQ", "m", self.bbq_img, 148, 135),
            ("Keju", "n", self.keju_img, 225, 135),
            ("Jagung Bakar", "o", self.jagung_img, 90, 225),
            ("Rumput Laut", "p", self.laut_img, 182, 225)
        ]
        
        for name, state, img, lx, ly in seasoning_buttons:
            button = tk.Button(self.root, image=img, borderwidth=0, command=lambda state=state,name=name: self.select_seasoning(name,state))
            button.place(x=lx, y=ly)

    def select_seasoning(self, name,state):
        self.seasoning = name
        self.current_state, _ = self.update_state(state)
        self.current_state, _ = self.update_state("q")
        self.complete_order()

    def confirmation_payment(self):
        self.current_state = self.update_state("Q")
        self.complete_order()

    def complete_order(self):
        self.clear_frame()
        self.set_bg()

        label = tk.Label(self.root, text="Pesanan Anda telah selesai!")
        label.pack(pady=155)

        state = f"State yang dilalui:\n {self.state}"
        state_label = tk.Label(self.root, text=state)
        state_label.place(x=80,y=200)
        
    def cancel_order(self):
        self.clear_frame()
        self.set_bg()
        self.current_state, _ = self.update_state("e")
        self.complete_order()
    
    def update_state(self, state):
        next_state, output = self.transitions[self.current_state].get(state)
        self.state.append(next_state)
        return next_state, output
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def set_bg(self):
        self.root.geometry("357x600")
        self.img_bg = tk.PhotoImage(file="assets/background.png")
        background = tk.Label(self.root, image=self.img_bg)
        background.place(x=0, y=0, relwidth=1, relheight=1)

        
if __name__ == "__main__":
    root = tk.Tk()
    vending_machine = VendingMachine(root)
    root.mainloop()