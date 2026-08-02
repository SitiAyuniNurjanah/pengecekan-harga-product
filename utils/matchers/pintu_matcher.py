from utils.helper import bersihkan_text, warna_cocok


def match_pintu(row, df_pintu):

    produk = bersihkan_text(row["Nama Barang"])
    warna = bersihkan_text(row["Warna"])
    jenis = bersihkan_text(row["Jenis"])

    master_match = df_pintu.copy()

    # =====================================
    # RUVVO ALUMUNIUM
    # =====================================
    if "RUVVO" in produk and "ALUMUNIUM" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("RUVVO", na=False)
        ]

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("ALUMUNIUM", na=False)
        ]

        produk_master = (
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
        )


        if "WHITE" in produk:

            master_match = master_match[
                produk_master.str.contains("WHITE", na=False)
            ]


        elif any(x in produk for x in [
            "WALNUT",
            "SAPELI",
            "BAMBOO"
        ]):

            master_match = master_match[
                produk_master.str.contains("WALNUT", na=False)
            ]


        else:

            master_match = master_match[
                produk_master.str.contains("WHITE", na=False)
            ]


        return master_match
 
    # =====================================
    # RUVVO UPVC
    # =====================================

    if "RUVVO" in produk and "UPVC" in produk:

        if "KACA 8" in produk:

            master_match = master_match[
                master_match["Produk"]
                .fillna("")
                .apply(bersihkan_text)
                .str.contains("PINTU UPVC RUVVO KACA 8", na=False)
            ]

        else:

            master_match = master_match[
                master_match["Produk"]
                .fillna("")
                .apply(bersihkan_text)
                .str.contains("PINTU UPVC RUVVO FULL & 1/2 KACA", na=False)
            ]

        return master_match

    # =====================================
    # ALUMUNIUM FULL
    # =====================================

    if "PINTU ALUMUNIUM FULL" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("PINTU ALUMUNIUM FULL METRO", na=False)
        ]

        return master_match

    # =====================================
    # ALUMUNIUM KACA A
    # =====================================

    if "PINTU KACA ALUMUNIUM A" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("PINTU KACA ALUMUNIUM A", na=False)
        ]

        return master_match

    # =====================================
    # UPVC KACA 8 + HANDLE
    # =====================================

    if "UPVC" in produk and "KACA 8" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("PINTU UPVC KACA 8", na=False)
        ]

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("HANDLE", na=False)
        ]

        return master_match

    # =====================================
    # UPVC 1/2 KACA PUTIH
    # =====================================

    if "UPVC" in produk and "1/2 KACA" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("PINTU UPVC 1/2 KACA 8 PUTIH", na=False)
        ]

        return master_match

    # =====================================
    # UPVC MINIMALIS
    # =====================================

    if "UPVC" in produk and "MINIMALIS" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("MINIMALIS", na=False)
        ]

        return master_match

    # # =====================================
    # # UPVC FULL PANEL
    # # =====================================

    # if "UPVC" in produk and "FULL PANEL" in produk:

    #     master_match = master_match[
    #         master_match["Produk"]
    #         .fillna("")
    #         .apply(bersihkan_text)
    #         .str.contains("UPVC", na=False)
    #     ]

    #     master_match = master_match[
    #         master_match["Produk"]
    #         .fillna("")
    #         .apply(bersihkan_text)
    #         .str.contains("FULL", na=False)
    #     ]

    #     master_match = master_match[
    #         master_match["Produk"]
    #         .fillna("")
    #         .apply(bersihkan_text)
    #         .str.contains("KUNCI", na=False)
    #     ]

    #     return master_match

    # =====================================
    # UPVC FULL PANEL
    # =====================================

    if "UPVC" in produk and "FULL PANEL" in produk:


        # minimalis 1/4 dan 1/2
        if "MINIMALIS" in produk:

            master_match = master_match[
                master_match["Produk"]
                .fillna("")
                .apply(bersihkan_text)
                .str.contains("MINIMALIS", na=False)
            ]

            return master_match


        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("FULL", na=False)
        ]

        return master_match

    # =====================================
    # PINTU KACA ALUMUNIUM B
    # =====================================

    if "PINTU KACA ALUMUNIUM B" in produk:

        master_match = master_match[
            master_match["Produk"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains("PINTU KACA ALUMUNIUM B", na=False)
        ]

        return master_match

    # =====================================
    # NORMAL
    # =====================================

    jenis = bersihkan_text(row["Jenis"])

    if jenis:

        master_match = master_match[
            master_match["Jenis"]
            .fillna("")
            .apply(bersihkan_text)
            .str.contains(jenis, na=False)
        ]

    if not master_match.empty:

        master_match = master_match[
            master_match.apply(
                lambda x: warna_cocok(
                    warna, x.get("Produk", ""), x.get("Warna", ""), x.get("Jenis", "")
                ),
                axis=1,
            )
        ]

    return master_match
