import pandas as pd
from utils.helper import bersihkan_text


def match_pureflo_fitting(row, df_pureflo_fitting):

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

    return master_match