import re

from utils.helper import bersihkan_text


def match_campur(row, df_campur):

    if df_campur is None or df_campur.empty:
        return df_campur

    nama = bersihkan_text(row["Nama Barang"])

    master_match = df_campur.copy()

    # =====================================================
    # TOREN POLOS
    # =====================================================

    if "POLOS TANGKI" in nama or "TOREN POLOS" in nama:

        master_match = master_match[
            master_match["Jenis"].apply(bersihkan_text)
            == "TOREN POLOS"
        ]

        # =========================
        # UKURAN
        # =========================

        m = re.search(
            r"POLOS\s*TANGKI\s*(\d+)",
            nama
        )

        if m:

            ukuran = m.group(1)

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    rf"POLOS\s*TANGKI\s*{ukuran}\b",
                    regex=True,
                    na=False
                )
            ]

        return master_match

    # =====================================================
    # FIBER PAGAR / TSUYULITE
    # =====================================================

    elif "TSUYULITE" in nama:

        master_match = master_match[
            master_match["Jenis"].apply(bersihkan_text)
            == "FIBER PAGAR"
        ]

        # =========================
        # TYPE
        # =========================

        if "POLOS" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    "TSUYULITE POLOS",
                    regex=False,
                    na=False
                )
            ]

        elif "GARIS" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    "TSUYULITE GARIS",
                    regex=False,
                    na=False
                )
            ]

        # =========================
        # UKURAN
        # =========================

        m = re.search(
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+)",
            nama
        )

        if m:

            ukuran = (
                f"{m.group(1).replace(',', '.')} X "
                f"{m.group(2).replace(',', '.')} X "
                f"{m.group(3)}"
            )

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    ukuran,
                    regex=False,
                    na=False
                )
            ]

        return master_match

    # =====================================================
    # PP FLAT SHEET
    # =====================================================

    elif "PP FLAT SHEET" in nama:

        master_match = master_match[
            master_match["Jenis"].apply(bersihkan_text)
            == "PP FLAT SHEET"
        ]

        # =========================
        # TYPE
        # =========================

        tipe = None

        if "DIAMOND BATIK" in nama:
            tipe = "BATIK"

        elif "GARIS" in nama:
            tipe = "GARIS"

        elif "POLOS" in nama:
            tipe = "POLOS"

        elif "BAMBU" in nama:
            tipe = "BAMBU"

        elif "DIMENSI" in nama:
            tipe = "DIMENSI"

        elif "BATIK" in nama:
            tipe = "BATIK"

        if tipe:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    tipe,
                    regex=False,
                    na=False
                )
            ]

        # =========================
        # UKURAN
        # =========================

        m = re.search(
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+(?:[.,]\d+)?)\s*X\s*"
            r"(\d+)",
            nama
        )

        if m:

            ukuran1 = m.group(1).replace(",", ".")
            ukuran2 = m.group(2).replace(",", ".")
            ukuran3 = m.group(3)

            ukuran1 = str(
                float(ukuran1)
            ).rstrip("0").rstrip(".")

            ukuran2 = str(
                float(ukuran2)
            ).rstrip("0").rstrip(".")

            ukuran = (
                f"{ukuran1} X "
                f"{ukuran2} X "
                f"{ukuran3}"
            )

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    ukuran,
                    regex=False,
                    na=False
                )
            ]

        # =========================
        # WARNA TIDAK DIPAKAI
        # =========================

        return master_match

    # =====================================================
    # BAK MANDI WALRUS
    # =====================================================

    elif "BAK MANDI" in nama:

        master_match = master_match[
            master_match["Jenis"].apply(bersihkan_text)
            == "BAK MANDI"
        ]

        # =========================
        # SUDUT
        # =========================

        if "SUDUT" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    "BAK MANDI WALRUS SUDUT",
                    regex=False,
                    na=False
                )
            ]

        # =========================
        # KOTAK
        # =========================

        elif "KOTAK" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains(
                    "BAK MANDI WALRUS KOTAK",
                    regex=False,
                    na=False
                )
            ]

        return master_match

    # =====================================================
    # DEFAULT
    # =====================================================

    master_match = master_match[
        master_match["Produk"]
        .apply(bersihkan_text)
        == nama
    ]

    return master_match