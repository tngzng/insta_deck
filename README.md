# insta_deck
like tweet deck, but for instagram

## usage
1. install the dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip && pip3 install -r requirements.txt
```
2. add your instagram account info to env.json in the following format
```
{
    "ACCOUNTS": [
        {
            "INSTAGRAM_USER": "your-username",
            "INSTAGRAM_PASSWORD": "your-password",
            "MAIN_ACCOUNT": true
        }
    ]
}
```
3. export your followed accounts
```
python scripts/export_accounts.py
```
4. upload the followed accounts to notion and add a category label to each
5. export the categorized account info from notion as a csv and move it to the `uploads` folder in a file named "categorized_accounts.csv"
6. add info for additional instagram accounts to env.json in the following format. use the categories you applied in step 4 in the follow list, specifying "+" to start following accounts in the category or "-" to unfollow accounts in the category.
```
{
    "ACCOUNTS": [
        {
            "INSTAGRAM_USER": "your-username",
            "INSTAGRAM_PASSWORD": "your-password",
            "FOLLOW_CATEGORIES": [
                "-unfollow"
            ]
            "MAIN_ACCOUNT": true
        },
        {
            "INSTAGRAM_USER": "your-username",
            "INSTAGRAM_PASSWORD": "your-password",
            "FOLLOW_CATEGORIES": [
                "+close friends"
            ]
        }
    ]
}
```
7. follow (and unfollow) the accounts you specified above
```
python scripts/follow_accounts.py
```
8. start using your insta deck 😎