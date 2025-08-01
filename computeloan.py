import tkinter as tk
from tkinter import messagebox


class Loan:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Compare Interest Rates")

        self.frame1= tk.Frame(self.root)
        self.frame1.grid(row = 1, column = 1, columnspan=10, pady= 10)
        

        

        self.label_amount = tk.Label(self.frame1, text = "Loan Amount ")
        self.label_amount.grid(row = 1, column = 2, padx=5) 
        self.entry_amount = tk.Entry(self.frame1)
        self.entry_amount.grid(row = 1, column = 3, padx=5)
        

        self.label_year = tk.Label(self.frame1, text = "Year ")
        self.label_year.grid(row = 1, column = 5, padx=5)
        self.entry_year = tk.Entry(self.frame1)
        self.entry_year.grid(row = 1, column = 6)

        self.button = tk.Button(self.frame1, text= "Calculate", command = self.calculate_loan)
        self.button.grid(row = 1, column = 7, padx=5)


        self.text = tk.Text(self.root, height=20, width=60)
        self.text.grid(row = 2, column=1, columnspan=10, pady=10)

        scrollbar = tk.Scrollbar(self.root, command=self.text.yview)
        scrollbar.grid(row=2, column=11, sticky='nsew')
        self.text.config(yscrollcommand=scrollbar.set) 
        
        



    def run(self):
        self.root.mainloop()

    def calculate_loan(self):
        amount = float(self.entry_amount.get())
        year = float(self.entry_year.get())

        self.text.delete(1.0, tk.END)

        header = f"{'Interest Rate':<15}{'Monthly Payment':<20}{'Total Payment':<20}\n"
        self.text.insert(tk.END, header + "\n")
        
        rate = 5.0    

        while rate <= 8.001:
            monthly_rate = rate / 100 / 12
            months = year * 12
            monthly_payment = amount * monthly_rate / (1 - 1/((1+ monthly_rate)** months))
            total_payment = monthly_payment * months

            result = f"{rate:5.2f}{' ' * 9}${monthly_payment:<18,.2f}${total_payment:<18,.2f}\n"
            self.text.insert(tk.END, result)
                
            rate += 0.125
            
            

        
        
        

        
        
        

    

        
loan = Loan()
loan.run()
