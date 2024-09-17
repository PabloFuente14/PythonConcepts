#Create a sales report by aggeregating two lists of data: one of them containing some product names, and the other the corresponding sales and generate a report.
import pandas as pd

class SalesReport:
    def __init__ (self, products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch'], sales = [150, 300, 120, 200, 80]):
        self.products = products
        self.sales = sales
        self.report = self.generate_report()
        
    def aggregate_data(self):
        return list(zip(self.products,self.sales))
    
    def generate_report(self):
        data = self.aggregate_data()
        df = pd.DataFrame(data ,columns = ['Products', 'Sales'])
        df.to_csv('sales_report.csv', index=False)
        return df

    
if __name__ == '__main__':
    report_generator = SalesReport()
    print(report_generator.report.head())