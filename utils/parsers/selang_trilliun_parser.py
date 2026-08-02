import re


def parse_trilliun(text):

    text = str(text).upper().strip()

    result = {"brand": "TRILLIUN", "jenis": "", "type": "", "ukuran": "", "warna": ""}

    # JENIS - JENIS SELANG

    if "SPIRAL PREMIUM" in text:
        result["jenis"] = "SPIRAL"

    elif "SPIRAL" in text:
        result["jenis"] = "SPIRAL"

    elif "SUPERFLEX" in text or "SFLEX" in text:
        result["jenis"] = "SUPERFLEX"

    elif "HIPREX" in text:
        result["jenis"] = "HIPREX"

    elif "DOF" in text or "SELANG DOF" in text:
        result["jenis"] = "DOF"

    elif "STABILO" in text:
        result["jenis"] = "STABILO"

    elif "ELASTIS TEBAL" in text or "TEBAL" in text:
        result["jenis"] = "ELASTIS TEBAL"

    elif "TRANSPARAN" in text or "TRS" in text:
        result["jenis"] = "TRANSPARAN"

    # PANJANG SELANG

    meter = re.search(r"\((\d+)\s*M?\)", text)

    if not meter:
        meter = re.search(r"(\d+)\s*M", text)

    if not meter:
        meter = re.search(r"\((\d+)\)", text)

    if meter:
        result["ukuran"] = meter.group(1) + "M"

    # UKURAN SELANG

    uk = re.search(r'(\d+\s+\d+/\d+|\d+/\d+|\d+)\s*(?:"|”|″)', text)

    if uk:
        result["type"] = uk.group(1).strip()

    # WARNA SELANG

    warna = re.search(
        r"(BRILLIANT WHITE|LIGHT BLUE|BLACK|GREY|IVORY|PUTIH|BIRU|HIJAU|MERAH|KUNING)",
        text,
    )

    if warna:
        result["warna"] = warna.group(1)

    return result
