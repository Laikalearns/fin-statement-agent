# Financial Statement Analyzer Agent

A lightweight, runnable agent that ingests a company’s income statement, balance sheet, and cash flow statement and produces:

- Key financial ratios
- Simple trend observations
- A short **TLDR**
- Highlighted **pros** and **cons**

Designed to be demo-ready and interview-friendly. No external API keys required for the core analysis (rule-based narrative).

## Why this exists

Reading full financial statements is time-consuming. This agent quickly surfaces the most important signals (profitability, liquidity, leverage, cash generation) and gives a plain-language summary with clear pros/cons so you can decide where to dig deeper.

## Features

- Accepts CSV files (or uses built-in demo data)
- Calculates common ratios: gross margin, operating margin, net margin, current ratio, debt-to-equity, ROE, free cash flow, etc.
- Generates a concise TLDR
- Lists specific pros and cons based on the numbers
- Simple CLI or script interface
- Easy to extend with real data or an LLM layer later

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analyze.py
```

By default it runs on the sample company data in `data/`.

## Input format

Place three CSVs in the `data/` folder (or pass paths):

- `income.csv`
- `balance.csv`
- `cashflow.csv`

Expected columns are simple (see the demo files). The agent looks for standard line items (Revenue, Gross Profit, Operating Income, Net Income, Total Assets, Total Liabilities, Equity, Operating Cash Flow, Capex, etc.).

## Example output

The agent prints something like:

```
=== TLDR ===
Company shows healthy top-line growth and strong cash generation, but leverage is elevated and margins are under pressure.

=== PROS ===
- Positive free cash flow
- Current ratio above 1.5
- ...

=== CONS ===
- Declining operating margin
- Debt-to-equity > 1.5
- ...
```

## Project structure

```
analyze.py              Main entry point
agent/
  ratios.py             Ratio calculations
  narrative.py          TLDR + pros/cons logic
data/
  income.csv            Demo income statement
  balance.csv           Demo balance sheet
  cashflow.csv          Demo cash flow
requirements.txt
```

## Next steps / ideas

- Add year-over-year comparison when multiple periods are provided
- Plug in an LLM for richer narrative
- Web UI (similar to workforce-scout)
- Support for more line-item aliases

## License

MIT
