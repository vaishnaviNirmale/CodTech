import matplotlib.pyplot as plt
import numpy as np

# Generating random data for demonstration
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = np.random.randint(1, 100, size=len(categories))

# Creating subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

# Bar Chart
axes[0, 0].bar(categories, values, color='skyblue')
axes[0, 0].set_title('Bar Chart')
axes[0, 0].set_xlabel('Categories')
axes[0, 0].set_ylabel('Values')

# Pie Chart
axes[0, 1].pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue', 'lightgoldenrodyellow'])
axes[0, 1].set_title('Pie Chart')

# Line Graph
x_values = np.arange(len(categories))
axes[1, 0].plot(x_values, values, marker='o', linestyle='-', color='orange')
axes[1, 0].set_title('Line Graph')
axes[1, 0].set_xlabel('Categories')
axes[1, 0].set_ylabel('Values')
axes[1, 0].set_xticks(x_values)
axes[1, 0].set_xticklabels(categories)

# Scatter Plot
axes[1, 1].scatter(np.arange(len(categories)), values, color='purple', alpha=0.6)
axes[1, 1].set_title('Scatter Plot')
axes[1, 1].set_xlabel('Data Points')
axes[1, 1].set_ylabel('Values')

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()
