from tweet_strings.tweet_strings import string_to_tweet

import unittest
import random
import string


class TestTweetStrings(unittest.TestCase):

    def setUp(self):
        # 151 characters
        self.big_words = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis pa"

    def test_correct_tweet_length(self):
        output = string_to_tweet(self.big_words)

        self.assertTrue(len(output) <= 140)

    def test_truncate_does_not_end_mid_word(self):
        # Shouldn't end in 183

        kepi = "The kepi was formerly the most common headgear in the French Army. Its predecessor originally appeared " \
               "during the 1830s, in the course of the initial stages of the occupation of Algeria, as a series of " \
               "various lightweight cane-framed cloth undress caps called casquette d'Afrique."

        output = string_to_tweet(kepi)

        self.assertFalse(output.endswith('183', 116))

    def test_appends_suffix(self):
        output = string_to_tweet(self.big_words)

        self.assertTrue(output.endswith('... https://ocpython.com'))

    def test_continuous_string(self):
        rand_string = ''.join(random.choice(string.ascii_letters) for n in range(151))
        output = string_to_tweet(rand_string)

        self.assertEquals(len(output), 140)


if __name__ == '__main__':
    unittest.main()
