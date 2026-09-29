# 10-Minute Demonstration Video Script

**0:00–0:45 — Problem.** Explain that the engine ranks sectors cross-sectionally conditional on regime rather than predicting absolute index levels.

**0:45–2:00 — Data & features.** Show the sector panel, 63-day RS baseline, momentum, volatility, breadth, valuation and macro sensitivity.

**2:00–3:15 — Graph.** Show correlation/partial-correlation/signed graph and explain why edges are time-varying.

**3:15–4:30 — TGAT ranking.** Run a live date through the model. Display top-5 sector scores.

**4:30–5:45 — Attention explanation.** Select one sector. Show top incoming edges and attention weights; then run counterfactual edge ablation.

**5:45–6:45 — Uncertainty.** Show MC-dropout standard deviation and conformal top-k set. Apply the three-condition confidence gate.

**6:45–7:45 — Backtest.** Show after-cost overlay return, IR, drawdown and turnover.

**7:45–8:45 — Robustness.** Inject small feature noise and demonstrate ranking stability; show the IL&FS decorrelation stress-test result.

**8:45–9:30 — Audit trail.** Open the experiment registry: data hash, configuration, seed, model version and explanation snapshot.

**9:30–10:00 — Sector Compass.** Briefly show the eight campaign levels and the stress-test mode.

**Recording note:** The final video must be recorded in the user’s live environment after the empirical market-data run. Do not narrate synthetic smoke-test numbers as real-market evidence.

Strictly Private and Confidential · Zetheta Algorithms Private Limited · CIN: U62012MH2023PTC410415
