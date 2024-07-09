# Scrapper

### Common Requirements
* Code must correspond to `pep8` (use `pycodestyle` utility for self-check).
  * You can set line lengths up to 120 symbols.

### Task Description 
For this task, you can join with an RSS reader using **Python 3.10**.

For the testing, you are going to isolate the parts you will work on. Namely, you are going to work only on the RSS (XML) scrapping part. Your task is to parse the RSS document and provide two formatted outputs: JSON and the standard output.


You are going to:
* Command line parsing.
* Receive the XML document from the web.

Because you can create your own style of formatting, it will be difficult to test you. So, we will provide you with the exact style for the format to ease the testing part.

The format of the RSS feed that you are going to parse is [RSS 2.0](https://www.rssboard.org/rss-draft-1). You can follow the link to get a full understanding of the specification. But in this task, we are asking for the following requirements:
```html
<channel>...</channel> <!-- Required tags are <title>, <link>, <description>  but we are asking you to be able to parse <title>, <link>, <description>, <category>, <language>, <lastBuildDate>, <managingEditor>, <pubDate>, <item> -->
<item>...</item> <!-- All of the fields here are optional, but each item should have at least <title> or <description>, but for the purposes of the test we are asking to be able to parse <title>, <author>, <pubDate>, <link>, <category>, <description> -->
```

The order of the RSS items in all the output types should be the following:
* For `<channel>` element:
  1. `<title>`
  2. `<link>`
  3. `<lastBuildDate>`
  4. `<pubDate>`
  5. `<language>`
  6. `<category>` `for category in categories`
  7. `<managinEditor>`
  8. `<description>`
  9. `<item>` `for item in items`
* For `<item>` element:
  1. `<title>`
  2. `<author>`
  3. `<pubDate>`
  4. `<link>`
  5. `<category>`
  6. `<description>`

The CLI is going to have the following interface. You can use it for testing purposes when you develop XML document parsing.
 ```shell
usage: rss_reader.py [-h] [--json] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --json         Print result as JSON in stdout
  --limit LIMIT  Limit news topics if this parameter is provided
```

### Command Line Arguments

1) If the `limit` is not specified, then the user should get _all_ available feeds. 
2) If the `limit` is larger than the feed size, then the user should get _all_ available news.
3) The `limit` argument should also affect JSON generation
4) In the case of using the `--json` argument, your utility should convert the news into the [JSON](https://en.wikipedia.org/wiki/JSON) format.


### Console Output:

* For `<channel>` element:
  1. `<title>` is equal to Feed
  2. `<link>` is equal to Link
  3. `<lastBuildDate>` is equal to Last Build Date
  4. `<pubDate>` is equal to Publish Date 
  5. `<language>` is equal to Language
  6. `<category>` `for category in categories` is equal to Categories: category1, category2
  7. `<managinEditor>` is equal to Editor
  8. `<description>` is equal to Description
  9. `<item>` `for item in items` each item is separated by a custom separator, and all items within except for the description are stuck together.
* For `<item>` element:
  1. `<title>` is equal to Title
  2. `<author>` is equal to Author
  3. `<pubDate>` is equal to Published
  4. `<link>` is equal to Link
  5. `<category>` is equal to Categories: category1, category2
  6. `<description>` is on a separate line without any name.

For the console output you are looking for the order of things – channel items go first and then the other items. You should also have a space between the channel elements and items. Also, the description within the item should be on the new line, separated by space. For example:
```shell
Feed: Yahoo News - Latest News & Headlines
Link: https://news.yahoo.com/rss
Description: Yahoo news description

Title: Nestor heads into Georgia after tornados damage Florida
Published: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its march across a swath of the U.S. Southeast... <--- !!! THIS IS DESCRIPTION !!!

Title: Some Other Title
Published: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://some.other.link/some-other-news


Some other new cool information. <--- !!! THIS IS DESCRIPTION
```

### JSON Output:

For the JSON output, you are looking for the exact names of the tags. Ask for the pretty output:

```json
{
  "title": "Yahoo News - Latest News & Headlines",
  "link": "https://news.yahoo.com/rss",
  "description": "Yahoo news description",
  "items": [
    {
      "title": "Nestor heads into Georgia after tornados damage Florida",
      "pubDate": "Sun, 20 Oct 2019 04:21:44 +0300",
      "link": "https://some.other.link/some-other-news",
      "description": "Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its march across a swath of the U.S. Southeast..."
    },
    {
      "title": "Some other title",
      "pubDate": "Sun, 20 Oct 2019 04:21:44 +0300",
      "link": "https://some.other.link/some-other-news",
      "description": "Some other new cool information."
    }
  ]
}
```
You should have an indent to be equal to two spaces.

> * Ensure that your app has no encoding issues (meaning symbols like &#39, etc.) when printing news to stdout.
> * Ensure that your app has no encoding issues (meaning symbols like &#39, etc.) when printing news to stdout in JSON format.
> * The limit argument should also affect JSON generation.
> *It is preferable to have different custom exceptions for different situations (if needed).

---
Implementations will be checked with the latest CPython interpreter of the 3.10 branch.
---

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability. **John F. Woods**
