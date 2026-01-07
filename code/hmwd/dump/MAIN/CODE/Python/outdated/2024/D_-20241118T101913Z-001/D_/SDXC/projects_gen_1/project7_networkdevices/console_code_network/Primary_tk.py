from datetime import datetime

from tkinter import *
import subprocess, os, time, platform, threading

from console_code_network import primary_program
from console_code_network.primary_program import *


def network_satus_run():
    print("network satus can run")
    global x
    global test

    x = 1
    system = 0
    count = 0
    prev_min = 5
    system_health = "Unknown"
    main = Tk()

    for widget in main.winfo_children():
        widget.destroy()

    main.attributes("-fullscreen", True)

    main.config(bg="black")

    main.resizable(False, False)
    main.title("Primary Telemetry")
    main.columnconfigure(0, weight=1)
    main.columnconfigure(1, weight=1)
    main.columnconfigure(2, weight=1)
    main.columnconfigure(3, weight=1)
    main.columnconfigure(4, weight=1)
    main.columnconfigure(5, weight=1)
    main.columnconfigure(6, weight=1)

    main.rowconfigure(0, weight=1)
    main.rowconfigure(1, weight=1)
    main.rowconfigure(2, weight=1)
    main.rowconfigure(3, weight=1)
    main.rowconfigure(4, weight=1)
    main.rowconfigure(5, weight=1)
    main.rowconfigure(6, weight=1)
    main.rowconfigure(7, weight=1)
    main.rowconfigure(8, weight=1)
    main.rowconfigure(9, weight=1)
    system_satus = Label(main, text="Network Devices statuses",
                         font='Impact 19')
    system_satus_message = Label(main,
                                 text="INFO: the items on the network seem to be in a BAD state currently, this requires attention",
                                 font=20)
    system_satus_message.config(bg="white")
    system_count = Label(text="Num:", font=6)

    header1 = Label(text="\/ Highest \/ (2)", font='Impact 16', bg="black", fg="white")
    header2 = Label(text="\/ Meduim \/(1-0.25)", font='Impact 14', bg="black", fg="white")
    header2b = Label(text="\/ Meduim \/(1-0.25)", font='Impact 14', bg="black", fg="white")
    header3 = Label(text="\/ Lowest \/(0.125-0)priortiy", font='Impact 12', bg="black", fg="white")
    item1 = Label(main, text="Wifi Hub(192.168.01)", font=10,width=29)
    item2 = Label(main, text="Booster(192.168.0.26)", font=10,width=29)
    item3 = Label(main, text="Blink Module(192.168.0.6)", font=10,width=29)
    item4 = Label(main, text="Silver Laptop(192.168.0.7)", font=10,width=29)
    item5 = Label(main, text="Blue laptop(192.168.0.70)", font=10,width=29)
    item6 = Label(main, text="Haydens Iphone(192.168.0.53)", font=10,width=29)
    item7 = Label(main, text="Megans Iphone(192.168.0.50)", font=10,width=29)
    item8 = Label(main, text="PS5(192.169.0.43)", font=10,width=29)
    item9 = Label(main, text="PS4(192.168.0.51)", font=10,width=29)
    item10 = Label(main, text="Printer(192.168.0.16)", font=10,width=29)
    item11 = Label(main, text="HaysTV(192.168.0.24)", font=10,width=29)
    item12 = Label(main, text="Tinas Iphone(192.168.0.52)", font=10,width=29)
    item13 = Label(main, text="Ross Iphone(192.168.0.55)", font=10,width=29)
    item14 = Label(main, text="FrontTv(192.168.0.3)", font=10,width=29)

    test = Label(main, text=x, font=6)

    def system_flash():

        global count

        current_colour = main.cget("bg")

        if current_colour == "red":



            main.config(bg="#FF5F15")

            system_satus.config(bg="red")
        elif current_colour == "#FF5F15":

            main.config(bg="red")

        else:
            pass

        if count > 5:

            return
        else:
            main.after(200, system_flash)
            count = count + 1

    def system_time(arg):
        global prev_min
        current_time = datetime.now()
        hours = current_time.strftime("%H")
        minutes = current_time.strftime("%M")
        print(minutes)

        if minutes != prev_min:
            prev_min = minutes.copy()
            print(prev_min)
            return 0
        else:
            pass

    def update():

        # Global Variables for General Use
        global test
        global x

        x = x + 1
        global a
        global b
        global c
        global count
        count = 0
        global system
        system = 0
        global system2
        system2 = 0


        global item1_sy, item2_sy, item3_sy, item4_sy, item5_sy
        global item6_sy, item7_sy, item8_sy, item9_sy, item10_sy
        global item11_sy, item12_sy, item13_sy, item14_sy, item15_sy
        global item16_sy, item17_sy, item18_sy, item19_sy, item20_sy
        global item21_sy, item22_sy, item23_sy, item24_sy, item25_sy
        global item26_sy, item27_sy, item28_sy, item29_sy, item30_sy
        global item31_sy, item32_sy, item33_sy, item34_sy


        item1_sy = 0
        item2_sy = 0
        item3_sy = 0
        item4_sy = 0
        item5_sy = 0
        item6_sy = 0
        item7_sy = 0
        item8_sy = 0
        item9_sy = 0
        item10_sy = 0
        item11_sy = 0
        item12_sy = 0
        item13_sy = 0
        item14_sy = 0
        item15_sy = 0
        item16_sy = 0
        item17_sy = 0
        item18_sy = 0
        item19_sy = 0
        item20_sy = 0
        item21_sy = 0
        item22_sy = 0
        item23_sy = 0
        item24_sy = 0
        item25_sy = 0
        item26_sy = 0
        item27_sy = 0
        item28_sy = 0
        item29_sy = 0
        item30_sy = 0
        item31_sy = 0
        item32_sy = 0
        item33_sy = 0
        item34_sy = 0

        # Global Variables for Status
        global item1_satus, item2_satus, item3_satus, item4_satus, item5_satus
        global item6_satus, item7_satus, item8_satus, item9_satus, item10_satus
        global item11_satus, item12_satus, item13_satus, item14_satus, item15_satus
        global item16_satus, item17_satus, item18_satus, item19_satus, item20_satus
        global item21_satus, item22_satus, item23_satus, item24_satus, item25_satus
        global item26_satus, item27_satus, item28_satus, item29_satus, item30_satus
        global item31_satus, item32_satus, item33_satus, item34_satus

        # Global Variables for Health
        global item1_health, item2_health, item3_health, item4_health, item5_health
        global item6_health, item7_health, item8_health, item9_health, item10_health
        global item11_health, item12_health, item13_health, item14_health, item15_health
        global item16_health, item17_health, item18_health, item19_health, item20_health
        global item21_health, item22_health, item23_health, item24_health, item25_health
        global item26_health, item27_health, item28_health, item29_health, item30_health
        global item31_health, item32_health, item33_health, item34_health



        item1_satus = primary_program.hub_wifi(1)

        if item1_satus == "Bad":
            item1.config(bg="Red")
            if item1_sy == 0:
                system = system + 2
                item1_sy += 0.5
        else:
            item1.config(bg="Green")
            item1_sy = 0

        item2_satus = primary_program.booster_hub(1)

        if item2_satus == "Bad":
            item2.config(bg="Red")

            if item2_sy == 0:
                system = system + 1

                item2_sy += 0.5
        else:
            item2.config(bg="Green")
            item2_sy = 0

        item3_satus = primary_program.blink_mod(1)

        if item3_satus == "Bad":
            item3.config(bg="Red")

            if item3_sy == 0:
                system = system + 2

                item3_sy += 0.5
        else:
            item3.config(bg="Green")
            item3_sy = 0

        item4_satus = primary_program.silver_laptop(1)

        if item4_satus == "Bad":
            item4.config(bg="Red")
            if item4_sy == 0:
                system = system + 0.25  #has a lower infuence
                item4_sy += 0.5

        else:
            item4.config(bg="Green")
            item4_sy = 0

        item5_satus = primary_program.blue_laptop(1)

        if item5_satus == "Bad":
            item5.config(bg="Red")
            if item5_sy == 0:
                system = system + 0.25  # has a lower infuence
                item5_sy += 0.5

        else:
            item5.config(bg="Green")
            item5_sy = 0

        item6_satus = primary_program.haydens_iphone(1)

        if item6_satus == "Bad":
            item6.config(bg="Red")
            if item6_sy == 0:
                system = system + 0.125  # has a lower infuence
                item6_sy += 0.5

        else:
            item6.config(bg="Green")
            item6_sy = 0

        item7_satus = primary_program.megans_iphone(1)

        if item7_satus == "Bad":
            item7.config(bg="Red")
            if item7_sy == 0:
                system = system + 0.125  # has a lower infuence
                item7_sy += 0.5

        else:
            item7.config(bg="Green")
            item7_sy = 0

        item8_satus = primary_program.ps5(1)

        if item8_satus == "Bad":
            item8.config(bg="Red")
            if item8_sy == 0:
                system = system + 0.25  # has a lower infuence
                item8_sy += 0.5

        else:
            item8.config(bg="Green")
            item8_sy = 0

        item9_satus = primary_program.ps4(1)

        if item9_satus == "Bad":
            item9.config(bg="Red")
            if item9_sy == 0:
                system = system + 0.125  # has a lower infuence
                item9_sy += 0.5

        else:
            item9.config(bg="Green")
            item9_sy = 0

        item10_satus = primary_program.printer(1)

        if item10_satus == "Bad":
            item10.config(bg="Red")
            if item10_sy == 0:
                system = system + 0.125  # has a lower infuence
                item10_sy += 0.5

        else:
            item10.config(bg="Green")
            item10_sy = 0

        item11_satus = primary_program.haydens_tv(1)

        if item11_satus == "Bad":
            item11.config(bg="Red")
            if item11_sy == 0:
                system = system + 0.125  # has a lower infuence
                item11_sy += 0.5

        else:
            item11.config(bg="Green")
            item11_sy = 0

        item12_satus = primary_program.tinas_iphone(1)
        if item12_satus == "Bad":
            item12.config(bg="Red")
            if item12_sy == 0:
                system = system + 0.125  # has a lower infuence
                item12_sy += 0.5

        else:
            item12.config(bg="Green")
            item12_sy = 0

        item13_satus = primary_program.rosss_iphone(1)
        if item13_satus == "Bad":
            item13.config(bg="Red")
            if item13_sy == 0:
                system = system + 0.125  # has a lower influence
                item13_sy += 0.5
        else:
            item13.config(bg="Green")
            item13_sy = 0

        item14_satus = primary_program.front_room_tv(1)
        if item14_satus == "Bad":
            item14.config(bg="Red")
            if item14_sy == 0:
                system = system + 0.125  # has a lower influence
                item14_sy += 0.5

        else:
            item14.config(bg="Green")
            item14_sy = 0

        if system >= 2:

            count = 0
            main.config(bg="red")
            system_satus_message.config(bg="white")
            system_flash()

        else:
            system_satus.config(bg="green")
            main.config(bg="black")
            try:
                system_satus_message.config(bg="black")
            except:
                pass

        system_count.config(text=system)

        test.config(text=str(x))
        main.after(1000, update)

    test.grid(row=0, column=6)
    system_count.grid(row=0, column=1)

    header1.grid(row=1, column=1)
    header2.grid(row=1, column=2)
    header2b.grid(row=1, column=3)
    header3.grid(row=1, column=5)

    item14.grid(row=5, column=5) # f tv low

    item13.grid(row=5, column=2)  #r i med

    item12.grid(row=2, column=2)  # t i med

    item11.grid(row=4, column=5)  #h tv low

    item10.grid(row=3, column=5)  #printer low

    item9.grid(row=2, column=5)  #ps4 low

    item8.grid(row=5, column=3)  #ps5 med

    item7.grid(row=3, column=2)  #meg i med

    item6.grid(row=4, column=2)  #haydens i med

    item5.grid(row=2, column=3)  #b laptop med

    item4.grid(row=3, column=3)  #s laptop med

    item3.grid(row=3, column=1)  #blink high

    item2.grid(row=4, column=3)  #booster med

    item1.grid(row=2, column=1)  #hub high

    system_satus.grid(row=0, column=1, columnspan=3)
    system_satus_message.grid(row=8, column=1, columnspan=2)
    update()
    main.mainloop()

