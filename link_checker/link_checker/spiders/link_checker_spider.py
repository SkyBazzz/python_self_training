import scrapy


class LinkCheckerSpider(scrapy.Spider):
    name = "link_checker_spider"
    start_urls = ["https://savelife.in.ua"]  # Starting URL for crawling
    found_links = set()  # Store found links
    max_depth = 3  # Set the maximum depth to crawl

    def parse(self, response, **kwargs):
        # Get all links from the page
        links = response.css("a::attr(href)").getall()
        links.append(response.css("link::attr(href)").getall())
        print("PRINTING LINKS")
        print(links)
        print(len(links))
        current_depth = response.meta.get("depth", 0)

        for link in links:
            # Check if it's an internal link (with the main domain)
            if self.is_internal_link(link):
                self.found_links.add(link)  # Add the link to the set
                yield response.follow(link, self.check_link, meta={"depth": current_depth + 1})

                # Follow the link and parse it for additional links if depth is within the limit
                if current_depth + 1 <= self.max_depth:
                    yield scrapy.Request(link, callback=self.parse, meta={"depth": current_depth + 1})

    def check_link(self, response):
        # Check the HTTP status of the page
        status = response.status
        url = response.url
        if status == 404:
            self.log(f"Page {url} not found (HTTP 404)")
        else:
            self.log(f"Page {url} is accessible (HTTP {status})")

    def is_internal_link(self, link):
        # Check if it's an internal link with the main domain
        return link.startswith("https://savelife.in.ua")

    def closed(self, reason):
        # Display all found links at the end of crawling
        self.log(f'Found {len(self.found_links)} links: {", ".join(self.found_links)}')
        self.log(f"{reason=}")
