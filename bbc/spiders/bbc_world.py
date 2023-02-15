import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BbcWorldSpider(CrawlSpider):
    name = 'bbc_world'
    allowed_domains = ['www.bbc.com']
    start_urls = ['https://www.bbc.com/news/world']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = "//a[@class = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor']"), 
             callback='parse_item', 
             follow=True),
    )

    def parse_item(self, response):
        yield{
        'title':response.xpath("//h1[@class='ssrcss-15xko80-StyledHeading e1fj1fc10']/text()").get(),
        'datetime':response.xpath("//time/@datetime").get(),
        'category':response.xpath("(//a[@class='ssrcss-w6az1r-StyledLink ed0g1kj0'])[1]/text()").get(),
        'article':response.xpath("//p[@class='ssrcss-1q0x1qg-Paragraph eq5iqo00']/text()").getall(),
        'related_topics':response.xpath("(//a[@class='ssrcss-w6az1r-StyledLink ed0g1kj0'])[position()>1]/text()").getall()

        }
