# Instagram Follow Checker

This repository contains two Python scripts to help you analyze your Instagram followings and followers:

1. `check-following.py`: Identifies users you follow who are not following you back.
2. `check-followback.py`: Identifies users who follow you but you are not following back.

## Usage

### Prerequisites

- Download your Instagram data from your account center.
- Extract the `following.json` and `followers.json` files from the downloaded data.
- Place the two files in the same directory as these scripts.

### Running the Scripts

#### Check Followings Not Following You Back

This script checks your Instagram following list to identify users who are not following you back.

```sh
python check-following.py
```

#### Check Followers You Didn't Follow Back

This script checks your Instagram followers list to identify users who follow you but you are not following back.

```sh
python check-followback.py
```

## How It Works

### `check-following.py`

1. **Load JSON Data**: The script loads the `following.json` and `followers.json` files.
2. **Extract Usernames**: It extracts the usernames from the JSON data.
3. **Compare Lists**: It compares the list of users you are following with the list of your followers.
4. **Identify Non-Followers**: It prints the list of users you follow who are not following you back.

### 

check-followback.py

1. **Load JSON Data**: The script loads the `following.json` and `followers.json` files.
2. **Extract Usernames**: It extracts the usernames from the JSON data.
3. **Compare Lists**: It compares the list of your followers with the list of users you are following.
4. **Identify Non-Followed**: It prints the list of users who follow you but you are not following back.

## Example Output

### `check-following.py`

```
Followings not following you back:
user1
user2
user3
...
```

If everyone you follow also follows you back, the script will print:

```
Everyone you follow also follows you back!
```

### 

check-followback.py



```
Followers you didn't follow back:
user1
user2
user3
...
```

If you follow back all your followers, the script will print:

```
You follow back all your followers!
```

## Author

Written by Jeff Steveanus
