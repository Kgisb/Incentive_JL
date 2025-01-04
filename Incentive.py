import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def calculate_cash_in_incentive(total_upfront_cash_in):
    conversion_rate = 88  # Conversion value from Euro to INR
    if 499 <= total_upfront_cash_in < 999:
        return 0
    elif 999 <= total_upfront_cash_in < 1499:
        return 0.015 * total_upfront_cash_in * conversion_rate
    elif 1499 <= total_upfront_cash_in < 1999:
        return 0.025 * total_upfront_cash_in * conversion_rate
    elif 1999 <= total_upfront_cash_in < 2499:
        return 0.05 * total_upfront_cash_in * conversion_rate
    elif 2499 <= total_upfront_cash_in < 2999:
        return 0.075 * total_upfront_cash_in * conversion_rate
    elif 2999 <= total_upfront_cash_in < 3499:
        return 0.1 * total_upfront_cash_in * conversion_rate
    elif 3499 <= total_upfront_cash_in < 3999:
        return 0.125 * total_upfront_cash_in * conversion_rate
    elif total_upfront_cash_in >= 3999:
        return 0.15 * total_upfront_cash_in * conversion_rate
    else:
        return 0


def calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source):
    conversion_rate = 88  # Conversion value from Euro to INR
    if deal_source in ["PM-Search", "PM-Social", "Organic", "Others"]:
        if mrp == 649 and full_payment_cash_in >= 449:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1199 and full_payment_cash_in >= 899:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1999 and full_payment_cash_in >= 1549:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        else:
            return 0
    elif deal_source in ["Referral", "Events", "Goldmine", "DP"]:
        if mrp == 649 and full_payment_cash_in >= 399:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1199 and full_payment_cash_in >= 799:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        elif mrp == 1999 and full_payment_cash_in >= 1429:
            return 0.075 * (full_payment_cash_in / mrp) * conversion_rate * full_payment_cash_in
        else:
            return 0
    else:
        return 0


class IncentiveCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Incentive Calculator")

        # Upfront Cash-in Section
        self.upfront_label = ttk.Label(root, text="Total Upfront Cash-in (€):")
        self.upfront_label.grid(row=0, column=0, padx=10, pady=10)
        self.upfront_entry = ttk.Entry(root)
        self.upfront_entry.grid(row=0, column=1, padx=10, pady=10)
        self.upfront_button = ttk.Button(root, text="Calculate Upfront Incentive", command=self.calculate_upfront)
        self.upfront_button.grid(row=0, column=2, padx=10, pady=10)
        self.upfront_result = ttk.Label(root, text="")
        self.upfront_result.grid(row=0, column=3, padx=10, pady=10)

        # Full Payment Section
        self.full_payment_label = ttk.Label(root, text="Full Payment Cash-in (€):")
        self.full_payment_label.grid(row=1, column=0, padx=10, pady=10)
        self.full_payment_entry = ttk.Entry(root)
        self.full_payment_entry.grid(row=1, column=1, padx=10, pady=10)

        self.mrp_label = ttk.Label(root, text="MRP (€):")
        self.mrp_label.grid(row=2, column=0, padx=10, pady=10)
        self.mrp_combobox = ttk.Combobox(root, values=[119, 349, 649, 1199, 1999])
        self.mrp_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.deal_source_label = ttk.Label(root, text="Deal Source:")
        self.deal_source_label.grid(row=3, column=0, padx=10, pady=10)
        self.deal_source_combobox = ttk.Combobox(root, values=["PM-Search", "PM-Social", "Organic", "Others", "Referral", "Events", "Goldmine", "DP"])
        self.deal_source_combobox.grid(row=3, column=1, padx=10, pady=10)

        self.price_control_button = ttk.Button(root, text="Calculate Price Control Incentive", command=self.calculate_price_control)
        self.price_control_button.grid(row=4, column=1, padx=10, pady=10)
        self.price_control_result = ttk.Label(root, text="")
        self.price_control_result.grid(row=4, column=2, padx=10, pady=10)

        # Final Incentive Section
        self.final_button = ttk.Button(root, text="Calculate Final Incentive", command=self.calculate_final_incentive)
        self.final_button.grid(row=5, column=1, padx=10, pady=10)
        self.final_result = ttk.Label(root, text="", font=("Arial", 16, "bold"))
        self.final_result.grid(row=5, column=2, padx=10, pady=10)

    def calculate_upfront(self):
        try:
            total_upfront_cash_in = float(self.upfront_entry.get())
            result = calculate_cash_in_incentive(total_upfront_cash_in)
            self.upfront_result.config(text=f"INR {result:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    def calculate_price_control(self):
        try:
            full_payment_cash_in = float(self.full_payment_entry.get())
            mrp = int(self.mrp_combobox.get())
            deal_source = self.deal_source_combobox.get()
            result = calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source)
            self.price_control_result.config(text=f"INR {result:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid inputs.")

    def calculate_final_incentive(self):
        try:
            total_upfront_cash_in = float(self.upfront_entry.get())
            upfront_incentive = calculate_cash_in_incentive(total_upfront_cash_in)

            full_payment_cash_in = float(self.full_payment_entry.get())
            mrp = int(self.mrp_combobox.get())
            deal_source = self.deal_source_combobox.get()
            price_control_incentive = calculate_price_control_incentive(full_payment_cash_in, mrp, deal_source)

            total_incentive = upfront_incentive + price_control_incentive
            self.final_result.config(text=f"Total Incentive: INR {total_incentive:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid inputs.")


if __name__ == "__main__":
    root = tk.Tk()
    app = IncentiveCalculatorApp(root)
    root.mainloop()
