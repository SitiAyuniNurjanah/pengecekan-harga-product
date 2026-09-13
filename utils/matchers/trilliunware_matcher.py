import pandas as pd

from utils.helper import bersihkan_text


# ============================================================
# HELPER
# ============================================================

def _clean(value):
    if pd.isna(value):
        return ""
    return bersihkan_text(value)


def _produk_series(df):
    if df is None or df.empty or "Produk" not in df.columns:
        return pd.Series(dtype=str)

    return df["Produk"].fillna("").apply(bersihkan_text)


def _contains(series, keyword):
    if series is None:
        return pd.Series(dtype=bool)

    return series.str.contains(
        keyword,
        na=False,
        regex=False
    )


def _has_any(text, keywords):
    return any(keyword in text for keyword in keywords)


def _match_produk(master, produk, *keywords):
    """
    Semua keyword harus ditemukan di kolom Produk.
    Tidak bergantung pada prefix CD/CJ.
    """
    if master is None or master.empty:
        return pd.DataFrame()

    mask = pd.Series(True, index=master.index)

    for keyword in keywords:
        mask &= _contains(produk, keyword)

    return master[mask]


def _match_model(master, produk, model):
    """
    Cari berdasarkan nama model saja.
    Contoh:
    - CD SAPPHIRA
    - SAPPHIRA
    - SAPPHIRA CLOSE COUPLED

    Semuanya tetap bisa ditemukan selama mengandung SAPPHIRA.
    """
    if master is None or master.empty:
        return pd.DataFrame()

    return master[
        _contains(produk, model)
    ]


def _filter_variant(df, *keywords):
    if df is None or df.empty:
        return pd.DataFrame()

    produk = _produk_series(df)

    mask = pd.Series(True, index=df.index)

    for keyword in keywords:
        mask &= _contains(produk, keyword)

    return df[mask]


def _exclude_variant(df, *keywords):
    if df is None or df.empty:
        return pd.DataFrame()

    produk = _produk_series(df)

    mask = pd.Series(True, index=df.index)

    for keyword in keywords:
        mask &= ~_contains(produk, keyword)

    return df[mask]


def _first_not_empty(*matches):
    for match in matches:
        if match is not None and not match.empty:
            return match

    return pd.DataFrame()


# ============================================================
# MAIN MATCHER
# ============================================================

