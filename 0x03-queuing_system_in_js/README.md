Queuing System in Node.js

Redis (Remote Dictionary Server) is an open-source, in-memory data structure store that is widely used as a database, cache, and message broker. It is known for its speed, flexibility, and ease of use.

# Background Context
Learn to create a queuing system using Node.js, Redis, and Kue.

## Resources

Redis Quick Start
Node Redis Client
Kue - Job Queue
Learning Objectives
By the end of this project, you should be able to explain:

## How to run a Redis server on your machine.

Basic operations with the Redis client using Node.js.
How to store hash values in Redis.
Handling asynchronous operations with Redis.
Using Kue for job queues.
Building a basic Express app that interacts with Redis and a queue.
Requirements
Node.js Scripts
Code should be interpreted/compiled on Ubuntu 18.04 LTS using Node 12.x and Redis 5.0.7.
All files should end with a new line.
A README.md file at the root of the project folder is mandatory.
Code should use the .js extension.

## Install a Redis Instance

Objective: Install and run a Redis server.

Instructions:

Download, extract, and compile Redis:

wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make


## Start Redis in the background:

src/redis-server &

## Verify the server is running:

src/redis-cli ping

## Set and get a value in Redis:

src/redis-cli set Holberton School
src/redis-cli get Holberton

## Kill the server:

kill [PID_OF_Redis_Server]
