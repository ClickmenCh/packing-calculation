import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Расчёт пакет")
# icon = PhotoImage(file="logo2.png")
# root.iconphoto(False, icon)
root.geometry("400x350+700+500")
root["bg"] = "green"
root.resizable(False, False)

PET = 1.4
MPET = 1.4
BOPP = 0.91
MOPP = 0.92
LDPE = 0.92
LDPEwihte = 0.95
HDPE = 0.96
Al = 2.7
BOPPpepl = 0.72
BOPPpepl_LOBA = 0.68
Paper = 1.0

B = 0
By = 1.4
P = 2.6
M = 1.10


films = [PET, BOPP, MOPP, LDPE, MPET, LDPEwihte, HDPE, Al, BOPPpepl, BOPPpepl_LOBA, Paper]
handle = [B, By, P, M]


films_var = StringVar(value=films[0])
films_var1 = StringVar(value=films[0])

def new_win_label():
    win = Toplevel(root)
    win.title("Расчет Этикетка")
    win.geometry("400x350+950+500")
    win["bg"] = "brown"
    win.resizable(False, False)

    def clean_l():
        btn1_l.delete(0, END)
        btn1_l.insert(0, "0")

        btn2_l.delete(0, END)
        btn2_l.insert(0, "0")

        btn3_l.delete(0, END)
        btn3_l.insert(0, "0")

        mkm1_l.delete(0, END)
        mkm1_l.insert(0, "0")

        mkm2_l.delete(0, END)
        mkm2_l.insert(0, "0")

        mkm3_l.delete(0, END)
        mkm3_l.insert(0, "0")

        width1_l.delete(0, END)
        width1_l.insert(0, "")

        height1_l.delete(0, END)
        height1_l.insert(0, "")

        amount1_l.delete(0, END)
        amount1_l.insert(0, "")

    def click_l():
        p1_l = btn1_l.get()
        p1_l = float(p1_l)

        p2_l = btn2_l.get()
        p2_l = float(p2_l)

        p3_l = btn3_l.get()
        p3_l = float(p3_l)

        d1_l = mkm1_l.get()
        d1_l = int(d1_l)
        d2_l = mkm2_l.get()
        d2_l = int(d2_l)
        d3_l = mkm3_l.get()
        d3_l = int(d3_l)

        size1_l = width1_l.get()
        size1_l = int(size1_l)
        size2_l = height1_l.get()
        size2_l = int(size2_l)

        am_l = amount1_l.get()
        am_l = int(am_l)

        size_pack = (size1_l / 1000) * (size2_l / 1000)

        if p2_l <= 0 and d2_l <= 0 and p3_l <= 0 and d3_l <= 0:
            kg1_l ["text"] = "{:,}".format(round((size_pack * (p1_l * d1_l)  / 1000) * am_l, 5)).replace(",", " ")
            kgp1a_l ["text"] = "{:,}".format(round(((p1_l * d1_l) * size_pack / 1000 * am_l), 5)).replace(",", " ")
            kg_v1000a_l ["text"] = "{:,}".format(round(((p1_l * d1_l) * size_pack), 5)).replace(",", " ")

        elif p3_l <= 0 and d3_l <= 0:
            kg1_l ["text"] = "{:,}".format(
                round((size_pack * (p1_l * d1_l + p2_l * d2_l) / 1000) * am_l, 5)).replace(",", " ")

            kgp1a_l ["text"] = "{:,}".format(
                round(((p1_l * d1_l + p2_l * d2_l) * size_pack * am_l * (p1_l * d1_l) / (p1_l * d1_l + p2_l * d2_l) / 1000), 5)).replace(",", " ")
            kgp2a_l ["text"] = "{:,}".format(
                round(((p1_l * d1_l + p2_l * d2_l) * size_pack * am_l * (p2_l * d2_l) / (p1_l * d1_l + p2_l * d2_l) / 1000), 5)).replace(",", " ")
            kg_v1000a_l ["text"] = "{:,}".format(
                round((size_pack * (p1_l * d1_l + p2_l * d2_l) / 1000) * 1000, 5)).replace(",", " ")

        else:
            kg1_l ["text"] = "{:,}".format(
                round((size_pack * (p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) / 1000) * am_l, 5)).replace(",", " ")
            kgp1a_l ["text"] = "{:,}".format(
                round(((p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) * size_pack * am_l * (p1_l * d1_l) / (p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) / 1000), 5)).replace(",", " ")
            kgp2a_l ["text"] = "{:,}".format(
                round(((p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) * size_pack * am_l * (p2_l * d2_l) / (p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) / 1000), 5)).replace(",", " ")
            kgp3a_l ["text"] = "{:,}".format(
                round(((p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) * size_pack * am_l * (p3_l * d3_l) / (p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) / 1000), 5)).replace(",", " ")
            kg_v1000a_l ["text"] = "{:,}".format(
                round((size_pack * (p1_l * d1_l + p2_l * d2_l + p3_l * d3_l) / 1000) * 1000, 5)).replace(",", " ")

    btn1_l = ttk.Combobox(win, textvariable=films_var1, values=films, justify="center")
    btn1_l.place(x=80, y=30, anchor="center", relwidth="0.30", relheight="0.10")

    btn2_l = ttk.Combobox(win, values=films, justify="center")
    btn2_l.place(x=80, y=70, anchor="center", relwidth="0.30", relheight="0.10")
    btn2_l.insert(0, "0")

    btn3_l = ttk.Combobox(win, values=films, justify="center")
    btn3_l.place(x=80, y=110, anchor="center", relwidth="0.30", relheight="0.10")
    btn3_l.insert(0, "0")

    mkm1_l = ttk.Entry(win, justify="center")
    mkm1_l.place(x=190, y=30, anchor="center", relwidth="0.20", relheight="0.10")
    mkm1_l.insert(0, "0")

    mkm2_l = ttk.Entry(win, justify="center")
    mkm2_l.place(x=190, y=70, anchor="center", relwidth="0.20", relheight="0.10")
    mkm2_l.insert(0, "0")

    mkm3_l = ttk.Entry(win, justify="center")
    mkm3_l.place(x=190, y=110, anchor="center", relwidth="0.20", relheight="0.10")
    mkm3_l.insert(0, "0")

    kgp1_l = ttk.Label(win, text="кг.  ", font=("Arial 10 bold"), background="brown")
    kgp1_l.place(x=250, y=20)

    kgp1a_l = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="brown")
    kgp1a_l.place(x=330, y=31, anchor="center", relwidth="0.27", relheight="0.08")

    kgp2_l = ttk.Label(win, text="кг.  ", font=("Arial 10 bold"), background="brown")
    kgp2_l.place(x=250, y=60)

    kgp2a_l = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="brown")
    kgp2a_l.place(x=330, y=70, anchor="center", relwidth="0.27", relheight="0.08")

    kgp3_l = ttk.Label(win, text="кг.  ", font=("Arial 10 bold"), background="brown")
    kgp3_l.place(x=250, y=100)

    kgp3a_l = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="brown")
    kgp3a_l.place(x=330, y=110, anchor="center", relwidth="0.27", relheight="0.08")

    kg_v1000_l = ttk.Label(win, text="кг./тыс.шт.", font=("Arial 14 italic bold"), foreground="blue", background="brown")
    kg_v1000_l.place(x=240, y=205)

    kg_v1000a_l = ttk.Label(win, justify="center", font=("Arial 14 italic bold"), foreground="blue", background="brown")
    kg_v1000a_l.place(x=310, y=250, anchor="center", relwidth="0.27", relheight="0.08")

    width_l = ttk.Label(win, text="Ширина, мм", font=("Arial 9 italic bold"), background="brown")
    width_l.place(x=18, y=140)

    width1_l = ttk.Entry(win, justify="center")
    width1_l.place(x=170, y=150, anchor="center", relwidth="0.30", relheight="0.08")

    height_l = ttk.Label(win, text="Высота, мм", font=("Arial 9 italic bold"), background="brown")
    height_l.place(x=18, y=170)

    height1_l = ttk.Entry(win, justify="center")
    height1_l.place(x=170, y=180, anchor="center", relwidth="0.30", relheight="0.08")

    amount_l = ttk.Label(win, text="Количество шт.", font=("Arial 9 bold"), background="brown")
    amount_l.place(x=18, y=210)

    amount1_l = ttk.Entry(win, justify="center")
    amount1_l.place(x=170, y=220, anchor="center", relwidth="0.25", relheight="0.08")

    kg_l = ttk.Label(win, text="Количество кг.", font=("Arial 9 bold"), foreground="black", background="brown")
    kg_l.place(x=18, y=240)

    kg1_l = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="brown")
    kg1_l.place(x=195, y=250, anchor="center", relwidth="0.25", relheight="0.08")

    cl_l = ttk.Button(win, text="Решение", command=click_l)
    cl_l.place(x=100, y=300, anchor="center", relwidth="0.38", relheight="0.08")

    cln_l = ttk.Button(win, text="Очистить", command=clean_l)
    cln_l.place(x=300, y=300, anchor="center", relwidth="0.38", relheight="0.08")

