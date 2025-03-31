# System Design Table of Contents

## 1. Introduction to System Design

* 1.1. What is System Design?
* 1.2. Importance of System Design
* 1.3. Components of a System
* 1.4. System Design Preparation
    * 1.4.1. Prerequisite Subjects (MAKAUT)
        * Computer Organization and Architecture
        * Operating Systems
        * Object-Oriented Programming
        * Software Engineering
        * Computer Networks
        * Database Management
        * Distributed Database Management
        * Big Data
    * 1.4.2. Recommended Resources
        * System Design Roadmap
        * System Design Primer (repo)
        * Designing Data-Intensive Applications (Martin Kleppmann)
        * System Design Interview (Alex Xu)
        * Building Microservices
        * LeetCode Discuss System Design
        * YouTube Playlists (High-Level Design, Low-Level Design)
    * 1.4.3. Problem Approach Template

## 2. Design Principles

* 2.1. SOLID Principles
* 2.2. DRY (Don't Repeat Yourself)
* 2.3. KISS (Keep It Simple, Stupid)
* 2.4. YAGNI (You Aren't Gonna Need It)

## High-Level Design (HLD)

### 3. System Design Basics (HLD)

* 3.1. Requirements Gathering (HLD)
* 3.2. High-Level System Architecture (HLD)
* 3.3. Breaking Down Components (HLD)

### 4. Scalability and Performance (HLD)

* 4.1. Horizontal vs. Vertical Scaling (HLD)
* 4.2. Load Balancing (HLD)
* 4.3. Caching (HLD)
    * 4.3.1. Cache Invalidation (HLD)
    * 4.3.2. Cache Eviction (HLD)
* 4.4. Database Sharding (Horizontal & Vertical Partitioning) (HLD)
* 4.5. CDN (Content Delivery Network) (HLD)

### 6. Databases and Data Models (HLD)

* 6.1. Relational vs. NoSQL (HLD)
* 6.2. ACID Properties (HLD)
* 6.3. CAP Theorem (HLD)
* 6.4. SQL vs NoSQL, When to Use Which DB (HLD)

### 7. API Design (HLD)

* 7.1. REST vs. GraphQL (HLD)
* 7.2. API Versioning (HLD)
* 7.3. Rate Limiting (e.g. Design Rate Limiter) (HLD)
* 7.4. Authentication & Authorization (HLD)

### 8. Concurrency and Multithreading (HLD)

* 8.1. Threading Models (HLD)
* 8.2. Asynchronous Processing (HLD)
* 8.3. Message Queues (e.g., Kafka) (HLD)

### 9. Microservices and Distributed Systems (HLD)

* 9.1. Microservices Architecture (HLD)
* 9.2. Event-Driven Design (HLD)
* 9.3. Data Consistency Models (HLD)
* 9.4. Microservices Imp. Design Patterns (SAGA pattern, Strangler Pattern) (HLD)

### 10. High Availability and Fault Tolerance (HLD)

* 10.1. Redundancy (HLD)
* 10.2. Replication (HLD)
* 10.3. Failover Systems (HLD)

### 11. Security Considerations (HLD)

* 11.1. Data Encryption (HLD)
* 11.2. Secure API Design (HLD)
* 11.3. Authentication and Authorization (HLD)

### 12. Monitoring and Maintenance (HLD)

* 12.1. Logging (HLD)
* 12.2. Metrics Collection (HLD)
* 12.3. Alerting (HLD)

### 13. Networking and Storage (HLD)

* 13.1. Network Protocols (TCP, Websocket, HTTP, etc.) (HLD)
* 13.2. Client-Server vs. Peer-to-Peer Architecture (HLD)
* 13.3. Proxy Servers (HLD)
* 13.4. CDN (HLD)
* 13.5. Storage Types (HLD)
    * 13.5.1. Block Storage (HLD)
    * 13.5.2. File Storage (HLD)
    * 13.5.3. Object Storage (S3) (HLD)
    * 13.5.4. RAID (HLD)
* 13.6. File Systems (Google File System, HDFS) (HLD)

### 14. Advanced Concepts (HLD)

* 14.1. Consistent Hashing (HLD)
* 14.2. Bloom Filter (HLD)
* 14.3. Merkle Tree, Gossiping Protocol (HLD)
* 14.4. Leader Election (HLD)

### 15. High-Level Design Case Studies (HLD)

* 15.1. Scale from 0 to Million Users (HLD)
* 15.2. URL Shortening (HLD)
* 15.3. Back of the Envelope Estimation (HLD)
* 15.4. Key-Value Store (HLD)
* 15.5. Design WhatsApp (HLD)
* 15.6. Design Search Autocomplete System / Typeahead System (HLD)
* 15.7. Design Notification System (HLD)
* 15.8. Design Pastebin (HLD)
* 15.9. Design Twitter (HLD)
* 15.10. Design Dropbox (HLD)
* 15.11. Design Instagram (HLD)
* 15.12. Design YouTube (HLD)
* 15.13. Design Google Drive (HLD)
* 15.14. Design Web Crawler (HLD)
* 15.15. Design Facebook News Feed / Newsfeed System (HLD)
* 15.16. Design Ticket Master (HLD)
* 15.17. Design NearByFriends or Yelp (HLD)
* 15.18. Design Learning Management System (HLD)
* 15.19. Design Community Discussion Platform (HLD)
* 15.20. Design Food delivery app like Swiggy and Zomato (HLD)

## Low-Level Design (LLD)

### 5. Design Patterns (LLD)

* 5.1. Overview of Design Patterns (LLD)
* 5.2. Types of Design Patterns (LLD)
    * 5.2.1. **Creational Patterns** (LLD)
        * Singleton (e.g., Design ATM) (LLD)
        * Factory (e.g., Design Parking Lot) (LLD)
        * Abstract Factory (e.g., Design Snake n Ladder game) (LLD)
        * Builder (e.g., Design Chess game) (LLD)
        * Prototype (e.g., Design File System) (LLD)
    * 5.2.2. **Structural Patterns** (LLD)
        * Adapter (e.g., Design Vending Machine) (LLD)
        * Composite (e.g., Design BookMyShow & Concurrency handling) (LLD)
        * Decorator (e.g., Design Pizza Billing System) (LLD)
        * Proxy (e.g., Design Car Rental System) (LLD)
        * Bridge (e.g., Design Splitwise) (LLD)
        * Façade (e.g., Splitwise Simplify Algorithm) (LLD)
        * Flyweight (e.g., Design CricBuzz / CricketInfo) (LLD)
    * 5.2.3. **Behavioral Patterns** (LLD)
        * Observer (e.g., Design Notify-Me Button Functionality) (LLD)
        * Strategy (e.g., SOLID principles) (LLD)
        * Chain of Responsibility (e.g., Design Elevator System) (LLD)
        * Null Object (e.g., Design Logging System) (LLD)
        * State (e.g., Design Tic-Tac-Toe game) (LLD)
        * Command (e.g., Design True Caller) (LLD)
        * Interpreter (LLD)
        * Iterator (e.g., Design Online Hotel Booking System) (LLD)
        * Mediator (e.g., Design Library Management System) (LLD)
        * Memento (e.g., Design Traffic Light System) (LLD)
        * Template Method (e.g., Design Meeting Scheduler) (LLD)
        * Visitor (e.g., Design Online Voting System) (LLD)
* 5.3. Applying Design Patterns in System Design (LLD)
* 5.4. Common Use Cases for Design Patterns (LLD)

### 16. Low-Level Design Case Studies (LLD)

* 16.1. Design Inventory Management System (LLD)
* 16.2. Design Cache Mechanism (LLD)
* 16.3. Design LinkedIn (LLD)
* 16.4. Design Amazon (LLD)
* 16.5. Design Airline Management System (LLD)
* 16.6. Design Stock Exchange System (LLD)
* 16.7. Design Calendar Application (LLD)
* 16.8. Design (LLD) Payment System (LLD)
* 16.9. Design (LLD) Chat based system (LLD)
* 16.10. Design Restaurant Management System (LLD)
* 16.11. Design Bowling Alley Machine (LLD)
* 16.12. Design (LLD) Rate Limiter (LLD)