import csv
import logging
from typing import Dict, Any

from config import config
from instagram import MyClient, paginate_all


def format_account(account: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "instagram_id": account["id"],
        "username": account["username"],
        "full_name": account["full_name"],
        "account_url": f"https://www.instagram.com/{account['username']}",
    }


def export_followed_accounts(username: str, password: str) -> None:
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
    logging.info(f"Found {len(followed_accounts)} followed accounts")

    FILEPATH = "downloads/followed_accounts.csv"
    headers = followed_accounts[0].keys()
    with open(FILEPATH, "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, headers)
        dict_writer.writeheader()
        dict_writer.writerows(followed_accounts)
    logging.info(f"Exported followed accounts to '{FILEPATH}'")


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main_account = next(
        (a for a in config.get("ACCOUNTS", []) if a.get("MAIN_ACCOUNT")), {}
    )
    username = main_account.get("INSTAGRAM_USER")
    password = main_account.get("INSTAGRAM_PASSWORD")
    if main_account and username and password:
        export_followed_accounts(username, password)
    else:
        logging.error(f"env.json does not contain the expected account info")
