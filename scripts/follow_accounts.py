import time
import csv
import logging
from typing import Dict, Any, List, Set

from config import config
from instagram import MyClient, paginate_all, format_account


def check_sign(category: str) -> bool:
    sign = category[:1]
    if sign == "+":
        return True
    if sign == "-":
        return False
    else:
        raise Exception(f"categories to follow must begin with '+' or '-'")


def is_action_needed(
    follow: bool, account_id: int, followed_accounts: Set[int]
) -> bool:
    if not account_id:
        return False
    elif follow & (account_id in followed_accounts):
        return False
    elif not follow & (account_id not in followed_accounts):
        return False
    else:
        return True


def follow_accounts(
    username: str,
    password: str,
    follow_categories: List[str],
    accounts: Dict[str, List[Dict[str, Any]]],
) -> None:
    authed_web_api = MyClient(
        auto_patch=True,
        authenticate=True,
        username=username,
        password=password,
    )

    followed_accounts = [
        format_account(account)
        for account in paginate_all(
            authed_web_api.user_following, authed_web_api, "edge_follow"
        )
    ]
    followed_account_ids = {a["instagram_id"] for a in followed_accounts}

    for category in follow_categories:
        follow = check_sign(category)
        category = category[1:]
        category_accounts = accounts[category]
        prefix = "" if follow else "un"
        logging.info(f"{prefix}following {category} accounts from {username}")

        web_api_func = (
            authed_web_api.friendships_create
            if follow
            else authed_web_api.friendships_destroy
        )
        for account in category_accounts:
            action_needed = is_action_needed(
                follow, account["instagram_id"], followed_account_ids
            )
            if action_needed:
                logging.info(f"{prefix}following {account['username']}...")
                web_api_func(account["instagram_id"])
                time.sleep(60)
            else:
                logging.info(
                    f"already {prefix}follow {account['username']}, skipping..."
                )


def import_accounts() -> Dict[str, List[Dict[str, Any]]]:
    FILEPATH = "uploads/categorized_accounts.csv"
    with open(FILEPATH, "r", encoding="utf-8-sig") as f:
        accounts = [row for row in csv.DictReader(f, skipinitialspace=True)]

    categories = {account["category"] for account in accounts}
    categorized_accounts = {category: [] for category in categories}

    for account in accounts:
        category = account["category"]
        categorized_accounts[category].append(account)

    return categorized_accounts


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    my_accounts = config.get("ACCOUNTS", [])
    categorized_accounts = import_accounts()
    for account in my_accounts:
        username = account.get("INSTAGRAM_USER")
        password = account.get("INSTAGRAM_PASSWORD")
        follow_categories = account.get("FOLLOW_CATEGORIES")
        if username and password and follow_categories:
            follow_accounts(username, password, follow_categories, categorized_accounts)
        else:
            logging.error(
                f"env.json does not contain the expected account info for: {account}"
            )
