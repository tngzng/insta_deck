import time
import csv
import logging
from typing import Dict, Any, List

from config import config
from instagram import MyClient


def check_sign(category: str) -> bool:
    sign = category[:1]
    if sign == "+":
        return True
    if sign == "-":
        return False
    else:
        raise Exception(f"categories to follow must begin with '+' or '-'")


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
            web_api_func(account["instagram_id"])
            time.sleep(0.01)


def import_accounts() -> Dict[str, List[Dict[str, Any]]]:
    FILEPATH = "uploads/categorized_accounts.csv"
    with open(FILEPATH, "r", encoding="utf-8-sig") as f:
        accounts = [row for row in csv.DictReader(f, skipinitialspace=True)]

    ### temp
    FILEPATH = "downloads/followed_accounts.csv"
    with open(FILEPATH, "r", encoding="utf-8-sig") as f:
        accounts_with_ids = [row for row in csv.DictReader(f, skipinitialspace=True)]

    for account in accounts:
        matching_account = next(
            (a for a in accounts_with_ids if a["username"] == account["username"]), {}
        )
        account["instagram_id"] = matching_account.get("instagram_id")

    account = [a for a in accounts if a["instagram_id"]]
    ### end temp

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
