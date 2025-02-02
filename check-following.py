import json

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Preview the first few entries
            #print(f"Loaded data from {file_path}: {data[:2] if isinstance(data, list) else list(data.keys())}")
            return data
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {file_path}")
        return []

def extract_usernames(data, root_key=None):
    """
    Extract usernames from the nested JSON structure.
    Supports an optional root_key for accessing data.
    """
    usernames = []
    if root_key:
        data = data.get(root_key, [])
    for entry in data:
        if isinstance(entry, dict):
            string_list_data = entry.get("string_list_data", [])
            for item in string_list_data:
                if isinstance(item, dict):
                    username = item.get("value")
                    if username:
                        usernames.append(username)
    return usernames

def compare_followings_and_followers(followings_file, followers_file):
    """
    Compare the lists of followings and followers.
    Identify followings who are not in the followers list.
    """
    followings_data = load_json(followings_file)
    followers_data = load_json(followers_file)

    followings = extract_usernames(followings_data, root_key="relationships_following")
    followers = extract_usernames(followers_data)

    not_following_back = [user for user in followings if user not in followers]

    print("\nFollowings not following you back:")
    if not_following_back:
        for user in not_following_back:
            print(user)
    else:
        print("Everyone you follow also follows you back!")

if __name__ == "__main__":
    followings_file = "following.json"
    followers_file = "followers.json"

    compare_followings_and_followers(followings_file, followers_file)
