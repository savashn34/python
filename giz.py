import random

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
    choice = input(">>> ").lower()

    while choice not in ["e", "d", "p", "info"]:
        print("")
        print("--- You entered an invalid command.")
        print("")
        choice = input(">>> ").lower()

    if choice == "info":
        return info()
    elif choice == "e":
        return encrypt()
    elif choice == "d":
        return decrypt()
    elif choice == "p":
        return password()

    return entry()
    
def info():
    print("")
    print("--- This is a personal encryptor.")
    print("--- It's for creating complex passwords that can be easily remembered, or encrypting texts.")
    print("--- Note that your text should not exceed a total of 720 characters.")
    print("--- Text encryptor has support for English and Turkish letters.")
    print("")
    print("----- FOR CREATING A PASSWORD -----")
    print("")
    print("--- Password creation support is limited to 12-32 characters.")
    print("--- You must use only letters. No numbers, no marks. The program will be add them for you.")
    print("--- You should just type something basic that you'll never forget.")
    print("--- It's recommended to pick a keyword to use in your passwords. For example:")
    print("")
    print("--- Your keyword: mykeyword, platform to use: github, password: mykeywordforgithub")
    print("--- Output: {9J2BG$iE?t=MX8>HLIxRDvZ3sAK5|!4")
    print("")
    print("--- Type 'E' to encrypt a script.")
    print("--- Type 'C' to decrypt an encrypted script.")
    print("--- Type 'P' to create a password.")
    print("")
    return entry()

