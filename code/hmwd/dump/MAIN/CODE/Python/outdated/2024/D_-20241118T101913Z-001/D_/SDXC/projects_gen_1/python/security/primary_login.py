import subprocess, os, time, platform,threading,socket,importlib,sys


def security_login(user,pas):
    global access
    global logged_username
    orginal1 = ""
    orginal2=""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9',
               '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
               ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
               '~', '`', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9',
               '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
               ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
               '~', '`', ' ', ]
    alpha2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
              '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
              ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
              '~', '`', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
              '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
              ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
              '~', '`', ' ', ]


    a= 1
    from security import login_details
    from security.login_details.login_info import username,password
    from security.login_details import login_log
    from security.login_details.login_log import logged
    from security.login_details import auth
    from security.login_details.auth import authorised

    try:

        username_pos = login_details.login_info.username.index(user)

        password_actual = login_details.login_info.password[username_pos]
        for letters in password_actual:
            pos = alpha2.index(letters)
            orginal_pos = pos - 9
            orginal1 = orginal1 + alpha2[orginal_pos]

        if pas == orginal1:
            access = True
            logged.append(user)

            with open('security/login_details/login_log.py', 'w') as file:
                file.write(f'logged={repr(login_log.logged)}\n')


            with open('security/login_details/auth.py', 'w') as file:
                file.write('authorised = True')

            print("access granted")



            access = True
            return "1"

    except:

        print("access denied")
        access = False
        return "0"

    else:

        return "0"






def security_create(new_user,new_pas,admin):
    shifted1 = ""
    shifted2 = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9',
               '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
               ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
               '~', '`', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9',
               '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
               ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
               '~', '`', ' ', ]
    alpha2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
              '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
              ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
              '~', '`', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
              '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
              ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?',
              '~', '`', ' ', ]


    new_user = new_user.lower()
    new_pas = new_pas.lower()
    for letters in new_pas:
        pos = alpha2.index(letters)
        pos = pos + 9
        shifted2 = shifted2 + alpha2[pos]

    bad_passwords = ["12345678","87654321",new_user,f"{new_user}{new_user}"]
    new_pas = str(new_pas)

    try:
        del sys.modules['login_details.logi_info']

    except:
        pass

    from security.login_details import login_info as login_info
    from security.login_details.adminstrator import admin_pas

    if admin != admin_pas:

        return "0"


    if new_user in login_info.username:
        return "2"

    if len(new_pas) < 8:
        return "3"
    if new_pas in bad_passwords:
        return "3"

    
    login_info.username.append(new_user)

    login_info.password.append(shifted2)
    with open('security/login_details/login_info.py','w') as file:
        file.write(f'username={repr(login_info.username)}\n')
        file.write(f'password={repr(login_info.password)}\n')

    return "1"







