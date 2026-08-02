import pandas as pd
from utils.helper import bersihkan_text


def match_pipa_bestlon(row, df_pipa_bestlon):

    def normalisasi_ukuran(x):
        return (
            str(x)
            .replace(".0", "")
            .replace('"', "")
            .replace("”", "")
            .replace("″", "")
            .strip()
        )

    if df_pipa_bestlon is None or df_pipa_bestlon.empty:
        return pd.DataFrame()

    master_match = df_pipa_bestlon.copy()

    type_row = bersihkan_text(row["Type"])
    ukuran_row = normalisasi_ukuran(row["Ukuran"])


    # =========================
    # FILTER TYPE
    # =========================
    if type_row:

        master_match = master_match[
            master_match["Type"]
            .fillna("")
            .apply(bersihkan_text)
            == type_row
        ]


    # =========================
    # FILTER UKURAN
    # =========================
    if ukuran_row:

        master_match = master_match[
            master_match["Ukuran"]
            .fillna("")
            .apply(normalisasi_ukuran)
            == ukuran_row
        ]


    return master_match