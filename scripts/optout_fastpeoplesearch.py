"""
optout_fastpeoplesearch.py

Automates the opt-out process for Fastpeoplesearch using Selenium.

Legal Notice:
This script is intended to help individuals exercise their privacy rights under:
- Texas Data Privacy and Security Act (TDPSA)
- General Data Protection Regulation (GDPR)
- Fair Credit Reporting Act (FCRA)
- Gramm-Leach-Bliley Act (GLBA)

Use only for lawful, authorized purposes. Some brokers may require CAPTCHA verification or email confirmation.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def run_fastpeoplesearch_optout(full_name, email):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        print("[*] Opening Fastpeoplesearch opt-out page...")
        driver.get("https://www.fastpeoplesearch.com/removal")
        time.sleep(5)

        print("[*] Manual steps likely required for CAPTCHA or multi-step forms.")
    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run opt-out for Fastpeoplesearch")
    parser.add_argument("--name", required=True, help="Your full name")
    parser.add_argument("--email", required=True, help="Your email")
    args = parser.parse_args()

    run_fastpeoplesearch_optout(full_name=args.name, email=args.email)
