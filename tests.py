import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1
    def test_add_new_book_adds_book(self):
        collector = BooksCollector()
        name_of_book = "Портрет Дориана Грея"

        collector.add_new_book(name_of_book)

        assert name_of_book in collector.get_books_genre()

    # 2
    @pytest.mark.parametrize(
        "name_of_book, genre",
        [
            ("English alphabet", ""),
            ("Шерлок Холмс", "Детективы"),
        ]
    )
    def test_add_and_set_book_genre(self, name_of_book, genre):
        collector = BooksCollector()
        collector.add_new_book(name_of_book)

        if genre:
            collector.set_book_genre(name_of_book, genre)

        assert collector.get_book_genre(name_of_book) == genre

    # 3
    @pytest.mark.parametrize(
        "target_genre, books, expected",
        [
            (
                    "Комедии",
                    [("Мцыри", "Фантастика"), ("Ревизор", "Комедии"), ("Обломов", "Детективы")],
                    ["Ревизор"],
            ),
            (
                    "Комедии",
                    [("Горе от ума", "Комедии"), ("Недоросль", "Комедии"), ("Дикий помещик", "Мультфильмы")],
                    ["Горе от ума", "Недоросль"],
            ),
            (
                    "Мультфильмы",
                    [("Двенадцать", "Мультфильмы"), ("Облако в штанах", "Мультфильмы"), ("Реквием", "Мультфильмы")],
                    ["Двенадцать", "Облако в штанах", "Реквием"],
            ),
        ],
    )
    def test_get_books_with_specific_genre(self, target_genre, books, expected):
        collector = BooksCollector()

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        result = collector.get_books_with_specific_genre(target_genre)

        assert result == expected

    # 4
    @pytest.mark.parametrize(
        "books",
        [
            [("Мцыри", ""), ("Ревизор", "Комедии"), ("Обломов", "")],
            [("Горе от ума", "Комедии"), ("Недоросль", "Комедии"), ("Дикий помещик", "")],
            [("Двенадцать", "Мультфильмы"), ("Облако в штанах", "Мультфильмы"), ("Реквием", "Мультфильмы")],
        ],
    )
    def test_get_books_genre_returns_expected_dict(self, books):
        collector = BooksCollector()

        for name, genre in books:
            collector.add_new_book(name)
            if genre:
                collector.set_book_genre(name, genre)

        expected = {}
        for name, genre in books:
            expected[name] = genre

        assert collector.get_books_genre() == expected

    # 5
    @pytest.mark.parametrize(
        "books, expected",
        [
            (
                    [("Убийство Роджера Экройда", "Ужасы"), ("Гарри Поттер", "Мультфильмы")],
                    ["Гарри Поттер"],
            ),
            (
                    [("Шерлок Холмс", "Детективы"), ("Сказка о царе Салтане", "Мультфильмы")],
                    ["Сказка о царе Салтане"],
            ),
        ],
    )
    def test_get_books_for_children(self, books, expected):
        collector = BooksCollector()

        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        result = collector.get_books_for_children()

        assert result == expected

    # 6
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        name_of_book = "Голодные игры"

        collector.add_new_book(name_of_book)
        collector.set_book_genre(name_of_book, "Фантастика")
        collector.add_book_in_favorites(name_of_book)

        assert collector.get_list_of_favorites_books() == [name_of_book]

    # 7
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        books = ["Голодные игры", "Тень и Кость"]

        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        result = collector.get_list_of_favorites_books()
        assert result == books

    # 8
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        books = ["Голодные игры", "Портрет Дориана Грея", "Спеши любить"]

        for name in books:
            collector.add_new_book(name)
            collector.add_book_in_favorites(name)

        book_to_delete = "Портрет Дориана Грея"
        collector.delete_book_from_favorites(book_to_delete)

        favorites = collector.get_list_of_favorites_books()

        assert book_to_delete not in favorites
        assert len(favorites) == len(books) - 1
        assert favorites == ["Голодные игры", "Спеши любить"]

    # 9
    def test_add_new_book_too_long_name_not_added(self):
        collector = BooksCollector()
        long_name = "Книга" * 45

        collector.add_new_book(long_name)

        assert long_name not in collector.get_books_genre()
