# Exceptions. Task 1 

Implement a Pagination class helpful to arrange text on pages and list content on the given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per page (take spaces into account as well).

You need to be able to get the number of whole symbols in the text, get the number of pages that came out and the method that accepts the page number, and return the number of symbols on this page. If the provided number of the page is missing raise exception with message "Invalid index. Page is missing". 

Implement searching/filtering pages by symbols/words and displaying pages with all the symbols on it. If the provided symbols/words are missing raise exception with message "'<symbol/word>' is missing on the pages". 

If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

Pages indexing starts with 0.

Example:
```python
>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19

>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
>>> pages.find_page('Your')
[0]
>>> pages.find_page('e')
[1, 3]
>>> pages.find_page('beautiful')
[1, 2]
>>> pages.find_page('great')
Exception: 'great' is missing on the pages
>>> pages.display_page(0)
'Your '
```
