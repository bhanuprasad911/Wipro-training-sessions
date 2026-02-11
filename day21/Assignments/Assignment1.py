import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

data = pd.DataFrame({
    "Month": months,
    "Sales": sales
})
plt.figure()
plt.plot(months, sales, marker='o')
plt.figure()
sns.barplot(x="Month", y="Sales", data=data)
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()
plt.savefig("Linechart.png")
plt.savefig("Barplot.png")