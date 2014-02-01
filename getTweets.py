import oauth2 as oauth
import urllib2

def oauth_req(url, key, secret, http_method="GET", post_body=None,

            http_headers=None):

        consumer = oauth.Consumer(key, secret)

        token = oauth.Token(key=key, secret=secret)

        client = oauth.Client(consumer, token)

     

        resp, content = client.request(

            url,

            method=http_method,

            body=post_body,

            headers=http_headers,

            force_auth_header=True

        )

        return content

     
n = raw_input("Enter the no. of images")
hashtag = raw_input("Enter the hashtag")
url = "https://api.twitter.com/1.1/search/tweets.json?q=%23"+hashtag+"&result_type=recent&count="+n+"&include_entities=true"
images = oauth_req(

      url,

      'Xj9675DPCkz5iqKXRqDNFA',

      'F0SOhhcS2PSrqGvv0kG3QaCMOmh9J6IQ8Fala0rE5q8'

    )

