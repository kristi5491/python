class Pagination:
    def __init__(self, data, items_on_page):
        if items_on_page <= 0:
            raise ValueError("items_on_page must be a positive integer")
        self.data = data
        self.items_on_page = items_on_page
        self.pages = self._paginate()

    def _paginate(self):
        return [self.data[i:i + self.items_on_page] for i in range(0, len(self.data), self.items_on_page)]

    @property
    def page_count(self):
        return len(self.pages)

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise IndexError("Invalid index. Page is missing")
        return len(self.pages[page_number])

    def find_page(self, data):
        results = []
        for i, page in enumerate(self.pages):
            if data in page:
                results.append(i)
        if not results:
            raise ValueError(f"'{data}' is missing on the pages")
        return results

    def display_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise IndexError("Invalid index. Page is missing")
        return self.pages[page_number]


pages = Pagination('Your beautiful text', 5)
print(pages.page_count)  # Output: 4
print(pages.count_items_on_page(0))  # Output: 5
print(pages.find_page('Y'))  # Output: [0]
