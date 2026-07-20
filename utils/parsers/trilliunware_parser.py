# import re


# def parse_trilliunware(text):

#     text = str(text).upper().strip()


#     warna_list = [
#         "BRILLIANT WHITE",
#         "WHITE",
#         "IVORY",
#         "BLACK",
#         "GREY",
#         "MAROON",
#         "LIGHT BLUE",
#         "SORRENTO BLUE",
#         "APPLE GREEN",
#         "PINK",
#     ]


#     warna = ""

#     for w in warna_list:
#         if w in text:
#             warna = w
#             break


#     # ==========================
#     # PRODUK
#     # ==========================

#     produk = ""


#     if "CLOSET DUDUK" in text and "EUREKA" in text:

#         produk = "CD SIRAM EUREKA + SEAT COVER (SET)"


#     else:

#         produk = (
#             text
#             .replace("TRILLIUNWARE", "")
#             .replace("(SET)", "")
#             .strip()
#         )


#     return {

#         "brand": "TRILLIUNWARE",

#         "jenis": "",

#         "type": "",

#         "kode": "",

#         "ukuran": "",

#         "warna": warna,

#         "produk": produk,

#     }


def parse_trilliunware(text):

    text = str(text).upper().strip()

    result = {
        "brand": "TRILLIUNWARE",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
        "produk": "",
    }

    # ======================
    # JENIS
    # ======================

    jenis_list = [
        "CLOSET DUDUK",
        "CLOSET JONGKOK",
        "WALL HUNG",
        "WASTAFEL",
        "URINAL",
        "SOAP DISH",
        "AVENA",
    ]

    for j in jenis_list:
        if j in text:
            result["jenis"] = j
            break

    # ======================
    # TYPE
    # ======================

    type_list = [
        "EUREKA",
        "EMERALD",
        "CAPRI",
        "CARRIBEAN",
        "MARION",
        "RUBY",
        "SAPPHIRA",
        "OPAL",
        "JASPER",
        "HARVEST",
        "ANDALUZITE",
        "CHRYSOLITE",
        "RHODOLITE",
        "SODALITE",
        "SPENE",
        "MALACHITE",
        "GARNET",
        "COBALT",
        "LILAC",
        "KROOZ",
        "PYRITE",
        "JUNIPER",
        "TOURMALINE",
        "VISCARIA",
        "VELVET",
        "PARTISI",
    ]

    for t in type_list:
        if t in text:
            result["type"] = t
            break

    # ======================
    # WARNA
    # ======================

    warna_list = [
        "BRILLIANT WHITE",
        "WHITE",
        "IVORY",
        "BLACK",
        "GREY",
        "MAROON",
        "LIGHT BLUE",
        "SORRENTO BLUE",
        "APPLE GREEN",
        "PINK",
    ]

    for w in warna_list:
        if w in text:
            result["warna"] = w
            break

    result["produk"] = text

    return result
