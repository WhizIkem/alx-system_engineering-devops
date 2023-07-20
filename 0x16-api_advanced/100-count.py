#!/usr/bin/python3

import requests

""" Count it! """
def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursive function to count words in hot articles on Reddit"""

    # Base case: if word_list is empty, print the results in descending order
    if not word_list:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    # If word_list is not empty, take the first word and remove it from the list
    current_word = word_list[0].lower()
    remaining_words = word_list[1:]

    # If the current_word is empty or None, stop the recursion for this word
    if not current_word:
        count_words(subreddit, remaining_words, after, word_count)
        return

    # Fetch hot articles from Reddit using the provided subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My User Agent"}  # Add your user agent here
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If the subreddit is invalid or no more articles to fetch, stop the recursion
    if response.status_code != 200:
        return

    # Get the data from the API response
    data = response.json().get("data")
    if not data:
        return

    # Extract the titles from the data and count the occurrences of the current_word
    articles = data.get("children", [])
    for article in articles:
        title = article.get("data", {}).get("title", "").lower()
        word_count[current_word] = word_count.get(current_word, 0) + title.count(current_word)

    # Recursively call the function with the remaining words and continue fetching articles
    count_words(subreddit, remaining_words, data.get("after"), word_count)

