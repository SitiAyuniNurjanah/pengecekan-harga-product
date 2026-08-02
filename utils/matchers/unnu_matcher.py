from utils.helper import bersihkan_text


def match_unnu(row, df_unnu):

    if df_unnu is None or df_unnu.empty:
        return df_unnu

    nama = bersihkan_text(row["Nama Barang"])

    master_match = df_unnu.copy()

    # =========================
    # FILTER JENIS KHUSUS
    # =========================

    if "Jenis" in master_match.columns:

        jenis_master = master_match["Jenis"].fillna("").apply(bersihkan_text)

        # Floating Valve -> PP
        if "FLOATING VALVE" in nama:

            master_match = master_match[
                jenis_master == "PP"
            ]

        # Tusen Klep -> TK
        elif "TUSEN KLEP" in nama or "TK" in nama:

            master_match = master_match[
                jenis_master == "TK"
            ]

    # =========================
    # FILTER TYPE
    # =========================

    type_row = bersihkan_text(row["Type"])

    if (
        type_row
        and not master_match.empty
        and "Type" in master_match.columns
    ):

        master_match = master_match[
            master_match["Type"]
            .fillna("")
            .apply(bersihkan_text)
            == type_row
        ]

    # =========================
    # FILTER UKURAN
    # =========================

    ukuran_row = bersihkan_text(row["Ukuran"])

    if (
        ukuran_row
        and not master_match.empty
        and "Ukuran" in master_match.columns
    ):

        ukuran_master = (
            master_match["Ukuran"]
            .fillna("")
            .apply(bersihkan_text)
            .str.replace('"', "", regex=False)
            .str.replace("CM", "", regex=False)
        )

        master_match = master_match[
            ukuran_master
            == ukuran_row.replace('"', "").replace("CM", "")
        ]

    # =========================
    # FILTER WARNA
    # =========================

    warna_row = bersihkan_text(row["Warna"])

    if (
        warna_row
        and not master_match.empty
        and "Warna" in master_match.columns
        and master_match["Warna"].fillna("").apply(bersihkan_text).ne("").any()
    ):

        master_match = master_match[
            master_match["Warna"]
            .fillna("")
            .apply(bersihkan_text)
            == warna_row
        ]

    return master_match