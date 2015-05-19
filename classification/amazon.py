import amazonproduct, os


aws_api = amazonproduct.API(cfg={
    'access_key': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'associate_tag': os.getenv('AWS_ASSOCIATE_TAG'),
    'locale': os.getenv('AWS_LOCALE')
})


from pprint import pprint

class Amazon:

	@staticmethod
	def search(keywords):
		products = []
		#limit to 5, get reviews of each and return them
		items = aws_api.item_search('All', Keywords=keywords)

		limit = len(items) if len(items) < 5 else 5
		count = 0
		for item in items:
			if count >= limit:
				break
			#print '%s: "%s"' % (book.ItemAttributes.Author, book.ItemAttributes.Title)
			products.append(item)
			product_id = item.ASIN
			#product = aws_api.item_lookup(str(product_id), ResponseGroup='Reviews', IncludeReviewsSummary=True)[0]
			count += 1


		return products