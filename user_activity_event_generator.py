import csv
import random
from datetime import datetime, timedelta
import uuid

# Enhanced category mapping
category_subcategory = {
    "Beauty": ["Skincare", "Makeup", "Haircare", "Fragrance"],
    "Sports": ["Football", "Cricket", "Basketball", "Tennis"],
    "Lifestyle": ["Fashion", "Wellness", "Home", "Travel"],
    "Outdoor": ["Hiking", "Camping", "Cycling", "Swimming"],
    "Food": ["Restaurant", "Cooking", "Healthy", "Desserts"],
    "Movie": ["Action", "Comedy", "Drama", "Horror"],
    "Adventure": ["Trekking", "Skydiving", "Surfing", "Climbing"]
}

# User preferences mapping
user_preferences = {
    "550e8400-e29b-41d4-a716-446655440000": {  # Sarah
        "primary": ["Beauty", "Lifestyle"],
        "secondary": ["Food", "Movie"]
    },
    "91a3b7c8-d4e5-4f6g-8h9i-123456789abc": {  # Michael
        "primary": ["Sports", "Adventure"],
        "secondary": ["Outdoor", "Food"]
    },
    "2f3e4d5c-6b7a-8c9d-0e1f-456789abcdef": {  # Emma
        "primary": ["Lifestyle", "Beauty"],
        "secondary": ["Food", "Movie"]
    },
    "3g4h5i6j-7k8l-9m0n-1o2p-789abcdef012": {  # David
        "primary": ["Outdoor", "Sports"],
        "secondary": ["Adventure", "Food"]
    },
    "4j5k6l7m-8n9o-0p1q-2r3s-abcdef012345": {  # Lisa
        "primary": ["Food", "Lifestyle"],
        "secondary": ["Beauty", "Movie"]
    }
}

event_types = ["like_post", "unlike_post", "ad_click", "story_view", "reel_view", "profile_view", "bookmark_post"]
sources = ["feed", "explore", "profile", "search"]
content_types = ["photo", "video", "carousel"]


def get_user_relevant_category(user_id):
    """Get a category based on user preferences with higher chance of primary interests"""
    prefs = user_preferences[user_id]
    if random.random() < 0.7:  # 70% chance of primary interest
        return random.choice(prefs["primary"])
    return random.choice(prefs["secondary"])


def generate_events(num_events=1000):
    events = []
    base_time = datetime(2025, 2, 8, 8, 0, 0)  # Starting at 8 AM

    for i in range(num_events):
        event_time = base_time + timedelta(minutes=random.randint(0, 960))  # Spread over 16 hours
        user_id = random.choice(list(user_preferences.keys()))
        event_type = random.choice(event_types)

        # Select category based on user preferences
        category = get_user_relevant_category(user_id)
        sub_category = random.choice(category_subcategory[category])

        # Base event structure
        event = {
            'event_type': event_type,
            'timestamp': event_time.isoformat() + 'Z',
            'user_id': user_id,
            'post_id': '',
            'story_id': '',
            'reel_id': '',
            'ad_id': '',
            'content_type': random.choice(content_types),
            'category': category,
            'sub_category': sub_category,
            'author_id': f"creator_{random.randint(1, 100)}",
            'engagement_time': random.randint(2, 10),
            'session_duration': '',
            'like_duration': '',
            'view_duration': '',
            'view_percentage': '',
            'source': random.choice(sources),
            'placement': '',
            'destination': '',
            'campaign_id': '',
            'impression_id': '',
            'creative_type': '',
            'reason_category': '',
            'share_type': '',
            'platform': '',
            'recipient_count': '',
            'collection_id': '',
            'sound_on': '',
            'position': '',
            'completion_type': '',
            'comment_id': '',
            'comment_type': '',
            'reply_to_comment_id': '',
            'text_length': '',
            'mentioned_users': ''
        }

        # Customize based on event type
        if event_type == 'ad_click':
            event['ad_id'] = f"ad_{i}"
            event['campaign_id'] = f"camp_{random.randint(1, 10)}"
            event['impression_id'] = f"imp_{i}"
            event['placement'] = random.choice(['feed', 'story', 'explore'])
            event['destination'] = random.choice(['shop', 'external_link', 'profile'])
            event['creative_type'] = random.choice([
                'product_showcase',
                'product_demo',
                'brand_story',
                'influencer_collab',
                'limited_time_offer'
            ])
            # Ad categories are more closely tied to user preferences
            if random.random() < 0.8:  # 80% chance of showing relevant ads
                event['category'] = random.choice(user_preferences[user_id]["primary"])
                event['sub_category'] = random.choice(category_subcategory[event['category']])

        elif event_type == 'like_post':
            event['post_id'] = f"post_{i}"

        elif event_type == 'unlike_post':
            event['post_id'] = f"post_{i}"
            event['like_duration'] = random.randint(300, 7200)
            # Unlike events more likely for non-preferred categories
            non_preferred = [cat for cat in category_subcategory.keys()
                             if cat not in user_preferences[user_id]["primary"]]
            event['category'] = random.choice(non_preferred)
            event['sub_category'] = random.choice(category_subcategory[event['category']])

        elif event_type == 'story_view':
            event['story_id'] = f"story_{i}"
            event['view_duration'] = random.randint(2, 15)
            event['view_percentage'] = random.randint(50, 100)
            event['sound_on'] = random.choice(['true', 'false'])

        elif event_type == 'reel_view':
            event['reel_id'] = f"reel_{i}"
            event['view_duration'] = random.randint(5, 30)
            event['view_percentage'] = random.randint(30, 100)
            event['sound_on'] = random.choice(['true', 'false'])
            event['completion_type'] = random.choice(['watched_full', 'skipped', 'scrolled_away'])

        elif event_type == 'profile_view':
            event['session_duration'] = random.randint(30, 300)

        elif event_type == 'bookmark_post':
            event['post_id'] = f"post_{i}"
            event['collection_id'] = f"collection_{event['category'].lower()}"

        events.append(event)

    # Sort events by timestamp
    events.sort(key=lambda x: x['timestamp'])
    return events


# Generate and write events to CSV
events = generate_events(1000)
with open('social_media_events.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=events[0].keys())
    writer.writeheader()
    writer.writerows(events)