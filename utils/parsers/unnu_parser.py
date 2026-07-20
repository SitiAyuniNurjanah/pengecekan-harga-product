# import re


# def parse_unnu(text):

#     text = str(text).upper().strip()

#     result = {
#         "brand": "UNNU",
#         "jenis": "",
#         "type": "",
#         # "kode": "",
#         "ukuran": "",
#         "warna": "",
#     }

#     # ==================================
#     # JENIS PRODUK
#     # ==================================

#     mapping_jenis = [
#         ("TOILET SHOWER", "TOILET SHOWER"),
#         ("HAND SHOWER", "HAND SHOWER"),
#         ("PVC FOOT VALVE", "PVC FOOT VALVE"),
#         ("PVC VALVE", "PVC VALVE"),
#         ("FOOT VALVE", "FOOT VALVE"),
#         ("BIBCOCK", "BIBCOCK"),
#         ("BOBCOCK", "BOBCOCK"),
#         ("KRAN DAPUR", "KRAN DAPUR"),
#         ("STOP KRAN OTOMATIS", "STOP KRAN OTOMATIS"),
#         ("STOP KRAN", "STOP KRAN"),
#         ("METERAN", "METERAN"),
#         ("TUSEN KLEP", "TUSEN KLEP"),
#         ("BALL VALVE", "BALL VALVE"),
#         ("GATE VALVE", "GATE VALVE"),
#         ("CHECK VALVE", "CHECK VALVE"),
#         ("FILTER", "FILTER"),
#     ]

#     for keyword, jenis in mapping_jenis:
#         if keyword in text:
#             result["jenis"] = jenis
#             break
#     # ==================================
#     # KODE PRODUK
#     # ==================================

#     pola_kode = (
#         r"\b("
#         r"PVBV\d+|"
#         r"PKM\d+|"
#         r"PK\d+|"
#         r"FVP\d+|"
#         r"GTP\d+|"
#         r"GTA\d+|"
#         r"GTB\d+|"
#         r"GTL\d+|"
#         r"GT\d+|"
#         r"KTL\d+|"
#         r"KTA\d+|"
#         r"KT\d+BK|"
#         r"KT\d+|"
#         r"STL\d+|"
#         r"ST\d+BK|"
#         r"ST\d+|"
#         r"DTL\d+|"
#         r"DT\d+BK|"
#         r"DT\d+|"
#         r"AVSS\d+BK|"
#         r"AVSS\d+|"
#         r"AVB\d+|"
#         r"HSS\d+|"
#         r"TS\d+|"
#         r"SD\d+[A-Z]*|"
#         r"SE\d+|"
#         r"SH\d+|"
#         r"FDA\d+|"
#         r"FD\d+|"
#         r"MXT\d+|"
#         r"MT\d+[A-Z]?|"
#         r"BV|GV|CV|"
#         r"AWH|AWV|"
#         r"PP|FR|TK"
#         r")"
#     )

#     kode = re.search(pola_kode, text)

#     if kode:

#         result["type"] = kode.group(1)

#     # ==================================
#     # KHUSUS HAND SHOWER
#     # ==================================

#     if "HAND SHOWER SET 01" in text:

#         result["type"] = "HSS01"

#     elif "HAND SHOWER SET 02" in text:

#         result["type"] = "HSS02"

#     # ==================================
#     # KHUSUS TOILET SHOWER
#     # ==================================

#     ts = re.search(r"(TS\d+)(CR|WH|IV|BK)?", text)

#     if ts:

#         result["type"] = ts.group(1)

#         kode_warna = ts.group(2)

#         mapping = {"CR": "CROME", "WH": "WHITE", "IV": "IVORY", "BK": "BLACK"}

#         if kode_warna:

#             result["warna"] = mapping.get(kode_warna, "")

#     # ==================================
#     # WARNA DARI KODE
#     # ==================================

#     warna_kode = re.search(r"(HSS\d+|TS\d+)(CR|WH|IV|BK)", text)

#     if warna_kode:

#         result["type"] = warna_kode.group(1)

#         mapping = {"CR": "CROME", "WH": "WHITE", "IV": "IVORY", "BK": "BLACK"}

#         result["warna"] = mapping.get(warna_kode.group(2), "")

#     # ==================================
#     # WARNA TEXT MASTER
#     # ==================================

#     if result["warna"] == "":

#         if "CHROME" in text or "CROME" in text:

#             result["warna"] = "CROME"

#         elif "WHITE" in text:

#             result["warna"] = "WHITE"

#         elif "IVORY" in text:

#             result["warna"] = "IVORY"

#         elif "BLACK" in text:

#             result["warna"] = "BLACK"

#         elif "PINK" in text:

#             result["warna"] = "PINK"

#         elif "BLUE" in text:

#             result["warna"] = "BLUE"

#     # ==================================
#     # PRODUK TANPA KODE
#     # ==================================

#     if result["type"] == "":

#         if "BALL VALVE" in text:

#             result["type"] = "BV"

#         elif "GATE VALVE" in text:

#             result["type"] = "GV"

#         elif "CHECK VALVE" in text:

#             result["type"] = "CV"

#         elif "FILTER" in text:

#             result["type"] = "FR"

#         elif "TUSEN KLEP" in text:

#             result["type"] = "TK"

#     # ==================================
#     # UKURAN
#     # ==================================

#     ukuran = re.search(r'(\d+/\d+"|\d+\s*M|\d+\s*CM|\d+\s*ML)', text)

