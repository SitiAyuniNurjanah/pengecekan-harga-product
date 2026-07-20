import re


def parse_pipa_bestlon(text):

    text = str(text).upper().strip()

    result = {
        "brand": "BESTLON",
        "jenis": "PIPA",
        "type": "",
        "ukuran": "",
        "warna": "PUTIH",
    }

    # =====================
    # TYPE
    # =====================

    if re.search(r"\bAW\b", text):
        result["type"] = "AW"

    elif re.search(r"\bD\b", text):
        result["type"] = "D"

    elif re.search(r"\bC\b", text):
        result["type"] = "C"

    # =====================
    # UKURAN
    # =====================

    ukuran = re.search(r'(\d+\s+\d+/\d+|\d+/\d+|\d+)\s*(?:"|”|″)', text)

    if ukuran:
        result["ukuran"] = ukuran.group(1).strip()

    return result
