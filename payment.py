class Payment:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description
        self.is_paid = False

    def view_payment_process(self):
        if self.is_paid:
            print("Payment has been completed.")
        else:
            print("Payment is pending.")

    def cancel_payment(self):
        if self.is_paid:
            print("Payment has been completed. Cannot cancel.")
        else:
            print("Payment has been cancelled.")
            self.amount = 0 

    def generate_receipt(self):
        if self.is_paid:
            print("Receipt:")
            print(f"Amount: ${self.amount}")
            print(f"Description: {self.description}")
            print("Payment status: Completed")
        else:
            print("Payment is pending. Receipt cannot be generated.")

    def make_payment(self):
        self.is_paid = True
        print("Payment completed.")


