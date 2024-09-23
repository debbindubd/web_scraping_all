import scrapy


class PopulationSpider(scrapy.Spider):
    name = "population"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"]

    def parse(self, response):
        pass
