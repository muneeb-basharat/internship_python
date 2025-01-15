import requests
import random

# Use a different word list URL if the previous one is invalid
url = 'http://www.ibiblio.org/webster/'  # alternative URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    text = response.text

    # Split the text into individual words
    individual_words = text.split()

    # Generate a random index within the valid range
    random_number = random.randint(0, len(individual_words) - 1)

    # Select a random word from the list using the random index
    random_word = individual_words[random_number]

    # Create a username by concatenating the random word and the random number
    username = random_word + str(random_number)

    # Print the generated username
    print(f"Generated username: {username}")
else:
    print(f"Failed to retrieve the word list. Status code: {response.status_code}")
