#https://medium.com/machine-learning-mastery/how-to-scrape-millions-of-tweets-using-snscraper-aa47cee400ec
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Setting variables to be used below
#100000で57分
#100000で80分
#200000で163分
#100000で76分
search_term = 'アゼライン'
maxTweets = 10000
# Creating list to append tweet data to
tweets_list2 = []
# Using TwitterSearchScraper to scrape data and append tweets to list
#min_replies:1 min_faves:1 min_retweets:1 until:2023-03-31 since:2023-01-01
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search_term+' until:2023-07-31 since:2023-01-01').get_items()):
  if i>maxTweets:
    break
  tweets_list2.append([tweet.url, tweet.date, tweet.id, tweet.username, tweet.rawContent, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount, tweet.viewCount, tweet.hashtags, tweet.media])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['URL','Datetime', 'Tweet Id', 'Username','Tweet', 'Like','Reply', 'Retweet','Quote', 'View','Hashtags','Media'])
tweets_df2.to_csv("/Users/andkntr/Downloads/demeran.csv", index = False)
