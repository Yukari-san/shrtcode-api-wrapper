# shrtcode-api-wrapper
An API wrapper made in Python for the [Shrtcode API](https://app.shrtco.de/docs)

# Installing
```
# Linux/macOS
python3 -m pip install -U shrtcode

# Windows
py -3 -m pip install -U shrtcode
```

# Examples

## Shorten a link
```
from shrtcode.shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.shorten("https://example.org/") # calls the function 'shorten()' which returns a 'shrtcode.shrtcode.Shrtcode.Shortcode' object
print(shortened) # and finally prints the shortened link in the terminal
print(shortened.short_link) # also you can print the short version (without the https://)
```
or
```
from shrtcode.shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.shorten("https://example.org/", json=True) # calls the function 'shorten()' which returns a dict
print(shortened["result"]["full_short_link"]) # prints the shortened link in the terminal
print(shortened["result"]["short_link"]) # the short version (the 'Shortcode' object support the same attributes as this dict keys)
```

## Get info about a shortened link
```
from shrtcode.shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.get_info("xsyV8") # calls the function 'get_info()' which returns a 'Shortcode' object
print(shortened.original_link) # prints the original link in the terminal
```
or
```
from shrtcode.shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.get_info("xsyV8", json=True) # calls the function 'get_info()' which returns a dict
print(shortened["result"]["original"]) # prints the original link in the terminal
```
The first method is good if you want the information _and_ the links in one object, use the second version if you want _just_ the information.

# Dependencies
  - [requests](https://pypi.org/project/requests/)
  - urllib (built-in)

# Contribuiting
This is my first module ever, if you have found some error or have an idea to improve the code feel free to fork and edit in any way that you want.
Also sorry for my bad english, i'm still learning :p
