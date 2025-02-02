import json

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
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
        if isinstance(entry, dict):  # Ensure entry is a dictionary
            string_list_data = entry.get("string_list_data", [])
            for item in string_list_data:
                if isinstance(item, dict):  # Ensure each item is a dictionary
                    username = item.get("value")
                    if username:
                        usernames.append(username)
    return usernames

def find_unfollowed_followers(followings_file, followers_file):
    """
    Identify followers that you didn't follow back.
    """
    followings_data = load_json(followings_file)
    followers_data = load_json(followers_file)

    # Extract usernames from the JSON data
    followings = extract_usernames(followings_data, root_key="relationships_following")
    followers = extract_usernames(followers_data)

    # Find followers not in followings
    not_followed_back = [user for user in followers if user not in followings]

    # Print results
    print("\nFollowers you didn't follow back:")
    if not_followed_back:
        for user in not_followed_back:
            print(user)
    else:
        print("You follow back all your followers!")

if __name__ == "__main__":
    # Replace these with the paths to your JSON files
    followings_file = "following.json"  # Path to your followings JSON file
    followers_file = "followers.json"  # Path to your followers JSON file

    find_unfollowed_followers(followings_file, followers_file)
