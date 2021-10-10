import scrapy

from express_entry.items import DrawItem

class ExpressEntryDraw(scrapy.Spider):
    name = "draw"

    start_urls = [
        "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/ministerial-instructions/express-entry-rounds.html"
    ]

    def parse(self, response):
        rows = response.xpath('//*[@class="wb-tables table"]//tbody//tr')

        draw_item = DrawItem()

        for row in rows:
            draw_item['round_id'] = row.xpath('td[1]//a//text()').get()
            draw_item['date'] = row.xpath('td[6]//text()').extract_first()
            draw_item['immigration_program'] = row.xpath('td[3]//text()').extract_first()

            invitations = row.xpath('td[4]//text()').extract_first().replace(',', '')
            draw_item['invitations_issued'] = int(invitations)
            draw_item['crs_score'] = int(row.xpath('td[5]//text()').extract_first())

            yield draw_item
