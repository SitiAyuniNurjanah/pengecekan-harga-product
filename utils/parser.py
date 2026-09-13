from utils.parsers.penguin_parser import parse_penguin
from utils.parsers.selang_trilliun_parser import parse_trilliun
from utils.parsers.basic_putih_parser import parse_basic_putih
from utils.parsers.basic_abu_parser import parse_basic_abu
from utils.parsers.pipa_bestlon_parser import parse_pipa_bestlon
from utils.parsers.unnu_parser import parse_unnu
from utils.parsers.trilliunware_parser import parse_trilliunware
from utils.parsers.fitting_basic_parser import parse_fitting_basic
from utils.parsers.pureflo_fitting_parser import pureflo_fitting_parser
from utils.parsers.pintu_parser import pintu_parser
from utils.parsers.steel_parser import parse_steel
from utils.parsers.campur_parser import parse_campur
from utils.parsers.accsware_parser import parse_accsware


def parse_product(product_name):

    text = str(product_name).upper().strip()

    # =====================================================
    # 1. TRILLIUNWARE
    # =====================================================
    # WAJIB PALING ATAS.
    #
    # Kalau nama barang secara eksplisit mengandung
    # "TRILLIUNWARE", maka HARUS masuk TRILLIUNWARE.
    #
    # Jangan biarkan keyword seperti:
    # - BASIN TAP
    # - SOAP DISH
    # - FLUSH VALVE
    # - dll
    #
    # mengambil alih sebagai ACCSWARE.
    # =====================================================

    if "TRILLIUNWARE" in text:
        return parse_trilliunware(text)

    # =====================================================
    # 2. ACCSWARE
    # =====================================================
    #
    # ACCSWARE dikenali berdasarkan keyword produknya.
    #
    # Karena TRILLIUNWARE sudah dicek di atas, produk
    # TRILLIUNWARE yang kebetulan memiliki keyword yang
    # sama tidak akan salah masuk ACCSWARE.
    # =====================================================

    accsware_keyword = [
        "VESSEL BASIN",
        "ANGLE VALVE",
        "BOWL GASKET",
        "FLUSH VALVE",
        "SELF CLOSING BASIN TAP",
        "BASIN TAP",
        "JET WASHER",
        "FLEXIBLE HOSE",
        "P-TRAP",
        "KRAN TEMBOK",
        "TANKTRIM",
        "POP UP",
        "KRAN CABANG",
        "FLOOR DRAIN",
        "PAN CONNECTOR",
        "SIPHON",
        "AKSESORIS SEAT",
        "SEAT COVER",
        "SOAP DISH",
        "SENSOR BASIN TAP",
    ]

    for keyword in accsware_keyword:
        if keyword in text:
            return parse_accsware(text)

    # =====================================================
    # 3. PENGUIN FILTER
    # =====================================================
    #
    # Filter / cartridge / housing PENGUIN tidak diproses
    # sebagai produk PENGUIN biasa.
    # =====================================================

    if "PENGUIN" in text and any(
        keyword in text
        for keyword in [
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

    # =====================================================
    # 4. PENGUIN
    # =====================================================

    if (
        "PENGUIN" in text
        or "PLUMBING" in text
        or "KIT" in text
    ):
        return parse_penguin(text)

    # =====================================================
    # 5. BASIC PUTIH
    # =====================================================

    if "TRILLIUN BASIC" in text and "PUTIH" in text:
        return parse_basic_putih(text)

    # =====================================================
    # 6. BASIC ABU
    # =====================================================

    if "TRILLIUN BASIC" in text and "ABU" in text:
        return parse_basic_abu(text)

    # =====================================================
    # 7. FITTING BASIC
    # =====================================================

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

    # =====================================================
    # 8. PUREFLO FITTING
    # =====================================================

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

    # =====================================================
    # 9. PINTU
    # =====================================================

    pintu_keyword = [
        "PINTU PVC",
        "PINTU PANEL",
        "PINTU MINIMALIS",
        "PINTU OVAL",
        "PINTU KACA",
        "RUVVO",
        "METRO",
        "UPVC",
        "ALUMUNIUM",
    ]

    for keyword in pintu_keyword:

        if keyword in text:
            return pintu_parser(text)

    # =====================================================
    # 10. STEEL
    # =====================================================

    steel_keyword = [
        "BONDEK",
        "CANAL",
        "CANNAL",
        "GALVALUM",
        "HOLLOW",
        "KASSO",
        "SENG GELOMBANG",
        "GENTENG METAL",
        "SPANDEK",
        "TRIMDEK",
        "SUTERA TRIMDEK",
    ]

    for keyword in steel_keyword:

        if keyword in text:
            return parse_steel(text)

    # =====================================================
    # 11. CAMPUR
    # =====================================================

    campur_keyword = [
        "POLOS TANGKI",
        "TSUYULITE",
        "PP FLAT SHEET",
        "PP SHEET MOTIF",
        "BAK MANDI WALRUS",
        "TRILLIUN GLUE",
    ]

    for keyword in campur_keyword:

        if keyword in text:
            return parse_campur(text)

    # =====================================================
    # 12. BESTLON
    # =====================================================

    if "BESTLON PIPA" in text and "PUTIH" in text:
        return parse_pipa_bestlon(text)

    # =====================================================
    # 13. TRILLIUN SELANG
    # =====================================================

    if "TRILLIUN" in text or "SELANG" in text:
        return parse_trilliun(text)

    # =====================================================
    # 14. UNNU
    # =====================================================

    if "UNNU" in text:
        return parse_unnu(text)

    # =====================================================
    # 15. UNKNOWN
    # =====================================================

    return {
        "brand": "UNKNOWN",
        "jenis": "",
        "type": "",
        "kode": "",
        "ukuran": "",
        "warna": "",
    }