def new_win_film():
    win = Toplevel(root)
    win.title("Расчет Плёнка")
    win.geometry("400x350+500+320")
    win["bg"] = "orange"
    win.resizable(False, False)

    # m = Menu(new_win_film)
    # new_win_film.config(menu=m)
    # fm = Menu(m)
    # m.add_cascade(label="Этикетка", command=new_win_label)  # , menu=fm)
    # # fm.add_command(label="Расчет-Плёнка", command=self.new_win)
    # m.add_cascade(label="Плёнка", command=new_win_film)

    def clean_p():
        btn1_p.delete(0, END)
        btn1_p.insert(0, "0")

        btn2_p.delete(0, END)
        btn2_p.insert(0, "0")

        btn3_p.delete(0, END)
        btn3_p.insert(0, "0")

        mkm1_p.delete(0, END)
        mkm1_p.insert(0, "0")

        mkm2_p.delete(0, END)
        mkm2_p.insert(0, "0")

        mkm3_p.delete(0, END)
        mkm3_p.insert(0, "0")

        width1_p.delete(0, END)
        width1_p.insert(0, "")

        # height1_p.delete(0, END)
        # height1_p.insert(0, "")

        kilogram1_p.delete(0, END)
        kilogram1_p.insert(0, "")

        kgp1a_p.config (text = " ")
        kgp2a_p.config (text = " ")
        kgp3a_p.config (text = " ")
        meter1.config  (text = " ")

    def click_p():
        p1_p = btn1_p.get()
        p1_p = float(p1_p)

        p2_p = btn2_p.get()
        p2_p = float(p2_p)

        p3_p = btn3_p.get()
        p3_p = float(p3_p)

        d1_p = mkm1_p.get()
        d1_p = int(d1_p)
        d2_p = mkm2_p.get()
        d2_p = int(d2_p)
        d3_p = mkm3_p.get()
        d3_p = int(d3_p)

        size1_p = width1_p.get()
        size1_p = int(size1_p)
        # size2_p = height1_p.get()
        # size2_p = int(size2_p)

        kg = kilogram1_p.get()
        kg = int(kg)

        size_pack = (size1_p  / 1000 * 1)

        if p2_p <= 0 and d2_p <= 0 and p3_p <= 0 and d3_p <= 0:
            kgp1a_p ["text"] = "{:,}".format(round(kg, 2)).replace(",", " ")
            meter1["text"] = "{:,}".format(round(kg / ((p1_p * d1_p) * (size1_p /1000)) * 1000, 2)).replace(",", " ")


        elif p3_p <= 0 and d3_p <= 0:
            kgp1a_p ["text"] = "{:,}".format(round((kg * (p1_p * d1_p) / (p1_p * d1_p + p2_p * d2_p)), 2)).replace(",", " ")
            kgp2a_p ["text"] = "{:,}".format(round((kg * (p2_p * d2_p) / (p1_p * d1_p + p2_p * d2_p)), 2)).replace(",", " ")
            meter1["text"] = "{:,}".format(round(kg / ((p1_p * d1_p + p2_p * d2_p) * (size1_p / 1000)) * 1000, 2)).replace(",", " ")


        else:
            kgp1a_p["text"] = "{:,}".format(round((kg * (p1_p * d1_p) / (p1_p * d1_p + p2_p * d2_p + p3_p * d3_p)), 2)).replace(",", " ")
            kgp2a_p["text"] = "{:,}".format(round((kg * (p2_p * d2_p) / (p1_p * d1_p + p2_p * d2_p + p3_p * d3_p)), 2)).replace(",", " ")
            kgp3a_p["text"] = "{:,}".format(round((kg * (p3_p * d3_p) / (p1_p * d1_p + p2_p * d2_p + p3_p * d3_p)), 2)).replace(",", " ")
            meter1["text"] = "{:,}".format(round(kg / ((p1_p * d1_p + p2_p * d2_p + p3_p * d3_p) * (size1_p / 1000)) * 1000, 2)).replace(",", " ")


    btn1_p = ttk.Combobox(win, textvariable=films_var1, values=films, justify="center")
    btn1_p.place(x=80, y=30, anchor="center", relwidth="0.30", relheight="0.10")

    btn2_p = ttk.Combobox(win, values=films, justify="center")
    btn2_p.place(x=80, y=70, anchor="center", relwidth="0.30", relheight="0.10")
    btn2_p.insert(0, "0")

    btn3_p = ttk.Combobox(win, values=films, justify="center")
    btn3_p.place(x=80, y=110, anchor="center", relwidth="0.30", relheight="0.10")
    btn3_p.insert(0, "0")

    mkm1_p = ttk.Entry(win, justify="center")
    mkm1_p.place(x=190, y=30, anchor="center", relwidth="0.20", relheight="0.10")
    mkm1_p.insert(0, "0")

    mkm2_p = ttk.Entry(win, justify="center")
    mkm2_p.place(x=190, y=70, anchor="center", relwidth="0.20", relheight="0.10")
    mkm2_p.insert(0, "0")

    mkm3_p = ttk.Entry(win, justify="center")
    mkm3_p.place(x=190, y=110, anchor="center", relwidth="0.20", relheight="0.10")
    mkm3_p.insert(0, "0")

    kgp1_p = ttk.Label(win, text="кг.  ", font=("Arial 10 bold"), background="orange")
    kgp1_p.place(x=250, y=20)

    kgp1a_p = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="orange")
    kgp1a_p.place(x=330, y=31, anchor="center", relwidth="0.27", relheight="0.08")

    kgp2_p = ttk.Label(win, text="кг.  ", font=("Arial 10 bold"), background="orange")
    kgp2_p.place(x=250, y=60)

    kgp2a_p = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="orange")
    kgp2a_p.place(x=330, y=70, anchor="center", relwidth="0.27", relheight="0.08")

    kgp3_p = ttk.Label(win, text="кг.  ", font=("Arial 10 bold"), background="orange")
    kgp3_p.place(x=250, y=100)

    kgp3a_p = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="orange")
    kgp3a_p.place(x=330, y=110, anchor="center", relwidth="0.27", relheight="0.08")

    width_p = ttk.Label(win, text="Ширина, мм", font=("Arial 9 italic bold"), background="orange")
    width_p.place(x=18, y=140)

    width1_p = ttk.Entry(win, justify="center")
    width1_p.place(x=170, y=150, anchor="center", relwidth="0.30", relheight="0.08")

    # height_p = ttk.Label(win, text="Высота, мм", font=("Arial 9 italic bold"), background="orange")
    # height_p.place(x=18, y=170)

    # height1_p = ttk.Entry(win, justify="center")
    # height1_p.place(x=170, y=180, anchor="center", relwidth="0.30", relheight="0.08")

    kilogram_p = ttk.Label(win, text="Количество кг", font=("Arial 9 bold"), background="orange")
    kilogram_p.place(x=18, y=210)

    kilogram1_p= ttk.Entry(win, justify="center")
    kilogram1_p.place(x=170, y=220, anchor="center", relwidth="0.25", relheight="0.08")

    meter = ttk.Label(win, text="Пагонных метров:", font=("Arial 9 bold"), background="orange")
    meter.place(x=18, y=250)

    meter1 = ttk.Label(win, justify="center", font=("Arial 10 bold"), foreground="black", background="orange")
    meter1.place(x=185, y=260, anchor="center", relwidth="0.27", relheight="0.08")

    cl_p = ttk.Button(win, text="Решение", command=click_p)
    cl_p.place(x=100, y=300, anchor="center", relwidth="0.38", relheight="0.08")

    cln_p = ttk.Button(win, text="Очистить", command=clean_p)
    cln_p.place(x=300, y=300, anchor="center", relwidth="0.38", relheight="0.08")


m = Menu(root)
root.config(menu=m)
fm=Menu(m)
m.add_cascade(label="Этикетка", command=new_win_label) #, menu=fm)
# fm.add_command(label="Расчет-Плёнка", command=self.new_win)
m.add_cascade(label="Плёнка", command=new_win_film)



def clean():

    btn1.delete(0,END)
    btn1.insert(0, "0")

    btn2.delete(0, END)
    btn2.insert(0, "0")

    btn3.delete(0, END)
    btn3.insert(0, "0")

    mkm1.delete(0, END)
    mkm1.insert(0, "0")

    mkm2.delete(0, END)
    mkm2.insert(0, "0")

    mkm3.delete(0, END)
    mkm3.insert(0, "0")

    width1.delete(0, END)
    width1.insert(0, " ")

    height1.delete(0, END)
    height1.insert(0, " ")

    hdl.delete(0, END)
    hdl.insert(0, "0")

    amount1.delete(0, END)
    amount1.insert(0, " ")

    kg1.config (text = " ")
    kgp1a.config (text = " ")
    kgp2a.config (text = " ")
    kgp3a.config (text = " ")
    kg_v1000a.config(text = " ")


def click():

    kgp1a.config(text=" ")
    kgp2a.config(text=" ")
    kgp3a.config(text=" ")

    p1 = btn1.get()
    p1 = float(p1)

    p2 = btn2.get()
    p2 = float(p2)

    p3 = btn3.get()
    p3 = float(p3)

    d1 = mkm1.get()
    d1 = int(d1)
    d2 = mkm2.get()
    d2 = int(d2)
    d3 = mkm3.get()
    d3 = int(d3)

    size1 = width1.get()
    size1 = int(size1)
    size2 = height1.get()
    size2 = int(size2)

    handle = hdl.get()
    handle = float(handle)

    am = amount1.get()
    am = int(am)

    size_pack = (size1 * 2 / 1000)*(size2 / 1000)


    if p2 <= 0 and d2 <= 0 and p3 <= 0 and d3 <= 0:
        kg1["text"] = "{:,}".format(round(((size_pack * (p1 * d1) + handle)/ 1000) * am, 5)).replace(",", " ")

        kgp1a["text"] = "{:,}".format(round(((p1 * d1) * size_pack / 1000 * am), 5)).replace(",", " ")

        kg_v1000a["text"] = "{:,}".format(round(((p1 * d1) * size_pack), 5)).replace(",", " ")


    elif p3 <= 0 and d3 <= 0:

        kg1["text"] = "{:,}".format(round(((size_pack * (p1 * d1 + p2 * d2) + handle) / 1000) * am, 5)).replace(",", " ")

        kgp1a["text"] = "{:,}".format(
            round(((p1 * d1 + p2 * d2) * size_pack * am * (p1 * d1) / (p1 * d1 + p2 * d2) / 1000), 5)).replace(",", " ")

        kgp2a["text"] = "{:,}".format(
            round(((p1 * d1 + p2 * d2) * size_pack * am * (p2 * d2) / (p1 * d1 + p2 * d2) / 1000), 5)).replace(",", " ")

        kg_v1000a["text"] = "{:,}".format(
            round(((size_pack * (p1 * d1 + p2 * d2) + handle) / 1000) * 1000, 5)).replace(",", " ")

    else:
        kg1["text"] = "{:,}".format(round(((size_pack * (p1 * d1 + p2 * d2 + p3 * d3) + handle) / 1000) * am, 5)).replace(",", " ")

        kgp1a["text"] = "{:,}".format(
            round(((p1 * d1 + p2 * d2 + p3 * d3) * size_pack * am * (p1 * d1) / (p1 * d1 + p2 * d2 + p3 * d3) / 1000), 5)).replace(",", " ")

        kgp2a["text"] = "{:,}".format(
            round(((p1 * d1 + p2 * d2 + p3 * d3) * size_pack * am * (p2 * d2) / (p1 * d1 + p2 * d2 + p3 * d3) / 1000), 5)).replace(",", " ")

        kgp3a["text"] = "{:,}".format(
            round(((p1 * d1 + p2 * d2 + p3 * d3) * size_pack * am * (p3 * d3) / (p1 * d1 + p2 * d2 + p3 * d3) / 1000),
                  5)).replace(",", " ")

        kg_v1000a["text"] = "{:,}".format(
            round(((size_pack * (p1 * d1 + p2 * d2 + p3 * d3) + handle) / 1000) * 1000, 5)).replace(",", " ")


