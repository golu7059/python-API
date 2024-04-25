# API in python 

`What is an API?` .

__API__ stands for “Application Programming Interface.” In simple terms, it’s a set of rules and protocols that allow how different software applications can communicate and interact with each other. APIs define the methods and data formats that applications can use to request and exchange information. To retrieve data from a web server, a client application initiates a request, and the server responds with the requested data. APIs facilitate this communication by serving as intermediaries, allowing seamless integration between diverse software systems. In essence, APIs act as bridges that enable the smooth exchange of data and functionality, enhancing interoperability across various applications.
```
 pip install requests
```
#### to install the request module that will handle the API requests

```
import requests
```
#### To import requests in file


## API Status Codes : 

As we know Status code tells us about what happened with our request, whether it was successfully executed or other was some error while processing it. They are returned with every request we place.

Codes related to “GET” request:

> `200 OK` : The server successfully processed the request, and the requested data is returned.

> `201 Created` : A new resource is created on the server as a result of the request.

> `204 No Content` : The request is successful, but there is no additional data to return.

> `300 Multiple Choices` : The requested resource has multiple representations, each with its own URL.

> `302 Found (Temporary Redirect)` : The requested resource is temporarily located at a different URL.

> `304 Not Modified` : The client’s cached copy of the resource is still valid, and no re-download is necessary.

> `400 Bad Request` : The request has malformed syntax or contains invalid data, making it incomprehensible to the server.

> `401 Unauthorized` : Authentication is required, and the client’s credentials (e.g., API key) are missing or invalid.

> `500 Internal Server Error` : An unexpected server error occurred during request processing.

> `502 Bad Gateway` : Acting as a gateway or proxy, the server received an invalid response from an upstream server.

These status codes help communicate the outcome of API requests and guide developers and clients in understanding the results, errors, or necessary actions.