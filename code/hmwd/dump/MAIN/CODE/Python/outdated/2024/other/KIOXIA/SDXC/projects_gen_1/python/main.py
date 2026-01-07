import subprocess, os, time, platform,threading,socket, importlib
import console_code_network.Primary_tk
import console_code_network.primary_program
print("main start")
def primary_trigger():
    from security import primary_tk_login
    import security.primary_tk_login as primary_tk_login
    from security import primary_login
    from security.login_details import login_log
    import main_menu_tk
    from main_menu_tk import main_menu_run
    from security.primary_tk_login import sc_login_run


    with open('security/login_details/auth.py','w') as file:
        file.write('authorised = False')

    primary_tk_login.sc_login_run()

    authorised = primary_login.access


    print(authorised)
    if authorised == False:
        print("exit")
        exit()



    main_menu_run()

    print("after main menu")



primary_trigger()
