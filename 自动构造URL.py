pageNum = 80000
total = 85000
self.pageNum = self.pageNum + 1
if(self.pageNum < self.total):
new_url = self.url + str(self.pageNum) + ".htm"
yield Request(new_url, callback = self.parse)