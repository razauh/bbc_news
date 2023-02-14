import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MostReadSpider(CrawlSpider):
    name = 'most_read'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/news']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//a[@class = 'gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs']"), 
        callback='parse_item', 
        follow=True),
    )

    def parse_item(self, response):
        yield{
            'title':response.xpath("//h1[@class='ssrcss-15xko80-StyledHeading e1fj1fc10']/text()").get,
            'author':response.xpath("//div[@class='ssrcss-68pt20-Text-TextContributorName e8mq1e96']/text()").get,
            'summary':response.xpath("//b[@class = 'ssrcss-hmf8ql-BoldText e5tfeyi3']/text()").get,
            'article':response.xpath("//p[@class='ssrcss-1q0x1qg-Paragraph eq5iqo00']/text()").getall(),
            'url':response.url
        }



# //a[@class = 'gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs']
