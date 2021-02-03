# shrtcode-api-wrapper
A wrapper made in Python for the [Shrtcode API](https://app.shrtco.de/docs)

# Examples

## Shorten a link
```
from shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.shorten("https://example.org/") # calls the function 'shorten()' which returns a 'Shortcode' object
print(shortened) # and finally prints the shortened link in the terminal
print(shortened.short_link) # also you can print the short version (without the https://)
```

## Get info about a shortened link
```
from shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.get_info("xsyV8") # calls the function 'get_info()' which returns a 'Shortcode' object
print(shortened.original_link) # prints the original link in the terminal
```

# Dependencies
  - [requests](https://pypi.org/project/requests/)
  - urllib (built-in)

# Contribuiting
This is my first module ever, if you have found some error or have an idea to improve the code feel free to fork and edit in any way that you want.
Also sorry for my bad english, i'm still learning :p