#     if ukuran:

#         result["ukuran"] = ukuran.group(1).replace(" ", "")

#     return result

import re


def parse_unnu(text):
    text = str(text).upper().strip()

    result = {
        "brand": "UNNU",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    # ==================================
    # JENIS
    # ==================================
    mapping_jenis = [
        ("TOILET SHOWER", "TOILET SHOWER"),
        ("HAND SHOWER", "HAND SHOWER"),
        ("PVC FOOT VALVE", "PVC FOOT VALVE"),
        ("PVC VALVE", "PVC VALVE"),
        ("FOOT VALVE", "FOOT VALVE"),
        ("BIBCOCK", "BIBCOCK"),
        ("BOBCOCK", "BOBCOCK"),
        ("KRAN DAPUR", "KRAN DAPUR"),
        ("STOP KRAN OTOMATIS", "STOP KRAN OTOMATIS"),
        ("STOP KRAN", "STOP KRAN"),
        ("METERAN", "METERAN"),
        ("TUSEN KLEP", "TUSEN KLEP"),
        ("BALL VALVE", "BALL VALVE"),
        ("GATE VALVE", "GATE VALVE"),
        ("CHECK VALVE", "CHECK VALVE"),
        ("FILTER", "FILTER"),
    ]

    for keyword, jenis in mapping_jenis:
        if keyword in text:
            result["jenis"] = jenis
            break

    # ==================================
    # TYPE
    # ==================================
    pola_type = (
        r"\b("
        r"PVBV\d+|"
        r"PKM\d+|"
        r"PK\d+|"
        r"FVP\d+|"
        r"GTP\d+|"
        r"GTA\d+|"
        r"GTB\d+|"
        r"GTL\d+|"
        r"GT\d+|"
        r"KTL\d+|"
        r"KTA\d+|"
        r"KT\d+BK|"
        r"KT\d+|"
        r"STL\d+|"
        r"ST\d+BK|"
        r"ST\d+|"
        r"DTL\d+|"
        r"DT\d+BK|"
        r"DT\d+|"
        r"AVSS\d+BK|"
        r"AVSS\d+|"
        r"AVB\d+|"
        r"HSS\d+|"
        r"TS\d+|"
        r"SD\d+[A-Z]*|"
        r"SE\d+|"
        r"SH\d+|"
        r"FDA\d+|"
        r"FD\d+|"
        r"MXT\d+|"
        r"MT\d+[A-Z]?|"
        r"BV|GV|CV|"
        r"AWH|AWV|"
        r"PP|FR|TK"
        r")\b"
    )

    type_match = re.search(pola_type, text)

    # Posisi awal pencarian ukuran.
    # Default-nya setelah kode/type supaya "01" di PVBV01 tidak terbaca ukuran.
    posisi_setelah_type = 0

    if type_match:
        result["type"] = type_match.group(1)
        posisi_setelah_type = type_match.end()

    # ==================================
    # HAND SHOWER
    # ==================================
    hand_shower_match = re.search(r"HAND SHOWER SET\s+(01|02)\b", text)

    if hand_shower_match:
        result["type"] = f"HSS{hand_shower_match.group(1)}"
        posisi_setelah_type = hand_shower_match.end()

    # ==================================
    # WARNA DARI KODE TS / HSS
    # Contoh: TS01WH, HSS01CR
    # ==================================
    warna_kode = re.search(r"(TS\d+|HSS\d+)(CR|WH|IV|BK)\b", text)

    if warna_kode:
        result["type"] = warna_kode.group(1)
        posisi_setelah_type = warna_kode.end()

        mapping_warna_kode = {
            "CR": "CROME",
            "WH": "WHITE",
            "IV": "IVORY",
            "BK": "BLACK",
        }

        result["warna"] = mapping_warna_kode.get(
            warna_kode.group(2),
            ""
        )

    # ==================================
    # WARNA DARI NAMA
    # ==================================
    if result["warna"] == "":
        if "CHROME" in text or "CROME" in text:
            result["warna"] = "CROME"
        elif "WHITE" in text:
            result["warna"] = "WHITE"
        elif "IVORY" in text:
            result["warna"] = "IVORY"
        elif "BLACK" in text:
            result["warna"] = "BLACK"
        elif "PINK" in text:
            result["warna"] = "PINK"
        elif "BLUE" in text:
            result["warna"] = "BLUE"

    # ==================================
    # TYPE TANPA KODE
    # ==================================
    if result["type"] == "":
        if "BALL VALVE" in text:
            result["type"] = "BV"
        elif "GATE VALVE" in text:
            result["type"] = "GV"
        elif "CHECK VALVE" in text:
            result["type"] = "CV"
        elif "FILTER" in text:
            result["type"] = "FR"
        elif "TUSEN KLEP" in text:
            result["type"] = "TK"

    # ==================================
    # UKURAN
    # Dicari SETELAH type/kode.
    # Mendukung: 1/2", 3/4", 1", 1 1/4", 1 1/2", 2"
    # ==================================
    teks_ukuran = text[posisi_setelah_type:].strip()

    ukuran_match = re.search(
        r'(?<!\d)(\d+\s+\d+/\d+|\d+/\d+|\d+)\s*(?:"|”|″)?',
        teks_ukuran,
    )

    if ukuran_match:
        result["ukuran"] = re.sub(
            r"\s+",
            " ",
            ukuran_match.group(1).strip(),
        )

    return result