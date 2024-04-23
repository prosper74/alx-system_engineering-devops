# Web Servers

A web server is a software application responsible for serving web content to clients over the internet. Its primary role is to handle incoming requests from clients (typically web browsers) and deliver the appropriate response, which could be a webpage, an image, a file download, or any other content hosted on the server.

### What is a child process
A child process is a process that is spawned or created by another process, known as the parent process. Child processes inherit certain attributes and resources from their parent process but operate independently. In the context of web servers, child processes are often used to handle incoming client requests.

### Why web servers usually have a parent process and child processes
Web servers usually have a parent process and multiple child processes to handle incoming HTTP requests efficiently. The parent process manages the overall operation of the server, such as listening for incoming connections and spawning child processes as needed. Each child process is responsible for handling one or more client requests concurrently, allowing the server to serve multiple clients simultaneously.

### What are the main HTTP requests
The main HTTP requests are:

- GET: Requests data from a specified resource.
- POST: Submits data to be processed to a specified resource.
- PUT: Uploads a representation of a specified resource.
- DELETE: Deletes the specified resource.
- HEAD: Similar to GET but returns only the headers, not the actual data.
- OPTIONS: Returns the HTTP methods that the server supports for a specified URL.
- PATCH: Applies partial modifications to a resource.

### How the web works
The web works by clients (such as web browsers) sending HTTP requests to web servers, which then process these requests and return appropriate responses. These responses may include HTML documents, images, CSS files, JavaScript, or other resources necessary to render a web page in the client's browser.

### Nginx
Nginx is a popular open-source web server and reverse proxy server. It's known for its high performance, stability, and low resource consumption. Nginx is often used as a front-end web server to serve static content or as a reverse proxy to forward requests to other web servers or applications.

### How to Configure Nginx
To configure Nginx, you typically modify its configuration file, which is usually located in the /etc/nginx directory on Linux systems. The configuration file contains directives that define how Nginx should handle incoming requests, manage server resources, and interact with upstream servers or applications.

### Root and sub domain
Root and subdomains are part of the Domain Name System (DNS) hierarchy. The root domain is the highest level in the DNS hierarchy and is represented by a dot (.), while subdomains are subdivisions of the root domain. For example, in the domain example.com, "example" is the root domain, and "subdomain.example.com" is a subdomain.

### HTTP requests
HTTP (Hypertext Transfer Protocol) requests are the foundation of data communication on the World Wide Web. They are messages sent by a client (such as a web browser) to a server, specifying an action to be performed. There are several types of HTTP requests, each serving a different purpose:

### HTTP redirection
HTTP redirection is the process of forwarding a web browser from one URL to another. It's commonly used for URL redirection, where a server responds to a request for a specific URL with a redirect response containing the new URL to which the client should navigate.

### Not found HTTP response code
The "404 Not Found" HTTP response code indicates that the server could not find the requested resource. It's returned when the requested URL is not available on the server.

### Logs files on Linux
Logs files on Linux are typically stored in the /var/log directory. Web servers like Nginx usually have their log files stored in this directory, with filenames such as access.log for recording HTTP requests and error.log for recording server errors and warnings. These log files are useful for troubleshooting server issues, monitoring traffic, and analyzing server performance.
