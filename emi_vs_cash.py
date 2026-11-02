#!/usr/bin/env python3
"""Car EMI vs Cash comparison calculator (Pakistan context).

Compares the total cost of buying a car on a bank loan (EMI) against
paying the full price in cash up front, so a buyer can see exactly how
much extra the loan costs in interest.

Run:  python3 emi_vs_cash.py
"""

MONTHS_PER_YEAR = 12


def monthly_emi(principal: float, annual_rate_percent: float, months: int) -> float:
    """Standard EMI formula. Handles the zero-interest edge case."""
    if months <= 0:
        raise ValueError("Loan tenure must be more than 0 months.")
    if principal < 0:
        raise ValueError("Loan amount cannot be negative.")
    monthly_rate = annual_rate_percent / 100.0 / MONTHS_PER_YEAR
    if monthly_rate == 0:
        return principal / months
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


def compare(car_price: float, down_payment: float,
            annual_rate_percent: float, years: int) -> dict:
    """Return a comparison of loan vs cash purchase for one car."""
    if car_price <= 0:
        raise ValueError("Car price must be positive.")
    if not 0 <= down_payment < car_price:
        raise ValueError("Down payment must be between 0 and the car price.")
    if years <= 0:
        raise ValueError("Loan tenure must be more than 0 years.")
    months = years * MONTHS_PER_YEAR
    loan_amount = car_price - down_payment
    emi = monthly_emi(loan_amount, annual_rate_percent, months)
    total_paid_on_loan = down_payment + emi * months
    total_interest = emi * months - loan_amount
    return {
        "car_price": car_price,
        "down_payment": down_payment,
        "loan_amount": loan_amount,
        "months": months,
        "monthly_emi": emi,
        "total_interest": total_interest,
        "total_cost_loan": total_paid_on_loan,
        "total_cost_cash": car_price,
        "extra_cost_of_loan": total_paid_on_loan - car_price,
    }


def fmt(amount: float) -> str:
    return f"Rs {amount:,.0f}"


def main() -> None:
    print("=== Car EMI vs Cash Comparison ===")
    try:
        car_price = float(input("Car price (Rs): "))
        down_payment = float(input("Down payment (Rs, 0 if none): "))
        annual_rate = float(input("Bank annual interest/markup rate (%): "))
        years = int(input("Loan tenure (years): "))
    except ValueError:
        print("Please enter valid numbers only.")
        return
    try:
        result = compare(car_price, down_payment, annual_rate, years)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print("\n--- Loan option ---")
    print(f"Loan amount:        {fmt(result['loan_amount'])}")
    print(f"Monthly EMI:        {fmt(result['monthly_emi'])} for "
          f"{result['months']} months")
    print(f"Total interest:     {fmt(result['total_interest'])}")
    print(f"Total cost (loan):  {fmt(result['total_cost_loan'])}")
    print("\n--- Cash option ---")
    print(f"Total cost (cash):  {fmt(result['total_cost_cash'])}")
    print("\n--- Verdict ---")
    extra = result["extra_cost_of_loan"]
    if extra > 0:
        print(f"Loan costs {fmt(extra)} MORE than paying cash.")
    elif extra == 0:
        print("Loan and cash cost exactly the same (0% markup).")
    else:
        print(f"Loan costs {fmt(-extra)} LESS than cash (unusual — "
              "check the rate).")


if __name__ == "__main__":
    main()
