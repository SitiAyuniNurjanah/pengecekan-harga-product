import re


def parse_penguin(text):

    text = str(text).upper().strip()

    result = {
        "brand": "PENGUIN",
        "jenis": "",
        "type": "",
        "ukuran": "",
        "warna": "STANDAR",
    }

    # ===================
    # JENIS
    # ===================

    if "PLUMBING" in text:
        result["jenis"] = "SET KIT TOREN"
    
    elif "PENGUIN OTO LEVEL (NL)" in text:
        result["jenis"] = "SET KIT TOREN"

    elif "SLIM TANK" in text:
        result["jenis"] = "SLIM TANK"

    elif "UNDERGROUND" in text:
        result["jenis"] = "UNDERGROUND TANK"

    elif "DOSING" in text:
        result["jenis"] = "DOSING TANK"

    elif "SEPTICTANK" in text or "SEPTIC" in text:
        result["jenis"] = "SEPTIC TANK"

    elif "BLOW TANK" in text:
        result["jenis"] = "BLOW TANK"

    elif "CUBIC" in text:
        result["jenis"] = "CUBIC TANK"

    elif "HORIZONTAL" in text:
        result["jenis"] = "HORIZONTAL TANK"

    elif "STAINLESS" in text:
        result["jenis"] = "STAINLESS TANK"

    elif "MODULAR" in text:
        result["jenis"] = "MODULAR TANK"

    elif "SILO" in text:
        result["jenis"] = "SILO TANK"

    elif "TANGKI" in text or "TOREN" in text:
        result["jenis"] = "TANGKI"

    # ===================
    # TYPE & UKURAN
    # ===================

    match = re.search(
        r"\b(TBSK|BIO|BIS|TB|TD|TH|TW|TQ|TU|TA|TS|TR|TE|BT|TV|DC|SL)\s*[-/]?\s*([0-9]+(?:\.[0-9]+)?)",
        text,
    )

    if match:
        result["type"] = match.group(1)
        result["ukuran"] = match.group(2)

    # ===================
    # WARNA (FIX)
    # ===================

    if re.search(r"(ORANGE|ORANYE|OREN)", text):
        result["warna"] = "OREN"

    elif "KUNING" in text:
        result["warna"] = "KUNING"

    else:
        result["warna"] = "STANDAR"

    return result
