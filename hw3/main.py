from my_class import CountVectorizer


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vec = CountVectorizer()
    count_matrix = vec.fit_transform(corpus)
    print(vec.get_feature_names())
    print(count_matrix)
