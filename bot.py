# Copyright (c) 2015–2016 Molly White 
2 # 
3 # Permission is hereby granted, free of charge, to any person obtaining a copy 
4 # of this software and associated documentation files (the "Software"), to deal 
5 # in the Software without restriction, including without limitation the rights 
6 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
7 # copies of the Software, and to permit persons to whom the Software is 
8 # furnished to do so, subject to the following conditions: 
9 # 
10 # The above copyright notice and this permission notice shall be included in 
11 # all copies or substantial portions of the Software. 
12 # 
13 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
14 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
15 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
16 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
17 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
18 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
19 # SOFTWARE. 
20 
 
21 import os 
22 import tweepy 
23 from secrets import * 
24 from time import gmtime, strftime 
25 
 
26 
 
27 # ====== Individual bot configuration ========================== 
28 bot_username = 'No_pain_bot' 
29 logfile_name = bot_username + ".log" 
30 
 
31 # ============================================================== 
32 
 
33 
 
34 def create_tweet(): 
35     """Create the text of the tweet you want to send.""" 
36     # Replace this with your code! 
37     text = "" 
38     return text 
39 
 
40 
 
41 def tweet(text): 
42     """Send out the text as a tweet.""" 
43     # Twitter authentication 
44     auth = tweepy.OAuthHandler(C_KEY, C_SECRET) 
45     auth.set_access_token(A_TOKEN, A_TOKEN_SECRET) 
46     api = tweepy.API(auth) 
47 
 
48     # Send the tweet and log success or failure 
49     try: 
50         api.update_status(text) 
51     except tweepy.error.TweepError as e: 
52         log(e.message) 
53     else: 
54         log("Tweeted: " + text) 
55 
 
56 
 
57 def log(message): 
58     """Log message to logfile.""" 
59     path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
60     with open(os.path.join(path, logfile_name), 'a+') as f: 
61         t = strftime("%d %b %Y %H:%M:%S", gmtime()) 
62         f.write("\n" + t + " " + message) 
63 
 
64 
 
65 if __name__ == "__main__": 
66     tweet_text = create_tweet() 
67     tweet(tweet_text) 
