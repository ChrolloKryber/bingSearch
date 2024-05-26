# bingSearch

A simple python script for linux to open your browser and conduct bing searches, with a main goal to prevent detection.

Even though I have tried my best to make it hard to figure out that the searches are automated, there is still a chance to get caught.

```diff
- Use at your own risk, automating bing searches goes against Microsoft's ToS
```

##### Big shoutout to @[jack-mil](https://github.com/jack-mil), the script is inspired by his own implementation of the same, and I have used his keywords file for the same.


### Installation
1. Run `pip -r requirements.txt`
2. Make sure you have either Chromium installed or edit the script to run the browser of your choice and Bing is the default search engine
3. Use the keyword file of your own or run as is for using the included keywords

### About the script

My goal was to create a script which could mimick the most human behavior. 
The script utilizes Pynput library for emulating input via your keyboard, the script will automatically open a chromium window, conduct searches and close it. All with a set interval.

Since bing uses a bunch of URL parameters for every search, it's not possible to directly enter an appended URL with the search term attached to it. Hence, bing has to be set your default search engine.
