import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path("02_Data/meta_quarterly.csv")
CHART_DIR = Path("04_Charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(DATA_FILE)

plt.figure(figsize=(11, 6))
plt.plot(df["calendar_quarter"], df["operating_cash_flow_usd_m"], marker="o", label="Operating Cash Flow")
plt.plot(df["calendar_quarter"], df["cash_capex_usd_m"], marker="o", label="Cash CAPEX")
plt.title("Meta: Operating Cash Flow vs Cash CAPEX")
plt.xlabel("Calendar Quarter"); plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
plt.savefig(CHART_DIR / "meta_ocf_vs_capex.png", dpi=180); plt.close()

plt.figure(figsize=(11, 6))
plt.plot(df["calendar_quarter"], df["capex_to_ocf_pct"], marker="o")
plt.axhline(100, linestyle="--", linewidth=1)
plt.title("Meta: Cash CAPEX as % of Operating Cash Flow")
plt.xlabel("Calendar Quarter"); plt.ylabel("Percent")
plt.xticks(rotation=45, ha="right"); plt.tight_layout()
plt.savefig(CHART_DIR / "meta_capex_to_ocf.png", dpi=180); plt.close()

plt.figure(figsize=(11, 6))
plt.plot(df["calendar_quarter"], df["free_cash_flow_before_finance_lease_principal_usd_m"], marker="o", label="OCF - Cash CAPEX")
plt.axhline(0, linestyle="--", linewidth=1)
plt.title("Meta: Cash Remaining After CAPEX")
plt.xlabel("Calendar Quarter"); plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right"); plt.legend(); plt.tight_layout()
plt.savefig(CHART_DIR / "meta_cash_after_capex.png", dpi=180); plt.close()
