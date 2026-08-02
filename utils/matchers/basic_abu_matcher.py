import pandas as pd
from utils.helper import bersihkan_text


def match_basic_abu(row, df_basic_abu):

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

    return master_match