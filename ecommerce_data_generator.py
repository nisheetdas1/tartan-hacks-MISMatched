import random
from datetime import datetime, timedelta
import csv

# User preferences (mapping from previous data)
users = {
    "550e8400-e29b-41d4-a716-446655440000": {  # Sarah (Female)
        "primary": ["Beauty"],
        "secondary": ["Fitness", "Fashion"]
    },
    "91a3b7c8-d4e5-4f6g-8h9i-123456789abc": {  # Michael (Male)
        "primary": ["Sports", "Fitness"],
        "secondary": [ "Adventure"]
    },
    "2f3e4d5c-6b7a-8c9d-0e1f-456789abcdef": {  # Emma (Female)
        "primary": ["Fashion", "Beauty"],
        "secondary": [ "Wellness"]
    },
    "3g4h5i6j-7k8l-9m0n-1o2p-789abcdef012": {  # David (Male)
        "primary": ["Sports", "Adventure"],
        "secondary": ["Fitness", "Fashion"]
    },
    "4j5k6l7m-8n9o-0p1q-2r3s-abcdef012345": {  # Lisa (Female)
        "primary": ["Beauty", "Fashion"],
        "secondary": ["Wellness"]
    }
}

# Product categories and subcategories
product_categories = {
    "Beauty": {
        "subcategories": ["Skincare", "Makeup", "Haircare", "Fragrance"],
        "products": {
            "Skincare": ["face-serum", "moisturizer", "face-wash", "toner"],
            "Makeup": ["lipstick", "foundation", "mascara", "eyeliner"],
            "Haircare": ["shampoo", "conditioner", "hair-oil", "hair-mask"],
            "Fragrance": ["perfume", "body-mist", "deodorant"]
        }
    },
    "Sports": {
        "subcategories": ["Equipment", "Apparel", "Accessories", "Footwear"],
        "products": {
            "Equipment": ["dumbbells", "yoga-mat", "resistance-bands", "cricket-bat"],
            "Apparel": ["sports-tshirt", "track-pants", "shorts", "jersey"],
            "Accessories": ["sports-bag", "wrist-band", "sports-bottle"],
            "Footwear": ["running-shoes", "training-shoes", "sports-sandals"]
        }
    },
    "Fashion": {
        "subcategories": ["Casual", "Formal", "Ethnic", "Accessories"],
        "products": {
            "Casual": ["jeans", "t-shirts", "dresses", "shorts"],
            "Formal": ["shirts", "trousers", "blazers", "formal-shoes"],
            "Ethnic": ["kurtas", "sarees", "lehengas"],
            "Accessories": ["bags", "belts", "scarves"]
        }
    },
    "Fitness": {
        "subcategories": ["Equipment", "Supplements", "Wearables"],
        "products": {
            "Equipment": ["treadmill", "exercise-bike", "weights", "bench"],
            "Supplements": ["protein-powder", "vitamins", "energy-drinks"],
            "Wearables": ["fitness-tracker", "smartwatch", "heart-rate-monitor"]
        }
    },
    "Adventure": {
        "subcategories": ["Adventure_Equipment", "Adventure_Wearables", "Adventure_sports"],
        "products": {
            "Adventure_Equipment": ["torch", "umbrella", "rope", "tent"],
            "Adventure_Wearables": ["mask", "boots", "helmet", "protection-guard"],
            "Adventure_sports": ["rock-climbing-boots", "skiing-trunks", "strong-sunscreen", "hunting-gun", "parachute"]
        }
    },
    "Wellness": {
        "subcategories": ["Wellness_Equipment", "Wellness_Wearables"],
        "products": {
            "Wellness_Equipment": ["yoga-mat", "stretch-bands"],
            "Wellness_Wearables": ["yoga-pants", "sports-bra"]
        }
    },
    "Lifestyle": {
        "subcategories": ["Lifestyle_Equipment", "Lifestyle_Wearables"],
        "products": {}
    }
}

# Traffic sources
sources = ["instagram_ad", "facebook_ad", "google_ad", "website_nav", "direct", "email", "social_media"]


def generate_product_id():
    return f"prod_{random.randint(1000, 9999)}"


def generate_sku_id(product_id):
    return f"{product_id}_sku_{random.randint(100, 999)}"


def get_user_relevant_category(user_id):
    prefs = users[user_id]
    if random.random() < 0.7:  # 70% chance of primary interest
        return random.choice(prefs["primary"])
    return random.choice(prefs["secondary"])


def generate_events(num_events=1000):
    events = []
    base_time = datetime(2025, 2, 8, 8, 0, 0)

    for i in range(num_events):
        event_time = base_time + timedelta(minutes=random.randint(0, 960))
        user_id = random.choice(list(users.keys()))

        # Determine event type with weighted probabilities
        event_weights = [
            ("home_page_view", 15),
            ("plp_page_view", 20),
            ("pdp_page_view", 25),
            ("search_page_view", 10),
            ("add_to_cart", 10),
            ("add_to_wishlist", 5),
            ("remove_from_cart", 3),
            ("remove_from_wishlist", 2),
            ("share_product_click", 2),
            ("checkout_initiated_item_level", 5),
            ("checkout_complete_item_level", 3)
        ]

        event_type = random.choices(
            [ew[0] for ew in event_weights],
            weights=[ew[1] for ew in event_weights]
        )[0]

        # Base event structure
        event = {
            "event_type": event_type,
            "timestamp": event_time.isoformat() + "Z",
            "userId": user_id,
            "pageType": "",
            "slug": "",
            "productId": "",
            "skuId": "",
            "quantity": "",
            "source": "",
            "category": "",
            "subcategory": "",
            "search_term": "",
            "results_count": ""
        }

        # Get relevant category based on user preferences
        category = get_user_relevant_category(user_id)

        if event_type == "home_page_view":
            event["pageType"] = "home_page"

        elif event_type == "plp_page_view":
            event["pageType"] = "plp"
            subcategory = random.choice(product_categories[category]["subcategories"])
            event["slug"] = random.choice(product_categories[category]["products"][subcategory])
            event["category"] = category
            event["subcategory"] = subcategory

        elif event_type == "pdp_page_view":
            event["pageType"] = "pdp"
            subcategory = random.choice(product_categories[category]["subcategories"])
            event["productId"] = generate_product_id()
            event["slug"] = random.choice(product_categories[category]["products"][subcategory])
            event["source"] = random.choice(sources)
            event["category"] = category
            event["subcategory"] = subcategory

        elif event_type == "search_page_view":
            event["pageType"] = "search"
            subcategory = random.choice(product_categories[category]["subcategories"])
            event["search_term"] = random.choice(product_categories[category]["products"][subcategory])
            event["results_count"] = random.randint(5, 50)

        else:  # Cart, wishlist, and checkout events
            event["productId"] = generate_product_id()
            event["skuId"] = generate_sku_id(event["productId"])
            event["quantity"] = random.randint(1, 3)
            event["source"] = random.choice(sources)
            subcategory = random.choice(product_categories[category]["subcategories"])
            event["category"] = category
            event["subcategory"] = subcategory

        events.append(event)

    # Sort events by timestamp
    events.sort(key=lambda x: x["timestamp"])
    return events


# Generate and write events to CSV
events = generate_events(1000)
with open('ecommerce_events_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=events[0].keys())
    writer.writeheader()
    writer.writerows(events)