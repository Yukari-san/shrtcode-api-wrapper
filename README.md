# shrtcode-api-wrapper
An wrapper made in Python for the [Shrtcode API](https://app.shrtco.de/docs)

# Example
```
from shrtcode import Shrtcode

shortener = Shrtcode() # initialize the 'Shrtcode' class
shortened = shortener.shorten("https://example.org/") # calls the function 'shorten' and stores the returned object in the variable 'shortened'
print(shortened.short_link) # and finally prints the shortened link in the terminal
```

# Contribuiting
This is my first module ever, if you have found some error or have a idea to improve the code feel free to fork in any way that you want.
