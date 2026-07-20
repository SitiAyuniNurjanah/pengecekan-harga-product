import pandas as pd

from utils.helper import bersihkan_harga


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
    # df_pureflo_fitting = master.get("pureflo_fitting", pd.DataFrame())
    df_pureflo_fitting = master.get(
        "pureflo_fitting",
        pd.DataFrame(columns=["Brand", "Jenis", "Type", "Ukuran", "Harga"]),
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

        # # =========================
        # # PRODUK UNNU
        # # =========================
        # elif row["Brand"] == "UNNU":

        #     if str(row["Ukuran"]).strip() != "":

        #         master_match = df_unnu[
        #             (
        #                 df_unnu["Type"].apply(bersihkan_text)
        #                 == bersihkan_text(row["Type"])
        #             )
        #             & (
        #                 df_unnu["Ukuran"].apply(bersihkan_text)
        #                 == bersihkan_text(row["Ukuran"])
        #             )
        #         ]

        #     else:

        #         master_match = df_unnu[
        #             df_unnu["Type"].apply(bersihkan_text) == bersihkan_text(row["Type"])
        #         ]

        #         # Kalau produk tidak punya warna (misal PVC Valve)
        #         if len(master_match) == 0:

        #             master_match = df_unnu[
        #                 (
        #                     df_unnu["Type"].apply(bersihkan_text)
        #                     == bersihkan_text(row["Type"])
        #                 )

        #                 & (
        #                     df_unnu["Ukuran"].apply(bersihkan_text)
        #                     == bersihkan_text(row["Ukuran"])
        #                 )
        #             ]

        #         else:

        #             master_match = df_unnu[
        #                 df_unnu["Type"].apply(bersihkan_text)
        #                 == bersihkan_text(row["Type"])
        #             ]

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

            # default supaya tidak error
            master_match = pd.DataFrame()
            harga_master = None

            # =========================
            # EUREKA
            # =========================

            if "EUREKA" in nama:

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("CD SIRAM EUREKA", na=False)
                ]

            # =========================
            # MALACHITE
            # =========================

            elif "MALACHITE" in nama:

                if "LILAC" in nama:

                    master_match = df_trilliunware[
                        df_trilliunware["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MALACHITE - LILAC", na=False)
                    ]

                elif "GARNET" in nama:

                    master_match = df_trilliunware[
                        df_trilliunware["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MALACHITE - GARNET", na=False)
                    ]

            # =========================
            # KROOZ
            # =========================

            elif "KROOZ" in nama:

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("KROOZ", na=False)
                ]

            # =========================
            # GARNET
            # =========================

            elif "GARNET" in nama:

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("GARNET", na=False)
                ]

            # =========================
            # COBALT
            # =========================

            elif "COBALT" in nama:

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("COBALT", na=False)
                ]

            # =========================
            # LILAC
            # =========================

            elif "LILAC" in nama:

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("LILAC", na=False)
                ]

            # =========================
            # MARION
            # =========================

            elif "MARION" in nama:

                if "SINGLE FLUSH" in nama:

                    master_match = df_trilliunware[
                        df_trilliunware["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MARION", na=False)
                        & df_trilliunware["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("SINGLE FLUSH", na=False)
                    ]

                else:

                    master_match = df_trilliunware[
                        df_trilliunware["Produk"]
                        .apply(bersihkan_text)
                        .str.contains("MARION", na=False)
                    ]

            # =========================
            # SAPPHIRA
            # =========================

            elif "SAPPHIRA" in nama:

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains("SAPPHIRA", na=False)
                ]

            # =========================
            # EMERALD / CAPRI / CARRIBEAN
            # =========================

            elif "EMERALD" in nama or "CAPRI" in nama or "CARRIBEAN" in nama:

                keyword = ""

                if "EMERALD" in nama:
                    keyword = "EMERALD"

                elif "CAPRI" in nama:
                    keyword = "CAPRI"

                elif "CARRIBEAN" in nama:
                    keyword = "CARRIBEAN"

                master_match = df_trilliunware[
                    df_trilliunware["Produk"]
                    .apply(bersihkan_text)
                    .str.contains(keyword, na=False)
                ]

            # =========================
            # AMBIL HARGA BERDASARKAN WARNA
            # =========================

            if len(master_match) > 0:

                master_row = master_match.iloc[0]

                warna = bersihkan_text(row["Warna"])

                warna_muda = ["WHITE", "BRILLIANT WHITE", "IVORY", "LIGHT BLUE", "PINK"]

                if warna in warna_muda:

                    harga_master = master_row["Harga Muda"]

                else:

                    harga_master = master_row["Harga Tua"]
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

                print("\n=== CEK PUREFLO ORDER ===")
                print(row["Jenis"], row["Type"], row["Ukuran"])

                print("\n=== ISI MASTER PUREFLO ===")
                print(
                    df_pureflo_fitting[
                        df_pureflo_fitting["Jenis"]
                        .apply(bersihkan_text)
                        .str.contains("VALVE|FAUCET|REDUCER|CAP", na=False)
                    ].to_string()
                )
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

                print(
                    "CEK HARGA:",
                    row["@Harga"],
                    "=>",
                    harga_pelanggan,
                    "| MASTER:",
                    harga_master_asli,
                    "=>",
                    harga_master,
                )

                if harga_pelanggan == harga_master:

                    hasil.at[index, "Status"] = "COCOK"

                else:

                    hasil.at[index, "Status"] = "TIDAK COCOK"

            except Exception as e:

                hasil.at[index, "Status"] = "FORMAT HARGA SALAH"

                print("ERROR MATCH:", e)

        else:

            hasil.at[index, "Status"] = "TIDAK DITEMUKAN"

    return hasil
