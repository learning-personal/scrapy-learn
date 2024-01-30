import scrapy

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    start_urls = ['https://inventhigh.net/index']

    def parse(self, response):
        base_url = 'https://inventhigh.net/'
        course_elements = response.css('.gridboximg')

        for element in course_elements:
            udemy_relative_link = element.css('a.btn.btndarkgrid::attr(href)').get()
            udemy_link = base_url + udemy_relative_link
            yield {
                'udemy_link': udemy_link
            }
