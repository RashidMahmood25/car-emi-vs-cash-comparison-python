# Car EMI vs Cash Comparison (Python)

A small calculator that compares buying a car on a bank loan (monthly EMI)
against paying the full price in cash, so you can see exactly how much
extra the loan costs in interest.

## How to run

```bash
python3 emi_vs_cash.py
```

Enter the car price, down payment, annual markup rate and loan tenure.
The script prints the monthly EMI, total interest, total loan cost, cash
cost, and the difference between the two.

## Example

Car price Rs 3,000,000, down payment Rs 600,000, markup 18% per year,
tenure 5 years:

- Loan amount: Rs 2,400,000
- Monthly EMI: ~Rs 60,944 for 60 months
- Total interest: ~Rs 1,256,654
- Total cost on loan: ~Rs 4,256,654
- Cash cost: Rs 3,000,000
- **Loan costs ~Rs 1,256,654 more than cash.**

## What was practiced

- The standard EMI formula: `EMI = P * r * (1+r)^n / ((1+r)^n - 1)`
- Input validation and clear error messages
- Separating calculation logic (`compare`, `monthly_emi`) from user input

## Notes

- This is a simple comparison tool, not financial advice. Actual bank
  charges (processing fee, insurance, taxes) are not included.
- No real data is used — all figures come from the numbers you enter.
