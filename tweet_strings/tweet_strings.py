def string_to_tweet(in_string):
    """
    Takes an input string and if it is above 140 characters, truncate it to the nearest word under the limit.
    Appends a URL

    Args:
        in_string: A string

    Returns:
        A string with the url suffix appended

    """

    max_length = 140 - 24
    suffix = '...'
    url = 'https://ocpython.com'

    if len(in_string) >= 140:
        truncate = in_string[:max_length].rsplit(' ', 1)[0]
        tweet = '{}{} {}'.format(truncate, suffix, url)

    else:
        tweet = '{} {}'.format(in_string, url)

    return tweet
