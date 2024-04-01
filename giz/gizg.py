def introduction():
    print("__________________________________________")
    print("")
    print("------ Copyright © 2024 Savas Sahin ------")
    print("__________________________________________")
    print("")
    print("------ Type 'info' for information. ------")
    print("__________________________________________")
    print("")

introduction()

def entry():
    global given
    given = input(">>> ").lower()

    if given == "info":
        return info()
    else:
        while (len(given) < 12) or (len(given) > 32) or not given.isalpha():
            print("")
            print("Your input must consist of at least 12, at most 32 characters and must contain only letters.")
            print("")
            given = input(">>> ")
            print("")

        given = given.lower()
        return gizg()
    
def info():
    print("")
    print("--- This is a personal password creator.")
    print("--- This app is for creating complex passwords that can be easily remembered.")
    print("--- Password creation support is limited to 12-32 characters.")
    print("--- You must use only letters. No numbers, no marks. The app will be add them for you.")
    print("--- You should just type something basic that you'll never forget.")
    print("--- It's recommended to pick a keyword to use in your passwords. For example:")
    print("")
    print("--- Your keyword: mykeyword, platform to use: github, password: mykeywordforgithub")
    print("--- Output: {oJ:BG[iE.x=M%8>HLIj|Dzw3]AKtv*4")
    print("")
    return entry()

