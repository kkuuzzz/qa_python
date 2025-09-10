Список реализованных тестов

test_add_new_book_adds_book 
Книга добавляется в словарь.  
Проверяю: метод `add_new_book`.

test_add_and_set_book_genre
У новой книги жанр пустой по умолчанию и может быть установлен.  
Проверяю: методы `add_new_book`, `set_book_genre`, `get_book_genre`.

test_get_books_with_specific_genre
Проверяет выборку книг по определённому жанру.  
Проверяю: метод `get_books_with_specific_genre`.

test_get_books_genre_returns_expected_dict 
Проверяет, что возвращается словарь всех книг с их жанрами.  
Проверяю: метод `get_books_genre`.

test_get_books_for_children
Проверяет, что книги с возрастным рейтингом не попадают в список детских.  
Проверяю: метод `get_books_for_children`.

test_add_book_in_favorites 
Добавление книги в список избранного.  
Проверяю: метод `add_book_in_favorites`.

test_get_list_of_favorites_books  
Получение актуального списка избранных книг.  
Проверяю: метод `get_list_of_favorites_books`.

test_delete_book_from_favorites 
Удаление книги из списка избранного.  
Проверяю: метод `delete_book_from_favorites`.

test_add_new_book_too_long_name_not_added 
Проверяет, что книга с названием длиннее 40 символов не добавляется.  
Проверяю: метод `add_new_book`.
