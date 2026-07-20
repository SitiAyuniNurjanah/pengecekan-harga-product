import re


def parse_fitting_basic(text):

    text = str(text).upper().strip()

    result = {
        "brand": "TRILLIUN",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }

    # ==========================
    # JENIS FITTING
    # ==========================

    # mapping = {
    #     "FAUCET SOCKET": "FAUCET SOCKET",
    #     "FAUCET KNEE": "FAUCET KNEE",
    #     "FAUCET TEE": "FAUCET TEE",
    #     "VALVE SOCKET": "VALVE SOCKET",
    #     "WATER MUR SOCKET": "WATERMUR",
    #     "WATER MUR VALVE SOCKET": "WATERMUR",
    #     "LONG ELBOW": "LONG ELBOW",
    #     "SOCKET": "SOCKET",
    #     "KNEE": "KNEE",
    #     "TEE": "TEE",
    #     "PLUG": "PLUG",
    #     "DOP": "DOP",
    # }

    mapping = {
        "WATER MUR VALVE SOCKET": "WATERMUR",
        "WATER MUR SOCKET": "WATERMUR",
        "FAUCET SOCKET": "FAUCET SOCKET",
        "FAUCET KNEE": "FAUCET KNEE",
        "FAUCET TEE": "FAUCET TEE",
        "VALVE SOCKET": "VALVE SOCKET",
        "LONG ELBOW": "LONG ELBOW",
        "SOCKET": "SOCKET",
        "KNEE": "KNEE",
        "TEE": "TEE",
        "PLUG": "PLUG",
        "DOP": "DOP",
    }

    for key, value in mapping.items():
        if key in text:
            result["jenis"] = value
            break

    # ==========================
    # TYPE TS / DV / AW / D
    # ==========================

    tipe = re.search(r"\b(TS|DV|AW|D)\b", text)

    if tipe:
        result["type"] = tipe.group(1)

    # ==========================
    # UKURAN
    # ==========================

    # ukuran = re.search(
    #     r'((\d+\s*\d*/\d+"|\d+/\d+"|\d+")(\s*[Xx]\s*(\d+\s*\d*/\d+"|\d+/\d+"|\d+"))?)',
    #     text,
    # )

    # ukuran = re.search(
    #     r'(\d+(?:\s+\d+/\d+)?(?:/\d+)?"?(?:\s*[Xx]\s*\d+(?:\s+\d+/\d+)?(?:/\d+)?"?)?)',
    #     text,
    # )

    ukuran = re.search(
        r"(\d+(?:\s+\d+/\d+)?(?:/\d+)?\"?(?:\s*[Xx]\s*\d+(?:\s+\d+/\d+)?(?:/\d+)?\"?)?)",
        text,
    )

    # if ukuran:
    #     result["ukuran"] = ukuran.group(1).replace("X", "x").replace("  ", " ").strip()

    # if ukuran:
    #     result["ukuran"] = ukuran.group(1).replace("X", "x").replace("  ", " ").strip()
    result["ukuran"] = ukuran.group(1).replace("X","x").strip()
    
    return result
