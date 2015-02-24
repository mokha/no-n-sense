import amazonproduct, os


aws_api = amazonproduct.API(cfg={
    'access_key': os.getenv('AWS_ACCESS_KEY_ID'),
    'secret_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'associate_tag': os.getenv('AWS_ASSOCIATE_TAG'),
    'locale': os.getenv('AWS_LOCALE')
})


class Amazon:

	@staticmethod
	def search(keywords):

		#limit to 5, get reviews of each and return them
		items = aws_api.item_search(keywords)

		for book in items:
			print '%s: "%s"' % (book.ItemAttributes.Author, book.ItemAttributes.Title)