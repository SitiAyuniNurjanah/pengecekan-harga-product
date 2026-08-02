# import pandas as pd
# from utils.helper import bersihkan_text


# def match_trilliunware(row, df_trilliunware):

#     if df_trilliunware is None or df_trilliunware.empty:
#         return pd.DataFrame()

#     nama = bersihkan_text(row["Nama Barang"])

#     master_match = df_trilliunware.copy()

#     # ==================================================
#     # URINAL
#     # ==================================================

#     if "VISCARIA" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("URINAL VISCARIA", na=False)
#         ]

#         if "BODY" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("BODY ONLY", na=False)
#             ]

#         elif "SET" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("SET", na=False)
#             ]

#         return master_match
#     # ==================================================
#     # VELVET
#     # ==================================================

#     if "VELVET" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("URINAL VELVET", na=False)
#         ]

#         if "SET" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("SET", na=False)
#             ]

#         elif "BODY" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("BODY ONLY", na=False)
#             ]

#         return master_match

#     # ==================================================
#     # CLOSET JONGKOK CAPRI MAROON
#     # ==================================================

#     if "CAPRI" in nama and "MAROON" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("ARABIAN", na=False)
#         ]

#         return master_match

#     # ==================================================
#     # RUBY
#     # ==================================================

#     if "RUBY" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("CD RUBY", na=False)
#         ]

#         if "TANKTRIM" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("TANKTRIM", na=False)
#             ]

#         else:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("BLACK", na=False)
#             ]

#         return master_match

#     # ==================================================
#     # SAPPHIRA
#     # ==================================================

#     if "SAPPHIRA" in nama:

#         produk = master_match["Produk"].apply(bersihkan_text)

#         # Smart Washer
#         if "SMART WASHER" in nama:

#             master_match = master_match[produk.str.contains("SMART WASHER", na=False)]

#         # Black
#         elif "BLACK" in nama:

#             master_match = master_match[
#                 produk.str.contains("SAPPHIRA", na=False)
#                 & produk.str.contains("BLACK", na=False)
#             ]

#         # White / Light Blue / warna lainnya
#         else:

#             master_match = master_match[
#                 produk.str.contains("SAPPHIRA", na=False)
#                 & produk.str.contains("TANKTRIM", na=False)
#             ]

#         return master_match

#         # ==================================================
#     # CLOSET JONGKOK CAPRI
#     # ==================================================

#     if "CLOSET JONGKOK" in nama and "CAPRI" in nama:

#         produk = master_match["Produk"].apply(bersihkan_text)

#         # 206000
#         if any(warna in nama for warna in ["S BLUE", "GREY", "BLACK"]):

#             master_match = master_match[produk.str.contains("CJ CAPRI", na=False)]

#         # 193000
#         elif "MAROON" in nama:

#             master_match = master_match[produk.str.contains("ARABIAN", na=False)]

#         # 149000
#         else:

#             master_match = master_match[produk.str.contains("ARABIAN", na=False)]

#         return master_match

#     # ==================================================
#     # CLOSET DUDUK OPAL
#     # ==================================================

#     if "OPAL" in nama:

#         produk = master_match["Produk"].apply(bersihkan_text)


#         # ============================
#         # OPAL BLACK
#         # CD Opal (SET) - BLACK
#         # 1498000
#         # ============================
#         if "BLACK" in nama:

#             master_match = master_match[
#                 produk.str.contains(
#                     "CD OPAL",
#                     na=False
#                 )
#                 &
#                 produk.str.contains(
#                     "BLACK",
#                     na=False
#                 )
#             ]


#         # ============================
#         # OPAL NON BLACK
#         # CD Opal (SET) - Tanktrim 01
#         # 1208000
#         # ============================
#         else:

#             master_match = master_match[
#                 produk.str.contains(
#                     "CD OPAL",
#                     na=False
#                 )
#                 &
#                 produk.str.contains(
#                     "TANKTRIM",
#                     na=False
#                 )
#             ]


#         return master_match


#     # ==================================================
#     # CLOSET DUDUK JASPER
#     # ==================================================

#     if "JASPER" in nama:

#         produk = master_match["Produk"].apply(bersihkan_text)


#         # ============================
#         # JASPER SMART WASHER
#         # 1560000
#         # ============================
#         if "SMART WASHER" in nama:

#             master_match = master_match[
#                 produk.str.contains(
#                     "JASPER SMART WASHER",
#                     na=False
#                 )
#             ]


#         # ============================
#         # JASPER GREY
#         # 1327000
#         # ============================
#         elif "GREY" in nama:

