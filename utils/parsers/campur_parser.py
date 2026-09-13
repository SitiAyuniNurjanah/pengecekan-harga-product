import re

from utils.helper import bersihkan_text


def parse_campur(text):

    text = bersihkan_text(text)

    result = {
        "brand": "CAMPUR",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    # =========================
    # TOREN POLOS
    # =========================

    if "TOREN POLOS" in text or "POLOS TANGKI" in text:

        result["jenis"] = "TOREN POLOS"

        # Contoh:
        # TOREN POLOS 1000
        # POLOS TANGKI 1000

        m = re.search(r"(\d+)", text)

        if m:
            result["ukuran"] = m.group(1)

    # =========================
    # FIBER PAGAR
    # =========================

    elif "TSUYULITE" in text:

        result["jenis"] = "FIBER PAGAR"

        # Type
        if "POLOS" in text:
            result["type"] = "POLOS"

        elif "GARIS" in text:
            result["type"] = "GARIS"

        # Ukuran
        # Contoh:
        # 0.6 X 1 X 50
        # 0.8 X 1 X 50

        m = re.search(
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+)",
            text
        )

        if m:

            ukuran1 = m.group(1).replace(",", ".")
            ukuran2 = m.group(2).replace(",", ".")
            ukuran3 = m.group(3)

            result["ukuran"] = (
                f"{ukuran1} X {ukuran2} X {ukuran3}"
            )

    # =========================
    # PP FLAT SHEET
    # =========================

    elif "PP FLAT SHEET" in text:

        result["jenis"] = "PP FLAT SHEET"

        # =========================
        # TYPE
        # =========================
        
        if "GARIS" in text:
            result["type"] = "GARIS"

        elif "POLOS" in text:
            result["type"] = "POLOS"

        elif "BAMBU" in text:
            result["type"] = "BAMBU"

        elif "DIMENSI" in text:
            result["type"] = "DIMENSI"

        elif "DIAMOND BATIK" in text:
            result["type"] = "BATIK"

        elif "BATIK" in text:
            result["type"] = "BATIK"

        # =========================
        # UKURAN
        # =========================

        # Contoh:
        # PP FLAT SHEET POLOS 1.2 X 1 X 30 CLEAR
        # PP FLAT SHEET BAMBU 0.6 X 1 X 50 CLEAR
        # PP FLAT SHEET BATIK 0.6 X 1 X 40 CLEAR

        m = re.search(
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+)",
            text
        )

        if m:

            ukuran1 = m.group(1).replace(",", ".")
            ukuran2 = m.group(2).replace(",", ".")
            ukuran3 = m.group(3)

            result["ukuran"] = (
                f"{ukuran1} X {ukuran2} X {ukuran3}"
            )

        # =========================
        # WARNA
        # =========================

        if "CLEAR" in text:
            result["warna"] = "CLEAR"

        elif "BROWN" in text:
            result["warna"] = "BROWN"

        elif "GREEN" in text:
            result["warna"] = "GREEN"

        elif "WHITE" in text:
            result["warna"] = "WHITE"

        elif "BLACK" in text:
            result["warna"] = "BLACK"

    # =========================
    # PP SHEET MOTIF
    # =========================

    elif "PP SHEET MOTIF" in text:

        result["jenis"] = "PP SHEET MOTIF"

        if "MINIMALIS" in text:
            result["type"] = "MINIMALIS"

        # Contoh:
        # 0.6 X 1 M X 40

        m = re.search(
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+(?:[.,]\d+)?)\s*M\s*X\s*"
            r"(\d+)",
            text
        )

        if m:

            ukuran1 = m.group(1).replace(",", ".")
            ukuran2 = m.group(2).replace(",", ".")
            ukuran3 = m.group(3)

            result["ukuran"] = (
                f"{ukuran1} X {ukuran2} M X {ukuran3}"
            )

    # =========================
    # BAK MANDI
    # =========================

    elif "BAK MANDI" in text:

        result["jenis"] = "BAK MANDI"

        if "WALRUS" in text:
            result["type"] = "WALRUS"

        if "KOTAK" in text:
            result["ukuran"] = "KOTAK"

        elif "SUDUT" in text:
            result["ukuran"] = "SUDUT"

    # =========================
    # LEM
    # =========================

    elif "GLUE" in text:

        result["jenis"] = "LEM"

        # Contoh:
        # GLUE 40 GR
        # GLUE 60 GR
        # GLUE 100 GR
        # GLUE 400 GR

        m = re.search(
            r"(\d+)\s*GR",
            text
        )

        if m:
            result["ukuran"] = m.group(1)

    return result