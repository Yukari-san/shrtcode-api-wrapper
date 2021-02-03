import json
import requests
from urllib.parse import quote
from datetime import datetime


class Shrtcode:
    """
    Methods
    -------
    shorten(url)
        Shorten the provided url
    get_info(code)
        Fetch info about the given code

    Raises
    ------
    NoUrlSpecified
        No URL specified ("url" parameter is empty)
    InvalidSubmited
        Invalid URL submitted
    RateLimitReached
        Rate limit reached. Wait a second and try again
    IpBlocked
        P-Address has been blocked because of violating our terms of service (https://shrtco.de/tos)
    CodeAlreadyInUse
        shrtcode code (slug) already taken/in use
    UnknowError
        Unknown error
    NoCodeSpecified
        No code specified ("code" parameter is empty)
    InvalidCodeSubmited
        Invalid code submitted (code not found/there is no such short-link)
    MissingRequiredParameters
        Missing required parameters
    BlackListedLink
        Trying to shorten a disallowed Link. More information on disallowed links (https://app.shrtco.de/disallowed)
    """
    def __init__(self):
        self.BASE_URL = 'https://api.shrtco.de/v2/'
        self.session = requests.Session()
        self.errors = self._Errors()
    
    def shorten(self, url, json=False):
        """
        Shorten an url

        Parameters
        ----------
        url : str
            The URL to shorten
        json : bool
            If True then will return a dict. Default to False
        
        Returns
        -------
        shortcode : shrtcode.Shrtcode.Shortcode or dict
            An object/dict containing the shortened link and its variations
        """
        url = quote(url)
        r = self.session.get(self.BASE_URL + "shorten?url=" + url)
        data = r.json()
        if data["ok"]:
            if json:
                return data
            else:
                return self.Shortcode(data["result"]["code"], url)
        else:
            error_code = data["error_code"]
            error_message = data["error"]
            raise self.errors.errors_list[error_code - 1](error_message)
    
    def get_info(self, code, json=False):
        """
        Get info about a shortened link

        Parameters
        ----------
        code : str
            The code to fetch information about
        json : bool
            If True then will return a dict. Default to False
        
        Returns
        -------
        shortcode : shrtcode.Shrtcode.Shortcode or dict
            An object/dict containing the shortened link, its variations and some additional information
        """
        r = self.session.get(self.BASE_URL + "info?code=" + code)
        data = r.json()
        if data["ok"]:
            if json:
                return data
            else:
                return self.Shortcode(code, data["result"]["url"], data["result"])
        else:
            error_code = data["error_code"]
            error_message = data["error"]
            raise self.errors.errors_list[error_code - 1](error_message)

    class Shortcode:
        """
        An object containg the shortened code, link and its variations.

        Attributes
        ----------
        code : str
            The code of the shortened link
        short_link : str
            A short version of the shortened link
        full_short_link : str
            The full version of the shortened link (containing HTTPS://)
        short_link2 : str
            An alternative version of the shortened link
        full_short_link2 : str
            The full version of the first alternative version of the link
        short_link3 : str
            The second alternative version of the shortened link
        full_short_link3 : str
            The full version of the second alternative version of the link
        share_link : str
            The link for sharing
        full_share_link : str
            The full version of the link for sharing
        original_link : str
            The original link
        password_protected : bool or None
            Check if the link is protected by a password. None if created with shorten().
        blocked : bool or None
            Check if the link is blocked. None if created with shorten().
        block_reason : str or None
            The reason for the block, if exists. None if created with shorten().
        created : str or None
            description
        timestamp : int or None
            description
        """
        def __init__(self, code, original_link, extra={}):
            self.code = code
            self.short_link = f"shrtco.de/{code}"
            self.full_short_link = f"https://{self.short_link}"
            self.short_link2 = f"9qr.de/{code}"
            self.full_short_link2 = f"https://{self.short_link2}"
            self.short_link3 = f"shiny.link/{code}"
            self.full_short_link3 = f"https://{self.short_link3}"
            self.share_link = f"shrtco.de/share/{code}"
            self.full_share_link = f"https://{self.share_link}"
            self.original_link = original_link

            self.password_protected = extra.get("password_protected")
            self.blocked = extra.get("blocked")
            self.block_reason = extra.get("block_reason")
            self.created = extra.get("created")
            self.timestamp = extra.get("timestamp")
        
        def __repr__(self):
            return self.full_short_link
        
        def __eq__(self, other):
            return other.code == self.code
        
        def __str__(self):
            return self.full_short_link

    class _Errors:
        def __init__(self):
            self.errors_list = [self.NoUrlSpecified, self.InvalidUrlSubmited, self.RateLimitReached, self.IpBlocked, self.CodeAlreadyInUse, self.UnknownError, self.NoCodeSpecified, self.InvalidCodeSubmited, self.MissingRequiredParameters, self.BlackListedLink]

        class Error(Exception):
            def __init__(self, message):
                self.message = message

            def __str__(self):
                return self.message

        class NoUrlSpecified(Error):
            pass
        
        class InvalidUrlSubmited(Error):
            pass

        class RateLimitReached(Error):
            pass

        class IpBlocked(Error):
            pass

        class CodeAlreadyInUse(Error):
            pass

        class UnknownError(Error):
            pass

        class NoCodeSpecified(Error):
            pass

        class InvalidCodeSubmited(Error):
            pass

        class MissingRequiredParameters(Error):
            pass

        class BlackListedLink(Error):
            pass
