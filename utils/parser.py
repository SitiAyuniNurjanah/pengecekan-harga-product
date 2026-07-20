from utils.parsers.penguin_parser import parse_penguin
from utils.parsers.trilliun_parser import parse_trilliun
from utils.parsers.basic_putih_parser import parse_basic_putih
from utils.parsers.basic_abu_parser import parse_basic_abu
from utils.parsers.pipa_bestlon_parser import parse_pipa_bestlon
from utils.parsers.unnu_parser import parse_unnu
from utils.parsers.trilliunware_parser import parse_trilliunware
from utils.parsers.fitting_basic_parser import parse_fitting_basic
from utils.parsers.pureflo_fitting_parser import pureflo_fitting_parser


def parse_product(product_name):

    text = str(product_name).upper()

    # =========================
    # TRILLIUNWARE
    # HARUS DI ATAS TRILLIUN
    # =========================

    if "TRILLIUNWARE" in text:
        return parse_trilliunware(text)

    # =========================
    # PENGUIN FILTER
    # =========================

    if "PENGUIN" in text and any(
        k in text
        for k in [
            "FILTER",
            "CARTRIDGE",
            "CARTDRIDGE",
            "HOUSING",
        ]
    ):
        return {
            "brand": "UNKNOWN",
            "jenis": "",
            "type": "",
            "kode": "",
            "ukuran": "",
            "warna": "",
        }

    # =========================
    # PENGUIN
    # =========================

    if "PENGUIN" in text or "PLUMBING" in text or "KIT" in text:
        return parse_penguin(text)
    elif "PENGUIN" in text or "OTO LEVEL (NL)" in text or "KIT" in text:
        return parse_penguin(text)

    # =========================
    # BASIC PUTIH
    # =========================

    if "TRILLIUN BASIC" in text and "PUTIH" in text:
        return parse_basic_putih(text)

    # =========================
    # BASIC ABU
    # =========================

    if "TRILLIUN BASIC" in text and "ABU" in text:
        return parse_basic_abu(text)

    # =========================
    # FITTING BASIC
    # =========================

    fitting_keyword = [
        "KNEE",
        "SOCKET",
        "TEE",
        "PLUG",
        "DOP",
        "VALVE SOCKET",
        "FAUCET SOCKET",
        "FAUCET KNEE",
        "FAUCET TEE",
        "WATER MUR",
        "LONG ELBOW",
    ]

    if "TRILLIUN" in text and "BASIC" in text:

        for keyword in fitting_keyword:
            if keyword in text:
                return parse_fitting_basic(text)

    # =========================
    # PUREFLO FITTING
    # =========================

    pureflo_keyword = [
        "FAUCET ELBOW WITH METAL",
        "FAUCET SOCKET WITH METAL",
        "FAUCET ELBOW",
        "FAUCET SOCKET",
        "FAUCET TEE",
        "VALVE SOCKET",
        "REDUCER SOCKET",
        "INCREASER SOCKET",
        "UNION THREAD",
        "Y-BRANCH",
        "ELBOW 45",
        "ELBOW",
        "SOCKET",
        "TEE",
        "PLUG",
        "CAP",
    ]

    if "PUREFLO" in text:

        for keyword in pureflo_keyword:
            if keyword in text:
                return pureflo_fitting_parser(text)

    # =========================
    # BESTLON
    # =========================

    if "BESTLON PIPA" in text and "PUTIH" in text:
        return parse_pipa_bestlon(text)

    # =========================
    # TRILLIUN SELANG
    # =========================

    if "TRILLIUN" in text or "SELANG" in text:
        return parse_trilliun(text)

    # =========================
    # UNNU
    # =========================

    if "UNNU" in text:
        return parse_unnu(text)

    return {
        "brand": "UNKNOWN",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }
