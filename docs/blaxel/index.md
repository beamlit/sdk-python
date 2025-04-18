Module blaxel
=============
A client library for accessing Blaxel Control Plane

Sub-modules
-----------
* blaxel.agents
* blaxel.api
* blaxel.authentication
* blaxel.client
* blaxel.common
* blaxel.deploy
* blaxel.errors
* blaxel.functions
* blaxel.knowledgebases
* blaxel.models
* blaxel.run
* blaxel.serve
* blaxel.types

Classes
-------

`AuthenticatedClient(base_url: str = '', provider: httpx.Auth = None, *, raise_on_unexpected_status: bool = True, cookies: dict[str, str] = _Nothing.NOTHING, headers: dict[str, str] = _Nothing.NOTHING, timeout: httpx.Timeout | None = None, verify_ssl: str | bool | ssl.SSLContext = True, follow_redirects: bool = False, httpx_args: dict[str, typing.Any] = _Nothing.NOTHING)`
:   A Client which has been authenticated for use on secured endpoints
    
    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:
    
        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL
    
        ``cookies``: A dictionary of cookies to be sent with every request
    
        ``headers``: A dictionary of headers to be sent with every request
    
        ``provider``: An implementation of httpx.Auth to use for authentication
    
        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.
    
        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.
    
        ``follow_redirects``: Whether or not to follow redirects. Default value is False.
    
        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.
    
    
    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
        provider: AuthProvider to use for authentication
    
    Method generated by attrs for class AuthenticatedClient.

    ### Instance variables

    `raise_on_unexpected_status: bool`
    :

    ### Methods

    `get_async_httpx_client(self) ‑> httpx.AsyncClient`
    :   Get the underlying httpx.AsyncClient, constructing a new one if not previously set

    `get_httpx_client(self) ‑> httpx.Client`
    :   Get the underlying httpx.Client, constructing a new one if not previously set

    `set_async_httpx_client(self, async_client: httpx.AsyncClient) ‑> blaxel.client.AuthenticatedClient`
    :   Manually the underlying httpx.AsyncClient
        
        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

    `set_httpx_client(self, client: httpx.Client) ‑> blaxel.client.AuthenticatedClient`
    :   Manually set the underlying httpx.Client
        
        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

    `with_cookies(self, cookies: dict[str, str]) ‑> blaxel.client.AuthenticatedClient`
    :   Get a new client matching this one with additional cookies

    `with_headers(self, headers: dict[str, str]) ‑> blaxel.client.AuthenticatedClient`
    :   Get a new client matching this one with additional headers

    `with_timeout(self, timeout: httpx.Timeout) ‑> blaxel.client.AuthenticatedClient`
    :   Get a new client matching this one with a new timeout (in seconds)

`Client(base_url: str = '', provider: httpx.Auth = None, *, raise_on_unexpected_status: bool = True, cookies: dict[str, str] = _Nothing.NOTHING, headers: dict[str, str] = _Nothing.NOTHING, timeout: httpx.Timeout | None = None, verify_ssl: str | bool | ssl.SSLContext = True, follow_redirects: bool = False, httpx_args: dict[str, typing.Any] = _Nothing.NOTHING)`
:   A class for keeping track of data related to the API
    
    The following are accepted as keyword arguments and will be used to construct httpx Clients internally:
    
        ``base_url``: The base URL for the API, all requests are made to a relative path to this URL
    
        ``cookies``: A dictionary of cookies to be sent with every request
    
        ``headers``: A dictionary of headers to be sent with every request
    
        ``provider``: An implementation of httpx.Auth to use for authentication
    
        ``timeout``: The maximum amount of a time a request can take. API functions will raise
        httpx.TimeoutException if this is exceeded.
    
        ``verify_ssl``: Whether or not to verify the SSL certificate of the API server. This should be True in production,
        but can be set to False for testing purposes.
    
        ``follow_redirects``: Whether or not to follow redirects. Default value is False.
    
        ``httpx_args``: A dictionary of additional arguments to be passed to the ``httpx.Client`` and ``httpx.AsyncClient`` constructor.
    
    
    Attributes:
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document. Can also be provided as a keyword
            argument to the constructor.
    
    Method generated by attrs for class Client.

    ### Instance variables

    `raise_on_unexpected_status: bool`
    :

    ### Methods

    `get_async_httpx_client(self) ‑> httpx.AsyncClient`
    :   Get the underlying httpx.AsyncClient, constructing a new one if not previously set

    `get_httpx_client(self) ‑> httpx.Client`
    :   Get the underlying httpx.Client, constructing a new one if not previously set

    `set_async_httpx_client(self, async_client: httpx.AsyncClient) ‑> blaxel.client.Client`
    :   Manually the underlying httpx.AsyncClient
        
        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

    `set_httpx_client(self, client: httpx.Client) ‑> blaxel.client.Client`
    :   Manually set the underlying httpx.Client
        
        **NOTE**: This will override any other settings on the client, including cookies, headers, and timeout.

    `with_cookies(self, cookies: dict[str, str]) ‑> blaxel.client.Client`
    :   Get a new client matching this one with additional cookies

    `with_headers(self, headers: dict[str, str]) ‑> blaxel.client.Client`
    :   Get a new client matching this one with additional headers

    `with_timeout(self, timeout: httpx.Timeout) ‑> blaxel.client.Client`
    :   Get a new client matching this one with a new timeout (in seconds)