import requests


class Dictionary:
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/{}'

    def search(self, lookup):
        if ' ' in lookup:
            print('please enter a single word for lookup.\n')
        else:
            url = self.url.format(str(lookup))
            response = requests.get(url)
            response_body = response.json()
            if response.status_code == 200:
                try:
                    response_body = response_body[0]
                    meaning_of = response_body.get('word', '').capitalize()
                    word_contents = response_body.get('meanings', [])
                    part_of_speech = word_contents[0].get('partOfSpeech', '').capitalize()
                    definition = word_contents[0].get('definitions', [])[0].get('definition').capitalize()
                    print(meaning_of+'. ', part_of_speech+'. ', definition)

                except IndexError:
                    print('Try again after checking the input')
            else:
                print(response_body)


dictionary = Dictionary()
word = input('Word?\n')
dictionary.search(word)
