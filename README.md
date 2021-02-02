# shrtcode-api-wrapper
An wrapper made in Python for the Shrtcode API

# Example
```
from shrtcode import Shrtcode

shortener = Shrtcode() # initialize the 'Shrtcode' class
shortened = shortener.shorten("https://example.org/") # call the function 'shorten' of the 'Shrtcode' and stores the returned object in the variable shortened
print(shortened.short_link) # and finally prints the shortened link in the terminal
```