#             master_match = master_match[
#                 produk.str.contains(
#                     "JASPER",
#                     na=False
#                 )
#                 &
#                 produk.str.contains(
#                     "GREY",
#                     na=False
#                 )
#             ]


#         # ============================
#         # JASPER SET TANKTRIM
#         # 985000
#         # ============================
#         else:

#             master_match = master_match[
#                 produk.str.contains(
#                     "JASPER",
#                     na=False
#                 )
#                 &
#                 produk.str.contains(
#                     "TANKTRIM",
#                     na=False
#                 )
#             ]


#         return master_match

#     # ==================================================
#     # CLOSET DUDUK MARION
#     # ==================================================

#     if "MARION" in nama:

#         produk = master_match["Produk"].apply(bersihkan_text)


#         # ============================
#         # MARION SINGLE FLUSH
#         # 933000
#         # ============================
#         if "SINGLE FLUSH" in nama:

#             master_match = master_match[
#                 produk.str.contains(
#                     "CD MARION",
#                     na=False
#                 )
#                 &
#                 produk.str.contains(
#                     "SINGLE FLUSH",
#                     na=False
#                 )
#             ]


#         # ============================
#         # MARION TANKTRIM
#         # 1046000
#         # ============================
#         else:

#             master_match = master_match[
#                 produk.str.contains(
#                     "CD MARION",
#                     na=False
#                 )
#                 &
#                 produk.str.contains(
#                     "TANKTRIM",
#                     na=False
#                 )
#             ]


#         return master_match

#     # ===================================
#     # FILTER TYPE
#     # ===================================

#     type_row = bersihkan_text(row["Type"])

#     if type_row:
#         master_match = master_match[
#             master_match["Type"].apply(bersihkan_text) == type_row
#         ]

#     # ===================================
#     # FILTER JENIS
#     # ===================================

#     jenis_row = bersihkan_text(row["Jenis"])

#     if jenis_row:
#         master_match = master_match[
#             master_match["Jenis"].apply(bersihkan_text) == jenis_row
#         ]


#     # ==================================================
#     # JASPER E-FLUSH
#     # ==================================================

#     if "JASPER" in nama and "E" in nama and "FLUSH" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("JASPER E - FLUSH", na=False, regex=False)
#         ]

#         return master_match

#     # ==================================================
#     # WASTAFEL GARNET TANPA KRAN
#     # ==================================================

#     if "GARNET" in nama and "TANPA KRAN" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("WALL HUNG GARNET", na=False)
#         ]

#         master_match = master_match[
#             master_match["Produk"].apply(bersihkan_text).str.contains("SET", na=False)
#         ]

#         return master_match

#     # ==================================================
#     # WASTAFEL LILAC TANPA KRAN
#     # ==================================================

#     if "LILAC" in nama and "TANPA KRAN" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("WALL HUNG LILAC", na=False)
#         ]

#         master_match = master_match[
#             master_match["Produk"].apply(bersihkan_text).str.contains("SET", na=False)
#         ]

#         return master_match

#     # ==================================================
#     # GARNET BLACK BODY
#     # ==================================================

#     if "GARNET" in nama and "BLACK" in nama and "BODY" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("WALL HUNG GARNET", na=False)
#         ]

#         master_match = master_match[
#             master_match["Produk"].apply(bersihkan_text).str.contains("BLACK", na=False)
#         ]

#         return master_match

#     # ==================================================
#     # KHUSUS CLOSET JONGKOK
#     # ==================================================
#     if "CLOSET JONGKOK" in nama:

#         if "CARRIBEAN" in nama:

#             if "WHITE" in nama:

#                 master_match = master_match[
#                     master_match["Produk"]
#                     .apply(bersihkan_text)
#                     .str.contains("WHITE & BLUE", na=False)
#                 ]

#             elif "LIGHT BLUE" in nama or "BLUE" in nama:

#                 master_match = master_match[
#                     master_match["Produk"]
#                     .apply(bersihkan_text)
#                     .str.contains("S. BLUE", na=False)
#                 ]

#             return master_match

#     elif "AMETHYST" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("AMETHYST", na=False)
#         ]

#     elif "JASPER" in nama:

#         if "TANKTRIM" in nama:

#             master_match = master_match[
#                 master_match["Produk"].apply(bersihkan_text)
#                 # .str.contains("JASPER (SET)", na=False)
#                 .str.contains("JASPER", na=False, regex=False)
#             ]

#         elif "GREY" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("JASPER - GREY", na=False)
#             ]

#     elif "EUREKA" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("EUREKA", na=False)
#         ]

#     elif "MALACHITE" in nama:

#         if "LILAC" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("MALACHITE - LILAC", na=False)
#             ]

