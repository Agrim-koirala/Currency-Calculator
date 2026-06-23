
# ==========================================
# NEPALI CURRENCY & TAX CALCULATOR
# Built by: [Your Name]
# ==========================================

import datetime

def run_calculator():
    print("====================================")
    print("      NEPALI FINANCIAL UTILITY      ")
    print("====================================")
    
   # 1. User Input for Conversion
    usd_amount = float(input("Enter amount in USD to convert to NPR: $"))
    
    # 2. Exchange Rate Logic 
    # (Using 1 USD = 135 NPR as a standard baseline)
    exchange_rate = 135.0
    npr_converted = usd_amount * exchange_rate
    
    print(f"\n💵 ${usd_amount} USD is approximately Rs. {npr_converted:,.2f} NPR.")
    print("------------------------------------")
    
    # 3. User Input for Monthly Income
monthly_income = float(input("Enter monthly income in NPR for Tax Check: Rs. "))
    
    # 4. Tax Calculation Logic (Simplified Nepal Tax Bracket)
    # Annualizing income to match real tax evaluation rules
annual_income = monthly_income * 12
annual_tax = 0.0
    
    # Simple single earner tax rule simulation:
    # First 500,000 is taxed at 1% (Social Security Tax)
    # Next 200,000 is taxed at 10%
if annual_income <= 500000:
        annual_tax = annual_income * 0.01
elif annual_income <= 700000:
        annual_tax = (500000 * 0.01) + ((annual_income - 500000) * 0.10)
else:
        annual_tax = (500000 * 0.01) + (200000 * 0.10) + ((annual_income - 700000) * 0.20)
        
monthly_tax = annual_tax / 12
take_home_pay = monthly_income - monthly_tax

    # 5. Printing a Clean Receipt Terminal Interface
print("\n====================================")
print("          SALARY SLIP REPORT        ")
print("====================================")
print(f"Date generated : {datetime.date.today()}")
print(f"Gross Monthly  : Rs. {monthly_income:}")
print(f"Estimated Tax  : Rs. {monthly_tax:,.2f}")
print("------------------------------------")
print(f"Net Take-Home  : Rs. {take_home_pay:,.2f}")
print("====================================\n")

if __name__ == "__main__":
    run_calculator()
