import pandas as pd
from pathlib import Path


# ATOC_4815/atoc_4815_lab6/data_files/wxobs20250213.txt
# resource used: https://labex.io/pythoncheatsheet/cheatsheet/file-directory-path
file_path_test = Path("..").joinpath("atoc_4815_lab6").joinpath("data_files").joinpath("wxobs20250213")
print(f"File path test: {file_path_test}")