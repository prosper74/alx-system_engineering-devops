# Load Balancer
This repository contains code and configuration files for a Load Balancer. Load balancing is a critical component in distributed systems architecture, ensuring optimal distribution of incoming network traffic across multiple servers or resources, thus improving reliability, scalability, and performance.

### Features
- Distribution of Incoming Traffic: The load balancer evenly distributes incoming requests among a pool of backend servers based on predefined algorithms.
- Health Checking: Regular health checks are performed on backend servers to ensure they are operational. Unhealthy servers are temporarily removed from the pool.
- Scalability: The load balancer can easily scale by adding or removing backend servers without affecting the overall system.
- Fault Tolerance: Provides fault tolerance by rerouting traffic away from failed servers to healthy ones.
- Session Persistence: Optionally supports session persistence, directing requests from the same client to the same backend server to maintain session state.

### Configuration
- Configure the load balancer settings such as IP addresses, ports, and routing algorithms in the config.yml file.
- Add backend servers to the configuration file along with their IP addresses and ports.

### Configuration Options
- IP Address: The IP address where the load balancer listens for incoming requests.
- Port: The port number on which the load balancer listens for incoming requests.
- Algorithm: The load balancing algorithm to use (e.g., Round Robin, Least Connections, IP Hash).
- Health Check Interval: The frequency of health checks performed on backend servers.
- Session Persistence: Enable or disable session persistence.
- Backend Servers: List of backend servers with their IP addresses, ports, and health check endpoints.