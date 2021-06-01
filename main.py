#Hadeed Pall
#251164522
#2020/11/18
#Western university
#finding happiness score for tweets in different zones



#importing compute_tweets from sentiment_analysis
from sentiment_analysis import compute_tweets
#letting user enter the name of the files
file_of_tweet = input('You may enter the tweet file: ')
main_file_word = input('You may enter the keyword file: ')
#print statment to create neat spacing
print()
print()
print()
#getting result
results = compute_tweets(file_of_tweet, main_file_word)
#if statement for when len(result) >0
if len(results) > 0:
    #print location
    print("EASTERN:")
    #print statement used to output the happiness score
    print("Happiness Score: %.2f"%results[0][0])
    #print statement used to output the keywords
    print("Keyword Tweets:",results[0][1])
    #print statement used to output the total tweets
    print("Total Tweets:",results[0][2])
    #print statment to create neat spacing
    print()
    print()
    print()
    #printing location
    print("CENTRAL:")
    #print statement used to output the happiness score
    print("Happiness Score: %.2f"%results[1][0])
    #print statement used to output the keywords
    print("Keyword Tweets:",results[1][1])
    #print statement used to output the total tweets
    print("Total Tweets:",results[1][2])
    #print statement to create neat spacing
    print()
    print()
    print()
    #print location
    print("MOUNTAIN:")
    #print the happiness score
    print("Happiness Score: %.2f"%results[2][0])
    #print keywords
    print("Keyword Tweets:",results[2][1])
    #print total tweets
    print("Total Tweets:",results[2][2])
    #print statement to create neat spacing
    print()
    print()
    print()
    #print statement used to output the location
    print("PACIFIC:")
    #print happiness score
    print("Happiness Score: %.2f"%results[3][0])
    #print keywords
    print("Keyword Tweets:",results[3][1])
    #print total tweets
    print("Total Tweets:",results[3][2])
else:
    # print statement to display error message to yser when results are not able to be collected
    print("Sorry these results are not able to be obtained.")
