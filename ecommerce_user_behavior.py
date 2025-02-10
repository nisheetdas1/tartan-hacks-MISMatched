import csv
import random
from datetime import datetime, timedelta

# Define e-commerce behaviors
behaviors = [
    "Cart Abandonment", "Product Comparison", "Impulse Buying", "Wishlist Addition",
    "Price Sensitivity", "Loyalty Program Usage", "Coupon Hunting",
    "Flash Sale Participation", "Browsing Without Purchase", "Repeat Purchase",
    "Product Review Reading", "Checkout Completion", "Search Query Refinement",
    "Personalized Recommendation Interaction", "Mobile App Browsing",
    "Desktop Browsing", "Social Media Ad Clickthrough",
    "Email Campaign Engagement", "Subscription Box Signup"
]

# Generate 100 entries
data = []
for i in range(500):
    user_id = f"User_{i+1:03d}"
    behavior = random.choice(behaviors)
    timestamp = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    data.append([user_id, behavior, timestamp.strftime('%Y-%m-%d %H:%M:%S')])

# Write to CSV
filename = 'ecommerce_behaviors.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User ID", "Behavior", "Timestamp"])
    writer.writerows(data)

print(f"CSV file '{filename}' has been created.")
