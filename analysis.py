import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load CSV data
file_path = r"C:\Users\Suryansh Singh\OneDrive\Attachments\Desktop\student-performance-analysis\data\students.csv"
data = pd.read_csv(file_path)

# STEP 2: Basic Analysis
print("Average Marks:")
print(data[["Maths", "Science", "English"]].mean())

print("\nHighest Marks:")
print(data[["Maths", "Science", "English"]].max())

print("\nLowest Marks:")
print(data[["Maths", "Science", "English"]].min())

# STEP 3: Visualization (Bar Chart)
data.set_index("Name")[["Maths", "Science", "English"]].plot(kind="bar")

plt.title("Student Performance Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()