def match_trilliunware(row, df_trilliunware):

    if df_trilliunware is None or df_trilliunware.empty:
        return pd.DataFrame()

    nama = _clean(row.get("Nama Barang", ""))
    jenis = _clean(row.get("Jenis", ""))
    type_row = _clean(row.get("Type", ""))
    warna = _clean(row.get("Warna", ""))

    if not nama:
        return pd.DataFrame()

    master = df_trilliunware.copy()

    produk = _produk_series(master)

    if produk.empty:
        return pd.DataFrame()


    # ========================================================
    # 1. URINAL VISCARIA
    # ========================================================

    if "VISCARIA" in nama:

        match = _match_produk(
            master,
            produk,
            "VISCARIA"
        )

        if "BODY" in nama:
            body = _filter_variant(
                match,
                "BODY ONLY"
            )

            if not body.empty:
                return body

        if "SET" in nama:
            set_match = _filter_variant(
                match,
                "SET"
            )

            if not set_match.empty:
                return set_match

        return match


    # ========================================================
    # 2. URINAL VELVET
    # ========================================================

    if "VELVET" in nama:

        match = _match_produk(
            master,
            produk,
            "VELVET"
        )

        if "BODY" in nama:
            body = _filter_variant(
                match,
                "BODY ONLY"
            )

            if not body.empty:
                return body

        if "SET" in nama:
            set_match = _filter_variant(
                match,
                "SET"
            )

            if not set_match.empty:
                return set_match

        return match


    # ========================================================
    # 3. URINAL PARTISI
    # ========================================================

    if "URINAL" in nama and "PARTISI" in nama:

        return _match_produk(
            master,
            produk,
            "URINAL",
            "PARTISI"
        )


    # ========================================================
    # 4. SOAP DISH
    # ========================================================

    if "SOAP DISH" in nama:

        return _match_produk(
            master,
            produk,
            "SOAP DISH"
        )


    # ========================================================
    # 5. BASIN TAP / KROOZ
    # ========================================================

    if "BASIN TAP" in nama:

        match = _match_produk(
            master,
            produk,
            "BASIN TAP"
        )

        krooz = _filter_variant(
            match,
            "KROOZ"
        )

        if not krooz.empty:
            return krooz

        return match


    # ========================================================
    # 6. MALACHITE
    # ========================================================

    if "MALACHITE" in nama:

        match = _match_model(
            master,
            produk,
            "MALACHITE"
        )

        if "GARNET" in nama:

            garnet = _filter_variant(
                match,
                "GARNET"
            )

            if not garnet.empty:
                return garnet

        if "LILAC" in nama:

            lilac = _filter_variant(
                match,
                "LILAC"
            )

            if "KAKI ONLY" in nama:

                kaki = _filter_variant(
                    lilac,
                    "KAKI ONLY"
                )

                if not kaki.empty:
                    return kaki

            if "TANPA KRAN" in nama:

                tanpa_kran = _filter_variant(
                    lilac,
                    "SET",
                    "TANPA KRAN"
                )

                if not tanpa_kran.empty:
                    return tanpa_kran

            if not lilac.empty:
                return lilac

        return match


    # ========================================================
    # 7. WASTAFEL GARNET
    # ========================================================

    if "GARNET" in nama and "WALL HUNG" in nama:

        match = _match_produk(
            master,
            produk,
            "GARNET",
            "WALL HUNG"
        )

        if "TANPA KRAN" in nama:

            tanpa_kran = _filter_variant(
                match,
                "SET"
            )

            tanpa_kran = _exclude_variant(
                tanpa_kran,
                "BLACK",
                "GREY"
            )

            if not tanpa_kran.empty:
                return tanpa_kran

        if "BLACK" in nama:

            black = _filter_variant(
                match,
                "BLACK"
            )

            if "SET" in nama or "KRAN" in nama:

                set_black = _filter_variant(
                    black,
                    "SET"
                )

                if not set_black.empty:
                    return set_black

            return black

        if "GREY" in nama:

            grey = _filter_variant(
                match,
                "GREY"
            )

            if "SET" in nama or "KRAN" in nama:

                set_grey = _filter_variant(
                    grey,
                    "SET"
                )

                if not set_grey.empty:
                    return set_grey

            return grey

        return match


    # ========================================================
    # 8. WASTAFEL LILAC
    # ========================================================

    if "LILAC" in nama and "WALL HUNG" in nama:

        match = _match_produk(
            master,
            produk,
            "LILAC",
            "WALL HUNG"
        )

        if "TANPA KRAN" in nama:

            set_match = _filter_variant(
                match,
                "SET"
            )

            if not set_match.empty:
                return set_match

        return match


    # ========================================================
    # 9. WASTAFEL CITRINE
    # ========================================================

    if "CITRINE" in nama and "WALL HUNG" in nama:

        match = _match_produk(
            master,
            produk,
            "CITRINE",
            "WALL HUNG"
        )

        if "BLACK" in nama:

            black = _filter_variant(
                match,
                "BLACK"
            )

            if not black.empty:
                return black

        body = _filter_variant(
            match,
            "BODY ONLY"
        )

        body = _exclude_variant(
            body,
            "BLACK"
        )

        if not body.empty:
            return body

        return match


    # ========================================================
    # 10. WASTAFEL COBALT
    # ========================================================

    if "COBALT" in nama and "WALL HUNG" in nama:

        return _match_produk(
            master,
            produk,
            "COBALT",
            "WALL HUNG",
            "BODY ONLY"
        )


    # ========================================================
    # 11. WASTAFEL PERIDOT
    # ========================================================

    if "PERIDOT" in nama and "WALL HUNG" in nama:

        return _match_produk(
            master,
            produk,
            "PERIDOT",
            "WALL HUNG",
            "BODY ONLY"
        )


    # ========================================================
    # 12. CLOSET JONGKOK - CAPRI
    # ========================================================

    if "CAPRI" in nama and (
        "CLOSET JONGKOK" in nama
        or "CJ" in nama
    ):

        match = _match_produk(
            master,
            produk,
            "CAPRI"
        )

        if "MAROON" in nama:

            maroon = _filter_variant(
                match,
                "MAROON"
            )

            if not maroon.empty:
                return maroon

            special = _filter_variant(
                match,
                "ARABIAN",
                "EMERALD",
                "CAPRI"
            )

            if not special.empty:
                return special

        return match


    # ========================================================
    # 13. CLOSET JONGKOK CARRIBEAN
    # ========================================================

    if "CARRIBEAN" in nama:

        match = _match_produk(
            master,
            produk,
            "CARRIBEAN"
        )

        if (
            "WHITE" in nama
            or "LIGHT BLUE" in nama
            or "SORRENTO BLUE" in nama
        ):

            white_blue = _filter_variant(
                match,
                "WHITE"
            )

            if not white_blue.empty:
                return white_blue

            blue = _filter_variant(
                match,
                "BLUE"
            )

            if not blue.empty:
                return blue

        if "GREY" in nama:

            grey = _filter_variant(
                match,
                "GREY"
            )

            if not grey.empty:
                return grey

        if "BLACK" in nama:

            black = _filter_variant(
                match,
                "BLACK"
            )

            if not black.empty:
                return black

        if "MAROON" in nama:

            maroon = _filter_variant(
                match,
                "MAROON"
            )

            if not maroon.empty:
                return maroon

        return match


    # ========================================================
    # 14. CLOSET JONGKOK JEWEL
    # ========================================================

    if "JEWEL" in nama:

        return _match_produk(
            master,
            produk,
            "JEWEL"
        )


    # ========================================================
    # 15. TOURMALINE FLUSH VALVE
    # ========================================================

    if "TOURMALINE" in nama:

        return _match_produk(
            master,
            produk,
            "TOURMALINE",
            "FLUSH VALVE"
        )


    # ========================================================
    # 16. CLOSET DUDUK
    # ========================================================

    is_closet_duduk = (
        jenis == "CLOSET DUDUK"
        or "CLOSET DUDUK" in nama
        or type_row in [
            "AMETHYST",
            "EUREKA",
            "EMERALD",
            "CAPRI",
            "CARRIBEAN",
            "MARION",
            "RUBY",
            "SAPPHIRA",
            "OPAL",
            "JASPER",
            "HARVEST",
            "ANDALUZITE",
            "CHRYSOLITE",
            "RHODOLITE",
            "SODALITE",
            "SPENE",
            "MALACHITE",
            "GARNET",
            "COBALT",
            "LILAC",
            "KROOZ",
            "PYRITE",
            "JUNIPER",
            "CITRINE",
            "PERIDOT",
        ]
    )

    if is_closet_duduk:

        # ====================================================
        # MODEL SIMPLE
        # ====================================================

        simple_models = [
            "AMETHYST",
            "HARVEST",
            "ANDALUZITE",
            "RHODOLITE",
            "SPENE",
            "CHRYSOLITE",
            "PYRITE",
            "JUNIPER",
        ]

        for model in simple_models:

            if (
                type_row == model
                or model in nama
            ):

                match = _match_model(
                    master,
                    produk,
                    model
                )

                if not match.empty:
                    return match


        # ====================================================
        # EUREKA
        # ====================================================

        if (
            type_row == "EUREKA"
            or "EUREKA" in nama
        ):

            match = _match_model(
                master,
                produk,
                "EUREKA"
            )

            if "SET" in nama:

                set_match = _filter_variant(
                    match,
                    "SET"
                )

                if not set_match.empty:
                    return set_match

            return match


        # ====================================================
        # JASPER
        # ====================================================

        if (
            type_row == "JASPER"
            or "JASPER" in nama
        ):

            match = _match_model(
                master,
                produk,
                "JASPER"
            )

            # E-FLUSH
            if _has_any(
                nama,
                [
                    "E-FLUSH",
                    "E FLUSH",
                    "E - FLUSH"
                ]
            ):

                flush = _filter_variant(
                    match,
                    "FLUSH"
                )

                if not flush.empty:
                    return flush


            # SMART WASHER
            if "SMART WASHER" in nama:

                smart = _filter_variant(
                    match,
                    "SMART WASHER"
                )

                if not smart.empty:
                    return smart

                smart = _filter_variant(
                    match,
                    "SW"
                )

                if not smart.empty:
                    return smart


            # GREY
            if "GREY" in nama:

                grey = _filter_variant(
                    match,
                    "GREY"
                )

                if not grey.empty:
                    return grey


            # NORMAL
            tanktrim = _filter_variant(
                match,
                "TANKTRIM"
            )

            if not tanktrim.empty:
                return tanktrim

            return match


        # ====================================================
        # MARION
        # ====================================================

        if (
            type_row == "MARION"
            or "MARION" in nama
        ):

            match = _match_model(
                master,
                produk,
                "MARION"
            )

            if "SINGLE FLUSH" in nama:

                single = _filter_variant(
                    match,
                    "SINGLE FLUSH"
                )

                if not single.empty:
                    return single


            if "DOUBLE FLUSH" in nama:

                double = _filter_variant(
                    match,
                    "DOUBLE FLUSH"
                )

                if not double.empty:
                    return double

                tanktrim = _filter_variant(
                    match,
                    "TANKTRIM"
                )

                if not tanktrim.empty:
                    return tanktrim


            tanktrim = _filter_variant(
                match,
                "TANKTRIM"
            )

            if not tanktrim.empty:
                return tanktrim

            return match


        # ====================================================
        # OPAL
        # ====================================================

        if (
            type_row == "OPAL"
            or "OPAL" in nama
        ):

            match = _match_model(
                master,
                produk,
                "OPAL"
            )

            if "BLACK" in nama:

                black = _filter_variant(
                    match,
                    "BLACK"
                )

                if not black.empty:
                    return black


            tanktrim = _filter_variant(
                match,
                "TANKTRIM"
            )

            if not tanktrim.empty:
                return tanktrim

            return match


        # ====================================================
        # RUBY
        # ====================================================

        if (
            type_row == "RUBY"
            or "RUBY" in nama
        ):

            match = _match_model(
                master,
                produk,
                "RUBY"
            )

            if "BLACK" in nama:

                black = _filter_variant(
                    match,
                    "BLACK"
                )

                if not black.empty:
                    return black


            if "MAROON" in nama:

                maroon = _filter_variant(
                    match,
                    "MAROON"
                )

                if not maroon.empty:
                    return maroon

                tanktrim = _filter_variant(
                    match,
                    "TANKTRIM"
                )

                if not tanktrim.empty:
                    return tanktrim


            tanktrim = _filter_variant(
                match,
                "TANKTRIM"
            )

            if not tanktrim.empty:
                return tanktrim

            return match


        # ====================================================
        # SAPPHIRA
        # ====================================================

        if (
            type_row == "SAPPHIRA"
            or "SAPPHIRA" in nama
        ):

            match = _match_model(
                master,
                produk,
                "SAPPHIRA"
            )

            # SMART WASHER
            if "SMART WASHER" in nama:

                smart = _filter_variant(
                    match,
                    "SMART WASHER"
                )

                if not smart.empty:
                    return smart

                smart = _filter_variant(
                    match,
                    "SW"
                )

                if not smart.empty:
                    return smart


            # BLACK
            if "BLACK" in nama:

                black = _filter_variant(
                    match,
                    "BLACK"
                )

                if not black.empty:
                    return black


            tanktrim = _filter_variant(
                match,
                "TANKTRIM"
            )

            if not tanktrim.empty:
                return tanktrim

            return match


        # ====================================================
        # SODALITE
        # ====================================================

        if (
            type_row == "SODALITE"
            or "SODALITE" in nama
        ):

            match = _match_model(
                master,
                produk,
                "SODALITE"
            )

            # SMART WASHER
            if "SMART WASHER" in nama:

                smart = _filter_variant(
                    match,
                    "SMART WASHER"
                )

                if not smart.empty:
                    return smart

                smart = _filter_variant(
                    match,
                    "SW"
                )

                if not smart.empty:
                    return smart


            # UFR
            if "UFR" in nama:

                ufr = _filter_variant(
                    match,
                    "UFR"
                )

                if not ufr.empty:
                    return ufr


            # NORMAL
            normal = _exclude_variant(
                match,
                "SMART WASHER",
                "UFR"
            )

            if not normal.empty:
                return normal

            return match


        # ====================================================
        # MODEL LAIN
        # ====================================================

        known_models = [
            "AMETHYST",
            "EUREKA",
            "EMERALD",
            "CAPRI",
            "CARRIBEAN",
            "MARION",
            "RUBY",
            "SAPPHIRA",
            "OPAL",
            "JASPER",
            "HARVEST",
            "ANDALUZITE",
            "CHRYSOLITE",
            "RHODOLITE",
            "SODALITE",
            "SPENE",
            "MALACHITE",
            "GARNET",
            "COBALT",
            "LILAC",
            "KROOZ",
            "PYRITE",
            "JUNIPER",
            "CITRINE",
            "PERIDOT",
        ]

        for model in known_models:

            if (
                type_row == model
                or model in nama
            ):

                match = _match_model(
                    master,
                    produk,
                    model
                )

                if not match.empty:
                    return match


    # ========================================================
    # 17. GENERIC TYPE
    # ========================================================

    if type_row and "Type" in master.columns:

        master_type = (
            master["Type"]
            .fillna("")
            .apply(bersihkan_text)
        )

        match = master[
            master_type == type_row
        ]

        if not match.empty:
            return match


    # ========================================================
    # 18. GENERIC JENIS
    # ========================================================

    if jenis and "Jenis" in master.columns:

        master_jenis = (
            master["Jenis"]
            .fillna("")
            .apply(bersihkan_text)
        )

        match = master[
            master_jenis == jenis
        ]

        if not match.empty:
            return match


    # ========================================================
    # 19. FALLBACK MODEL DARI NAMA
    # ========================================================

    known_models = [
        "AMETHYST",
        "EUREKA",
        "EMERALD",
        "CAPRI",
        "CARRIBEAN",
        "MARION",
        "RUBY",
        "SAPPHIRA",
        "OPAL",
        "JASPER",
        "HARVEST",
        "ANDALUZITE",
        "CHRYSOLITE",
        "RHODOLITE",
        "SODALITE",
        "SPENE",
        "MALACHITE",
        "GARNET",
        "COBALT",
        "LILAC",
        "KROOZ",
        "PYRITE",
        "JUNIPER",
        "CITRINE",
        "PERIDOT",
    ]

    for model in known_models:

        if model in nama:

            match = _match_model(
                master,
                produk,
                model
            )

            if not match.empty:
                return match


    # ========================================================
    # 20. TIDAK DITEMUKAN
    # ========================================================

    return pd.DataFrame()