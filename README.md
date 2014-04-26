Twitter-Sentiment-Analysis
==========================





About twitterstream.py: 

Used to fetch live stream data from twitter.

Requires oauth2, which is not part of the EnThought Python library.

usage:
Open the program and replace access_token_key, access_token_secret, consumer_key, and consumer_secret with the appropriate values. Then run
$ python twitterstream.py


To get credentials:

<ul>
<li>Create a twitter account if you do not already have one.</li>
<li>Go to https://dev.twitter.com/apps and log in with your twitter credentials.</li>
<li>Click "create an application"</li>
<li>Fill out the form and agree to the terms.  Put in a dummy website if you don't have one you want to use.</li>
<li>On the next page, scroll down and click "Create my access token"</li>
<li>Copy your "Consumer key" and your "Consumer secret" into twitterstream.py</li>
<li>Click "Create my access token."  You can <a href="https://dev.twitter.com/docs/auth">Read more about Oauth authorization.</a></li>
<li>Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret</li>
<li>Run the following and make sure you see data flowing.</li>
<pre>
$ python twitterstream.py > twitterstream.txt
</pre>
<li>
Ctrl-C to stop fetching tweets into twitterstream.txt
</li>
</li>

</ul>