def encrypt():
    script = []
    encrypted = []
    print("")
    print("Type the text to encrypt: ")
    print("")
    given = input(">>> ")

    while len(given) > 720:
        print("")
        print("The length of the text to be encrypted cannot exceed 720 characters.")
        print("")
        print("Type the script: ")
        print("")
        given = input(">>> ")

    else:
        given = given.lower()
        for i in given:     
            list(str(script.append(i)))

    for j in script:
        if j == "a" in script:
            list(str(encrypted.append("b")))
        if j == "b" in script:
            list(str(encrypted.append("ç")))
        if j == "c" in script:
            list(str(encrypted.append("e")))
        if j == "ç" in script:
            list(str(encrypted.append("g")))
        if j == "d" in script:
            list(str(encrypted.append("h")))
        if j == "e" in script:
            list(str(encrypted.append("i")))
        if j == "f" in script:
            list(str(encrypted.append("k")))
        if j == "g" in script:
            list(str(encrypted.append("m")))
        if j == "ğ" in script:
            list(str(encrypted.append("o")))
        if j == "h" in script:
            list(str(encrypted.append("p")))
        if j == "ı" in script:
            list(str(encrypted.append("s")))
        if j == "i" in script:
            list(str(encrypted.append("t")))
        if j == "j" in script:
            list(str(encrypted.append("ü")))
        if j == "k" in script:
            list(str(encrypted.append("y")))
        if j == "l" in script:
            list(str(encrypted.append("a")))
        if j == "m" in script:    
            list(str(encrypted.append("c")))
        if j == "n" in script:    
            list(str(encrypted.append("d")))
        if j == "o" in script:    
            list(str(encrypted.append("f")))
        if j == "ö" in script:    
            list(str(encrypted.append("ğ")))
        if j == "p" in script:    
            list(str(encrypted.append("ı")))
        if j == "r" in script:    
            list(str(encrypted.append("j")))
        if j == "s" in script:    
            list(str(encrypted.append("l")))
        if j == "ş" in script:    
            list(str(encrypted.append("n")))
        if j == "t" in script:    
            list(str(encrypted.append("ö")))
        if j == "u" in script:    
            list(str(encrypted.append("r")))
        if j == "ü" in script:    
            list(str(encrypted.append("ş")))
        if j == "v" in script:    
            list(str(encrypted.append("u")))
        if j == "y" in script:    
            list(str(encrypted.append("v")))
        if j == "z" in script:    
            list(str(encrypted.append("0")))
        if j == "w" in script:
            list(str(encrypted.append("@")))
        if j == "x" in script:
            list(str(encrypted.append("ß")))
        if j == "q" in script:
            list(str(encrypted.append("=")))
        if j == " " in script:
            list(str(encrypted.append("1")))
        if j == "." in script:
            list(str(encrypted.append("/")))
        if j == "," in script:
            list(str(encrypted.append("&")))
        if j == ":" in script:
            list(str(encrypted.append("%")))
        if j == ";" in script:
            list(str(encrypted.append("?")))
        if j == "?" in script:
            list(str(encrypted.append("$")))
        if j == "!" in script:
            list(str(encrypted.append("æ")))
        if j == "'" in script:
            list(str(encrypted.append("|")))

    if len(encrypted) < 360:
        while len(encrypted) < 360:
            ineffective = random.randint(2, 9)
            encrypted.append(ineffective)

    elif ((len(encrypted) >= 360) and (len(encrypted) < 720)):
        while len(encrypted) < 720:
            ineffective = random.randint(2, 9)
            encrypted.append(ineffective)

    positions_one = [
        (0, 358), (1, 233), (2, 357), (3, 326), (4, 295), (5, 264), (6, 359), (7, 202), (8, 15), (9, 140), (10, 109), (11, 78), (12, 47), (13, 171), (14, 16),
        (15, 13), (16, 248), (17, 327), (18, 341), (19, 310), (20, 279), (21, 14), (22, 217), (23, 30), (24, 155), (25, 124), (26, 93), (27, 62), (28, 186), (29, 31),
        (30, 28), (31, 263), (32, 342), (33, 356), (34, 325), (35, 294), (36, 29), (37, 232), (38, 45), (39, 170), (40, 139), (41, 108), (42, 77), (43, 201), (44, 46),
        (45, 43), (46, 278), (47, 12), (48, 296), (49, 340), (50, 309), (51, 44), (52, 247), (53, 60), (54, 185), (55, 154), (56, 123), (57, 92), (58, 216), (59, 61),
        (60, 58), (61, 293), (62, 27), (63, 311), (64, 355), (65, 324), (66, 59), (67, 262), (68, 75), (69, 200), (70, 169), (71, 138), (72, 107), (73, 231), (74, 76), 
        (75, 73), (76, 308), (77, 42), (78, 11), (79, 265), (80, 339), (81, 74), (82, 277), (83, 90), (84, 215), (85, 184), (86, 153), (87, 122), (88, 246), (89, 91),
        (90, 88), (91, 323), (92, 57), (93, 26), (94, 280), (95, 354), (96, 89), (97, 292), (98, 105), (99, 230), (100, 199), (101, 168), (102, 137), (103, 261), (104, 106), 
        (105, 103), (106, 338), (107, 72), (108, 41), (109, 10), (110, 234), (111, 104), (112, 307), (113, 120), (114, 245), (115, 214), (116, 183), (117, 152), (118, 276), (119, 121), 
        (120, 118), (121, 353), (122, 87), (123, 56), (124, 25), (125, 249), (126, 119), (127, 322), (128, 135), (129, 260), (130, 229), (131, 198), (132, 167), (133, 291), (134, 136),
        (135, 133), (136, 203), (137, 102), (138, 71), (139, 40), (140, 9), (141, 134), (142, 337), (143, 150), (144, 275), (145, 244), (146, 213), (147, 182), (148, 306), (149, 151),
        (150, 148), (151, 218), (152, 117), (153, 86), (154, 55), (155, 24), (156, 149), (157, 352), (158, 165), (159, 290), (160, 259), (161, 228), (162, 197), (163, 321), (164, 166),
        (165, 163), (166, 8), (167, 132), (168, 101), (169, 70), (170, 39), (171, 164), (172, 172), (173, 180), (174, 305), (175, 274), (176, 243), (177, 212), (178, 336), (179, 181),
        (180, 178), (181, 23), (182, 147), (183, 116), (184, 85), (185, 54), (186, 179), (187, 187), (188, 195), (189, 320), (190, 289), (191, 258), (192, 227), (193, 351), (194, 196),
        (195, 193), (196, 38), (197, 162), (198, 131), (199, 100), (200, 69), (201, 194), (202, 7), (203, 210), (204, 335), (205, 304), (206, 273), (207, 242), (208, 141), (209, 211),
        (210, 208), (211, 53), (212, 177), (213, 146), (214, 115), (215, 84), (216, 209), (217, 22), (218, 225), (219, 350), (220, 319), (221, 288), (222, 257), (223, 156), (224, 226), 
        (225, 223), (226, 68), (227, 192), (228, 161), (229, 130), (230, 99), (231, 224), (232, 37), (233, 240), (234, 110), (235, 334), (236, 303), (237, 272), (238, 6), (239, 241), 
        (240, 238), (241, 83), (242, 207), (243, 176), (244, 145), (245, 114), (246, 239), (247, 52), (248, 255), (249, 125), (250, 349), (251, 318), (252, 287), (253, 21), (254, 256), 
        (255, 253), (256, 98), (257, 222), (258, 191), (259, 160), (260, 129), (261, 254), (262, 67), (263, 270), (264, 5), (265, 79), (266, 333), (267, 302), (268, 36), (269, 271), 
        (270, 268), (271, 113), (272, 237), (273, 206), (274, 175), (275, 144), (276, 269), (277, 82), (278, 285), (279, 20), (280, 94), (281, 348), (282, 317), (283, 51), (284, 286), 
        (285, 283), (286, 128), (287, 252), (288, 221), (289, 190), (290, 159), (291, 284), (292, 97), (293, 300), (294, 35), (295, 4), (296, 48), (297, 332), (298, 66), (299, 301), 
        (300, 298), (301, 143), (302, 267), (303, 236), (304, 205), (305, 174), (306, 299), (307, 112), (308, 315), (309, 50), (310, 19), (311, 63), (312, 347), (313, 81), (314, 316), 
        (315, 313), (316, 158), (317, 282), (318, 251), (319, 220), (320, 189), (321, 314), (322, 127), (323, 330), (324, 65), (325, 34), (326, 3), (327, 17), (328, 96), (329, 331), 
        (330, 328), (331, 173), (332, 297), (333, 266), (334, 235), (335, 204), (336, 329), (337, 142), (338, 345), (339, 80), (340, 49), (341, 18), (342, 32), (343, 111), (344, 346), 
        (345, 343), (346, 188), (347, 312), (348, 281), (349, 250), (350, 219), (351, 344), (352, 157), (353, 0), (354, 95), (355, 64), (356, 33), (357, 2), (358, 126), (359, 1)]
    
    positions_two = [
        (360, 718), (361, 593), (362, 717), (363, 686), (364, 655), (365, 624), (366, 719), (367, 562), (368, 375), (369, 500), (370, 469), (371, 438), (372, 407), (373, 531), (374, 376),
        (375, 373), (376, 608), (377, 687), (378, 701), (379, 670), (380, 639), (381, 374), (382, 577), (383, 390), (384, 515), (385, 484), (386, 453), (387, 422), (388, 546), (389, 391), 
        (390, 388), (391, 623), (392, 702), (393, 716), (394, 685), (395, 654), (396, 389), (397, 592), (398, 405), (399, 530), (400, 499), (401, 468), (402, 437), (403, 561), (404, 406), 
        (405, 403), (406, 638), (407, 372), (408, 656), (409, 700), (410, 669), (411, 404), (412, 607), (413, 420), (414, 545), (415, 514), (416, 483), (417, 452), (418, 576), (419, 421), 
        (420, 418), (421, 653), (422, 387), (423, 671), (424, 715), (425, 684), (426, 419), (427, 622), (428, 435), (429, 560), (430, 529), (431, 498), (432, 467), (433, 591), (434, 436), 
        (435, 433), (436, 668), (437, 402), (438, 371), (439, 625), (440, 699), (441, 434), (442, 637), (443, 450), (444, 575), (445, 544), (446, 513), (447, 482), (448, 606), (449, 451), 
        (450, 448), (451, 683), (452, 417), (453, 386), (454, 640), (455, 714), (456, 449), (457, 652), (458, 465), (459, 590), (460, 559), (461, 528), (462, 497), (463, 621), (464, 466), 
        (465, 463), (466, 698), (467, 432), (468, 401), (469, 370), (470, 594), (471, 464), (472, 667), (473, 480), (474, 605), (475, 574), (476, 543), (477, 512), (478, 636), (479, 481), 
        (480, 478), (481, 713), (482, 447), (483, 416), (484, 385), (485, 609), (486, 479), (487, 682), (488, 495), (489, 620), (490, 589), (491, 558), (492, 527), (493, 651), (494, 496), 
        (495, 493), (496, 563), (497, 462), (498, 431), (499, 400), (500, 369), (501, 494), (502, 697), (503, 510), (504, 635), (505, 604), (506, 573), (507, 542), (508, 666), (509, 511), 
        (510, 508), (511, 578), (512, 477), (513, 446), (514, 415), (515, 384), (516, 509), (517, 712), (518, 525), (519, 650), (520, 619), (521, 588), (522, 557), (523, 681), (524, 526), 
        (525, 523), (526, 368), (527, 492), (528, 461), (529, 430), (530, 399), (531, 524), (532, 532), (533, 540), (534, 665), (535, 634), (536, 603), (537, 572), (538, 696), (539, 541), 
        (540, 538), (541, 383), (542, 507), (543, 476), (544, 445), (545, 414), (546, 539), (547, 547), (548, 555), (549, 680), (550, 649), (551, 618), (552, 587), (553, 711), (554, 556), 
        (555, 553), (556, 398), (557, 522), (558, 491), (559, 460), (560, 429), (561, 554), (562, 367), (563, 570), (564, 695), (565, 664), (566, 633), (567, 602), (568, 501), (569, 571), 
        (570, 568), (571, 413), (572, 537), (573, 506), (574, 475), (575, 444), (576, 569), (577, 382), (578, 585), (579, 710), (580, 679), (581, 648), (582, 617), (583, 516), (584, 586), 
        (585, 583), (586, 428), (587, 552), (588, 521), (589, 490), (590, 459), (591, 584), (592, 397), (593, 600), (594, 470), (595, 694), (596, 663), (597, 632), (598, 366), (599, 601), 
        (600, 598), (601, 443), (602, 567), (603, 536), (604, 505), (605, 474), (606, 599), (607, 412), (608, 615), (609, 485), (610, 709), (611, 678), (612, 647), (613, 381), (614, 616), 
        (615, 613), (616, 458), (617, 582), (618, 551), (619, 520), (620, 489), (621, 614), (622, 427), (623, 630), (624, 365), (625, 439), (626, 693), (627, 662), (628, 396), (629, 631), 
        (630, 628), (631, 473), (632, 597), (633, 566), (634, 535), (635, 504), (636, 629), (637, 442), (638, 645), (639, 380), (640, 454), (641, 708), (642, 677), (643, 411), (644, 646), 
        (645, 643), (646, 488), (647, 612), (648, 581), (649, 550), (650, 519), (651, 644), (652, 457), (653, 660), (654, 395), (655, 364), (656, 408), (657, 692), (658, 426), (659, 661), 
        (660, 658), (661, 503), (662, 627), (663, 596), (664, 565), (665, 534), (666, 659), (667, 472), (668, 675), (669, 410), (670, 379), (671, 423), (672, 707), (673, 441), (674, 676), 
        (675, 673), (676, 518), (677, 642), (678, 611), (679, 580), (680, 549), (681, 674), (682, 487), (683, 690), (684, 425), (685, 394), (686, 363), (687, 377), (688, 456), (689, 691), 
        (690, 688), (691, 533), (692, 657), (693, 626), (694, 595), (695, 564), (696, 689), (697, 502), (698, 705), (699, 440), (700, 409), (701, 378), (702, 392), (703, 471), (704, 706), 
        (705, 703), (706, 548), (707, 672), (708, 641), (709, 610), (710, 579), (711, 704), (712, 517), (713, 360), (714, 455), (715, 424), (716, 393), (717, 362), (718, 486), (719, 361)]

    def replace_array(encrypted, new_places):

        new_list = [ineffective] * len(encrypted)
        for old_place, new_place in new_places:
            new_list[new_place] = encrypted[old_place]
        
        return new_list
    
    if len(encrypted) == 720:
        new_places = positions_one + positions_two
        
    elif len(encrypted) == 360:
        new_places = positions_one

    edited_list = replace_array(encrypted, new_places)
    edited_list = [str(data) for data in edited_list]
    output = ''.join(edited_list)
    
    print("")
    print("Encrypted text: ")
    print("")
    print(output)
    print("")
    return entry()