btn1 = ttk.Combobox(root, textvariable=films_var, values = films, justify="center")
btn1.place(x=80, y=30,  anchor="center", relwidth= "0.30", relheight="0.10")

btn2 = ttk.Combobox(root, values=films, justify="center")
btn2.place(x=80, y=70, anchor="center", relwidth= "0.30", relheight="0.10")
btn2.insert(0, "0")

btn3 = ttk.Combobox(root, values=films, justify="center")
btn3.place(x=80, y=110, anchor="center", relwidth= "0.30", relheight="0.10")
btn3.insert(0, "0")

mkm1 = ttk.Entry(root, justify="center")
mkm1.place(x=190, y=30, anchor="center", relwidth= "0.20", relheight="0.10")
mkm1.insert(0, "0")

mkm2 = ttk.Entry(root, justify="center")
mkm2.place(x=190, y=70, anchor="center", relwidth= "0.20", relheight="0.10")
mkm2.insert(0, "0")

mkm3 = ttk.Entry(root, justify="center")
mkm3.place(x=190, y=110, anchor="center", relwidth= "0.20", relheight="0.10")
mkm3.insert(0, "0")

kgp1 = ttk.Label(root, text="кг.  ", font=("Arial 10 bold"), background = "green")
kgp1.place(x=250, y=20)

