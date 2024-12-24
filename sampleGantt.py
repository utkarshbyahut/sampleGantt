import pandas as pd
import matplotlib.pyplot as plt

# Define the phases and tasks
tasks = [
    {"Task": "Set up Xcode project and main app structure", "Start": "2024-12-25", "End": "2024-12-26"},
    {"Task": "Create app UI in SwiftUI", "Start": "2024-12-27", "End": "2024-12-28"},
    {"Task": "Implement local storage for offline tips", "Start": "2024-12-29", "End": "2024-12-30"},
    {"Task": "Research and integrate Weather API", "Start": "2024-12-31", "End": "2024-12-31"},
    {"Task": "Build basic home screen widget using WidgetKit", "Start": "2025-01-01", "End": "2025-01-02"},
    {"Task": "Enhance widget with dynamic timelines", "Start": "2025-01-03", "End": "2025-01-04"},
    {"Task": "Set up daily notifications", "Start": "2025-01-05", "End": "2025-01-06"},
    {"Task": "Test app and widget functionality", "Start": "2025-01-07", "End": "2025-01-07"},
    {"Task": "Add customization features", "Start": "2025-01-08", "End": "2025-01-09"},
    {"Task": "Implement fallback tips for offline usage", "Start": "2025-01-10", "End": "2025-01-11"},
    {"Task": "Test thoroughly on different iOS versions", "Start": "2025-01-12", "End": "2025-01-13"},
    {"Task": "Deploy on TestFlight", "Start": "2025-01-14", "End": "2025-01-14"},
]

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Convert Start and End to datetime
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["Duration"] = (df["End"] - df["Start"]).dt.days + 1

# Create Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))
for i, task in enumerate(df.itertuples()):
    ax.barh(task.Task, task.Duration, left=task.Start, color="skyblue", edgecolor="black")
    
# Format chart
ax.set_xlabel("Date")
ax.set_ylabel("Tasks")
ax.xaxis_date()
plt.title("Energy-Saving Tips App Development Gantt Chart")
plt.tight_layout()

# Show the chart
plt.show()
