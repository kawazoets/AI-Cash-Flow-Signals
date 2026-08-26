import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path("02_Data")
OUT_DIR = Path("06_Dashboard")
OUT_DIR.mkdir(parents=True, exist_ok=True)

ms = pd.read_csv(DATA_DIR / "microsoft_quarterly.csv")
goog = pd.read_csv(DATA_DIR / "alphabet_quarterly.csv")
amzn = pd.read_csv(DATA_DIR / "amazon_quarterly.csv")
meta = pd.read_csv(DATA_DIR / "meta_quarterly.csv")
avgo = pd.read_csv(DATA_DIR / "broadcom_quarterly.csv")

def calendar_q(df, date_col="period_end"):
    d = pd.to_datetime(df[date_col])
    return d.dt.to_period("Q").astype(str).str.replace("Q", " Q", regex=False)

ms["calendar_q"] = calendar_q(ms)
goog["calendar_q"] = goog["calendar_quarter"]
amzn["calendar_q"] = amzn["calendar_quarter"]
meta["calendar_q"] = meta["calendar_quarter"]

plt.figure(figsize=(12, 7))
plt.plot(ms["calendar_q"], ms["capex_to_ocf_pct"], marker="o", label="Microsoft")
plt.plot(goog["calendar_q"], goog["capex_to_ocf_pct"], marker="o", label="Alphabet")
plt.plot(amzn["calendar_q"], amzn["capex_to_ocf_pct"], marker="o", label="Amazon")
plt.plot(meta["calendar_q"], meta["capex_to_ocf_pct"], marker="o", label="Meta")
plt.axhline(100, linestyle="--", linewidth=1, label="100% of OCF")
plt.title("Hyperscalers: Cash CAPEX as % of Operating Cash Flow")
plt.xlabel("Calendar Quarter"); plt.ylabel("Percent")
plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
plt.savefig(OUT_DIR / "dashboard_hyperscaler_capex_to_ocf.png", dpi=180)
plt.close()

plt.figure(figsize=(12, 7))
plt.plot(ms["calendar_q"], ms["free_cash_flow_usd_m"], marker="o", label="Microsoft")
plt.plot(goog["calendar_q"], goog["free_cash_flow_usd_m"], marker="o", label="Alphabet")
plt.plot(amzn["calendar_q"], amzn["free_cash_flow_usd_m"], marker="o", label="Amazon")
plt.plot(meta["calendar_q"], meta["free_cash_flow_before_finance_lease_principal_usd_m"], marker="o", label="Meta")
plt.axhline(0, linestyle="--", linewidth=1)
plt.title("Hyperscalers: Cash Remaining After CAPEX")
plt.xlabel("Calendar Quarter"); plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
plt.savefig(OUT_DIR / "dashboard_hyperscaler_cash_after_capex.png", dpi=180)
plt.close()

plt.figure(figsize=(12, 7))
plt.plot(avgo["fiscal_quarter"], avgo["revenue_usd_m"], marker="o", label="Revenue")
plt.plot(avgo["fiscal_quarter"], avgo["operating_cash_flow_usd_m"], marker="o", label="Operating Cash Flow")
plt.plot(avgo["fiscal_quarter"], avgo["free_cash_flow_usd_m"], marker="o", label="Free Cash Flow")
ai = avgo.dropna(subset=["ai_semiconductor_revenue_usd_m"])
plt.plot(ai["fiscal_quarter"], ai["ai_semiconductor_revenue_usd_m"], marker="o", label="Reported AI Semiconductor Revenue")
plt.title("Broadcom: Supplier-Side Revenue and Cash Generation")
plt.xlabel("Fiscal Quarter"); plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
plt.savefig(OUT_DIR / "dashboard_broadcom_supplier_cash.png", dpi=180)
plt.close()
