import re

from utils.helper import bersihkan_text


def parse_steel(text):

    text = bersihkan_text(text)

    result = {
        "brand": "STEEL",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    # =====================
    # BONDEK
    # =====================
    if "BONDEK" in text:

        result["jenis"] = "BONDEK"

        m = re.search(r"(\d+)\s*M", text)
        if m:
            result["ukuran"] = m.group(1)

    # =====================
    # CANAL / CANNAL
    # =====================
    elif "CANAL" in text or "CANNAL" in text:

        result["jenis"] = "CANAL"

        m = re.search(r"C\.?\s*([\d\.]+)", text)
        if m:
            result["ukuran"] = m.group(1)

        if "ECO" in text:
            result["warna"] = "ECO"

        elif "PREMIUM" in text:
            result["warna"] = "PREMIUM"

    # =====================
    # HOLLOW
    # =====================
    elif "HOLLOW" in text:

        result["jenis"] = "HOLLOW"

        m = re.search(
            r"(\d+)\s*[Xx]\s*(\d+)",
            text
        )

        if m:
            result["ukuran"] = f"{m.group(1)} X {m.group(2)}"


    # =====================
    # GALVALUM
    # =====================
    elif "GALVALUM" in text:

        result["jenis"] = "GALVALUM"

        m = re.search(
            r"(\d+\.\d+)\s*X\s*(\d+)\s*X\s*(\d+)",
            text
        )

        if m:
            result["ukuran"] = (
                f"{m.group(1)} X {m.group(2)} X {m.group(3)}"
            )
    # =====================
    # KASSO
    # =====================
    elif "KASSO" in text:

        result["jenis"] = "KASSO"

        m = re.search(r"28\.(\d+)", text)

        if m:
            result["ukuran"] = "28." + m.group(1)

        if "PREMIUM" in text:
            result["warna"] = "PREMIUM"

    # =====================
    # GENTENG
    # =====================
    elif "GENTENG" in text:

        result["jenis"] = "GENTENG"

        if "MERAH" in text:
            result["warna"] = "MERAH"

    # =====================
    # SENG
    # =====================
    elif "SENG" in text:

        result["jenis"] = "SENG"

        m = re.search(r"(\d+)\s*CM", text)

        if m:
            result["ukuran"] = m.group(1)

    # =====================
    # SPANDEK
    # =====================
    elif "SPANDEK" in text:

        result["jenis"] = "SPANDEK"

        m = re.search(r"0[,\.](\d+)", text)

        if m:
            result["ukuran"] = "0." + m.group(1)


        # ambil feet
        m = re.search(r"(\d+)\s*F", text)

        if m:
            result["type"] = m.group(1) + " FEET"


        if "MERAH" in text:
            result["warna"] = "MERAH"
    # =====================
    # TRIMDEK
    # =====================
    elif "TRIMDEK" in text:

        result["jenis"] = "TRIMDEK"

        m = re.search(r"0[,\.](\d+)", text)

        if m:
            result["ukuran"] = "0." + m.group(1)

    return result