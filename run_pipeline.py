
"""End-to-end runner. 1) python -m src.run_smoke for smoke test.
2) python run_pipeline.py --download to fetch Yahoo/NSE-compatible data.
3) After data are present, extend train.py configuration for full empirical run.
"""
import argparse
from src.data import download_yahoo, load_panel, clean_panel
p=argparse.ArgumentParser(); p.add_argument("--download",action="store_true")
args=p.parse_args()
if args.download: download_yahoo()
panel=clean_panel(load_panel())
print("Loaded panel:",panel.shape, "date range:", panel.index.min(), panel.index.max())
print(panel.tail())