kgp1a = ttk.Label(root, justify="center", font=("Arial 10 bold"), foreground="black", background = "green")
kgp1a.place(x=330, y=31, anchor="center", relwidth= "0.27", relheight="0.08")

kgp2 = ttk.Label(root, text="кг.  ", font=("Arial 10 bold"), background = "green")
kgp2.place(x=250, y=60)

kgp2a = ttk.Label(root, justify="center", font=("Arial 10 bold"), foreground="black", background = "green")
kgp2a.place(x=330, y=70, anchor="center", relwidth= "0.27", relheight="0.08")

kgp3 = ttk.Label(root, text="кг.  ", font=("Arial 10 bold"), background = "green")
kgp3.place(x=250, y=100)

kgp3a = ttk.Label(root, justify="center", font=("Arial 10 bold"), foreground="black", background = "green")
kgp3a.place(x=330, y=110, anchor="center", relwidth= "0.27", relheight="0.08")

kg_v1000 = ttk.Label(root, text="кг./тыс.шт.", font=("Arial 14 italic bold"), foreground="blue", background = "green")
kg_v1000.place(x=240, y=205)

kg_v1000a = ttk.Label(root, justify="center", font=("Arial 14 italic bold"), foreground="blue", background = "green")
kg_v1000a.place(x=310, y=250, anchor="center", relwidth= "0.27", relheight="0.08")

