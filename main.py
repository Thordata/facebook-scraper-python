import argparse
import json
import os
import sys
import time
from typing import Any

# Add project root to Python path to ensure src module is found
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv

from src.scraper import FacebookScraper

load_dotenv()


def _now_ts() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def save_json(data: Any, name: str) -> str:
    os.makedirs("output", exist_ok=True)
    path = f"output/{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved to {path}")
    return path


def save_error(data: Any, name: str) -> str:
    os.makedirs("output", exist_ok=True)
    path = f"output/error_{name}_{_now_ts()}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved error to {path}")
    return path


def save_result(data: Any, name: str) -> None:
    if isinstance(data, dict) and data.get("error"):
        save_error(data, name)
        raise SystemExit(data.get("error"))
    save_json(data, name)


COMMENTS_SORT_CHOICES = [
    "Most Relevent",
    "Newest",
    "All comments",
]


def main():
    parser = argparse.ArgumentParser(description="Facebook scraper powered by Thordata")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # ==========================================================
    # 1) Facebook Posts Scraper
    # ==========================================================
    post = sub.add_parser("post", help="Facebook Posts Scraper")
    post.add_argument("url", help="Facebook post URL")

    # ==========================================================
    # 2) Facebook Events Scraper
    # ==========================================================
    event = sub.add_parser("event", help="Facebook Events Scraper")
    event_sub = event.add_subparsers(dest="event_cmd", required=True)

    e_eventlist = event_sub.add_parser("eventlist", help="facebook_event_by-eventlist-url")
    e_eventlist.add_argument("url", help="Event list URL")
    e_eventlist.add_argument("--upcoming-events-only", default=None, help="Optional upcoming_events_only (true/false)")

    e_search = event_sub.add_parser("search", help="facebook_event_by-search-url")
    e_search.add_argument("url", nargs="+", help="Search URL(s) - can provide multiple URLs")

    e_events = event_sub.add_parser("events", help="facebook_event_by-events-url")
    e_events.add_argument("url", nargs="+", help="Events URL(s) - can provide multiple URLs")

    # ==========================================================
    # 3) Facebook Profile Scraper
    # ==========================================================
    profile = sub.add_parser("profile", help="Facebook Profile Scraper")
    profile.add_argument("url", help="Facebook profile URL")

    # ==========================================================
    # 4) Facebook Post Comments Scraper
    # ==========================================================
    comment = sub.add_parser("comment", help="Facebook Post Comments Scraper")
    comment.add_argument("url", help="Facebook post comments URL")
    comment.add_argument("--get-all-replies", default=None, help="Optional get_all_replies (True/False)")
    comment.add_argument("--limit-records", default=None, help="Optional limit_records (number)")
    comment.add_argument("--comments-sort", choices=COMMENTS_SORT_CHOICES, default=None, help="Optional comments_sort")

    args = parser.parse_args()
    bot = FacebookScraper()

    if args.cmd == "post":
        save_result(bot.post_by_posts_url({"url": args.url}), "post_by_posts_url")

    elif args.cmd == "event":
        if args.event_cmd == "eventlist":
            params = {"url": args.url}
            if args.upcoming_events_only:
                params["upcoming_events_only"] = args.upcoming_events_only
            save_result(bot.event_by_eventlist_url(params), "event_by_eventlist_url")
        elif args.event_cmd == "search":
            # Support multiple URLs
            urls = args.url if isinstance(args.url, list) else [args.url]
            params_list = [{"url": url} for url in urls]
            save_result(bot.event_by_search_url(params_list), "event_by_search_url")
        elif args.event_cmd == "events":
            # Support multiple URLs
            urls = args.url if isinstance(args.url, list) else [args.url]
            params_list = [{"url": url} for url in urls]
            save_result(bot.event_by_events_url(params_list), "event_by_events_url")

    elif args.cmd == "profile":
        save_result(bot.profile_by_profiles_url({"url": args.url}), "profile_by_profiles_url")

    elif args.cmd == "comment":
        params = {"url": args.url}
        if args.get_all_replies:
            params["get_all_replies"] = args.get_all_replies
        if args.limit_records:
            params["limit_records"] = args.limit_records
        if args.comments_sort:
            params["comments_sort"] = args.comments_sort
        save_result(bot.comment_by_comments_url(params), "comment_by_comments_url")


if __name__ == "__main__":
    main()
