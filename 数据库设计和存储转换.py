class Script2Item(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
####
item = Script2Item()
if title:
    title = title[0]
else:
    title = ""
if content:
    content = content[0]
else:
    content = ""
if desc:
    desc = desc[0]
else:
    desc = ""
if tag:
    tag = tag
else:
    tag = ""
item['title'] = title
item['desc'] = desc
item['tag'] = ','.join(tag)
item['content'] = content
yield item