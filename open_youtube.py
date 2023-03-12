
import urllib.request
import urllib.parse
import re
import webbrowser


#query_string = urllib.parse.urlencode({"search_query" : input()})
#html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
#search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
#print("http://www.youtube.com/watch?v=" + search_results[0])


search_keyword=input ().split()

#print (len (search_keyword))
html = urllib.request.urlopen("https://www.youtube.com/results?search_query="
                              + '+'.join(search_keyword))
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_ids[0])
webbrowser.open_new("https://www.youtube.com/watch?v=" + video_ids[0])