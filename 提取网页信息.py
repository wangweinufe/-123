def parse(self, response):
    sel = scrapy.selector.Selector(response)
    title = el.xpath('//div[@class="title"]/h1/text()').extract()
    desc = sel.xpath('//div[@id="art_demo"]/text()').extract()
    content = sel.xpath('//div[@id="content"]').extract()
 tag = sel.xpath('//div[@class="tags mt10"]/a/text()').
extract()