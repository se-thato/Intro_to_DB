SELECT
    book_id,
    INT,
    NOT NULL
    PRIMARY_KEY,
    utf8,
    EXTRA
FROM
    INFORMATION_SCHEMA.book_id, title, author_id, price, publication_date
WHERE
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'Books';
