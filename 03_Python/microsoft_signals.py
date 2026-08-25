import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path("02_Data/microsoft_quarterly.csv")
CHART_DIR = Path("04_Charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)

# 1. Operating Cash Flow vs Cash CAPEX
plt.figure(figsize=(11, 6))
plt.plot(
    df["fiscal_quarter"],
    df["operating_cash_flow_usd_m"],
    marker="o",
    label="Operating Cash Flow"
)
plt.plot(
    df["fiscal_quarter"],
    df["cash_capex_usd_m"],
    marker="o",
    label="Cash CAPEX"
)
plt.title("Microsoft: Operating Cash Flow vs Cash CAPEX")
plt.xlabel("Fiscal Quarter")
plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.savefig(CHART_DIR / "microsoft_ocf_vs_capex.png", dpi=180)
plt.close()

# 2. CAPEX / Operating Cash Flow
plt.figure(figsize=(11, 6))
plt.plot(
    df["fiscal_quarter"],
    df["capex_to_ocf_pct"],
    marker="o"
)
plt.title("Microsoft: Cash CAPEX as % of Operating Cash Flow")
plt.xlabel("Fiscal Quarter")
plt.ylabel("Percent")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(CHART_DIR / "microsoft_capex_to_ocf.png", dpi=180)
plt.close()

# 3. Liquidity vs Debt
plt.figure(figsize=(11, 6))
plt.plot(
    df["fiscal_quarter"],
    df["cash_plus_short_term_investments_usd_m"],
    marker="o",
    label="Cash + Short-term Investments"
)
plt.plot(
    df["fiscal_quarter"],
    df["total_debt_usd_m"],
    marker="o",
    label="Total Debt"
)
plt.title("Microsoft: Liquidity vs Total Debt")
plt.xlabel("Fiscal Quarter")
plt.ylabel("USD million")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.tight_layout()
plt.savefig(CHART_DIR / "microsoft_liquidity_vs_debt.png", dpi=180)
plt.close()
