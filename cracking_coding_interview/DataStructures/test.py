import re
import unittest


# NER class, this change is made to increase the readibility of the code
# and reusability is also enhance while reducing the runtime memory otherwise
# all the methods and variables are in the memory whether the methods are used
# or not.
class NamedEntityRecognition:
    def __init__(self):
        """
        Construtor, Initialzing all the variables to
        reduce memory usage
        """
        # Buffer to store current named entity
        self.word_buffer = []
        self.token_reg = re.compile(r"([a-z]+)\s*(.*)$", re.I)
        self.uppercase_reg = re.compile(r"[A-Z][a-z]*$")

    def pop_token(self, text):
        """
        Take the first token off the beginning of text. If its first letter is
        capitalized, remember it in word buffer - we may have a named entity on our
        hands!!

        @return: Tuple (token, remaining_text). Token is None in case text is empty
        """

        token_match = self.token_reg.match(text)
        if token_match:
            token = token_match.group(1)
            if self.uppercase_reg.match(token):
                self.word_buffer.append(token)
            else:
                self.word_buffer = []
            return token, token_match.group(2)
        return None, text

    def has_named_entity(self):
        """
        Return a named entity, if we have assembled one in the current buffer.
        Returns None if we have to keep searching.
        """
        # print(self.word_buffer)
        if len(self.word_buffer) >= 2:
            named_entity = " ".join(self.word_buffer)
            self.word_buffer = []
            return named_entity


class NamedEntityTestCase(unittest.TestCase):
    # Now, this method can be used with other test cases as well
    # by simply providing the text.
    def __get_entities(self, text):
        """
        Takes the string as input and return the list of entities
        which matches the NER
        Returns emty if no entity matches
        """
        ner = NamedEntityRecognition()
        entities = set()
        while True:
            token, text = ner.pop_token(text)
            if not token:
                entity = ner.has_named_entity()
                if entity:
                    entities.add(entity)
                    break

                entity = ner.has_named_entity()
                if entity:
                    entities.add(entity)
        return entities

        # Now, this method can be used with other test cases as well
        # by simply providing the text.

    def __get_entities(self, text):
        """
        Takes the string as input and return the list of entities
        which matches the NER
        Returns emty if no entity matches
        """
        ner = NamedEntityRecognition()
        entities = set()
        while True:
            token, text = ner.pop_token(text)
            if not token:
                entity = ner.has_named_entity()
                if entity:
                    entities.add(entity)
                break

            entity = ner.has_named_entity()
            if entity:
                entities.add(entity)
        return entities

    def test_ner_extraction(self):
        text = "When we went to Los Angeles last year \
        we visited the Hollywood Sign"

        entities = self.__get_entities(text)
        self.assertEqual(set(["Los Angeles", "Hollywood Sign"]), entities)


if __name__ == "__main__":

    import sys

    # Test case names are passed in via sys.stdin, for scoring by remoteinterview.io

    for line in sys.stdin:
        test_name = line.rstrip()
        test_case = NamedEntityTestCase(test_name)
        runner = unittest.TextTestRunner()
        if runner.run(test_case).wasSuccessful():
            print("OK")
        else:
            print("Test {} failed!".format(test_name))