width = ttk.Label(root, text="Ширина, мм", font=("Arial 9 italic bold"), background = "green")
width.place(x=18, y=140)

width1 = ttk.Entry(root, justify="center")
width1.place(x=130, y=150, anchor="center", relwidth= "0.15", relheight="0.08")

height = ttk.Label(root, text="Высота, мм", font=("Arial 9 italic bold"), background = "green")
height.place(x=18, y=170)

height1 = ttk.Entry(root, justify="center")
height1.place(x=130, y=180, anchor="center", relwidth= "0.15", relheight="0.08")

hdl = ttk.Combobox(root, values=handle, justify="center")
hdl.place(x=195, y=165,  anchor="center", relwidth= "0.17", relheight="0.165")
hdl.insert(0, "0")

amount = ttk.Label(root, text="Количество шт.", font=("Arial 9 bold"), background = "green")
amount.place(x=18, y=210)

amount1 = ttk.Entry(root, justify="center")
amount1.place(x=170, y=220, anchor="center", relwidth= "0.25", relheight="0.08")

kg = ttk.Label(root, text="Количество кг.", font=("Arial 9 bold"), foreground="black", background = "green")
kg.place(x=18, y=240)

kg1 = ttk.Label(root, justify="center", font=("Arial 10 bold"), foreground="black", background = "green")
kg1.place(x=195, y=250, anchor="center", relwidth= "0.25", relheight="0.08")

cl = ttk.Button(root, text="Решение", command = click)
cl.place(x=100, y=300, anchor="center", relwidth= "0.38", relheight="0.08")

cln = ttk.Button(root, text="Очистить", command=clean)
cln.place(x=300, y=300, anchor="center", relwidth= "0.38", relheight="0.08")





root.mainloop()