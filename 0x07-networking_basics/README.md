# Networking Basics #0

### OSI Model:

**What is OSI model?**

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers. It facilitates communication between different systems by providing a common understanding of networking functions.

**How many layers it has?**

The OSI model consists of seven layers, each with specific functions and responsibilities.

**How it is organized?**

The OSI model is organized into seven layers, namely:
- Physical Layer
- Data Link Layer
- Network Layer
- Transport Layer
- Session Layer
- Presentation Layer
- Application Layer

### LAN:
**What is a LAN?**

A LAN (Local Area Network) is a network that connects computers and devices within a limited geographical area, such as a home, office building, or school campus. It allows for the sharing of resources and information among connected devices.

**Typical usage of LAN?**

LANs are commonly used for tasks such as file sharing, printer sharing, accessing shared databases or servers, and facilitating communication between devices within the same physical location.

**Typical geographical size?**

The geographical size of a LAN is typically limited to a few kilometers or less, covering areas such as a single building, floor, or room.

### WAN:
**What is a WAN?**

A WAN (Wide Area Network) is a network that spans a large geographical area, connecting multiple LANs and other networks over long distances. It enables communication between devices located in different cities, countries, or continents.

**Typical usage?**

WANs are used for tasks such as connecting branch offices of a company, accessing the internet, transmitting data between cities or countries, and facilitating remote communication and collaboration.

**Typical geographical size?**

The geographical size of a WAN can vary significantly and may cover vast distances, ranging from hundreds of kilometers to global coverage.

### Internet:
**What is the Internet?**

The Internet is a global network of interconnected computers and devices that use standardized communication protocols to exchange data and information. It provides access to a vast array of resources, services, and information worldwide.

**What is an IP address?**

An IP (Internet Protocol) address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves as a unique identifier for the device within the network.

**What are the 2 types of IP address?**

The two types of IP addresses are IPv4 (Internet Protocol version 4) and IPv6 (Internet Protocol version 6).

**What is localhost?**

localhost refers to the local computer or device that a user is currently working on. It is commonly associated with the loopback IP address 127.0.0.1, which allows a device to communicate with itself.

**What is a subnet?**

A subnet is a logically segmented portion of a larger network, created by dividing a single IP network into multiple smaller sub-networks. Subnetting helps to improve network efficiency, security, and manageability.

**Why IPv6 was created?**

IPv6 was created to address the limitations of IPv4, such as the depletion of available IP addresses due to the exponential growth of internet-connected devices. IPv6 provides a much larger address space, improved security features, and enhanced support for mobile and wireless networks.

### TCP/UDP:
**What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)?**

The two main data transfer protocols for IP are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

**What is the main difference between TCP and UDP?**

The main difference between TCP and UDP is that TCP provides reliable, connection-oriented communication with features such as error checking, sequencing, and flow control, while UDP offers faster, connectionless communication without these reliability mechanisms.

**What is a port?**

A port is a logical endpoint used in network communication to identify a specific service or application running on a computer or device. Ports are assigned unique numbers ranging from 0 to 65535.

**Memorize SSH, HTTP, and HTTPS port numbers?**

- SSH (Secure Shell): Port 22
- HTTP (Hypertext Transfer Protocol): Port 80
- HTTPS (Hypertext Transfer Protocol Secure): Port 443

**What tool/protocol is often used to check if a device is connected to a network?**

Ping is a commonly used tool/protocol to check if a device is connected to a network. It sends ICMP (Internet Control Message Protocol) echo requests to the target device and waits for a response.

### What is MAC addres?

A MAC (Media Access Control) address, also known as a hardware address or physical address, is a unique identifier assigned to a network interface controller (NIC) for communication within a network. It is assigned by the manufacturer of the network interface and is embedded into the hardware of the device.

**Key points about MAC addresses:**

- Uniqueness: Each MAC address is globally unique. This means no two devices should have the same MAC address.

- Format: A MAC address is typically represented as a series of six pairs of hexadecimal digits separated by colons or hyphens. For example, 00:1A:2B:3C:4D:5E.

- Two Types: MAC addresses can be of two types: universally administered addresses (UAA) and locally administered addresses (LAA). UAAs are assigned by the manufacturer and are globally unique, while LAAs can be set by the network administrator and may not be globally unique.

- Layer 2 Address: MAC addresses operate at the data link layer (Layer 2) of the OSI model and are used for identifying devices within the same network segment.

- Not Routable: MAC addresses are not routable across different network segments or over the internet. They are used for communication within a local network.

- Used in Ethernet: MAC addresses are primarily associated with Ethernet networks, where they are used by the Ethernet protocol for addressing and delivering data packets to the correct destination.

Overall, MAC addresses play a crucial role in facilitating communication between devices within a local network, enabling devices to identify and communicate with each other at the data link layer.
