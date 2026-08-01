# import re


# def pintu_parser(text):

#     # text = str(text).upper().strip()
#     text = str(text).upper().strip()
#     text = text.replace("ALUMINIUM", "ALUMUNIUM")
#     text = text.replace("SAPELLI", "SAPELI")
#     text = text.replace("BLACK", "HITAM")

#     result = {
#         "brand": "PINTU",
#         "jenis": "",
#         "type": "",
#         "kode": "",
#         "ukuran": "",
#         "warna": "",
#     }

#     # ======================
#     # JENIS
#     # ======================

#     if "RUVVO" in text and "UPVC" in text:
#         result["jenis"] = "RUVVO UPVC"

#     elif "RUVVO" in text and "ALUMUNIUM" in text:
#         result["jenis"] = "RUVVO ALUMUNIUM"

#     elif "PVC POLOS" in text:
#         result["jenis"] = "PVC POLOS"

#     elif "MINIMALIS GARIS" in text:
#         result["jenis"] = "PVC MINIMALIS GARIS"

#     elif "PVC OVAL" in text:
#         result["jenis"] = "PVC OVAL"

#     elif "PANEL BINGKAI" in text:
#         result["jenis"] = "PANEL BINGKAI"

#     elif "PANEL SPARTA" in text:
#         result["jenis"] = "PANEL SPARTA"

#     elif "PANEL ORION" in text:
#         result["jenis"] = "PANEL ORION"

#     elif "KACA PERSEGI" in text:
#         result["jenis"] = "KACA PERSEGI"

#     elif "METRO" in text and "UPVC" in text:
#         result["jenis"] = "METRO UPVC"

#     elif "UPVC" in text:
#         result["jenis"] = "UPVC"

#     if "FULL PANEL" in text:
#         result["type"] = "FULL PANEL"
#     elif "KACA" in text:
#         result["type"] = "KACA"

#     # ======================
#     # TYPE
#     # ======================

#     # type_list = []

#     # if "FULL" in text:
#     #     type_list.append("FULL")

#     # if "1/2" in text:
#     #     type_list.append("1/2")

#     # if "1/4" in text:
#     #     type_list.append("1/4")

#     # if "KACA 8" in text:
#     #     type_list.append("KACA 8")

#     # if "MINIMALIS" in text:
#     #     type_list.append("MINIMALIS")

#     # result["type"] = " ".join(type_list)

#     # ======================
#     # WARNA
#     # ======================

#     # warna = [
#     #     "PUTIH",
#     #     "WHITE",
#     #     "WALNUT",
#     #     "SAPELI",
#     #     "BAMBOO",
#     #     "KAYU",
#     #     "BIRU",
#     #     "PINK",
#     #     "HIJAU",
#     #     "CREAM",
#     #     "ABU",
#     #     "COKLAT",
#     #     "HITAM",
#     #     "KAYU",
#     #     "SAPELI",
#     #     "BAMBOO",
#     # ]

#     warna_map = {
#         "WHITE": "PUTIH",
#         "PUTIH": "PUTIH",
#         "WALNUT": "WALNUT",
#         "SAPELI": "SAPELI",
#         "BAMBOO": "BAMBOO",
#         "HITAM": "HITAM",
#         "BIRU": "BIRU",
#         "PINK": "PINK",
#         "HIJAU": "HIJAU",
#         "CREAM": "CREAM",
#         "ABU": "ABU",
#         "COKLAT": "COKLAT",
#         "KAYU": "KAYU",
#     }

#     # for w in warna:
#     #     if w in text:
#     #         result["warna"] = w
#     #         break

#     for sumber, hasil in warna_map.items():
#         if sumber in text:
#             result["warna"] = hasil
#             break

#     return result

import re

def pintu_parser(text):
    text = str(text).upper().strip()
    text = text.replace("ALUMINIUM", "ALUMUNIUM")
    text = text.replace("SAPELLI", "SAPELI")
    text = text.replace("BLACK", "HITAM")

    result = {
        "brand": "PINTU",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    # JENIS
    if "RUVVO" in text and "UPVC" in text:
        result["jenis"] = "RUVVO UPVC"
    elif "RUVVO" in text and "ALUMUNIUM" in text:
        result["jenis"] = "RUVVO ALUMUNIUM"
    elif "PVC POLOS" in text:
        result["jenis"] = "PVC POLOS"
    elif "MINIMALIS GARIS" in text:
        result["jenis"] = "PVC MINIMALIS GARIS"
    elif "PVC OVAL" in text:
        result["jenis"] = "PVC OVAL"
    elif "PANEL BINGKAI" in text:
        result["jenis"] = "PANEL BINGKAI"
    elif "PANEL SPARTA" in text:
        result["jenis"] = "PANEL SPARTA"
    elif "PANEL ORION" in text:
        result["jenis"] = "PANEL ORION"
    elif "KACA PERSEGI" in text:
        result["jenis"] = "KACA PERSEGI"
    elif "METRO" in text and "UPVC" in text:
        result["jenis"] = "METRO UPVC"
    elif "UPVC" in text:
        result["jenis"] = "UPVC"

    # TYPE: disamakan dengan kategori harga master
    if "FULL PANEL" in text:
        result["type"] = "FULL PANEL"
    elif "KACA" in text:
        result["type"] = "KACA"

    # WARNA
    warna_map = {
        "WHITE": "PUTIH",
        "PUTIH": "PUTIH",
        "WALNUT": "WALNUT",
        "SAPELI": "SAPELI",
        "BAMBOO": "BAMBOO",
        "HITAM": "HITAM",
        "BIRU": "BIRU",
        "PINK": "PINK",
        "HIJAU": "HIJAU",
        "CREAM": "CREAM",
        "ABU": "ABU",
        "COKLAT": "COKLAT",
        "KAYU": "KAYU",
    }

    for sumber, warna in warna_map.items():
        if sumber in text:
            result["warna"] = warna
            break

    return result