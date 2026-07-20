import re


def pureflo_fitting_parser(text):

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
    # JENIS
    # ==========================

    mapping = {
        "FAUCET SOCKET WITH METAL": "FAUCET SOCKET METAL",
        "FAUCET ELBOW WITH METAL": "FAUCET ELBOW METAL",
        "REDUCER SOCKET": "REDUCER SOCKET",
        "INCREASER SOCKET": "INCREASER SOCKET",
        "VALVE SOCKET": "VALVE SOCKET",
        "FAUCET SOCKET": "FAUCET SOCKET",
        "FAUCET ELBOW": "FAUCET ELBOW",
        "FAUCET TEE": "FAUCET TEE",
        "UNION THREAD": "UNION THREAD",
        "ELBOW 45": "ELBOW 45",
        "ELBOW": "ELBOW",
        "SOCKET": "SOCKET",
        "TEE": "TEE",
        "PLUG": "PLUG",
        "CAP": "CAP",
    }

    for key, value in mapping.items():
        if key in text:
            result["jenis"] = value
            break

    # ==========================
    # TYPE
    # ==========================

    tipe = re.search(r"\b(AW|D)\b", text)

    if tipe:
        result["type"] = tipe.group(1)

    # ==========================
    # UKURAN
    # ==========================

    ukuran = re.search(
        r'((\d+\s*\d*/\d+"|\d+/\d+"|\d+")(\s*[Xx]\s*(\d+\s*\d*/\d+"|\d+/\d+"|\d+"))?)',
        text,
    )

    if ukuran:
        result["ukuran"] = ukuran.group(1).replace("X", "x").replace("  ", " ").strip()

    return result
