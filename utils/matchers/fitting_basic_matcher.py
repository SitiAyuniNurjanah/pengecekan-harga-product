# import pandas as pd
# from utils.helper import bersihkan_text


# def match_fitting_basic(row, df_fitting_basic):

#     cek = df_fitting_basic[
#         df_fitting_basic["Jenis"]
#         .apply(bersihkan_text)
#         == bersihkan_text(row["Jenis"])
#     ]

#     master_match = df_fitting_basic[
#         (
#             df_fitting_basic["Jenis"].apply(bersihkan_text)
#             == bersihkan_text(row["Jenis"])
#         )
#         & (
#             df_fitting_basic["Type"].apply(bersihkan_text)
#             == bersihkan_text(row["Type"])
#         )
#         & (
#             df_fitting_basic["Ukuran"].apply(bersihkan_text)
#             == bersihkan_text(row["Ukuran"])
#         )
#     ]
    
#     return master_match

import re

from utils.helper import bersihkan_text


def normalisasi_type(text):
    """
    Normalisasi Type:
    TS -> TS
    DV -> DV
    ts -> TS
    """

    if text is None:
        return ""

    text = str(text).upper().strip()

    text = re.sub(r"\s+", " ", text)

    return text


def normalisasi_ukuran_match(text):
    """
    Normalisasi ukuran khusus untuk proses matching.
    """

    if text is None:
        return ""

    text = str(text).upper().strip()

    # Hilangkan tanda kutip
    text = text.replace('"', "")
    text = text.replace("'", "")

    # Samakan X
    text = re.sub(r"\s*X\s*", " X ", text)

    # Rapikan spasi
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def normalisasi_jenis(text):
    """
    Normalisasi jenis fitting.
    """

    if text is None:
        return ""

    text = str(text).upper().strip()

    text = re.sub(r"\s+", " ", text)

    return text


def match_fitting_basic(row, df_fitting_basic):

    if df_fitting_basic is None or df_fitting_basic.empty:
        return df_fitting_basic

    # =========================================================
    # NILAI DARI ORDER
    # =========================================================

    jenis_order = normalisasi_jenis(
        row.get("Jenis", "")
    )

    type_order = normalisasi_type(
        row.get("Type", "")
    )

    ukuran_order = normalisasi_ukuran_match(
        row.get("Ukuran", "")
    )

    # =========================================================
    # BUAT COPY MASTER
    # =========================================================

    master = df_fitting_basic.copy()

    # =========================================================
    # NORMALISASI MASTER
    # =========================================================

    master["_jenis_match"] = (
        master["Jenis"]
        .apply(normalisasi_jenis)
    )

    master["_type_match"] = (
        master["Type"]
        .apply(normalisasi_type)
    )

    master["_ukuran_match"] = (
        master["Ukuran"]
        .apply(normalisasi_ukuran_match)
    )

    # =========================================================
    # MATCH
    # =========================================================

    master_match = master[
        (master["_jenis_match"] == jenis_order)
        &
        (master["_type_match"] == type_order)
        &
        (master["_ukuran_match"] == ukuran_order)
    ]

    # =========================================================
    # HAPUS KOLOM BANTU
    # =========================================================

    master_match = master_match.drop(
        columns=[
            "_jenis_match",
            "_type_match",
            "_ukuran_match",
        ],
        errors="ignore"
    )

    return master_match