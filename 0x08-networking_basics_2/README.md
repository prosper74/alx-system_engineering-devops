# Networking Basics #1

### What is localhost/127.0.0.1?

- **localhost:** It refers to the local computer or device that you are currently working on. When you access localhost, you are connecting to your own machine.

- **127.0.0.1:** This is the loopback IP address assigned to the localhost. It is a special-purpose IP address used to establish a connection to the same device. Requests made to 127.0.0.1 are routed back to the local machine without going through the network.

### What is 0.0.0.0?

- **0.0.0.0:** It is a special-purpose IP address used to represent "all addresses" or "any address" in networking contexts. When used as a listening address, it indicates that the service should listen on all available network interfaces.

### What is /etc/hosts?

- **/etc/hosts:** It is a plain text file used by the operating system to map hostnames to IP addresses before querying DNS servers. It allows users to manually specify mappings between domain names and IP addresses, bypassing the DNS lookup process. This file is commonly used for local network configurations and resolving domain names locally.

### How to display your machine’s active network interfaces?

To display your machine's active network interfaces, you can use various commands depending on your operating system:

- On Linux/Unix-based systems, you can use the ifconfig command or the newer ip addr command to display network interface information.

- On Windows, you can use the ipconfig command to display network interface information.

These commands will provide details such as the interface name, IP address, MAC address, network mask, and other relevant information for each active network interface on your machine.
