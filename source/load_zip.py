# %%
import argparse
from io import BytesIO
import shutil
from pathlib import Path
import warnings
from zipfile import ZipFile

import pandas as pd

# %%
parser = argparse.ArgmentParser()

parser.add_argument('-- unzip', default=False)
parser.add_argument('--chunksize', default=100000)
args = parser.parse_args()

home = Path.home()
data_path = home / "data"
zfiles = data_path.glob('*.zip')
save_path = Path.cwd() / "result"

for zfile in zfiles:
    with ZipFile(zfile) as zf:
        csvfiles = zf.namelist()
        for csv in csvfiles:
            fname_out = save_path / csv
            
            if args.unzip and (not fname_out.exists()):
                shutil.unpack_archive (data_path, save_path)
                with warnings.catch_warnings():
                    warnings.simplefilter('error')
                    reader = pd.read_csv(csv, encoding='cp932', chunksize=args.chunksize)
            else:
                with warnings.catch_warnings():
                    warnings.simplefilter('error')
                    reader = pd.read_csv(BytesIO(zf.read(csv)), encoding='cp932', chunksize=args.chunksize)
        df = pd.concat((preprocess(r) for r in reader), ignore_index=True)

# %% 
def preprocess(r, inplace=True):
    print(r.memory_usage(index=True). sum() /10**6)
    return r

# %%
# dtypeを指定した方がメモリは小さくなる、早くはならない
# ddf = dd.read_csu(fname_out, dtype="object", encoding='cp932')
