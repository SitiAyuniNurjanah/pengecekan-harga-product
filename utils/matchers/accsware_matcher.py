from utils.helper import bersihkan_text


def match_accsware(row, df_accsware):

    if df_accsware is None or df_accsware.empty:
        return df_accsware

    nama = bersihkan_text(row["Nama Barang"])

    master_match = df_accsware.copy()

    # =====================================================
    # MATCH NAMA BARANG
    # =====================================================

    master_match = master_match[
        master_match["Produk"]
        .apply(bersihkan_text)
        == nama
    ]

    return master_match