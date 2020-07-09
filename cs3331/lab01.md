# Exercise 1: nslookup

## 1. Which is the IP address of the website www.koala.com.au? In your opinion, what is the reason of having several IP addresses as an output?

### Facts

- IP(Internet Protocol) addresses are assigned to each device connected to a computer network that uses IP for communication.
- IP addresses serve two main functions:
  - Host
  - Location addressing

### Answer

www.koala.com.au has IP addresses:
- 104.18.61.21
- 172.67.219.46
- 104.18.60.21

Having several IP addresses allow for sites to have different server locations, allowing users to connect to the closest server and reduce ping times and/or prevent connecting to an already congested server.

## 2. Find out the name of the IP address 127.0.0.1. What is special about this IP address?

The name of the IP address is:
- localhost

What's special about this IP address is that it allows for a network service to run locally (i.e. The server is hosted on the users machine).

# Exercise 2: Use ping to test host reachability:

Are the following hosts reachable from your machine by using ping:

## www.unsw.edu.au

- reachable (ping)
- reachable (website)

## www.getfittest.com.au

- unreachable (ping)
  - unknown host
- unreachable (website)

## www.mit.edu

- reachable (ping)
- reachable (website)

## www.intel.com.au

- reachable (ping)
- reachable (website)

## www.tpg.com.au

- reachable (ping)
- reachable (website)

## www.hola.hp

- unreachable (ping)
  - unknown host
- unreachable (website)

## www.amazon.com

- reachable (ping)
- reachable (website)

## www.tsinghua.edu.cn

- reachable (ping)
- reachable (website)

## www.kremlin.ru

- unreachable (ping)
  - firewall
- reachable (website)

## 8.8.8.8

- reachable (ping)
- unreachable (website)

# Exercise 3: Use traceroute to understand network topology

![](/traceroute1.png "")