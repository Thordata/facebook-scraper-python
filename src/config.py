# src/config.py

# Spider ID Configuration (Verified from Thordata Dashboard)
SPIDER_CONFIG = {
    # ========================================
    # 1. Facebook Posts Scraper
    # ========================================
    "post_by_posts_url": {
        "id": "facebook_post_by-posts-url",
        "name": "facebook.com",
        "desc": "Get Facebook post details by posts URL",
        "input_keys": ["url"],
    },

    # ========================================
    # 2. Facebook Events Scraper
    # ========================================
    "event_by_eventlist_url": {
        "id": "facebook_event_by-eventlist-url",
        "name": "facebook.com",
        "desc": "Get Facebook events by event list URL",
        "input_keys": ["url", "upcoming_events_only"],
    },
    "event_by_search_url": {
        "id": "facebook_event_by-search-url",
        "name": "facebook.com",
        "desc": "Get Facebook events by search URL",
        "input_keys": ["url"],
    },
    "event_by_events_url": {
        "id": "facebook_event_by-events-url",
        "name": "facebook.com",
        "desc": "Get Facebook events by events URL",
        "input_keys": ["url"],
    },

    # ========================================
    # 3. Facebook Profile Scraper
    # ========================================
    "profile_by_profiles_url": {
        "id": "facebook_profile_by-profiles-url",
        "name": "facebook.com",
        "desc": "Get Facebook profile information by profiles URL",
        "input_keys": ["url"],
    },

    # ========================================
    # 4. Facebook Post Comments Scraper
    # ========================================
    "comment_by_comments_url": {
        "id": "facebook_comment_by-comments-url",
        "name": "facebook.com",
        "desc": "Get Facebook post comments by comments URL",
        "input_keys": ["url", "get_all_replies", "limit_records", "comments_sort"],
    },
}

DEFAULT_TIMEOUT = 600
POLL_INTERVAL = 3
