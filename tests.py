from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        book = 'Гордость и предубеждение и зомби'
        book_genre = 'Фантастика'

        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, book_genre)

        assert collector.books_genre.get(book) == book_genre

    def test_get_book_genre(self):
        book = 'Гордость и предубеждение и зомби'
        book_genre = 'Фантастика'

        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, book_genre)

        assert collector.get_book_genre(book) == book_genre

    def test_get_books_with_specific_genre(self):
        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'
        book_genre = 'Фантастика'

        collector = BooksCollector()
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.set_book_genre(book1, book_genre)
        collector.set_book_genre(book2, book_genre)

        assert sorted(collector.get_books_with_specific_genre(book_genre)) == sorted([book1, book2])

    def test_get_books_genre(self):
        book1 = 'Гордость и предубеждение и зомби'
        book2 = 'Что делать, если ваш кот хочет вас убить'
        book_genre1 = 'Фантастика'
        book_genre2 = 'Детективы'

        collector = BooksCollector()
        collector.add_new_book(book1)
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre(book1, book_genre1)
        collector.set_book_genre(book2, book_genre2)
        result = collector.get_books_genre()
        books_list = {book1: book_genre1, book2: book_genre2}

        assert books_list == result

    def test_get_books_for_children(self):
        book1 = 'Мечтают ли андроиды о электроовцах'
        book2 = 'Дагон'

        collector = BooksCollector()
        collector.add_new_book(book1)
        collector.set_book_genre(book1, 'Фантастика')
        collector.add_new_book(book2)
        collector.set_book_genre(book2, 'Ужасы')
        expected_list = [book1]
        list_of_books_for_children = collector.get_books_for_children()

        assert expected_list == list_of_books_for_children

    @pytest.mark.parametrize('book_input', ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби', 'Ганнибал'])
    def test_add_book_in_favorites(self, book_input):
        collector = BooksCollector()
        collector.add_new_book(book_input)
        collector.set_book_genre(book_input, 'Фантастика')
        collector.add_book_in_favorites(book_input)

        assert book_input in collector.favorites

    @pytest.mark.parametrize('book_input', ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби', 'Ганнибал'])
    def test_delete_book_from_favorites(self, book_input):
        collector = BooksCollector()
        collector.add_new_book(book_input)
        collector.add_book_in_favorites(book_input)
        collector.delete_book_from_favorites(book_input)

        assert book_input not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book1 = 'Преступление и наказание'
        book2 = 'Ганнибал'
        expected_books = [book1, book2]

        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)
        favorite_books = collector.get_list_of_favorites_books()

        assert expected_books == favorite_books







