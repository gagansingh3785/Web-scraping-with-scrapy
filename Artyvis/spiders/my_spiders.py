import scrapy


from ..items import ArtyvisItem

class houseofindya(scrapy.Spider):
	#name to identify the spider, should be unique
	name = 'houseofindya'
	
	#spider begins crawling from these urls
	start_urls = [
		'https://www.houseofindya.com/zyra/necklace-sets/cat'
	]

	#specifying the order of output fields
	custom_settings = {
    	'FEED_EXPORT_FIELDS': ["Name", "Description", "Cost", "Images"],
  	}

  	#function that parses the response of crawler after crawling the start_urls
  	#collecting the urls of the necklaces sets in the root urls and sending request to those urls
	def parse(self, response):
		urls = response.xpath('//ul[@id="JsonProductList"]/li/@data-url').getall()
		for url in urls:
			yield scrapy.Request(url, callback=self.item_parsing)


	#method that parses the response after sending the request to necklaces sets urls
	#the data extracted from response is temporarily stored in an item container from where it is sent to json/csv file
	def item_parsing(self, response):
		image_urls = ""
		data_item = ArtyvisItem()
		data_item['Name'] = response.css('div.prodRight h1::text').get().strip()
		data_item['Description'] = response.css('div.prodRight #tab-1 p::text').get().strip().replace(',', ';')
		data_item['Cost'] = response.css('div.prodRight h4 span::text').getall()[1].strip()

		for url in response.css('div.prodLeft img::attr(data-original)').getall():
			image_urls += url + ';'

		data_item['Images'] = image_urls

		return data_item
