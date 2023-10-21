from typing import Iterable


class CountVectorizer:
    """
    Класс для работы с терм-документными матрицами.

    Attributes
    ----------
    _raw: None or list[list[str]]
        Предобработанные строки из Iterable-объекта, приведенные к нижнему
        регистру, разделенные на слова и преобразованные к виду списка.
        При инициализации инстанса класса переменная равна значению None.
        Атрибут приватный, не предполагает обращения к нему вне класса.
    _vocabulary: None or dict
        Словарь из слов, которые встретились в поданных на вход строках.
        В качестве ключа - уникальное слово из строк, в качестве значения -
        индекс этого слова.
        При инициализации инстанса класса переменная равна значению None.
        Атрибут приватный, не предполагает обращения к нему вне класса.
    _processed: None or list[list[int]]
        Приведенные к векторному виду строки в виде списков размерности
        длины словаря, где по индексу слова из словаря указано количество
        повторений слов в данной строке.
        При инициализации инстанса класса переменная равна значению None.
        Атрибут приватный, не предполагает обращения к нему вне класса.

    Methods
    -------
    fit_transform(corpus):
        Преобразование к виду терм-документной матрицы. При каждом
        новом вызове метода, значения атрибутов инстанса обновляются, подобно
        тому, как это сделано в методе библиотеки scikit-learn.

    get_feature_names():
        Вывод списка из всех значений терм-документной матрицы (т. е., все
        слова, которые встретились при обработке).

    string_preprocessing(string_to_preprocess):
        Преобразование строки для формирования _raw. Приводит строку
        к нижнему регистру, удаляет из строки специальные символ и trailing
        spaces, преобразует строку к списку из слов. Проверят, что объект на
        входе - строка.

    get_features_vocabulary():
        Составление словаря из встретившихся слов на основе _raw.
        В качестве ключа - уникальное слово, в качестве значения -
        индекс слова.
    """
    def __init__(self) -> None:
        self._raw = None
        self._vocabulary = None
        self._processed = None

    def fit_transform(self, corpus: Iterable) -> list[list[int]]:
        """
        Метод для преобразования к виду терм-документной матрицы. Каждый
        корректный вызов метода переинициализирует атрибуты _raw, _vocabulary,
        _processed.

        Parameters
        ----------
        corpus: Iterable
            Iterable-объект для приведения к виду терм-документной матрицы.
            Если в качестве объекта на вход идет строка - каждый символ
            считается за уникальную строку.

        Returns
        -------
        list[list[int]]
            Список из списков-векторов, в которых каждый вектор - строка из
            Iterable-объекта. Каждый вектор имеет размерность количества
            встретившихся уникальных слов, а для каждого индекса уникального
            слова указано количество его повторений в строке.
        """
        if not isinstance(corpus, Iterable):
            raise ValueError

        if isinstance(corpus, str):
            # Удаление пробелов, если Iterable-объекта - единственная строка.
            # Позволит как отловить случай, когда объект - набор из пробелов,
            # так и работать со строкой как с 'набором из строк'
            corpus = corpus.replace(' ', '')

        raw = []
        for item in corpus:
            # Использование strip() поможет отловить случай, когда в
            # Iterable-объекте одна из строк состоит полностью из пробелов
            if isinstance(item, str) and len(item.strip()) > 0:
                raw.append(self.string_preprocessing(item))
            else:
                raise ValueError
        # Если не было ошибок во входном объекте, то можно реинициализировать
        # значения атрибута
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
        """
        Метод для получения списка уникальных слов из Iterable-объекта.

        Returns
        -------
        list
            Список из уникальных слов, полученный на основе ключей словаря,
            состоящего из встретившихся слов.
        """
        return list(self._vocabulary.keys())

    @staticmethod
    def string_preprocessing(string_to_preprocess: str) -> list:
        """
        Метод для преобразования строки к нижнему регистру, удаления
        специальных символов и trailing spaces. Преобразованная строка
        возвращается в виде списка из слов. Метод является статическим
        и может быть вызван для любой строки без создания инстанса.

        Parameters
        ----------
        string_to_preprocess: str
            Строка для преобразования.

        Returns
        -------
        list
            Список из слов для преобразованной строки.
        """
        if isinstance(string_to_preprocess, str):
            # Удаление специальных символов и приведение к нижнему регистру:
            # оставшийся символ или буква, или число, или пробел.
            string_to_preprocess = ''.join(
                ch for ch in string_to_preprocess.lower()
                if ch.isalnum() or ch == ' '
            ).strip().split(' ')
            return string_to_preprocess
        else:
            raise ValueError

    def get_features_vocabulary(self) -> dict:
        """
        Метод для получения словаря из встретившихся в Iterable-объекте слов.
        В качестве ключа - уникальное слово, в качестве значения - индекс этого
        слова.

        Returns
        -------
        dict
            Словарь из уникальных слов вида уникальное слово-индекс.
        """
        vocabulary = {}
        for raw_str in self._raw:
            for word in raw_str:
                if word not in vocabulary:
                    vocabulary[word] = len(vocabulary)
        return vocabulary
