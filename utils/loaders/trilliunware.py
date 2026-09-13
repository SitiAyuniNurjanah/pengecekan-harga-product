import pandas as pd

from utils.helper import bersihkan_harga, bersihkan_text


def load_trilliunware(df):

    hasil = []

    # ============================================================
    # DAFTAR TYPE TRILLIUNWARE
    # ============================================================

    type_list = [
        "AMETHYST",
        "EUREKA",
        "EMERALD",
        "CAPRI",
        "CARRIBEAN",
        "MARION",
        "RUBY",
        "SAPPHIRA",
        "OPAL",
        "JASPER",
        "HARVEST",
        "ANDALUZITE",
        "CHRYSOLITE",
        "RHODOLITE",
        "SODALITE",
        "SPENE",
        "MALACHITE",
        "GARNET",
        "COBALT",
        "LILAC",
        "KROOZ",
        "PYRITE",
        "JUNIPER",
        "CITRINE",
        "PERIDOT",
    ]

    # ============================================================
    # DAFTAR TYPE YANG MERUPAKAN CLOSET DUDUK
    # ============================================================

    closet_duduk_types = {
        "AMETHYST",
        "EUREKA",
        "EMERALD",
        "MARION",
        "RUBY",
        "SAPPHIRA",
        "OPAL",
        "JASPER",
        "HARVEST",
        "ANDALUZITE",
        "CHRYSOLITE",
        "RHODOLITE",
        "SODALITE",
        "SPENE",
        "PYRITE",
        "JUNIPER",
    }

    # ============================================================
    # LOOP DATA MASTER
    # ============================================================

    for _, row in df.iterrows():

        # Pastikan minimal 4 kolom
        if len(row) < 4:
            continue

        kategori = bersihkan_text(row.iloc[0])
        produk = bersihkan_text(row.iloc[1])
        harga_muda = bersihkan_harga(row.iloc[2])
        harga_tua = bersihkan_harga(row.iloc[3])

        # Kalau produk kosong, skip
        if not produk:
            continue

        # ========================================================
        # TYPE
        # ========================================================

        type_produk = ""

        for t in type_list:
            if t in produk:
                type_produk = t
                break

        # ========================================================
        # JENIS
        # ========================================================

        jenis = ""

        # --------------------------------------------------------
        # 1. Kalau jelas ada CD
        # --------------------------------------------------------

        if "CD" in produk:
            jenis = "CLOSET DUDUK"

        # --------------------------------------------------------
        # 2. Kalau jelas ada CJ
        # --------------------------------------------------------

        elif "CJ" in produk:
            jenis = "CLOSET JONGKOK"

        # --------------------------------------------------------
        # 3. Kalau Type termasuk model Closet Duduk
        #
        # Ini bagian PERBAIKAN UTAMA.
        # Tidak lagi bergantung hanya pada tulisan "CD".
        # --------------------------------------------------------

        elif type_produk in closet_duduk_types:
            jenis = "CLOSET DUDUK"

        # --------------------------------------------------------
        # 4. Produk lain berdasarkan kategori
        # --------------------------------------------------------

        elif kategori == "WASTAFEL":
            jenis = "WASTAFEL"

        elif kategori == "URINAL":
            jenis = "URINAL"

        elif kategori == "SOAP DISH":
            jenis = "SOAP DISH"

        # ========================================================
        # VARIAN
        # ========================================================

        varian = ""

        # --------------------------------------------------------
        # VARIAN UMUM
        # --------------------------------------------------------

        if "SET" in produk and "TANPA KRAN" in produk:

            varian = "SET TANPA KRAN"

        elif "BODY ONLY" in produk:

            varian = "BODY ONLY"

        elif "KAKI ONLY" in produk:

            varian = "KAKI ONLY"

        elif "SET" in produk and (
            "DGN KRAN" in produk
            or "DENGAN KRAN" in produk
        ):

            varian = "SET DGN KRAN"

        elif "BASIN TAP" in produk:

            varian = "BASIN TAP"

        # ========================================================
        # KHUSUS MALACHITE
        # ========================================================

        if type_produk == "MALACHITE":

            sub_varian = ""

            if "GARNET" in produk:
                sub_varian = "GARNET"

            elif "LILAC" in produk:
                sub_varian = "LILAC"

            if sub_varian:

                if "BODY ONLY" in produk:

                    varian = f"{sub_varian} BODY ONLY"

                elif "KAKI ONLY" in produk:

                    varian = f"{sub_varian} KAKI ONLY"

                elif "SET" in produk and "TANPA KRAN" in produk:

                    varian = f"{sub_varian} SET TANPA KRAN"

                elif "SET" in produk and (
                    "DGN KRAN" in produk
                    or "DENGAN KRAN" in produk
                ):

                    varian = f"{sub_varian} SET DGN KRAN"

                else:

                    varian = sub_varian

        # ========================================================
        # WARNA
        # ========================================================

        warna = ""

        if "BLACK" in produk:

            warna = "BLACK"

        elif "GREY" in produk:

            warna = "GREY"

        # ========================================================
        # SIMPAN HASIL
        # ========================================================

        hasil.append(
            {
                "Brand": "TRILLIUNWARE",
                "Kategori": kategori,
                "Produk": produk,
                "Jenis": jenis,
                "Type": type_produk,
                "Varian": varian,
                "Warna": warna,
                "Harga Muda": harga_muda,
                "Harga Tua": harga_tua,
            }
        )

    # ============================================================
    # BUAT DATAFRAME
    # ============================================================

    df_hasil = pd.DataFrame(hasil)

    return df_hasil