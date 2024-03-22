# Web infrastructure design

### Network Basics:

- Understanding network fundamentals such as IP addressing, subnetting, routing, and protocols like TCP/IP and UDP is crucial.
- Familiarity with network hardware such as routers, switches, and firewalls is also important.

### Server:

A server is a computer or a system that provides resources, data, or services to other computers, known as clients, over a network.
Servers can serve various purposes, including file storage, web hosting, email, database management, and more.

### Web Server:

A web server is a type of server that delivers web content to clients over the internet or an intranet.
It receives requests from clients (web browsers) and responds with the requested web pages, typically using HTTP or HTTPS protocols.
Examples include Apache HTTP Server, Nginx, Microsoft Internet Information Services (IIS), etc.

### DNS (Domain Name System):

DNS is a decentralized naming system for computers, services, or other resources connected to the Internet or a private network.
It translates domain names (e.g., www.example.com) into IP addresses that computers use to identify each other.
DNS servers maintain a distributed database of domain names and their corresponding IP addresses.

### Load Balancer:

A load balancer distributes incoming network traffic across multiple servers to ensure high availability and reliability.
It helps prevent overloading of individual servers and improves performance and scalability.
Load balancers can be hardware-based or software-based and can operate at various layers of the OSI model.

### Monitoring:

Monitoring involves observing and analyzing the performance and health of a system or network.
Monitoring tools collect data on metrics such as CPU usage, memory usage, network traffic, and application performance.
Monitoring helps identify issues, troubleshoot problems, and optimize system performance.

### Database:

A database is an organized collection of structured data stored electronically in a computer system.
It allows users to store, retrieve, manipulate, and manage data efficiently.
Examples include relational databases like MySQL, PostgreSQL, NoSQL databases like MongoDB, and cloud-based databases like Amazon RDS, Google Cloud SQL, etc.

### Difference Between Web Server and App Server:

A web server primarily serves static content (HTML pages, images, etc.) over the web.
An app server hosts and executes application logic, handling dynamic content generation and processing requests from clients.

### DNS Record Types:

Common DNS record types include:
A (Address) records: Maps domain names to IPv4 addresses.
AAAA (IPv6 Address) records: Maps domain names to IPv6 addresses.
CNAME (Canonical Name) records: Alias of one domain name to another.
MX (Mail Exchange) records: Specifies mail servers responsible for receiving email.
NS (Name Server) records: Specifies authoritative name servers for the domain.

### Single Point of Failure:

A single point of failure is a component in a system whose failure would cause the entire system to stop working.
It poses a risk to system reliability and uptime because if the single point of failure fails, the entire system becomes unavailable.

### Avoiding Downtime When Deploying New Code:

Use rolling deployments: Gradually update servers one by one instead of all at once to minimize downtime.
Blue-green deployments: Deploy new code to a separate environment (green) and switch traffic once it's stable, avoiding downtime.
Canary deployments: Roll out new code to a small subset of users first and gradually increase the rollout if everything is working as expected.

### High Availability Cluster (Active-Active/Active-Passive):

A high availability cluster is a group of interconnected servers or systems designed to ensure continuous operation and minimize downtime.
In an active-active configuration, all servers actively handle incoming requests, providing load balancing and redundancy.
In an active-passive configuration, one server (active) handles incoming requests while others (passive) remain on standby, ready to take over if the active server fails.

### HTTPS (Hypertext Transfer Protocol Secure):

HTTPS is a secure version of HTTP that encrypts data transmitted between a web server and a client (e.g., web browser).
It uses SSL/TLS protocols to encrypt data, providing confidentiality, integrity, and authentication.
HTTPS is essential for secure communication over the internet, particularly for transmitting sensitive information like passwords, payment details, etc.

### Firewall:

A firewall is a network security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
It acts as a barrier between a trusted internal network and untrusted external networks (e.g., the internet), protecting against unauthorized access and cyber threats.
Firewalls can be implemented as hardware appliances, software applications, or a combination of both.
