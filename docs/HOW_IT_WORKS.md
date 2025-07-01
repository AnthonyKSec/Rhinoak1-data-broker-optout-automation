# How It Works

This project automates the opt-out process for data brokers using Selenium and disposable email services.

## CSV Format
Each row contains:
- broker_name
- optout_url
- status

## Flow
1. Load brokers from `brokers.csv`
2. Use Selenium to navigate and fill forms
3. Optionally validate using temp email
4. Log each submission status in SQLite
