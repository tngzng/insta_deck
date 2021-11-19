# insta_deck
like [tweet deck](https://tweetdeck.twitter.com/), but for instagram

## about 
i began dreading my instagram feed. it became an overwhelming stream of content that juxtaposed cute animals, influencer thirst traps, engagement announcements from acquaintances i could barely remember, and a highlighted selection of the worst news of the day. i was also terrified of posting. with so many glossy celelbrities in their feeds, why would my followers care about a mundane update from my mundane life? the app became unusable for me, even as i understood it's power to maintain social connection, and to provide a lens through which i could refract myself into the world.

i realized i was missing context — the ability to pick and choose what kind of content i wanted to engage with and when. i wanted an experience like [tweet deck](https://tweetdeck.twitter.com/) for instagram. i wanted to be able to categorize the accounts i followed (art, lifestyle, activism, entertainment) and to engage with each feed on my own terms. so i made this — a collection of python scripts and a notion template that i used to turn my monolithic feed into seven distinct accounts i can easily switch between on instagram's mobile app. 

## prerequisites 
to make your own insta deck, you'll need:
1. basic familiarity running scripts in terminal 
2. a free notion account 

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
4. duplicate [this template](https://www.notion.so/tngzng/5756d62703454f519107423dafbe0925?v=f3d0284f90ff4c53af4d1c7ac420fcbf) in notion and [import](https://www.notion.so/Import-data-into-Notion-18c37b470e8941789548b68049af750b) the csv of followed accounts to notion 
5. categorize the accounts by dragging them under the category header that fits best. (you can make your own categories too!)
![notion board](docs/notion-template.png)
7. export the categorized account info from notion in the ["Markdown & CSV"](https://www.notion.so/help/export-your-content) format and move it to the `uploads` folder in a file named `categorized_accounts.csv`
8. add info for additional instagram accounts to the `env.json` file in the following format. `FOLLOW_CATEGORIES` should use the notion categories you applied in step 5, specifying "+" to start following accounts in a category or "-" to unfollow accounts in a category
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
7. follow (and unfollow) accounts in the categories you specified above (this may take some time to avoid rate-limiting from instagram)
```
python scripts/follow_accounts.py
```
8. log into your new accounts to start using your insta deck 😎
![screenshot](docs/insta-deck-wide.png)
