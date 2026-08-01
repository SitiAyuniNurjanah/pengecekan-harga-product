import pandas as pd

# from utils.helper import bersihkan_harga
from utils.helper import bersihkan_text, bersihkan_harga, normalisasi_pintu, warna_cocok


def bersihkan_text(text):
    """
    Membersihkan text supaya format master dan pelanggan sama
    """
    return (
        str(text)
        .upper()
        .replace('"', "")
        .replace("”", "")
        .replace("″", "")
        .replace("“", "")
        .strip()
    )


def match_product(df_order, master):

    # =========================
    # Ambil master masing-masing brand
    # =========================
    df_penguin = master.get(
        "penguin", pd.DataFrame(columns=["Brand", "Type", "Ukuran", "Warna", "Harga"])
    )
    df_trilliun = master.get("trilliun", pd.DataFrame())
    df_basic_putih = master.get("basic_putih", pd.DataFrame())
    df_basic_abu = master.get("basic_abu", pd.DataFrame())
    df_pipa_bestlon = master.get("pipa_bestlon", pd.DataFrame())
    df_unnu = master.get("unnu", pd.DataFrame())
    df_trilliunware = master.get("trilliunware", pd.DataFrame())
    df_fitting_basic = master.get("fitting_basic", pd.DataFrame())
    df_pureflo_fitting = master.get(
        "pureflo_fitting",
        pd.DataFrame(columns=["Brand", "Jenis", "Type", "Ukuran", "Harga"]),
    )
    df_pintu = master.get(
        "pintu",
        pd.DataFrame(
            columns=[
                "Brand",
                "Jenis",
                "Type",
                "Kode",
                "Ukuran",
                "Warna",
                "Produk",
                "Harga",
            ]
        ),
    )

    hasil = df_order.copy()

    hasil["Harga Utama"] = None
    hasil["Status"] = ""

    for index, row in hasil.iterrows():

        master_match = pd.DataFrame()

        # =========================
        # PRODUK PENGUIN
        # =========================
        if row["Brand"] == "PENGUIN":

            if row["Jenis"] == "SET KIT TOREN":

                hasil.at[index, "Harga Utama"] = bersihkan_harga(row["@Harga"])
                hasil.at[index, "Status"] = "COCOK"
                continue

            master_match = df_penguin[
                (
                    df_penguin["Type"].apply(bersihkan_text)
                    == bersihkan_text(row["Type"])
                )
                & (
                    df_penguin["Ukuran"].apply(bersihkan_text)
                    == bersihkan_text(row["Ukuran"])
                )
                & (
                    df_penguin["Warna"].apply(bersihkan_text)
                    == bersihkan_text(row["Warna"])
                )
            ]

        # =========================
        # PIPA BESTLON
        # =========================
        elif row["Jenis"] == "PIPA" and row["Warna"] == "PUTIH":

            master_match = df_pipa_bestlon[
                (
                    df_pipa_bestlon["Type"].apply(bersihkan_text)
                    == bersihkan_text(row["Type"])
                )
                & (
                    df_pipa_bestlon["Ukuran"].apply(bersihkan_text)
                    == bersihkan_text(row["Ukuran"])
                )
            ]

        # =========================
        # PRODUK UNNU
        # =========================
        elif row["Brand"] == "UNNU":

            # =========================
            # Mulai cari berdasarkan Type
            # =========================
            master_match = df_unnu[
                df_unnu["Type"].apply(bersihkan_text) == bersihkan_text(row["Type"])
            ]

            # =========================
            # Jika master punya ukuran dan order punya ukuran
            # maka cocokkan ukuran
            # =========================
            if str(row["Ukuran"]).strip() != "":

                master_match = master_match[
                    master_match["Ukuran"].apply(bersihkan_text)
                    == bersihkan_text(row["Ukuran"])
                ]

            # =========================
            # Jika produk punya warna
            # maka cocokkan warna
            # =========================
            if str(row["Warna"]).strip() != "":

                master_match = master_match[
                    master_match["Warna"].apply(bersihkan_text)
                    == bersihkan_text(row["Warna"])
                ]

        # =========================
        # TRILLIUNWARE
        # =========================
        elif row["Brand"] == "TRILLIUNWARE":

            nama = bersihkan_text(row["Nama Barang"])

            master_match = df_trilliunware.copy()
            harga_master = None

            # ===================================
            # FILTER TYPE
            # ===================================

            type_row = bersihkan_text(row["Type"])

            if type_row:
                master_match = master_match[
                    master_match["Type"].apply(bersihkan_text) == type_row
                ]

            # ===================================
            # FILTER JENIS
            # ===================================

            jenis_row = bersihkan_text(row["Jenis"])

            if jenis_row:
                master_match = master_match[
                    master_match["Jenis"].apply(bersihkan_text) == jenis_row
                ]

            # # ===================================
            # # KHUSUS EUREKA
            # # ===================================

            # if "EUREKA" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("EUREKA", na=False)
            #     ]

            # # ===================================
            # # KHUSUS MALACHITE
            # # ===================================

            # if "MALACHITE" in nama:

            #     if "LILAC" in nama:

            #         master_match = master_match[
            #             master_match["Produk"]
            #             .apply(bersihkan_text)
            #             .str.contains("MALACHITE - LILAC", na=False, regex=False)
            #         ]

            #     elif "GARNET" in nama:

            #         master_match = master_match[
            #             master_match["Produk"]
            #             .apply(bersihkan_text)
            #             .str.contains("MALACHITE - GARNET", na=False, regex=False)
            #         ]

            # # ===================================
            # # BODY / SET
            # # ===================================

            # if "BODY ONLY" in nama:

            #     # White / Ivory
            #     if "BLACK" not in nama and "GREY" not in nama:

            #         master_match = master_match[
            #             master_match["Produk"]
            #             .apply(bersihkan_text)
            #             .str.contains("BODY ONLY", na=False, regex=False)
            #         ]

            # elif "SET" in nama:

            #     if "TANPA KRAN" in nama:

            #         master_match = master_match[
            #             master_match["Produk"]
            #             .apply(bersihkan_text)
            #             .str.contains("SET (TANPA KRAN)", na=False, regex=False)
            #         ]

            #     elif "BLACK" in nama or "GREY" in nama:

            #         master_match = master_match[
            #             master_match["Produk"]
            #             .apply(bersihkan_text)
            #             .str.contains("SET DGN KRAN", na=False, regex=False)
            #         ]
            #     # ===================================
            #     # TANKTRIM
            #     # ===================================

            #     if "TANKTRIM" in nama:

            #         master_match = master_match[
            #             master_match["Produk"]
            #             .apply(bersihkan_text)
            #             .str.contains("TANKTRIM", na=False, regex=False)
            #         ]

            # # ===================================
            # # KAKI ONLY
            # # ===================================

            # if "KAKI ONLY" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("KAKI ONLY", na=False, regex=False)
            #     ]

            # # ===================================
            # # SINGLE FLUSH
            # # ===================================

            # if "SINGLE FLUSH" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("SINGLE FLUSH", na=False, regex=False)
            #     ]

            # # ===================================
            # # INSERT / VESSEL
            # # ===================================

            # if "INSERT" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("INSERT", na=False, regex=False)
            #     ]

            # elif "VESSEL" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("VESSEL", na=False, regex=False)
            #     ]

            # # ===================================
            # # WARNA
            # # ===================================

            # if "BLACK" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("BLACK", na=False, regex=False)
            #     ]

            # elif "GREY" in nama:

            #     master_match = master_match[
            #         master_match["Produk"]
            #         .apply(bersihkan_text)
            #         .str.contains("GREY", na=False, regex=False)
            #     ]

            # # elif "MAROON" in nama:

            # #     master_match = master_match[
            # #         master_match["Produk"]
            # #         .apply(bersihkan_text)
            # #         .str.contains("MAROON", na=False, regex=False)
            # #     ]

            # # ===================================
            # # AMBIL HARGA
            # # ===================================

            # if not master_match.empty:

            #     # master_row = master_match.iloc[0]

            #     # warna = bersihkan_text(row["Warna"])

            #     # if warna == "MAROON":
            #     #     harga_master = master_row["Harga Tua"]
            #     # else:
            #     #     harga_master = master_row["Harga Muda"]
            #     master_row = master_match.iloc[0]

            #     warna = bersihkan_text(row["Warna"])

            #     if warna == "MAROON" and pd.notna(master_row["Harga Tua"]):
            #         harga_master = master_row["Harga Tua"]
            #     else:
            #         harga_master = master_row["Harga Muda"]
            #     hasil.at[index, "Harga Utama"] = harga_master

        # ==================================================
            # KHUSUS CLOSET JONGKOK
            # ==================================================

            if "CLOSET JONGKOK" in nama:

                if "CAPRI" in nama:

                    if "MAROON" in nama:

                        master_match = master_match[
                            master_match["Produk"]
                            .apply(bersihkan_text)
                            .str.contains("ARABIAN / EMERALD / CAPRI", na=False)
                        ]

                    else:

                        master_match = master_match[
                            master_match["Produk"]
                            .apply(bersihkan_text)
                            .str.contains("CJ CAPRI", na=False)
                        ]

                elif "EMERALD" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("ARABIAN / EMERALD / CAPRI", na=False)
                    ]

            # ==================================================
            # AMETHYST
            # ==================================================

            elif "AMETHYST" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("AMETHYST", na=False)
                ]

            # ==================================================
            # JASPER
            # ==================================================

            elif "JASPER" in nama:

                if "TANKTRIM" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("JASPER (SET)", na=False)
                    ]

                elif "GREY" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("JASPER - GREY", na=False)
                    ]

            # ==================================================
            # OPAL
            # ==================================================

            elif "OPAL" in nama:

                if "BLACK" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("OPAL (SET) - BLACK", na=False)
                    ]

                elif "TANKTRIM" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("OPAL (SET) - TANKTRIM", na=False)
                    ]

            # ==================================================
            # RUBY
            # ==================================================

            elif "RUBY" in nama:

                if "BLACK" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("RUBY (SET) - BLACK", na=False)
                    ]

                elif "TANKTRIM" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("RUBY (SET) - TANKTRIM", na=False)
                    ]

            # ==================================================
            # EUREKA
            # ==================================================

            elif "EUREKA" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("EUREKA", na=False)
                ]

            # ==================================================
            # MALACHITE
            # ==================================================

            elif "MALACHITE" in nama:

                if "LILAC" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MALACHITE - LILAC", na=False)
                    ]

                elif "GARNET" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MALACHITE - GARNET", na=False)
                    ]

            # ==================================================
            # BODY ONLY
            # ==================================================

            elif "BODY ONLY" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("BODY ONLY", na=False)
                ]

            # ==================================================
            # KAKI ONLY
            # ==================================================

            elif "KAKI ONLY" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("KAKI ONLY", na=False)
                ]

            # ==================================================
            # TANPA KRAN
            # ==================================================

            elif "TANPA KRAN" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("SET (TANPA KRAN)", na=False)
                ]

            # ==================================================
            # SINGLE FLUSH
            # ==================================================

            elif "SINGLE FLUSH" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("SINGLE FLUSH", na=False)
                ]

            # ==================================================
            # INSERT
            # ==================================================

            elif "INSERT" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("INSERT", na=False)
                ]

            # ==================================================
            # VESSEL
            # ==================================================

            elif "VESSEL" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("VESSEL", na=False)
                ]

            # ==================================================
            # HARGA
            # ==================================================

            if not master_match.empty:

                master_row = master_match.iloc[0]

                if (
                    bersihkan_text(row["Warna"]) == "MAROON"
                    and pd.notna(master_row["Harga Tua"])
                ):
                    harga_master = master_row["Harga Tua"]
                else:
                    harga_master = master_row["Harga Muda"]

                hasil.at[index, "Harga Utama"] = harga_master
        # =========================
        # PINTU
        # =========================
        elif row["Brand"] == "PINTU":

            master_match = df_pintu.copy()

            # print("\n==============================")
            # print(row["Nama Barang"])
            # print(df_pintu[["Produk", "Jenis", "Type", "Warna", "Harga"]])


            jenis_input = bersihkan_text(row["Jenis"])
            warna_input = bersihkan_text(row["Warna"])

            produk = bersihkan_text(row["Nama Barang"])

            print("PRODUK BERSIH :", produk)
            skip_warna = False

            # =====================================
            # KHUSUS RUVVO UPVC FULL PANEL BASIC
            # ambil harga ALUMUNIUM PANEL
            # =====================================

            if (
                "RUVVO" in produk
                and "UPVC" in produk
                and "FULL" in produk
                and "PANEL" in produk
                and "BASIC" in produk
            ):

                master_match = df_pintu[
                    df_pintu["Produk"]
                    .fillna("")
                    .str.contains("RUVVO", case=False, na=False)
                ]

                master_match = master_match[
                    master_match["Produk"]
                    .fillna("")
                    .str.contains("ALUMUNIUM", case=False, na=False)
                ]


                if "WALNUT" in produk:

                    master_match = master_match[
                        master_match["Produk"]
                        .str.contains("WALNUT", case=False, na=False)
                    ]

                else:

                    master_match = master_match[
                        master_match["Produk"]
                        .str.contains("WHITE", case=False, na=False)
                    ]


            else:

                # FILTER JENIS NORMAL
                if jenis_input:

                    master_match = master_match[
                        master_match["Jenis"]
                        .fillna("")
                        .apply(bersihkan_text)
                        .str.contains(jenis_input, na=False)
                    ]

            # =====================================
            # RUVVO ALUMUNIUM
            # =====================================

            if "RUVVO" in produk and "ALUMUNIUM" in produk:

                skip_warna = True

                master_match = df_pintu[
                    df_pintu["Produk"]
                    .fillna("")
                    .str.contains("RUVVO Pintu Alumunium", case=False, na=False)
                ]

                # Warna gelap = Walnut
                if any(x in produk for x in ["WALNUT", "SAPELI", "BAMBOO"]):
                    master_match = master_match[
                        master_match["Produk"]
                        .str.contains("WALNUT", case=False, na=False)
                    ]

                # Semua selain itu = White
                else:

                    master_match = master_match[
                        master_match["Produk"]
                        .str.contains("WHITE", case=False, na=False)
                    ]

            # =====================================
            # RUVVO UPVC
            # =====================================

            elif "RUVVO" in produk and "UPVC" in produk:

                master_match = df_pintu[
                    df_pintu["Produk"]
                    .fillna("")
                    .str.contains("Pintu UPVC RUVVO", case=False, na=False)
                ]
            # =====================
            # FILTER TYPE
            # =====================

            type_input = bersihkan_text(row["Type"])

            # filter type hanya untuk selain RUVVO
            if not ("RUVVO" in produk):

                if type_input:

                    master_match = master_match[
                        master_match["Type"]
                        .fillna("")
                        .apply(bersihkan_text)
                        .str.contains(type_input, na=False)
                    ]

            # =====================
            # CEK HASIL JENIS
            # =====================

            if master_match.empty:

                row["Harga Utama"] = None
                row["Status"] = "TIDAK DITEMUKAN"

            else:

                # =====================
                # FILTER WARNA
                # =====================

                if not skip_warna:

                    master_match = master_match[
                        master_match.apply(
                            lambda x: warna_cocok(
                                warna_input,
                                x.get("Produk", ""),
                                x.get("Warna", ""),
                                x.get("Jenis", ""),
                            ),
                            axis=1,
                        )
                    ]

                # =====================
                # HASIL AKHIR
                # =====================

                if not master_match.empty:

                    row["Harga Utama"] = master_match.iloc[0]["Harga"]

                else:

                    row["Harga Utama"] = None
                    row["Status"] = "TIDAK DITEMUKAN"

        # =========================
        # PRODUK TRILLIUN
        # =========================
        elif row["Brand"] == "TRILLIUN":

            nama_barang = bersihkan_text(row["Nama Barang"])

            # =========================
            # PUREFLO FITTING
            # PRIORITAS PALING ATAS
            # =========================
            if "PUREFLO" in nama_barang:

                master_match = df_pureflo_fitting[
                    (
                        df_pureflo_fitting["Jenis"].apply(bersihkan_text)
                        == bersihkan_text(row["Jenis"])
                    )
                    & (
                        df_pureflo_fitting["Type"].apply(bersihkan_text)
                        == bersihkan_text(row["Type"])
                    )
                    & (
                        df_pureflo_fitting["Ukuran"].apply(bersihkan_text)
                        == bersihkan_text(row["Ukuran"])
                    )
                ]

            # =========================
            # FITTING BASIC
            # =========================
            elif row["Jenis"] in [
                "KNEE",
                "SOCKET",
                "TEE",
                "PLUG",
                "DOP",
                "FAUCET KNEE",
                "FAUCET SOCKET",
                "FAUCET TEE",
                "VALVE SOCKET",
                "WATERMUR",
                "LONG ELBOW",
            ]:

                master_match = df_fitting_basic[
                    (
                        df_fitting_basic["Jenis"].apply(bersihkan_text)
                        == bersihkan_text(row["Jenis"])
                    )
                    & (
                        df_fitting_basic["Type"].apply(bersihkan_text)
                        == bersihkan_text(row["Type"])
                    )
                    & (
                        df_fitting_basic["Ukuran"].apply(bersihkan_text)
                        == bersihkan_text(row["Ukuran"])
                    )
                ]

            # =========================
            # PIPA BASIC PUTIH
            # =========================
            elif row["Jenis"] == "BASIC" and row["Warna"] == "PUTIH":

                master_match = df_basic_putih[
                    (
                        df_basic_putih["Type"].apply(bersihkan_text)
                        == bersihkan_text(row["Type"])
                    )
                    & (
                        df_basic_putih["Ukuran"].apply(bersihkan_text)
                        == bersihkan_text(row["Ukuran"])
                    )
                ]

            # =========================
            # PIPA BASIC ABU
            # =========================
            elif row["Jenis"] == "BASIC" and row["Warna"] == "ABU":

                master_match = df_basic_abu[
                    (
                        df_basic_abu["Type"].apply(bersihkan_text)
                        == bersihkan_text(row["Type"])
                    )
                    & (
                        df_basic_abu["Ukuran"].apply(bersihkan_text)
                        == bersihkan_text(row["Ukuran"])
                    )
                ]

            # =========================
            # SELANG TRILLIUN
            # =========================
            else:

                master_match = df_trilliun[
                    (
                        df_trilliun["Jenis"].apply(bersihkan_text)
                        == bersihkan_text(row["Jenis"])
                    )
                    & (
                        df_trilliun["Type"].apply(bersihkan_text)
                        == bersihkan_text(row["Type"])
                    )
                    & (
                        df_trilliun["Ukuran"].apply(bersihkan_text)
                        == bersihkan_text(row["Ukuran"])
                    )
                ]
        # =========================
        # CEK HASIL MATCHING
        # =========================
        if not master_match.empty:

            try:

                harga_pelanggan = bersihkan_harga(row["@Harga"])

                # ==================================
                # AMBIL HARGA MASTER
                # ==================================

                if row["Brand"] == "TRILLIUNWARE":

                    nama_barang = bersihkan_text(row["Nama Barang"])

                    if "MAROON" in nama_barang:
                        harga_master_asli = master_match.iloc[0]["Harga Tua"]
                    else:
                        harga_master_asli = master_match.iloc[0]["Harga Muda"]

                else:

                    # brand lain tetap pakai kolom Harga
                    harga_master_asli = master_match.iloc[0]["Harga"]

                harga_master = bersihkan_harga(harga_master_asli)

                hasil.at[index, "Harga Utama"] = harga_master

                hasil.at[index, "Harga Utama"] = harga_master

                if harga_pelanggan == harga_master:

                    hasil.at[index, "Status"] = "COCOK"

                else:

                    hasil.at[index, "Status"] = "TIDAK COCOK"

            except Exception as e:

                hasil.at[index, "Status"] = "FORMAT HARGA SALAH"

        else:

            hasil.at[index, "Status"] = "TIDAK DITEMUKAN"

    return hasil
