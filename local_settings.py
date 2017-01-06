'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'CpIcPJeQtwYUMkd8CItXNwUFd'
MY_CONSUMER_SECRET = 'rGEUPk5qPo5ISgWg6r2lYHIs99d4DEy9vCe58YGPrQkkVxdU57k'
MY_ACCESS_TOKEN_KEY = ''814563191887896577-U3FPkMrhCbpcskB1Za8BQ2SQ1vcBKs6'
MY_ACCESS_TOKEN_SECRET = 'nQpVVDO5k6SUZQLCYGfewAcKweRzNjHtaOF7q5DxJ3PO6'

SOURCE_ACCOUNTS = ["icancharity","AmnestyUK"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "" #The name of the account you're tweeting to.
