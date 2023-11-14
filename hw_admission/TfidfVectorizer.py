from CountVectorizer import CountVectorizer
import math
import numpy as np


class TfidfTransformer:
    """
    Класс для получения преобразования TF-IDF.

    Attributes
    ----------
    _tfidf: None or list[list[float]]
        Результат TF-IDF преобразования.
        При инициализации инстанса класса переменная равна значению None.
        Атрибут приватный, не предполагает обращения к нему вне класса.

    Methods
    -------
    fit_transform(count_matrix)
        Выполнение TF-IDF преобразования. При каждом
        новом вызове метода, значения атрибутов инстанса обновляются.
    tf_transform(count_matrix)
        Выполнение TF преобразования. Метод является статическим.
    id_transform(count_matrix)
        Выполнение IDF преобразования. Метод является статическим.
    """
    def __init__(self) -> None:
        self._tfidf = None

    def fit_transform(self, count_matrix: list[list[int]]
                      ) -> list[list[float]]:
        """
        Метод для выполнения TF-IDF преобразования. Каждый корректный вызов
        метода переинициализирует атрибут _tfidf.

        Parameters
        ----------
        count_matrix: list[list[int]]
            Терм-документная матрица, являющаяся результатом работы метода
            fit_transform() класса CountVectorizer.

        Returns
        -------
        list[list[float]]
            Результат TF-IDF преобразования.
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.id_transform(count_matrix)
        self._tfidf = np.round(np.array(tf_matrix) * np.array(idf_matrix), 3)
        return self._tfidf

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Метод для выполнения TF преобразования. Метод является статическим
        и может быть вызван без создания инстанса.

        Parameters
        ----------
        count_matrix: list[list[int]]
            Терм-документная матрица, являющаяся результатом работы метода
            fit_transform() класса CountVectorizer.

        Returns
        -------
        list[list[float]]
            Результат TF преобразования.
        """
        if not all(isinstance(x, list) for x in count_matrix):
            raise ValueError
        for vector in count_matrix:
            if not all(isinstance(x, int) for x in vector):
                raise ValueError

        result = []
        for vector in count_matrix:
            freq_vector = []
            for repeat_times in vector:
                freq_vector.append(round(repeat_times / sum(vector), 3))
            result.append(freq_vector)

        return result

    @staticmethod
    def id_transform(count_matrix: list[list[int]]) -> list[float]:
        """
        Метод для выполнения IDF преобразования. Метод является статическим
        и может быть вызван без создания инстанса.

        Parameters
        ----------
        count_matrix: list[list[int]]
            Терм-документная матрица, являющаяся результатом работы метода
            fit_transform() класса CountVectorizer.

        Returns
        -------
        list[list[float]]
            Результат IDF преобразования.
        """
        if not all(isinstance(x, list) for x in count_matrix):
            raise ValueError
        for vector in count_matrix:
            if not all(isinstance(x, int) for x in vector):
                raise ValueError

        result = []
        for i in range(len(count_matrix[0])):
            docs_with_word = 0
            for vector in count_matrix:
                if vector[i] != 0:
                    docs_with_word += 1

            result.append(
                round(math.log(
                    (len(count_matrix) + 1) / (docs_with_word + 1)) + 1, 3)
            )

        return result


class TfidfVectorizer(CountVectorizer):
    """
    Многофункциональный класс для получения терм-документной матрицы
    и ее TF-IDF преобразования.
    """
    def __init__(self):
        super().__init__()
        self._transformer = TfidfTransformer()
        self._tfidf = None

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        self._tfidf = self._transformer.fit_transform(count_matrix)
        return self._tfidf


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vec = CountVectorizer()
    count_matrix = vec.fit_transform(corpus)
    print(count_matrix)

    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
