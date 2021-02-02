# shrtcode-api-wrapper
An wrapper made in Python for the [Shrtcode API](https://app.shrtco.de/docs)

# Example

## Shorten a link
```
from shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.shorten("https://example.org/") # calls the function 'shorten()' and stores the returned object in the variable 'shortened'
print(shortened.short_link) # and finally prints the shortened link in the terminal
```

## Get info about a shortened link
```
from shrtcode import Shrtcode

shortener = Shrtcode() # init the 'Shrtcode' class
shortened = shortener.get_info("xsyV8") # calls the function 'get_info()' and stores the returned object in the variable 'shortened'
print(shortened.original_link) # prints the original link in the terminal
```

# Contribuiting
This is my first module ever, if you have found some error or have an idea to improve the code feel free to fork and edit in any way that you want.
Also sorry for my bad english, i'm still learning :p