def gizg():
    script = []
    encrypted = []

    for i in given:     
        script.append(i)

    for letter in script:

        if letter in ["e", "z"]:
            encrypted.append("A")

        elif letter in ["t", "q"]:
            encrypted.append("B")

        elif letter in ["a", "x"]:
            encrypted.append("C")

        elif letter in ["o", "j"]:
            encrypted.append("D")

        elif letter in ["i", "k"]:
            encrypted.append("E")

        elif letter in ["n", "v"]:
            encrypted.append("F")

        elif letter in ["s", "b"]:
            encrypted.append("G")

        elif letter in ["h", "p"]:
            encrypted.append("H")

        elif letter in ["r", "y"]:
            encrypted.append("I")

        elif letter in ["d", "g"]:
            encrypted.append("J")

        elif letter in ["l", "f"]:
            encrypted.append("K")

        elif letter in ["c", "w"]:
            encrypted.append("L")

        elif letter in ["u", "m"]:
            encrypted.append("M")

    length = len(encrypted)
    if length < 32:
        missing_rate = 32 - length
        missing_letter = ["o","*","]","[","t","v","x","|",":",".","z","w","j","%","&","#","=","?","!","$"]
        encrypted += missing_letter[:missing_rate]

    def replace(encrypted):
        a_counter = 0
        b_counter = 0
        c_counter = 0
        d_counter = 0
        e_counter = 0
        f_counter = 0
        g_counter = 0
        h_counter = 0
        i_counter = 0
        j_counter = 0
        k_counter = 0
        l_counter = 0
        m_counter = 0
        new_script = []

        for i in encrypted:
            if i == "A":
                a_counter += 1
                if a_counter == 2:
                    new_script.append("0")
                elif a_counter == 3:
                    new_script.append("!")
                elif a_counter == 4:
                    new_script.append("a")
                elif a_counter == 5:
                    new_script.append("O")
                elif a_counter == 6:
                    new_script.append("o")
                else:
                    new_script.append(i)

            elif i == "B":
                b_counter += 1
                if b_counter == 2:
                    new_script.append("1")
                elif b_counter == 3:
                    new_script.append("+")
                elif b_counter == 4:
                    new_script.append("b")
                elif b_counter == 5:
                    new_script.append("P")
                elif b_counter == 6:
                    new_script.append("*")
                else:
                    new_script.append(i)

            elif i == "C":
                c_counter += 1
                if c_counter == 2:
                    new_script.append("2")
                elif c_counter == 3:
                    new_script.append("-")
                elif c_counter == 4:
                    new_script.append("c")
                elif c_counter == 5:
                    new_script.append("Q")
                elif c_counter == 6:
                    new_script.append("]")
                else:
                    new_script.append(i)

            elif i == "D":
                d_counter += 1
                if d_counter == 2:
                    new_script.append("3")
                elif d_counter == 3:
                    new_script.append("%")
                elif d_counter == 4:
                    new_script.append("d")
                elif d_counter == 5:
                    new_script.append("R")
                elif d_counter == 6:
                    new_script.append("r")
                else:
                    new_script.append(i)

            elif i == "E":
                e_counter += 1
                if e_counter == 2:
                    new_script.append("4")
                elif e_counter == 3:
                    new_script.append("&")
                elif e_counter == 4:
                    new_script.append("e")
                elif e_counter == 5:
                    new_script.append("S")
                elif e_counter == 6:
                    new_script.append("[")
                else:
                    new_script.append(i)

            elif i == "F":
                f_counter += 1
                if f_counter == 2:
                    new_script.append("5")
                elif f_counter == 3:
                    new_script.append("/")
                elif f_counter == 4:
                    new_script.append("f")
                elif f_counter == 5:
                    new_script.append("T")
                elif f_counter == 6:
                    new_script.append("t")
                else:
                    new_script.append(i)

            elif i == "G":
                g_counter += 1
                if g_counter == 2:
                    new_script.append("6")
                elif g_counter == 3:
                    new_script.append("(")
                elif g_counter == 4:
                    new_script.append("g")
                elif g_counter == 5:
                    new_script.append("V")
                elif g_counter == 6:
                    new_script.append("v")
                else:
                    new_script.append(i)

            elif i == "H":
                h_counter += 1
                if h_counter == 2:
                    new_script.append("7")
                elif h_counter == 3:
                    new_script.append(")")
                elif h_counter == 4:
                    new_script.append("h")
                elif h_counter == 5:
                    new_script.append("X")
                elif h_counter == 6:
                    new_script.append("x")
                else:
                    new_script.append(i)

            elif i == "I":
                i_counter += 1
                if i_counter == 2:
                    new_script.append("8")
                elif i_counter == 3:
                    new_script.append("=")
                elif i_counter == 4:
                    new_script.append("i")
                elif i_counter == 5:
                    new_script.append("Y")
                elif i_counter == 6:
                    new_script.append("|")
                else:
                    new_script.append(i)

            elif i == "J":
                j_counter += 1
                if j_counter == 2:
                    new_script.append("{")
                elif j_counter == 3:
                    new_script.append("}")
                elif j_counter == 4:
                    new_script.append("n")
                elif j_counter == 5:
                    new_script.append(".")
                elif j_counter == 6:
                    new_script.append(":")
                else:
                    new_script.append(i)

            elif i == "K":
                k_counter += 1
                if k_counter == 2:
                    new_script.append("9")
                elif k_counter == 3:
                    new_script.append("?")
                elif k_counter == 4:
                    new_script.append("k")
                elif k_counter == 5:
                    new_script.append("Z")
                elif k_counter == 6:
                    new_script.append("z")
                else:
                    new_script.append(i)

            elif i == "L":
                l_counter += 1
                if l_counter == 2:
                    new_script.append("_")
                elif l_counter == 3:
                    new_script.append("<")
                elif l_counter == 4:
                    new_script.append("l")
                elif l_counter == 5:
                    new_script.append("W")
                elif l_counter == 6:
                    new_script.append("w")
                else:
                    new_script.append(i)

            elif i == "M":
                m_counter += 1
                if m_counter == 2:
                    new_script.append(">")
                elif m_counter == 3:
                    new_script.append("$")
                elif m_counter == 4:
                    new_script.append("m")
                elif m_counter == 5:
                    new_script.append("J")
                elif m_counter == 6:
                    new_script.append("j")
                else:
                    new_script.append(i)
            else:
                new_script.append(i)

        return (new_script)
    
    new_script = replace(encrypted)

    def replace_array(new_script, new_places):
        new_list = [""] * len(new_script)
        for old_place, new_place in new_places:
            new_list[new_place] = new_script[old_place]
        return new_list
    
    new_places = [
        (0, 12), (1, 18), (2, 8), (3, 26), (4, 14), (5, 17), (6, 21), (7, 11), 
        (8, 2), (9, 27), (10, 24), (11, 7), (12, 0), (13, 31), (14, 4), (15, 16), 
        (16, 15), (17, 5), (18, 1), (19, 30), (20, 25), (21, 6), (22, 28), (23, 29), 
        (24, 10), (25, 20), (26, 3), (27, 9), (28, 22), (29, 23), (30, 19), (31, 13)
    ]

    edited_list = replace_array(new_script, new_places)
    output = ''.join(edited_list)

    print("")
    print("Your password: ", output)
    print("")
    return entry()

entry()
