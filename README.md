# insta_deck
like tweet deck, but for instagram

## usage
1. install the dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip && pip3 install -r requirements.txt
```
2. add your instagram account info to a file called `env.json` in the following format
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
3. export a csv file of all the accounts you follow
```
python scripts/export_accounts.py
```
4. upload the csv of followed accounts to notion and add a category label to each
5. export the categorized account info from notion as a csv and move it to the `uploads` folder in a file named `categorized_accounts.csv`
6. add info for additional instagram accounts to the `env.json` file in the following format. `FOLLOW_CATEGORIES` should use the notion categories you applied in step 4, specifying "+" to start following accounts in a category or "-" to unfollow accounts in a category
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
7. follow (and unfollow) accounts in the categories you specified above
```
python scripts/follow_accounts.py
```
8. start using your insta deck 😎
