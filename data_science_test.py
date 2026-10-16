
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a small dataset
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [75, 88, 62, 95, 80]
}

df = pd.DataFrame(data)

# Display the dataset
print("Student Marks:")
print(df)

# Calculate average marks
print("\nAverage Marks:", np.mean(df["Marks"]))

# Create a visualization
sns.barplot(data=df, x="Student", y="Marks")
plt.title("Student Marks Analysis")
plt.show()