def decrypt():
    script = []
    list = []
    print("")
    print("Type the encrypted text to decrypt: ")
    print("")
    given = input(">>> ")

    while ((len(given) != 720) and (len(given) != 360)):
        print("")
        print("Encrypted text must consist of 360 or 720 characters.")
        print("")
        print("Type the encrypted script: ")
        given = input(">>> ")

    else:
        for i in given:
            script.append(i)

    positions_one = [
        (358, 0), (233, 1), (357, 2), (326, 3), (295, 4), (264, 5), (359, 6), (202, 7), (15, 8), (140, 9), (109, 10), (78, 11), (47, 12), (171, 13), (16, 14), 
        (13, 15), (248, 16), (327, 17), (341, 18), (310, 19), (279, 20), (14, 21), (217, 22), (30, 23), (155, 24), (124, 25), (93, 26), (62, 27), (186, 28), (31, 29), 
        (28, 30), (263, 31), (342, 32), (356, 33), (325, 34), (294, 35), (29, 36), (232, 37), (45, 38), (170, 39), (139, 40), (108, 41), (77, 42), (201, 43), (46, 44), 
        (43, 45), (278, 46), (12, 47), (296, 48), (340, 49), (309, 50), (44, 51), (247, 52), (60, 53), (185, 54), (154, 55), (123, 56), (92, 57), (216, 58), (61, 59), 
        (58, 60), (293, 61), (27, 62), (311, 63), (355, 64), (324, 65), (59, 66), (262, 67), (75, 68), (200, 69), (169, 70), (138, 71), (107, 72), (231, 73), (76, 74), 
        (73, 75), (308, 76), (42, 77), (11, 78), (265, 79), (339, 80), (74, 81), (277, 82), (90, 83), (215, 84), (184, 85), (153, 86), (122, 87), (246, 88), (91, 89), 
        (88, 90), (323, 91), (57, 92), (26, 93), (280, 94), (354, 95), (89, 96), (292, 97), (105, 98), (230, 99), (199, 100), (168, 101), (137, 102), (261, 103), (106, 104), 
        (103, 105), (338, 106), (72, 107), (41, 108), (10, 109), (234, 110), (104, 111), (307, 112), (120, 113), (245, 114), (214, 115), (183, 116), (152, 117), (276, 118), (121, 119), 
        (118, 120), (353, 121), (87, 122), (56, 123), (25, 124), (249, 125), (119, 126), (322, 127), (135, 128), (260, 129), (229, 130), (198, 131), (167, 132), (291, 133), (136, 134), 
        (133, 135), (203, 136), (102, 137), (71, 138), (40, 139), (9, 140), (134, 141), (337, 142), (150, 143), (275, 144), (244, 145), (213, 146), (182, 147), (306, 148), (151, 149), 
        (148, 150), (218, 151), (117, 152), (86, 153), (55, 154), (24, 155), (149, 156), (352, 157), (165, 158), (290, 159), (259, 160), (228, 161), (197, 162), (321, 163), (166, 164), 
        (163, 165), (8, 166), (132, 167), (101, 168), (70, 169), (39, 170), (164, 171), (172, 172), (180, 173), (305, 174), (274, 175), (243, 176), (212, 177), (336, 178), (181, 179), 
        (178, 180), (23, 181), (147, 182), (116, 183), (85, 184), (54, 185), (179, 186), (187, 187), (195, 188), (320, 189), (289, 190), (258, 191), (227, 192), (351, 193), (196, 194), 
        (193, 195), (38, 196), (162, 197), (131, 198), (100, 199), (69, 200), (194, 201), (7, 202), (210, 203), (335, 204), (304, 205), (273, 206), (242, 207), (141, 208), (211, 209), 
        (208, 210), (53, 211), (177, 212), (146, 213), (115, 214), (84, 215), (209, 216), (22, 217), (225, 218), (350, 219), (319, 220), (288, 221), (257, 222), (156, 223), (226, 224), 
        (223, 225), (68, 226), (192, 227), (161, 228), (130, 229), (99, 230), (224, 231), (37, 232), (240, 233), (110, 234), (334, 235), (303, 236), (272, 237), (6, 238), (241, 239), 
        (238, 240), (83, 241), (207, 242), (176, 243), (145, 244), (114, 245), (239, 246), (52, 247), (255, 248), (125, 249), (349, 250), (318, 251), (287, 252), (21, 253), (256, 254), 
        (253, 255), (98, 256), (222, 257), (191, 258), (160, 259), (129, 260), (254, 261), (67, 262), (270, 263), (5, 264), (79, 265), (333, 266), (302, 267), (36, 268), (271, 269), 
        (268, 270), (113, 271), (237, 272), (206, 273), (175, 274), (144, 275), (269, 276), (82, 277), (285, 278), (20, 279), (94, 280), (348, 281), (317, 282), (51, 283), (286, 284), 
        (283, 285), (128, 286), (252, 287), (221, 288), (190, 289), (159, 290), (284, 291), (97, 292), (300, 293), (35, 294), (4, 295), (48, 296), (332, 297), (66, 298), (301, 299), 
        (298, 300), (143, 301), (267, 302), (236, 303), (205, 304), (174, 305), (299, 306), (112, 307), (315, 308), (50, 309), (19, 310), (63, 311), (347, 312), (81, 313), (316, 314), 
        (313, 315), (158, 316), (282, 317), (251, 318), (220, 319), (189, 320), (314, 321), (127, 322), (330, 323), (65, 324), (34, 325), (3, 326), (17, 327), (96, 328), (331, 329), 
        (328, 330), (173, 331), (297, 332), (266, 333), (235, 334), (204, 335), (329, 336), (142, 337), (345, 338), (80, 339), (49, 340), (18, 341), (32, 342), (111, 343), (346, 344), 
        (343, 345), (188, 346), (312, 347), (281, 348), (250, 349), (219, 350), (344, 351), (157, 352), (0, 353), (95, 354), (64, 355), (33, 356), (2, 357), (126, 358), (1, 359)]

    positions_two = [
        (718, 360), (593, 361), (717, 362), (686, 363), (655, 364), (624, 365), (719, 366), (562, 367), (375, 368), (500, 369), (469, 370), (438, 371), (407, 372), (531, 373), (376, 374), 
        (373, 375), (608, 376), (687, 377), (701, 378), (670, 379), (639, 380), (374, 381), (577, 382), (390, 383), (515, 384), (484, 385), (453, 386), (422, 387), (546, 388), (391, 389), 
        (388, 390), (623, 391), (702, 392), (716, 393), (685, 394), (654, 395), (389, 396), (592, 397), (405, 398), (530, 399), (499, 400), (468, 401), (437, 402), (561, 403), (406, 404), 
        (403, 405), (638, 406), (372, 407), (656, 408), (700, 409), (669, 410), (404, 411), (607, 412), (420, 413), (545, 414), (514, 415), (483, 416), (452, 417), (576, 418), (421, 419), 
        (418, 420), (653, 421), (387, 422), (671, 423), (715, 424), (684, 425), (419, 426), (622, 427), (435, 428), (560, 429), (529, 430), (498, 431), (467, 432), (591, 433), (436, 434), 
        (433, 435), (668, 436), (402, 437), (371, 438), (625, 439), (699, 440), (434, 441), (637, 442), (450, 443), (575, 444), (544, 445), (513, 446), (482, 447), (606, 448), (451, 449), 
        (448, 450), (683, 451), (417, 452), (386, 453), (640, 454), (714, 455), (449, 456), (652, 457), (465, 458), (590, 459), (559, 460), (528, 461), (497, 462), (621, 463), (466, 464), 
        (463, 465), (698, 466), (432, 467), (401, 468), (370, 469), (594, 470), (464, 471), (667, 472), (480, 473), (605, 474), (574, 475), (543, 476), (512, 477), (636, 478), (481, 479), 
        (478, 480), (713, 481), (447, 482), (416, 483), (385, 484), (609, 485), (479, 486), (682, 487), (495, 488), (620, 489), (589, 490), (558, 491), (527, 492), (651, 493), (496, 494), 
        (493, 495), (563, 496), (462, 497), (431, 498), (400, 499), (369, 500), (494, 501), (697, 502), (510, 503), (635, 504), (604, 505), (573, 506), (542, 507), (666, 508), (511, 509), 
        (508, 510), (578, 511), (477, 512), (446, 513), (415, 514), (384, 515), (509, 516), (712, 517), (525, 518), (650, 519), (619, 520), (588, 521), (557, 522), (681, 523), (526, 524), 
        (523, 525), (368, 526), (492, 527), (461, 528), (430, 529), (399, 530), (524, 531), (532, 532), (540, 533), (665, 534), (634, 535), (603, 536), (572, 537), (696, 538), (541, 539), 
        (538, 540), (383, 541), (507, 542), (476, 543), (445, 544), (414, 545), (539, 546), (547, 547), (555, 548), (680, 549), (649, 550), (618, 551), (587, 552), (711, 553), (556, 554), 
        (553, 555), (398, 556), (522, 557), (491, 558), (460, 559), (429, 560), (554, 561), (367, 562), (570, 563), (695, 564), (664, 565), (633, 566), (602, 567), (501, 568), (571, 569), 
        (568, 570), (413, 571), (537, 572), (506, 573), (475, 574), (444, 575), (569, 576), (382, 577), (585, 578), (710, 579), (679, 580), (648, 581), (617, 582), (516, 583), (586, 584), 
        (583, 585), (428, 586), (552, 587), (521, 588), (490, 589), (459, 590), (584, 591), (397, 592), (600, 593), (470, 594), (694, 595), (663, 596), (632, 597), (366, 598), (601, 599), 
        (598, 600), (443, 601), (567, 602), (536, 603), (505, 604), (474, 605), (599, 606), (412, 607), (615, 608), (485, 609), (709, 610), (678, 611), (647, 612), (381, 613), (616, 614), 
        (613, 615), (458, 616), (582, 617), (551, 618), (520, 619), (489, 620), (614, 621), (427, 622), (630, 623), (365, 624), (439, 625), (693, 626), (662, 627), (396, 628), (631, 629), 
        (628, 630), (473, 631), (597, 632), (566, 633), (535, 634), (504, 635), (629, 636), (442, 637), (645, 638), (380, 639), (454, 640), (708, 641), (677, 642), (411, 643), (646, 644), 
        (643, 645), (488, 646), (612, 647), (581, 648), (550, 649), (519, 650), (644, 651), (457, 652), (660, 653), (395, 654), (364, 655), (408, 656), (692, 657), (426, 658), (661, 659), 
        (658, 660), (503, 661), (627, 662), (596, 663), (565, 664), (534, 665), (659, 666), (472, 667), (675, 668), (410, 669), (379, 670), (423, 671), (707, 672), (441, 673), (676, 674), 
        (673, 675), (518, 676), (642, 677), (611, 678), (580, 679), (549, 680), (674, 681), (487, 682), (690, 683), (425, 684), (394, 685), (363, 686), (377, 687), (456, 688), (691, 689), 
        (688, 690), (533, 691), (657, 692), (626, 693), (595, 694), (564, 695), (689, 696), (502, 697), (705, 698), (440, 699), (409, 700), (378, 701), (392, 702), (471, 703), (706, 704), 
        (703, 705), (548, 706), (672, 707), (641, 708), (610, 709), (579, 710), (704, 711), (517, 712), (360, 713), (455, 714), (424, 715), (393, 716), (362, 717), (486, 718), (361, 719)]
    
    if len(script) == 360:
        new_places = positions_one
    elif len(script) == 720:
        new_places = positions_one + positions_two

    def replace_array(script, new_places):
        new_list = [None] * len(script)
        
        for old_place, new_place in new_places:
            new_list[new_place] = script[old_place]
        
        return new_list  
    
    edited_list = replace_array(script, new_places)
    edited_list = [str(data) for data in edited_list]

    for j in edited_list:
        
        if j == "b" in edited_list:
            list.append("a")
        if j == "ç" in edited_list:
            list.append("b")
        if j == "e" in edited_list:
            list.append("c")
        if j == "g" in edited_list:
            list.append("ç")
        if j == "h" in edited_list:
            list.append("d")
        if j == "i" in edited_list:
            list.append("e")
        if j == "k" in edited_list:
            list.append("f")
        if j == "m" in edited_list:
            list.append("g")
        if j == "o" in edited_list:
            list.append("ğ")
        if j == "p" in edited_list:
            list.append("h")
        if j == "s" in edited_list:
            list.append("ı")
        if j == "t" in edited_list:
            list.append("i")
        if j == "ü" in edited_list:
            list.append("j")
        if j == "y" in edited_list:
            list.append("k")
        if j == "a" in edited_list:
            list.append("l")
        if j == "c" in edited_list:    
            list.append("m")
        if j == "d" in edited_list:    
            list.append("n")
        if j == "f" in edited_list:    
            list.append("o")
        if j == "ğ" in edited_list:    
            list.append("ö")
        if j == "ı" in edited_list:    
            list.append("p")
        if j == "j" in edited_list:    
            list.append("r")
        if j == "l" in edited_list:    
            list.append("s")
        if j == "n" in edited_list:    
            list.append("ş")
        if j == "ö" in edited_list:    
            list.append("t")
        if j == "r" in edited_list:    
            list.append("u")
        if j == "ş" in edited_list:    
            list.append("ü")
        if j == "u" in edited_list:    
            list.append("v")
        if j == "v" in edited_list:    
            list.append("y")
        if j == "0" in edited_list:    
            list.append("z")
        if j == "@" in edited_list:
            list.append("w")
        if j == "ß" in edited_list:
            list.append("x")
        if j == "=" in edited_list:
            list.append("q")
        if j == "1" in edited_list:
            list.append(" ")
        if j == "/" in edited_list:
            list.append(".")
        if j == "&" in edited_list:
            list.append(",")
        if j == "%" in edited_list:
            list.append(":")
        if j == "?" in edited_list:
            list.append(";")
        if j == "$" in edited_list:
            list.append("?")
        if j == "æ" in edited_list:
            list.append("!")
        if j == "|" in script:
            list.append("'")

    list = ''.join(list)

    def correct(list):
        correct_sentence = ""
        big = True
        for k in list:
            if big and k.isalpha():
                correct_sentence += k.upper()
                big = False
            else:
                correct_sentence += k
                if k in ".?!:":
                    big = True
        return correct_sentence

    output = correct(list)
    print("")
    print("Decrypted script: ")
    print("")
    print(output)
    print("")
    return entry()

