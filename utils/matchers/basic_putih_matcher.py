import pandas as pd
from utils.helper import bersihkan_text


def match_basic_putih(row, df_basic_putih):

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

    return master_match