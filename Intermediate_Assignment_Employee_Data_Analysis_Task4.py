import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the sample dataset
df = pd.read_csv("C:\python\Workearly\Employee_Data_Analysis.csv")

# Analyzing the distribution of employees across different departments
dept_distribution = df['Department'].value_counts()

# Salary statistics within each department
salary_stats = df.groupby('Department')['Salary'].describe()

# Display the salary statistics
print(salary_stats)

# Plotting the pie chart for department distribution
plt.figure(figsize=(10, 8))
plt.pie(dept_distribution, labels=dept_distribution.index, autopct='%1.1f%%', startangle=140,
        colors=plt.cm.viridis(np.linspace(0, 1, len(dept_distribution))))

# Adding titles
plt.title('Employee Distribution by Department')

# Show plot
plt.show()
