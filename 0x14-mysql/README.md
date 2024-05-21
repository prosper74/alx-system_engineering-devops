# MySQL

### What is the main role of a database
The main role of a database is to efficiently store, manage, and retrieve data. It serves as a structured collection of data that can be easily accessed, managed, and updated. Databases are used in various applications and systems to handle vast amounts of data in a structured manner, ensuring data integrity, security, and reliability.

### What is a database replica
A database replica is a copy of a database that is synchronized with the original database in near real-time or at regular intervals. It's created and maintained to provide redundancy and improve the availability, fault tolerance, and performance of the database system.

### The purpose of a database replica is multifold:
- **High availability:** Replicas can serve as backups in case the primary database fails, ensuring continuous access to data.
- **Load balancing:** Replicas can distribute read queries, reducing the load on the primary database and improving overall system performance.
- **Disaster recovery:** Replicas provide a failover mechanism in case of catastrophic events or data corruption in the primary database.
- **Geographic distribution:** Replicas can be placed in different geographical locations to serve users in various regions efficiently.

### Why database backups need to be stored in different physical locations
Database backups need to be stored in different physical locations to mitigate the risk of data loss due to disasters such as fires, floods, earthquakes, or other events that could damage or destroy the primary data center. Storing backups in diverse locations ensures that even if one location is compromised, the backups in other locations remain intact, thus preserving data integrity and facilitating disaster recovery.

### What operation should you regularly perform to make sure that your database backup strategy actually works
To ensure that your database backup strategy actually works, you should regularly perform backup validation or testing. This involves:

- **Automated backups:** Regularly scheduled backups should be performed automatically without manual intervention to ensure consistency and reliability.
- **Validation testing:** Periodically restore backups to a test environment to ensure that the backup files are not corrupted and can be successfully restored.
- **Recovery drills:** Simulate disaster scenarios and attempt to recover data from backups to verify that the backup and recovery procedures are effective.
- **Monitoring and alerts:** Implement monitoring systems to detect backup failures or anomalies, and set up alerts to notify administrators of any issues that arise during the backup process.

## Task 0.
Follow the steps in the installation_guide file

## Task 1.
- create the setup.sql file in both servers, use `pwd` to check your working directory.
- login to sql server and run the below command
```
source /home/ubuntu/setup.sql
```
