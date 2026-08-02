import pandas as pd
from utils.helper import bersihkan_text


def match_penguin(row, df_penguin):

    # =========================
    # KHUSUS SET KIT TOREN
    # =========================
    if bersihkan_text(row["Jenis"]) == "SET KIT TOREN":

        return None, "SET_KIT"


    type_row = bersihkan_text(row["Type"])
    warna_row = bersihkan_text(row["Warna"])


    type_match = (
        df_penguin["Type"].apply(bersihkan_text)
        == type_row
    )

    ukuran_match = (
        df_penguin["Ukuran"].apply(bersihkan_text)
        == bersihkan_text(row["Ukuran"])
    )


    # =========================
    # KHUSUS TQ
    # AMBIL DARI TYPE + UKURAN SAJA
    # =========================
    if type_row == "TQ":

        master_match = df_penguin[
            type_match
            &
            ukuran_match
        ]


    # =========================
    # HITAM PAKAI HARGA STANDAR
    # =========================
    elif warna_row == "HITAM":

        master_match = df_penguin[
            type_match
            &
            ukuran_match
            &
            (
                df_penguin["Warna"].apply(bersihkan_text)
                == "STANDAR"
            )
        ]


    # =========================
    # WARNA LAIN NORMAL
    # =========================
    else:

        master_match = df_penguin[
            type_match
            &
            ukuran_match
            &
            (
                df_penguin["Warna"].apply(bersihkan_text)
                == warna_row
            )
        ]


    return master_match, "NORMAL"