#         elif "GARNET" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("MALACHITE - GARNET", na=False)
#             ]
#     # ==================================================
#     # CITRINE BODY
#     # ==================================================

#     if "CITRINE" in nama and "BODY" in nama:

#         produk = master_match["Produk"].apply(bersihkan_text)

#         # Black
#         if "BLACK" in nama:

#             master_match = master_match[
#                 produk.str.contains("CITRINE", na=False)
#                 & produk.str.contains("BLACK", na=False)
#             ]

#         # selain black (white / warna lain)
#         else:

#             master_match = master_match[
#                 produk.str.contains("CITRINE", na=False)
#                 & ~produk.str.contains("BLACK", na=False)
#                 & produk.str.contains("BODY ONLY", na=False)
#             ]

#         return master_match

#     elif "BODY ONLY" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("BODY ONLY", na=False)
#         ]

#     elif "KAKI ONLY" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("KAKI ONLY", na=False)
#         ]

#     elif "TANPA KRAN" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("SET (TANPA KRAN)", na=False)
#         ]

#     elif "SINGLE FLUSH" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("SINGLE FLUSH", na=False)
#         ]

#     elif "INSERT" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("INSERT", na=False)
#         ]

#     elif "VESSEL" in nama:

#         master_match = master_match[
#             master_match["Produk"]
#             .apply(bersihkan_text)
#             .str.contains("VESSEL", na=False)
#         ]

#     elif "CARRIBEAN" in nama:

#         if "WHITE" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("WHITE & BLUE", na=False)
#             ]

#         elif "BLUE" in nama or "LIGHT BLUE" in nama:

#             master_match = master_match[
#                 master_match["Produk"]
#                 .apply(bersihkan_text)
#                 .str.contains("S. BLUE", na=False)
#             ]

#     return master_match

import pandas as pd
from utils.helper import bersihkan_text


def filter_produk(df, keyword):
    return df[
        df["Produk"]
        .apply(bersihkan_text)
        .str.contains(keyword, na=False, regex=False)
    ]


