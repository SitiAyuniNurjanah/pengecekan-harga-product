import pandas as pd

from utils.helper import bersihkan_harga, bersihkan_text

from utils.matchers.penguin_matcher import match_penguin
from utils.matchers.pipa_bestlon_matcher import match_pipa_bestlon
from utils.matchers.unnu_matcher import match_unnu
from utils.matchers.trilliunware_matcher import match_trilliunware
from utils.matchers.pintu_matcher import match_pintu
from utils.matchers.pureflo_fitting_matcher import match_pureflo_fitting
from utils.matchers.fitting_basic_matcher import match_fitting_basic
from utils.matchers.basic_putih_matcher import match_basic_putih
from utils.matchers.basic_abu_matcher import match_basic_abu
from utils.matchers.selang_trilliun_matcher import match_trilliun
from utils.matchers.steel_matcher import match_steel


def match_product(df_order, master):

    hasil = df_order.copy()

    hasil["Harga Utama"] = None
    hasil["Status"] = ""

    for index, row in hasil.iterrows():

        harga_utama = None
        status = "TIDAK DITEMUKAN"

        brand = bersihkan_text(row.get("Brand", ""))

        # # =========================
        # # PENGUIN
        # # =========================
        # if brand == "PENGUIN":

        #     master_match, tipe = match_penguin(row, master.get("penguin"))

        #     # =========================
        #     # SET KIT TOREN
        #     # =========================
        #     if tipe == "SET_KIT":

        #         harga_utama = bersihkan_harga(row["@Harga"])
        #         status = "COCOK"

        #     # =========================
        #     # NORMAL PENGUIN
        #     # =========================
        #     elif not master_match.empty:

        #         harga_utama = bersihkan_harga(master_match.iloc[0]["Harga"])

        #         status = "COCOK"

        #     else:

        #         harga_utama = None
        #         status = "TIDAK DITEMUKAN"

        # =========================
        # PENGUIN
        # =========================
        if brand == "PENGUIN":

            master_match, tipe = match_penguin(row, master.get("penguin"))

            # =========================
            # SET KIT TOREN
            # =========================
            if tipe == "SET_KIT":

                harga_utama = None
                status = ""

            # =========================
            # NORMAL PENGUIN
            # =========================
            elif master_match is not None and not master_match.empty:

                harga_utama = bersihkan_harga(
                    master_match.iloc[0]["Harga"]
                )

                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

        # =========================
        # PIPA BESTLON
        # =========================
        elif brand == "BESTLON" and row["Jenis"] == "PIPA":

            master_match = match_pipa_bestlon(
                row,
                master.get("pipa_bestlon")
            )

            if not master_match.empty:

                harga_utama = master_match.iloc[0]["Harga"]
                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"
                
        # =========================
        # UNNU
        # =========================
        elif brand == "UNNU":

            master_match = match_unnu(row, master.get("unnu"))

            if not master_match.empty:

                harga_utama = bersihkan_harga(master_match.iloc[0]["Harga"])

                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

        # =========================
        # TRILLIUNWARE
        # =========================
        elif brand == "TRILLIUNWARE":

            master_match = match_trilliunware(row, master.get("trilliunware"))

            if not master_match.empty:

                nama_barang = bersihkan_text(row["Nama Barang"])

                if "MAROON" in nama_barang:
                    harga_utama = master_match.iloc[0]["Harga Tua"]

                else:
                    harga_utama = master_match.iloc[0]["Harga Muda"]

                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

        # =========================
        # PINTU
        # =========================
        elif brand == "PINTU":

            master_match = match_pintu(row, master.get("pintu"))

            if not master_match.empty:

                harga_utama = master_match.iloc[0]["Harga"]
                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

        # =========================
        # SELANG / TRILLIUN
        # =========================

        elif brand == "TRILLIUN":

            nama_barang = bersihkan_text(row["Nama Barang"])

            master_match = match_trilliun(
                row,
                master.get("trilliun")
            )

            if not master_match.empty:

                harga_utama = master_match.iloc[0]["Harga"]
                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

            # =========================
            # PUREFLO FITTING
            # =========================
            if "PUREFLO" in nama_barang:

                master_match = match_pureflo_fitting(row, master.get("pureflo_fitting"))

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

                master_match = match_fitting_basic(row, master.get("fitting_basic"))

            # =========================
            # BASIC PUTIH
            # =========================
            elif row["Jenis"] == "BASIC" and row["Warna"] == "PUTIH":

                master_match = match_basic_putih(row, master.get("basic_putih"))

            # =========================
            # BASIC ABU
            # =========================
            elif row["Jenis"] == "BASIC" and row["Warna"] == "ABU":

                master_match = match_basic_abu(row, master.get("basic_abu"))

            # =========================
            # SELANG TRILLIUN
            # =========================
            else:

                master_match = match_trilliun(row, master.get("trilliun"))

            if master_match is not None and not master_match.empty:

                harga_utama = master_match.iloc[0]["Harga"]
                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

        # =========================
        # STEEL
        # =========================
        elif brand == "STEEL":
            print("MASUK MATCH STEEL")
            print(row["Nama Barang"])

            master_match = match_steel(
                row,
                master.get("steel")
            )

            if not master_match.empty:

                harga_utama = master_match.iloc[0]["Harga"]
                status = "COCOK"

            else:

                harga_utama = None
                status = "TIDAK DITEMUKAN"

        # =========================
        # SIMPAN HASIL
        # =========================
        hasil.at[index, "Harga Utama"] = harga_utama

        harga_pelanggan = bersihkan_harga(row.get("@Harga"))
        harga_master = bersihkan_harga(harga_utama)

        # =========================
        # KHUSUS STATUS KOSONG
        # SET KIT TOREN
        # =========================
        if status == "":
            hasil.at[index, "Status"] = ""

        # =========================
        # MASTER TIDAK DITEMUKAN
        # =========================
        elif harga_master is None:
            hasil.at[index, "Status"] = status

        # =========================
        # HARGA SAMA
        # =========================
        elif harga_pelanggan == harga_master:
            hasil.at[index, "Status"] = "COCOK"

        # =========================
        # HARGA BERBEDA
        # =========================
        else:
            hasil.at[index, "Status"] = "TIDAK COCOK"

    # =========================
    # FORMAT HARGA TAMPILAN
    # =========================
    hasil["Harga Utama"] = pd.to_numeric(
        hasil["Harga Utama"],
        errors="coerce"
    )
    # hasil["Harga Utama"] = (
    #     pd.to_numeric(hasil["Harga Utama"], errors="coerce").fillna(0).astype(int)
    # )

    return hasil
