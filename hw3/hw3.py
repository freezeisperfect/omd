from typing import Iterable


class CountVectorizer:
    def __init__(self) -> None:
        self._raw = None
        self._vocabulary = None
        self._processed = None

    def fit_transform(self, corpus: Iterable) -> list[list[int]]:
        if not isinstance(corpus, Iterable):
            raise ValueError

        if isinstance(corpus, str):
            corpus = corpus.replace(' ', '')

        raw = []
        for item in corpus:
            if isinstance(item, str) and len(item.strip()) > 0:
                raw.append(self.string_preprocessing(item))
            else:
                raise ValueError
        self._raw = raw
        self._vocabulary = self.get_features_vocabulary()

        processed = [[0 for _ in range(len(self._vocabulary))]
                     for _ in range(len(self._raw))]

        for idx_string, split_string in enumerate(self._raw):
            for word in split_string:
                processed[idx_string][self._vocabulary.get(word)] += 1

        self._processed = processed
        return self._processed

    def get_feature_names(self) -> list:
        return list(self._vocabulary.keys())

    @staticmethod
    def string_preprocessing(string_to_preprocess: str) -> list:
        if isinstance(string_to_preprocess, str):
            string_to_preprocess = ''.join(
                ch for ch in string_to_preprocess.lower()
                if ch.isalnum() or ch == ' '
            ).strip().split(' ')
            return string_to_preprocess
        else:
            raise ValueError

    def get_features_vocabulary(self) -> dict:
        vocabulary = {}
        for raw_str in self._raw:
            for word in raw_str:
                if word not in vocabulary:
                    vocabulary[word] = len(vocabulary)
        return vocabulary


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vec = CountVectorizer()
    count_matrix = vec.fit_transform(corpus)
    print(vec.get_feature_names())
    print(count_matrix)