def match_trilliunware(row, df_trilliunware):

    if df_trilliunware is None or df_trilliunware.empty:
        return pd.DataFrame()

    nama = bersihkan_text(row["Nama Barang"])

    master_match = df_trilliunware.copy()

    produk = master_match["Produk"].apply(bersihkan_text)


    # ==================================================
    # URINAL VISCARIA
    # ==================================================

    if "VISCARIA" in nama:

        master_match = master_match[
            produk.str.contains("URINAL VISCARIA", na=False)
        ]

        if "BODY" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains("BODY ONLY", na=False)
            ]

        elif "SET" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains("SET", na=False)
            ]

        return master_match


    # ==================================================
    # URINAL VELVET
    # ==================================================

    if "VELVET" in nama:

        master_match = master_match[
            produk.str.contains("URINAL VELVET", na=False)
        ]

        if "BODY" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains("BODY ONLY", na=False)
            ]

        elif "SET" in nama:

            master_match = master_match[
                master_match["Produk"]
                .apply(bersihkan_text)
                .str.contains("SET", na=False)
            ]

        return master_match


    # ==================================================
    # RUBY
    # ==================================================

    if "RUBY" in nama:

        produk = master_match["Produk"].apply(bersihkan_text)


        # ==================================
        # RUBY BLACK
        # CD Ruby (SET) - Black
        # 1293000
        # ==================================

        if "BLACK" in nama:

            master_match = master_match[
                produk.str.contains(
                    "CD RUBY",
                    na=False
                )
                &
                produk.str.contains(
                    "BLACK",
                    na=False
                )
            ]


        # ==================================
        # RUBY MAROON
        # CD Ruby (SET) - Tanktrim 01
        # 1241000
        # ==================================

        elif "MAROON" in nama:

            master_match = master_match[
                produk.str.contains(
                    "CD RUBY",
                    na=False
                )
                &
                produk.str.contains(
                    "TANKTRIM",
                    na=False
                )
            ]


        # ==================================
        # RUBY WARNA LAIN
        # Brilliant White
        # Ivory
        # Light Blue
        #
        # CD Ruby (SET) - Tanktrim 01
        # 1062000
        # ==================================

        else:

            master_match = master_match[
                produk.str.contains(
                    "CD RUBY",
                    na=False
                )
                &
                produk.str.contains(
                    "TANKTRIM",
                    na=False
                )
            ]


        return master_match

    # ==================================================
    # SAPPHIRA
    # ==================================================

    if "SAPPHIRA" in nama:

        if "SMART WASHER" in nama:

            master_match = master_match[
                produk.str.contains("SMART WASHER", na=False)
            ]

        elif "BLACK" in nama:

            master_match = master_match[
                produk.str.contains("SAPPHIRA", na=False)
                &
                produk.str.contains("BLACK", na=False)
            ]

        else:

            master_match = master_match[
                produk.str.contains("SAPPHIRA", na=False)
                &
                produk.str.contains("TANKTRIM", na=False)
            ]

        return master_match


    # ==================================================
    # CLOSET JONGKOK CAPRI
    # ==================================================

    if "CLOSET JONGKOK" in nama and "CAPRI" in nama:


        # ------------------------------
        # CAPRI WARNA KHUSUS 206000
        # ------------------------------

        if any(
            warna in nama
            for warna in [
                "S BLUE",
                "GREY",
                "BLACK"
            ]
        ):

            master_match = master_match[
                produk.str.contains(
                    "CJ CAPRI",
                    na=False
                )
            ]


        # ------------------------------
        # CAPRI MAROON 193000
        # ------------------------------

        elif "MAROON" in nama:

            master_match = master_match[
                produk.str.contains(
                    "ARABIAN",
                    na=False
                )
            ]


        # ------------------------------
        # CAPRI WARNA NORMAL 149000
        # ------------------------------

        else:

            master_match = master_match[
                produk.str.contains(
                    "ARABIAN / EMERALD / CAPRI",
                    na=False
                )
            ]

        return master_match


    # ==================================================
    # CLOSET DUDUK OPAL
    # ==================================================

    if "OPAL" in nama:


        if "BLACK" in nama:

            master_match = master_match[
                produk.str.contains("CD OPAL", na=False)
                &
                produk.str.contains("BLACK", na=False)
            ]


        else:

            master_match = master_match[
                produk.str.contains("CD OPAL", na=False)
                &
                produk.str.contains("TANKTRIM", na=False)
            ]


        return master_match


    # ==================================================
    # CLOSET DUDUK JASPER
    # ==================================================

    if "JASPER" in nama:


        # PRIORITAS 1 SMART WASHER

        if "SMART WASHER" in nama:

            master_match = master_match[
                produk.str.contains(
                    "JASPER SMART WASHER",
                    na=False
                )
            ]


        # PRIORITAS 2 GREY

        elif "GREY" in nama:

            master_match = master_match[
                produk.str.contains(
                    "CD JASPER",
                    na=False
                )
                &
                produk.str.contains(
                    "GREY",
                    na=False
                )
            ]


        # PRIORITAS 3 NORMAL

        else:

            master_match = master_match[
                produk.str.contains(
                    "CD JASPER",
                    na=False
                )
                &
                produk.str.contains(
                    "TANKTRIM",
                    na=False
                )
            ]

        return master_match

    # ==================================================
    # CLOSET DUDUK MARION
    # ==================================================

    if "MARION" in nama:

        # PRIORITAS SINGLE FLUSH

        if "SINGLE FLUSH" in nama:

            master_match = master_match[
                produk.str.contains(
                    "CD MARION",
                    na=False
                )
                &
                produk.str.contains(
                    "SINGLE FLUSH",
                    na=False
                )
            ]


        # NORMAL TANKTRIM

        else:

            master_match = master_match[
                produk.str.contains(
                    "CD MARION",
                    na=False
                )
                &
                produk.str.contains(
                    "TANKTRIM",
                    na=False
                )
            ]

        return master_match

    # ==================================================
    # JASPER E-FLUSH
    # ==================================================

    if "JASPER" in nama and "E" in nama and "FLUSH" in nama:

        master_match = master_match[
            produk.str.contains(
                "JASPER E - FLUSH",
                na=False
            )
        ]

        return master_match

    # ==================================================
    # WASTAFEL GARNET TANPA KRAN
    # ==================================================

    if "GARNET" in nama and "TANPA KRAN" in nama:

        master_match = master_match[
            produk.str.contains(
                "WALL HUNG GARNET",
                na=False
            )
        ]

        master_match = master_match[
            master_match["Produk"]
            .apply(bersihkan_text)
            .str.contains(
                "SET",
                na=False
            )
        ]

        return master_match

    # ==================================================
    # WASTAFEL LILAC TANPA KRAN
    # ==================================================

    if "LILAC" in nama and "TANPA KRAN" in nama:

        master_match = master_match[
            produk.str.contains(
                "WALL HUNG LILAC",
                na=False
            )
        ]

        master_match = master_match[
            master_match["Produk"]
            .apply(bersihkan_text)
            .str.contains(
                "SET",
                na=False
            )
        ]

        return master_match

    # ==================================================
    # GARNET BLACK BODY
    # ==================================================

    if "GARNET" in nama and "BLACK" in nama and "BODY" in nama:

        master_match = master_match[
            produk.str.contains(
                "WALL HUNG GARNET",
                na=False
            )
            &
            produk.str.contains(
                "BLACK",
                na=False
            )
        ]

        return master_match

    # ==================================================
    # CITRINE BODY
    # ==================================================

    if "CITRINE" in nama and "BODY" in nama:


        if "BLACK" in nama:

            master_match = master_match[
                produk.str.contains(
                    "CITRINE",
                    na=False
                )
                &
                produk.str.contains(
                    "BLACK",
                    na=False
                )
            ]


        else:

            master_match = master_match[
                produk.str.contains(
                    "CITRINE",
                    na=False
                )
                &
                produk.str.contains(
                    "BODY ONLY",
                    na=False
                )
                &
                ~produk.str.contains(
                    "BLACK",
                    na=False
                )
            ]

        return master_match

    # ==================================================
    # AMETHYST
    # ==================================================

    if "AMETHYST" in nama:

        master_match = master_match[
            produk.str.contains(
                "AMETHYST",
                na=False
            )
        ]

        return master_match

    # ==================================================
    # MALACHITE
    # ==================================================

    if "MALACHITE" in nama:


        if "LILAC" in nama:

            master_match = master_match[
                produk.str.contains(
                    "MALACHITE - LILAC",
                    na=False
                )
            ]


        elif "GARNET" in nama:

            master_match = master_match[
                produk.str.contains(
                    "MALACHITE - GARNET",
                    na=False
                )
            ]

        return master_match

    # ==================================================
    # BODY ONLY
    # ==================================================

    if "BODY ONLY" in nama:

        master_match = master_match[
            produk.str.contains(
                "BODY ONLY",
                na=False
            )
        ]

        return master_match



    # ==================================================
    # KAKI ONLY
    # ==================================================

    if "KAKI ONLY" in nama:

        master_match = master_match[
            produk.str.contains(
                "KAKI ONLY",
                na=False
            )
        ]

        return master_match



    # ==================================================
    # TANPA KRAN
    # ==================================================

    if "TANPA KRAN" in nama:

        master_match = master_match[
            produk.str.contains(
                "SET (TANPA KRAN)",
                na=False
            )
        ]

        return master_match



    # ==================================================
    # SINGLE FLUSH
    # ==================================================

    if "SINGLE FLUSH" in nama:

        master_match = master_match[
            produk.str.contains(
                "SINGLE FLUSH",
                na=False
            )
        ]

        return master_match



    # ==================================================
    # INSERT
    # ==================================================

    if "INSERT" in nama:

        master_match = master_match[
            produk.str.contains(
                "INSERT",
                na=False
            )
        ]

        return master_match



    # ==================================================
    # VESSEL
    # ==================================================

    if "VESSEL" in nama:

        master_match = master_match[
            produk.str.contains(
                "VESSEL",
                na=False
            )
        ]

        return master_match



    # ==================================================
    # CARRIBEAN
    # ==================================================

    if "CARRIBEAN" in nama:

        produk = master_match["Produk"].apply(bersihkan_text)


        # ==================================
        # WHITE & BLUE
        # Light Blue masuk sini
        # 188000
        # ==================================

        if "LIGHT BLUE" in nama or "WHITE" in nama:

            master_match = master_match[
                produk.str.contains(
                    "WHITE & BLUE",
                    na=False
                )
            ]


        # ==================================
        # S. BLUE / GREY / BLACK / MAROON
        # 261000
        # ==================================

        elif any(
            warna in nama
            for warna in [
                "S BLUE",
                "GREY",
                "BLACK",
                "MAROON"
            ]
        ):

            master_match = master_match[
                produk.str.contains(
                    "S BLUE",
                    na=False
                )
                |
                produk.str.contains(
                    "GREY",
                    na=False
                )
                |
                produk.str.contains(
                    "BLACK",
                    na=False
                )
                |
                produk.str.contains(
                    "MAROON",
                    na=False
                )
            ]

        return master_match

    # ==================================================
    # FILTER TYPE
    # ==================================================

    type_row = bersihkan_text(row["Type"])

    if type_row:

        master_match = master_match[
            master_match["Type"]
            .apply(bersihkan_text)
            ==
            type_row
        ]



    # ==================================================
    # FILTER JENIS
    # ==================================================

    jenis_row = bersihkan_text(row["Jenis"])

    if jenis_row:

        master_match = master_match[
            master_match["Jenis"]
            .apply(bersihkan_text)
            ==
            jenis_row
        ]



    return master_match