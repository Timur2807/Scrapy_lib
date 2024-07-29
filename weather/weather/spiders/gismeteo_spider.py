import scrapy


class GismeteoSpiderSpider(scrapy.Spider):

    custom_settings = {'FEED_URI': 'results/weather.csv'}
    name = "gismeteo_spider"
    allowed_domains = ["www.gismeteo.ru"]
    start_urls = ["https://www.gismeteo.ru/weather-kazan-4364/10-days/"]

    def parse(self, response):
        print("procesing:" + response.url)
        date = response.xpath("//div[@class='date']/text()").extract()
        day = response.xpath("//div[@class='day']/text()").extract()
        values = response.xpath("//span[@class='unit unit_temperature_c']/text()").extract()
        values_1 = []

        for value in values:
            if value == '°C':
                continue
            else:
                values_1.append(value)
        values_max = values_1[0:20:2]

        row_day_tmp = zip(day, date, values_max)

        for item in row_day_tmp:

            weather_info = {
                'day': item[0],
                'date': item[1],
                'values': item[2],
            }

            yield weather_info
