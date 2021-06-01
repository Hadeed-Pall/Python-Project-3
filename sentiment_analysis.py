#importing a string from punctuation
from string import punctuation

# variables for the maximum and minimum latitude/longitude
#max_latitude variable creation
max_latitude = 49.189787
#min_latitude variable creation
min_laitude  = 24.660845
#max_longitude variable creation
max_longitude = -67.444574
#min_longitude variable creation
min_longitude = -125.242264

#function created to find the longitude
def longitude_calc(longitude):
    if min_longitude <= longitude <= max_longitude:
        return True
    else:
        return False
    #function created to find the latitude
def latitude_calc(latitude):
    #if statement for when real_latitude is less then max_latitude, but greater then min_latitude
    if min_laitude <= latitude <= max_latitude:
        return True
    else:
        return False


#function to generate/calculate timezone
def place_calculator(latitude, longitude):
    if not latitude_calc(latitude) or not longitude_calc(
            longitude):
        return None
    #finding if location is Eastern
    elif longitude >= -87.518395:
        return "Eastern"
    #finding if location is Central
    elif longitude >= -101.998892:
        return "Central"
    #finding if location is Mountain
    elif longitude >= -115.236428:
        return "Mountain"
    #finding if location is Pacific
    else:
        return "Pacific"

# method used to calculate the total and increment the scores and the different tweets
def score_calc(v_average, total_of_scores, keyword_tweets, tweet_total, index):
        #if statement when average is >0
    if v_average > 0:
        total = total_of_scores[index]
        total += v_average
        total_of_scores[index] = total
        keyword_tweets[index] += 1
        tweet_total[index] += 1
    #else statement for when v_average<0
    else:
        tweet_total[index] += 1

#function to calculate tweets
def compute_tweets(file_of_tweet, main_file_word):
    #variable creation
    main_words = {}
    total_of_scores = [0, 0, 0, 0]
    count_of_keyword_tweets = [0, 0, 0, 0]
    count_of_tweets = [0, 0, 0, 0]
    v_averages = [0, 0, 0, 0]
    #try statement to test code block for errors
    try:
        file_of_tweet = open(file_of_tweet, encoding='utf‐8', errors='ignore')
        main_file_word = open(main_file_word, encoding='utf‐8', errors='ignore')
    #creating an exception for the IOError
    except IOError:
        print("Error: file not found.")
        return []
    #for statement for any line in main_file_word
    for line in main_file_word:
        keylist = line.split(",")
        word = keylist[0]
        score = keylist[1]
        main_words[word] = score
    #for statement for any line in file_of_tweet
    for line in file_of_tweet:
        count = 0
        score = 0
        v_average = 0
        line = line.rstrip()
     #spliting place_of_list by the "] " as intructed
        place_of_list = line.split("]")
        #spliting place_of_list by the ", " as intructed
        place_of_list[0] = line.split(",")
        area = place_of_list[0]
        latitude = float(area[0].lstrip(punctuation))
        longitude = area[1].split("]")
        longitude = float(longitude[0].lstrip(punctuation))
        tweet_of_the_text = place_of_list[1][23:]
        words = tweet_of_the_text.split()
        place = place_calculator(latitude, longitude)
     #if statement when place is not equal None
        if place is not None:
            #for statement for any word in words
            for word in words:
                word = word.strip(punctuation)
                if word.lower() in main_words:
                    score += int(main_words[word.lower()])
                    count += 1
            #when count>0
            if count > 0:
                v_average = float(score / count)
                    #finding if location is Eastern
            if place == "Eastern":
                score_calc(v_average, total_of_scores, count_of_keyword_tweets, count_of_tweets, 0)
                    #finding if location is Central
            elif place == "Central":
                score_calc(v_average, total_of_scores, count_of_keyword_tweets, count_of_tweets, 1)
            #finding if location is Mountain
            elif place == "Mountain":
                score_calc(v_average, total_of_scores, count_of_keyword_tweets, count_of_tweets, 2)
             #finding if location is Pacific
            elif place == "Pacific":
                score_calc(v_average, total_of_scores, count_of_keyword_tweets, count_of_tweets, 3)
    #for statement for any i in range
    for i in range(0, 4):
        if count_of_keyword_tweets[i] > 0:
            v_averages[i] = float(total_of_scores[i] / count_of_keyword_tweets[i])
        else:
            v_averages[i] = 0
 #tuple that puts the information into 3 elements, for reach element
    real_eastern = (v_averages[0], count_of_keyword_tweets[0], count_of_tweets[0])
    real_central = (v_averages[1], count_of_keyword_tweets[1], count_of_tweets[1])
    real_mountain = (v_averages[2], count_of_keyword_tweets[2], count_of_tweets[2])
    real_pacific = (v_averages[3], count_of_keyword_tweets[3], count_of_tweets[3])
    real_result = [real_eastern, real_central, real_mountain, real_pacific]
    return real_result