def password():
    global pgiven
    script = []
    crypted = []
    print("")
    print("Type to create a password: ")
    print("")
    pgiven = input(">>> ").lower()

    while (len(pgiven) < 12) or (len(pgiven) > 32) or not pgiven.isalpha():
            print("")
            print("Your input must consist of at least 12, at most 32 characters and must contain only letters.")
            print("")
            pgiven = input(">>> ").lower()
            print("")

    for i in pgiven:     
        script.append(i)

    for letter in script:

        if letter in ["e", "z"]:
            crypted.append("A")

        elif letter in ["t", "q"]:
            crypted.append("B")

        elif letter in ["a", "x"]:
            crypted.append("C")

        elif letter in ["o", "j"]:
            crypted.append("D")

        elif letter in ["i", "k"]:
            crypted.append("E")

        elif letter in ["n", "v"]:
            crypted.append("F")

        elif letter in ["s", "b"]:
            crypted.append("G")

        elif letter in ["h", "p"]:
            crypted.append("H")

        elif letter in ["r", "y"]:
            crypted.append("I")

        elif letter in ["d", "g"]:
            crypted.append("J")

        elif letter in ["l", "f"]:
            crypted.append("K")

        elif letter in ["c", "w"]:
            crypted.append("L")

        elif letter in ["u", "m"]:
            crypted.append("M")

    length = len(crypted)
    if length < 32:
        missing_rate = 32 - length
        missing_letter = ["o","*","]","[","t","v","x","|",":",".","z","w","j","%","&","#","=","?","!","$"]
        crypted += missing_letter[:missing_rate]

    def replace(crypted):
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

        for i in crypted:
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
    
    new_script = replace(crypted)

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
