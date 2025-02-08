import pandas as pd
import random
import uuid
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate dummy data
data = []
for _ in range(10000):
    user_id = str(uuid.uuid4())
    name = fake.name()
    gender = random.choice(['Male', 'Female', 'Other'])
    mobile_number = fake.phone_number()
    email_id = fake.email()
    avg_instagram_usage = round(random.uniform(0, 10), 2)  # hours per day

    data.append({
        'userId': user_id,
        'Name': name,
        'Gender': gender,
        'Mobile number': mobile_number,
        'email id': email_id,
        'average instagram usage per day': avg_instagram_usage
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('dummy_user_profiles.csv', index=False)
