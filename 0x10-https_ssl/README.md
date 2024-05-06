# HTTPS SSL

### What is HTTPS SSL 2 main roles
- **Data Encryption:** One of the primary roles of HTTPS SSL (Secure Sockets Layer) is to encrypt data transmitted between a client (such as a web browser) and a server. This encryption ensures that even if intercepted, the data cannot be easily read by unauthorized parties.
- **Authentication:** SSL certificates are used to authenticate the identity of the website or server to ensure that users are connecting to the intended destination. This helps prevent man-in-the-middle attacks where a malicious third party intercepts and alters communication between the client and server.

### The purpose of encrypting traffic:
Encrypting traffic serves to protect sensitive information from unauthorized access while it's being transmitted over the internet. Without encryption, data such as passwords, credit card details, or personal information could be intercepted and read by malicious actors. Encryption scrambles this data into unreadable ciphertext, which can only be deciphered by someone with the correct decryption key.

### SSL termination:
SSL termination, also known as SSL offloading or SSL acceleration, refers to the process of decrypting encrypted SSL/TLS traffic at the termination point, typically at a load balancer or proxy server, before forwarding it to the backend servers. This allows the backend servers to process the traffic in plaintext, which can improve performance and reduce the computational burden on the servers. Additionally, SSL termination enables the inspection of decrypted traffic for security purposes, such as scanning for malware or monitoring for suspicious activity.

### Usage
- Add the subdomains from task 0 and wait for them to propagate
- create our ssh key and copy the public key
- connect to your lb-01 server and add the ssh public key to authorization keys
- open the log file `com_log` in this repository and run all the commands



100.25.134.50
54.87.235.110
54.237.43.50