# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
import json as js
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import xml.etree.ElementTree as ET
import requests


class UnhandledException(Exception):
    pass


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        # >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        # >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        # >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    root = ET.fromstring(xml)
    channel = root.find("channel")
    if channel is None:
        raise UnhandledException("Невірний RSS-канал")
    feed_title = channel.find("title").text if channel.find("title") is not None else 'Без назви'
    feed_link = channel.find("link").text if channel.find("link") is not None else 'Без посилання'
    feed_description = channel.find("description").text if channel.find("description") is not None else 'Без опису'

    items = channel.findall("item")[:limit] if limit else channel.findall("item")
    new_items = []
    for item in items:
        title = item.find("title").text if item.find("title") is not None else 'Без назви'
        link = item.find("link").text if item.find("link") is not None else 'Без посилання'
        pub_date = item.find("pubDate").text if item.find("pubDate") is not None else None
        description = item.find("description").text if item.find("description") is not None else 'Без опису'
        author = item.find("author").text if item.find("author") is not None else None
        category = item.find("category").text if item.find("category") is not None else None

        item_dict = {
            'Title': title,
            'Link': link,
            'Description': description
        }
        if pub_date:
            item_dict['Published'] = pub_date
        if author:
            item_dict['Author'] = author
        if category:
            item_dict['Category'] = category

        new_items.append(item_dict)

    if json:
        output_dict = {
            'title': feed_title,
            'link': feed_link,
            'description': feed_description,
            'items': new_items if new_items else []
        }
        return [js.dumps(output_dict, indent=2)]

    else:
        output = [
            f"Feed: {feed_title}",
            f"Link: {feed_link}",
            f"Description: {feed_description}",
            ""
        ]
        if not new_items:
            output.append("No items found.")
        else:
            for item in new_items:
                output.append(f"Title: {item['Title']}")
                if 'Published' in item:
                    output.append(f"Published: {item['Published']}")
                if 'Author' in item:
                    output.append(f"Author: {item['Author']}")
                if 'Link' in item:
                    output.append(f"Link: {item['Link']}")
                if 'Category' in item:
                    output.append(f"Category: {item['Category']}")
                output.append("")
                output.append(f"{item['Description']}")
                output.append("")

        return output    # ти крута!!!!


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    if args.source is None:
        print("Помилка: URL не надано. Будь ласка, вкажіть RSS URL як аргумент.")
        return 1
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))

        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
