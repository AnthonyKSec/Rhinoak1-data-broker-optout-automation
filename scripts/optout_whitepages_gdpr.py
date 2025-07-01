"""
optout_whitepages.py

Automates the opt-out process for Whitepages using Selenium.

Legal Notice:
This automation is intended to help individuals exercise their data privacy rights under:

- The Texas Data Privacy and Security Act (TDPSA), effective July 1, 2024, which grants Texas residents the right to access, correct, and delete personal data.
- The General Data Protection Regulation (GDPR - EU 2016/679), which grants EU residents the right to object to data processing, request erasure ("right to be forgotten"), and access their personal data.
- The Fair Credit Reporting Act (FCRA), which regulates accuracy and privacy in personal data used for credit or background checks.
- The Gramm-Leach-Bliley Act (GLBA), which governs how personal financial data is shared and protected.

This script is intended for personal use or authorized agent requests only. Any automated use must comply with the relevant data protection laws and the website’s terms of service.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def run_whitepages_optout(full_name, email):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        print("[*] Opening Whitepages opt-out page...")
        driver.get("https://www.whitepages.com/suppression-requests")
        time.sleep(5)  # allow page to load

        # Click Start Removal Request
        start_btn = driver.find_element(By.XPATH, '//a[contains(text(), "Start Removal Request")]')
        start_btn.click()
        time.sleep(3)

        # Enter name and email (the actual form may require more complex interaction)
        # Note: You may need to adapt this to match updated form fields or interactions.

        print("[*] This page will require manual intervention due to CAPTCHA or dynamic form behavior.")

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Replace with your actual name and email for testing
    run_whitepages_optout(full_name="John Doe", email="johndoe@example.com")
