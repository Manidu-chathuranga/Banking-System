import tkinter as tk
from tkinter import messagebox

class BankingApp:
    def __init__(self, root):
        self.balance = 0
        
        # Main window setup
        root.title("Banking Application")
        root.geometry("300x400")
        
        # Label for title
        self.title_label = tk.Label(root, text="Banking Program", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Balance display
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance:.2f}", font=("Arial", 14))
        self.balance_label.pack(pady=10)
        
        # Buttons for actions
        self.show_balance_button = tk.Button(root, text="Show Balance", command=self.show_balance, width=20)
        self.show_balance_button.pack(pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, width=20)
        self.deposit_button.pack(pady=5)
        
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, width=20)
        self.withdraw_button.pack(pady=5)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=5)
    
    # Function to show balance
    def show_balance(self):
        messagebox.showinfo("Balance", f"Your balance is ${self.balance:.2f}")
    
    # Function to deposit money
    def deposit(self):
        try:
            amount = float(self.get_amount("Deposit Amount"))
            if amount < 0:
                messagebox.showerror("Error", "Amount must be greater than 0")
            else:
                self.balance += amount
                self.update_balance()
                messagebox.showinfo("Success", f"${amount:.2f} has been deposited.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
    
    # Function to withdraw money
    def withdraw(self):
        try:
            amount = float(self.get_amount("Withdraw Amount"))
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds.")
            elif amount < 0:
                messagebox.showerror("Error", "Amount must be greater than 0.")
            else:
                self.balance -= amount
                self.update_balance()
                messagebox.showinfo("Success", f"${amount:.2f} has been withdrawn.")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
    
    # Helper function to get input
    def get_amount(self, title):
        input_window = tk.Toplevel()
        input_window.title(title)
        
        tk.Label(input_window, text=f"{title}:").pack(pady=10)
        amount_entry = tk.Entry(input_window)
        amount_entry.pack(pady=10)
        
        amount = tk.DoubleVar()
        
        def submit():
            try:
                amount.set(float(amount_entry.get()))
                input_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")
        
        tk.Button(input_window, text="Submit", command=submit).pack(pady=10)
        input_window.wait_window()
        return amount.get()
    
    # Function to update balance label
    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

# Main script to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
