"""
В файле хранятся данные с сайта IMDB.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
1) top250_movies.txt – названия фильмов
2) ratings.txt – гистограмма рейтингов
3) years.txt – гистограмма годов
"""


with open('ratings.list') as file:
    lines_list = []
    years = []
    rates = []
    top250 = 250

    for line in file:
        if line.startswith('      000000'):
            lines_list.append(line)
            top250 -= 1
        if not top250:
            break

    titles = open("top250_movies.txt", 'w')

    for line in lines_list:
        split_line = line.split()
        years.append(split_line[-1].replace('(', '').replace(')', ''))
        rates.append(split_line[2])
        titles.write(" ".join(split_line[3:-1]))
        titles.write('\n')
    titles.close()

    def frequency_elem(seq):
        hist_ = {}

        for el in seq:
            hist_[el] = hist_.get(el, 0) + 1

        return hist_

    def histogram(seq):
        str_ = ''
        count_elem = frequency_elem(seq)
        for el in sorted(count_elem):
            str_ += '{0} {1}\n'.format(el, '|>' * count_elem[el])
        return str_

    hist_rates = open("ratings.txt", "w")
    frequency_elem(rates)
    hist_rates.write('Ratings histogram\n')
    hist_rates.write(histogram(rates))
    hist_rates.close()

    hist_years = open("years.txt", "w")
    frequency_elem(years)
    hist_years.write('Years histogram\n')
    hist_years.write(histogram(years))
    hist_years.close()
