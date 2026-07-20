import pandas as pd

from utils.loaders.penguin import load_penguin
from utils.loaders.trilliun import load_trilliun
from utils.loaders.basic_putih import load_basic_putih
from utils.loaders.basic_abu import load_basic_abu
from utils.loaders.pipa_bestlon import load_pipa_bestlon
from utils.loaders.unnu import load_unnu
from utils.loaders.trilliunware import load_trilliunware
from utils.loaders.fitting_basic import load_fitting_basic
from utils.loaders.pureflo_fitting import load_pureflo_fitting

def load_master(file):

    excel = pd.ExcelFile(file)

    master = {}

    # =========================
    # PENGUIN TOREN
    # =========================
    if "PENGUIN TOREN" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="PENGUIN TOREN", header=None)

        master["penguin"] = load_penguin(df)

    # =========================
    # SELANG TRILLIUN
    # =========================
    if "SELANG TRILLIUN" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="SELANG TRILLIUN", header=None)

        master["trilliun"] = load_trilliun(df)

    # # =========================
    # # PIPA BASIC PUTIH
    # # =========================
    if "PIPA BASIC PUTIH" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="PIPA BASIC PUTIH", header=None)

        master["basic_putih"] = load_basic_putih(df)

    # # =========================
    # # PIPA BASIC ABU
    # # =========================
    if "PIPA BASIC ABU" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="PIPA BASIC ABU", header=None)

        master["basic_abu"] = load_basic_abu(df)

    # # =========================
    # # PIPA BESTLON
    # # =========================
    if "PIPA BESTLON" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="PIPA BESTLON", header=None)

        master["pipa_bestlon"] = load_pipa_bestlon(df)

    # # =========================
    # # UNNU
    # # =========================
    if "UNNU" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="UNNU", header=None)

        master["unnu"] = load_unnu(df)

    # # =========================
    # # TRILLIUNWARE
    # # =========================
    if "TRILLIUNWARE" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="TRILLIUNWARE", header=None)

        master["trilliunware"] = load_trilliunware(df)

    # # =========================
    # # FITTING BASIC
    # # =========================
    if "FITTING BASIC" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="FITTING BASIC", header=None)

        # master["fitting_basic"] = load_fitting_basic(df)
        master["fitting_basic"] = load_fitting_basic(df)

        print(master["fitting_basic"].to_string())

    # # =========================
    # # FITTING PUREFLO
    # # =========================
    if "FITTING PUREFLO" in excel.sheet_names:

        df = pd.read_excel(excel, sheet_name="FITTING PUREFLO", header=None)

        master["pureflo_fitting"] = load_pureflo_fitting(df)

        print(
            master["pureflo_fitting"][
                master["pureflo_fitting"]["Jenis"].str.contains("CAP", na=False)
            ].to_string()
        )

        print(master["pureflo_fitting"].to_string())

    return master
