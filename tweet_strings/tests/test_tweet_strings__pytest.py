from tweet_strings.tweet_strings import string_to_tweet

import pytest
import random
import string


@pytest.fixture
def big_words():
    return "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis pa"


class TestStringToTweet:

    def test_correct_tweet_length(self, big_words):
        output = string_to_tweet(big_words)

        assert len(output) <= 140

    def test_truncate_does_not_end_mid_word(self):
        # Shouldn't end in 183

        kepi = "The kepi was formerly the most common headgear in the French Army. Its predecessor originally appeared " \
               "during the 1830s, in the course of the initial stages of the occupation of Algeria, as a series of " \
               "various lightweight cane-framed cloth undress caps called casquette d'Afrique."

        output = string_to_tweet(kepi)

        assert output.endswith('183', 116) is False

    def test_appends_suffix(self, big_words):
        output = string_to_tweet(big_words)

        assert output.endswith('... https://ocpython.com')

    def test_continuous_string(self, big_words):
        rand_string = ''.join(random.choice(string.ascii_letters) for n in range(151))
        output = string_to_tweet(rand_string)

        assert len(output) == 140
