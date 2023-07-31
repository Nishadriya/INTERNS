import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}
        
        def shorten_url(self,original_url):
            url_hash = hashlib.md5(original_url.encode()).hexdigest()[:8]
            short_url=f"http://short.url/{url_hash}"
            self.url_map[short_url] = original_url
            return short_url
        
def get_original_url(self,short_url):
    return self.url_map.get(short_url, "URL not found.")

#Example usage:
shortener = URLShortener()
short_url = shortener.shorten_url("https://www.example.com")
print("shortened URL:", short_url)
original__url = shortener.get_original_url(short_url)
print("Original URL:",original__url)