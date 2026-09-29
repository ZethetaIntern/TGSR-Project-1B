# Temporal Graph Sector Rotation Network (TGSR) — Project 1B

This package is aligned to the supplied Zetheta Algorithms Project 1B brief.

## Deliverables covered
1. Main Report — PDF + editable DOCX (40 pages)
2. Python codebase — ingestion, features, graph construction, GNN architectures, uncertainty, explainability, robustness, backtest
3. R validation codebase — independent RS/rank validation and structural-break/Granger/DCC-GARCH hooks
4. Model Experimentation & Ablation Report — PDF
5. Excel Validation Workbook — XLSX
6. Final Presentation — exactly 18 slides in PPTX + PDF

The brief explicitly requires honest out-of-sample IC, ablation evidence, calibration/conformal coverage, explanation stability, reproducible lineage and no fabricated claims. See the source brief's submission requirements and validation discipline. 

## Data
Primary production route: NSE sectoral indices + Nifty benchmarks and macro series. The code uses Yahoo Finance as a practical ingestion route and leaves a clean adapter point for official NSE downloads. The expected production panel is 14 sector indices from 2008 onward plus Nifty 50/500 and macro variables.

**Important execution note:** this environment does not provide outbound network access to download market data. Therefore the included empirical result files are explicitly labelled **engineering smoke-test results on synthetic data**, not market evidence. Do not present them as historical trading results. Run `python run_pipeline.py --download` in an internet-enabled environment and then execute the full CV pipeline before making empirical claims.

## Architecture
GCN → GraphSAGE → GAT → GATv2 → TGAT → EvolveGCN → RelationalSectorGAT → SignedSectorGAT → RegimeMoE.

The implementation includes dynamic-edge utilities, MC-dropout, conformal thresholding, attention extraction, counterfactual edge ablation, structural stress tests, event-window gating and transaction-cost backtesting.

## Run
```bash
cd python
pip install -r requirements.txt
python -m src.run_smoke
python run_pipeline.py --download
```

## Project-1 regime integration
A `regime_posterior.csv` adapter should contain date-indexed posterior columns matching the Project-1 regime states. If unavailable, use a clearly labelled research-only regime proxy; never imply that the proxy is the Project-1 Bayesian engine.

## Confidentiality
Strictly Private and Confidential · Zetheta Algorithms Private Limited · CIN: U62012MH2023PTC410415
