# import re


# def parse_fitting_basic(text):

#     text = str(text).upper().strip()

#     result = {
#         "brand": "TRILLIUN",
#         "jenis": "",
#         "type": "",
#         "kode": "",
#         "ukuran": "",
#         "warna": "",
#     }

#     # ==========================
#     # JENIS FITTING
#     # ==========================

#     mapping = [
#         ("WATER MUR VALVE SOCKET", "WATERMUR"),
#         ("WATER MUR SOCKET", "WATERMUR"),
#         ("FAUCET SOCKET", "FAUCET SOCKET"),
#         ("FAUCET KNEE", "FAUCET KNEE"),
#         ("FAUCET TEE", "FAUCET TEE"),
#         ("VALVE SOCKET", "VALVE SOCKET"),
#         ("LONG ELBOW", "LONG ELBOW"),
#         ("SOCKET", "SOCKET"),
#         ("KNEE", "KNEE"),
#         ("TEE", "TEE"),
#         ("PLUG", "PLUG"),
#         ("DOP", "DOP"),
#     ]

#     for key, value in mapping:
#         if key in text:
#             result["jenis"] = value
#             break

#     # ==========================
#     # TYPE
#     # TS / DV / AW / D
#     # ==========================

#     tipe = re.search(
#         r"\b(TS|DV|AW|D)\b",
#         text
#     )

#     if tipe:
#         result["type"] = tipe.group(1)

#     # ==========================
#     # UKURAN
#     # ==========================

#     ukuran = re.search(
#         r"\b\d+(?:\s+\d+/\d+)?(?:/\d+)?(?:\s*[Xx]\s*\d+(?:\s+\d+/\d+)?(?:/\d+)?)?\b",
#         text
#     )

#     if ukuran:
#         result["ukuran"] = (
#             ukuran.group(0)
#             .replace(" ", " ")
#             .replace("X", "x")
#             .strip()
#         )

#     return result

import re


def normalisasi_ukuran(text):
    """
    Menyamakan format ukuran agar:
    2 1/2"      -> 2 1/2
    2x1 1/2"    -> 2 x 1 1/2
    2 x 1/2     -> 2 x 1/2
    """

    text = str(text).upper().strip()

    # Hilangkan tanda kutip ukuran
    text = text.replace('"', "")
    text = text.replace("'", "")

    # Samakan X
    text = re.sub(r"\s*[X]\s*", " x ", text)

    # Rapikan spasi
    text = re.sub(r"\s+", " ", text)

    return text.strip()


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

    # =========================================================
    # JENIS FITTING
    # =========================================================

    mapping = [
        ("WATER MUR VALVE SOCKET", "WATERMUR"),
        ("WATER MUR SOCKET", "WATERMUR"),

        ("FAUCET SOCKET", "FAUCET SOCKET"),
        ("FAUCET KNEE", "FAUCET KNEE"),
        ("FAUCET TEE", "FAUCET TEE"),

        ("VALVE SOCKET", "VALVE SOCKET"),

        ("LONG ELBOW", "LONG ELBOW"),

        ("SOCKET", "SOCKET"),
        ("KNEE", "KNEE"),
        ("TEE", "TEE"),
        ("PLUG", "PLUG"),
        ("DOP", "DOP"),
    ]

    for key, value in mapping:
        if key in text:
            result["jenis"] = value
            break

    # =========================================================
    # TYPE
    # TS / DV / AW / D
    # =========================================================

    tipe = re.search(
        r"\b(TS|DV|AW|D)\b",
        text
    )

    if tipe:
        result["type"] = tipe.group(1)

    # =========================================================
    # UKURAN
    # =========================================================

    # Cari bagian setelah TS / DV / AW / D
    ukuran = ""

    if result["type"]:
        pattern = rf"\b{re.escape(result['type'])}\b\s+(.+)$"
        match = re.search(pattern, text)

        if match:
            ukuran = match.group(1).strip()

    # Kalau tidak ketemu, fallback cari pola ukuran
    if not ukuran:

        ukuran_match = re.search(
            r"""
            \d+
            (?:\s+\d+/\d+)?
            (?:\s*x\s*
                \d+
                (?:\s+\d+/\d+)?
            )?
            """,
            text,
            re.IGNORECASE | re.VERBOSE
        )

        if ukuran_match:
            ukuran = ukuran_match.group(0).strip()

    # =========================================================
    # KHUSUS REDUCER
    # =========================================================

    # Contoh:
    # SOCKET BASIC TS REDUCER 1 x 1/2
    # SOCKET BASIC TS REDUCER 1 x 3/4
    # SOCKET BASIC TS REDUCER 3/4 x 1/2

    if ukuran.upper().startswith("REDUCER "):
        ukuran = ukuran[8:].strip()

    # =========================================================
    # NORMALISASI UKURAN
    # =========================================================

    ukuran = normalisasi_ukuran(ukuran)

    result["ukuran"] = ukuran

    return result