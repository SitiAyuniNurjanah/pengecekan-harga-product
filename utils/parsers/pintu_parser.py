import re


def pintu_parser(text):

    # text = str(text).upper().strip()
    text = str(text).upper().strip()
    text = text.replace("ALUMINIUM", "ALUMUNIUM")
    text = text.replace("SAPELLI", "SAPELI")

    result = {
        "brand": "PINTU",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    # ======================
    # JENIS
    # ======================

    if "PVC POLOS" in text:
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

    elif "RUVVO" in text and "ALUMUNIUM" in text:
        result["jenis"] = "RUVVO ALUMUNIUM"

    elif "METRO" in text and "ALUMUNIUM" in text:
        result["jenis"] = "METRO ALUMUNIUM"

    elif "RUVVO" in text and "UPVC" in text:
        result["jenis"] = "RUVVO UPVC"

    elif "METRO" in text and "UPVC" in text:
        result["jenis"] = "METRO UPVC"

    # ======================
    # WARNA
    # ======================

    warna = [
        "PUTIH",
        "WHITE",
        "BIRU",
        "PINK",
        "HIJAU",
        "CREAM",
        "ABU",
        "COKLAT",
        "HITAM",
        "KAYU",
        "SAPELI",
        "BAMBOO",
    ]

    for w in warna:
        if w in text:
            result["warna"] = w
            break

    return result