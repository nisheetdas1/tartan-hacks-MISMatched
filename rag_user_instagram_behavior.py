import csv
import random
from datetime import datetime, timedelta

# Define Instagram scrolling behaviors
behaviors = [
    "Doomscrolling", "Infinite Scroll Engagement", "Time Distortion", "Content Skimming",
    "Focused Search", "Random Exploration", "Addictive Scrolling", "Zombie Scrolling Syndrome",
    "Variable Reward Seeking", "FOMO (Fear of Missing Out)", "Social Comparison",
    "Seamless Scrolling", "Algorithmic Feed Interaction", "Attention Retention",
    "Quick Content Consumption", "Emotional Impact Scrolling"
]

# Generate 100 entries
data = []
for i in range(500):
    user_id = f"User_{i+1:03d}"
    behavior = random.choice(behaviors)
    timestamp = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    data.append([user_id, behavior, timestamp.strftime('%Y-%m-%d %H:%M:%S')])

# Write to CSV
filename = 'instagram_scroll_behaviors.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User ID", "Behavior", "Timestamp"])
    writer.writerows(data)

print(f"CSV file '{filename}' has been created.")
