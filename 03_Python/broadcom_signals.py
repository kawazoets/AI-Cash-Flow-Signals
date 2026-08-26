import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path("02_Data/broadcom_quarterly.csv")
CHART_DIR = Path("04_Charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_FILE)

plt.figure(figsize=(11,6))
plt.plot(df["fiscal_quarter"], df["revenue_usd_m"], marker="o", label="Revenue")
plt.plot(df["fiscal_quarter"], df["operating_cash_flow_usd_m"], marker="o", label="Operating Cash Flow")
plt.plot(df["fiscal_quarter"], df["free_cash_flow_usd_m"], marker="o", label="Free Cash Flow")
plt.title("Broadcom: Revenue, Operating Cash Flow and Free Cash Flow")
plt.xlabel("Fiscal Quarter"); plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
plt.savefig(CHART_DIR / "broadcom_revenue_ocf_fcf.png", dpi=180); plt.close()

ai = df.dropna(subset=["ai_semiconductor_revenue_usd_m"])
plt.figure(figsize=(11,6))
plt.plot(ai["fiscal_quarter"], ai["ai_semiconductor_revenue_usd_m"], marker="o")
plt.title("Broadcom: Reported AI Semiconductor Revenue")
plt.xlabel("Fiscal Quarter"); plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right"); plt.tight_layout()
plt.savefig(CHART_DIR / "broadcom_ai_revenue.png", dpi=180); plt.close()

plt.figure(figsize=(11,6))
plt.plot(df["fiscal_quarter"], df["capex_to_ocf_pct"], marker="o")
plt.title("Broadcom: Cash CAPEX as % of Operating Cash Flow")
plt.xlabel("Fiscal Quarter"); plt.ylabel("Percent")
plt.xticks(rotation=45, ha="right"); plt.tight_layout()
plt.savefig(CHART_DIR / "broadcom_capex_to_ocf.png", dpi=180); plt.close()
