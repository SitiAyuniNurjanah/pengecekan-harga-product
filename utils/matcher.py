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
    # df_pintu = master.get("pintu", pd.DataFrame())
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

            # ===================================
            # KHUSUS EUREKA
            # ===================================

            if "EUREKA" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("EUREKA", na=False)
                ]

            # ===================================
            # KHUSUS MALACHITE
            # ===================================

            if "MALACHITE" in nama:

                if "LILAC" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MALACHITE - LILAC", na=False, regex=False)
                    ]

                elif "GARNET" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MALACHITE - GARNET", na=False, regex=False)
                    ]

            # ===================================
            # BODY / SET
            # ===================================

            if "BODY" in nama:

                # White / Ivory
                if "BLACK" not in nama and "GREY" not in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("BODY ONLY", na=False, regex=False)
                    ]

            elif "SET" in nama:

                if "TANPA KRAN" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("SET (TANPA KRAN)", na=False, regex=False)
                    ]

                elif "BLACK" in nama or "GREY" in nama:

                    master_match = master_match[
                        master_match["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("SET DGN KRAN", na=False, regex=False)
                    ]

            # ===================================
            # KAKI ONLY
            # ===================================

            if "KAKI ONLY" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("KAKI ONLY", na=False, regex=False)
                ]

            # ===================================
            # SINGLE FLUSH
            # ===================================

            if "SINGLE FLUSH" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("SINGLE FLUSH", na=False, regex=False)
                ]

            # ===================================
            # INSERT / VESSEL
            # ===================================

            if "INSERT" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("INSERT", na=False, regex=False)
                ]

            elif "VESSEL" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("VESSEL", na=False, regex=False)
                ]

            # ===================================
            # WARNA
            # ===================================

            if "BLACK" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("BLACK", na=False, regex=False)
                ]

            elif "GREY" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("GREY", na=False, regex=False)
                ]

            elif "MAROON" in nama:

                master_match = master_match[
                    master_match["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("MAROON", na=False, regex=False)
                ]

            # ===================================
            # DEBUG
            # ===================================

            # print("=" * 80)
            # print(nama)

            # if not master_match.empty:
            #     print(
            #         master_match[
            #             ["Produk", "Jenis", "Type", "Warna", "Harga Muda"]
            #         ].to_string()
            #     )
            # else:
            #     print("MASTER TIDAK DITEMUKAN")

            # ===================================
            # AMBIL HARGA
            # ===================================

            if not master_match.empty:

                master_row = master_match.iloc[0]

                warna = bersihkan_text(row["Warna"])

                if warna == "MAROON":
                    harga_master = master_row["Harga Tua"]
                else:
                    harga_master = master_row["Harga Muda"]

                hasil.at[index, "Harga Utama"] = harga_master
        # =========================
        # PINTU
        # =========================
        elif row["Brand"] == "PINTU":

            master_match = df_pintu.copy()

            jenis_input = bersihkan_text(row["Jenis"])
            warna_input = bersihkan_text(row["Warna"])

            # =====================
            # FILTER JENIS
            # =====================

            if jenis_input:

                master_match = master_match[
                    master_match["Jenis"]
                    .fillna("")
                    .apply(bersihkan_text)
                    .str.contains(jenis_input, na=False)
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

                master_match = master_match[
                    master_match.apply(
                        lambda x: warna_cocok(
                            warna_input, x.get("Produk", ""), x.get("Warna", ""), x.get("Jenis", "")
                        ),
                        axis=1,
                    )
                ]

                # =====================
                # HASIL AKHIR
                # =====================

                # if not master_match.empty:

                #     row["Harga Utama"] = master_match.iloc[0]["Harga"]
                #     row["Status"] = "COCOK"
                if not master_match.empty:

                    row["Harga Utama"] = master_match.iloc[0]["Harga"]

                else:

                    row["Harga Utama"] = None
                    row["Status"] = "TIDAK DITEMUKAN"

        # # =================
        # # PINTU
        # # =================
        # elif row["Brand"] == "PINTU":

        #     master_match = df_pintu.copy()
        # # Normalisasi nama input:
        # # ALUMUNIUM -> ALUMINIUM, SAPELLI -> SAPELI
        # nama = normalisasi_pintu(nama)

        # # Helper supaya kolom Produk selalu dinormalisasi sebelum dicocokkan
        # def filter_produk(kata):
        #     return master_match[
        #         master_match["Produk"]
        #         .apply(normalisasi_pintu)
        #         .str.contains(kata, na=False)
        #     ]

        # # =====================
        # # PVC POLOS
        # # =====================

        # if "PVC POLOS" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("PVC POLOS", na=False)
        #     ]

        #     if "URAT KAYU" in nama:
        #         master_match = master_match[
        #             master_match["Produk"]
        #             .apply(bersihkan_text)
        #             .str.contains("URAT KAYU", na=False)
        #         ]

        # # =====================
        # # PVC OVAL
        # # =====================

        # elif "PVC OVAL" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("PVC OVAL", na=False)
        #     ]

        # # =====================
        # # MINIMALIS
        # # =====================

        # elif "MINIMALIS" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("MINIMALIS", na=False)
        #     ]

        # # =====================
        # # PANEL BINGKAI
        # # =====================

        # elif "PANEL BINGKAI" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("PANEL BINGKAI", na=False)
        #     ]

        # # =====================
        # # PANEL SPARTA
        # # =====================

        # elif "SPARTA" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("SPARTA", na=False)
        #     ]

        # # =====================
        # # PANEL ORION
        # # =====================

        # elif "ORION" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("ORION", na=False)
        #     ]

        # # =====================
        # # KACA PERSEGI
        # # =====================

        # elif "KACA PERSEGI" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("KACA PERSEGI", na=False)
        #     ]

        # # =====================
        # # RUVVO ALUMUNIUM
        # # =====================

        # # elif "RUVVO" in nama and "ALUMUNIUM" in nama:
        # elif "RUVVO" in nama and "ALUMINIUM" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("RUVVO", na=False)
        #         & master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("ALUMUNIUM", na=False)
        #     ]

        # # =====================
        # # RUVVO UPVC
        # # =====================

        # elif "RUVVO" in nama and "UPVC" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("RUVVO", na=False)
        #         & master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("UPVC", na=False)
        #     ]

        # # =====================
        # # METRO ALUMUNIUM
        # # =====================

        # # elif "METRO" in nama and "ALUMUNIUM" in nama:
        # elif "METRO" in nama and "ALUMINIUM" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("METRO", na=False)
        #         & master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("ALUMUNIUM", na=False)
        #     ]

        # # =====================
        # # METRO UPVC
        # # =====================

        # elif "METRO" in nama and "UPVC" in nama:

        #     master_match = master_match[
        #         master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("METRO", na=False)
        #         & master_match["Produk"]
        #         .apply(bersihkan_text)
        #         .str.contains("UPVC", na=False)
        #     ]

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

                # print(
                #     "CEK HARGA:",
                #     row["@Harga"],
                #     "=>",
                #     harga_pelanggan,
                #     "| MASTER:",
                #     harga_master_asli,
                #     "=>",
                #     harga_master,
                # )

                if harga_pelanggan == harga_master:

                    hasil.at[index, "Status"] = "COCOK"

                else:

                    hasil.at[index, "Status"] = "TIDAK COCOK"

            except Exception as e:

                hasil.at[index, "Status"] = "FORMAT HARGA SALAH"

                # print("ERROR MATCH:", e)

        else:

            hasil.at[index, "Status"] = "TIDAK DITEMUKAN"

    return hasil
