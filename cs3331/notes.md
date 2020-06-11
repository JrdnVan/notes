# Introduction to Computer Networks

## What is the internet?

- Millions of **connected computing devices**:
  - Hosts = end systems
    - e.g. Computers, smart phones.
  - Running network apps

- **Communication links**
  - Wired links:
    - Fiber, copper, radio, satellite
  - Wireless links:
    - Wi-Fi, 4G, 5G
  - Transmission rate: Bandwidth
    - How fast we can transmit data?
    - Bits
      - 1 Byte = 8 Bits

- **Packet switches**: forward packets (chunks of data)
  - routers and switches

### What is the internet: "nuts and bolts" view

- **Internet: "network of networks"**
  - Interconnected ISPs (Internet Service Provider)
- **Protocols** control sending and receiving of messages.
  - e.g., TCP (Transmission Control Protocol), IP (Internet Protocol), HTTP (Web), Skype (Interactive), 802.11 (Wi-Fi)
- **Internet Standards** 
  - RFC: Request for comments
  - IETF: Internet Engineering Task Force

### What is the internet: a service view

- **Infrastructure that provides services to applications**:
  - Web, VoIP, email, games, e-commerce, social nets, ...

- **Provides programming interface to apps**
  - Hooks that allow sending and receiving app programs to "connect" to Internet
  - Provides service options, analogous to postal service

### What is a protocol?

How computers talk to each other.

Protocols define format, order of messages sent and received among network entities and actions taken on message transmission.

#### Human protocols:

- "What's the time?"
- "I have a question"

#### Network Protocols:

- Machines rather than humans
  - Bytes
- All communcation activity in Internet governed by protocols.
- Example (In order):
  - TCP connection request
  - TCP connection response
  - GET request
  - File transmission

## Network Edge

End systems (Devices), access networks, links

### Access networks and physical media

Question: How do we connect end systems to edge routers?

- residential access nets
- institutional access networks (schools, company)
- mobile access networks
  
Keep in mind:

- Bandwidth (bits per second) of access network?
- Shared or dedicated?

#### Access net: Digital Subscriber Lines (DSL)

- uses **existing** telephone line to central office DSLAM
- Data over DSL phone line goes to **Internet**
- Voice over DSL phone line goes to **Telephone Net**

#### Access net: Cable network

- **HFC**: Hybrid Fiber Coax
  - Asymmetric: Up to 30mbps downstream transmission rate, 2Mbps upstream transmission rate

- **Network** of cable, fiber attaches homes to ISP router
  - Homes **share access network** to cable headend
  - Unlike DSL, which has dedicated access to central office

#### Enterprise access networks (Ethernet)

- Typically used in companies, universities, etc.
- 10Mbps, 100Mbps, 1Gbps, 10Gbps transmission rates
- Today, end systems typically connect to Ethernet

#### Wireless access networks

Shared wireless access network connects end system to router

  - via base station aka "access point"

Wireless LANs:
  - Within building (100ft)

Wide-area wireless access:
  - Provided by telco (cellular) operator

## Network Core

Packet switching, circuit switching, network structure

- A mesh of **interconnected routers/switches**
- Two forms of switched networks:
  - Circuit switching: used in legacy telephone networks
  - Packet switching: used in the Internet

### Circuit Switching (Feasible for Telephone)

End-end resources allocated to, reserved for "call" between source & destination.

- Dedicated resources: No sharing
  - circuit-like (guaranteed) performance

- Circuit segment idle if not used by call (no sharing)

- Commonly used in traditional telephone networks

#### FDM (Frequency) vs TDM (Time)

FDM: All users are on different frequencies, hence can all interact at once.

TDM: Each user is given a small portion of time to interact (usually in the form of milliseconds)

#### Why circuit switching is not feasible (for the internet)

- Inefficient
  - Computer communications tend to be very bursty. For example, viewing sequence of web pages.
  - Dedicated circuit can't be used or shared in periods of silence.
  - Can't adopt to network dynamics.

- Fixed data rate
  - Computers communicate at very diverse rates. For example, video browsing vs web browsing.
  - Fixed data rate not useful

- Connection state maintenance
  - Requires per communication state to be maintained that is a considerale overhead.
  - Not scalable.

### Packet Switching (Feasible for Internet)

- Data sent as chunks of formatted bits (Packets)
- Each packet consists of:
  - **Header**:
    - Holds instructions to network for how to handle said packet.
    - Contains: 
      - Internet address
      - Age (Time to Leave)
        - Delete packets after a certain amount of time.
      - Checksum to protect header.
  - **Payload**:
    - Contains data being carried.
- Switches **forward** packets based on information in headers.
- Each packet travels independently
  - No notion of packets belonging to a "circuit"
- No link resources are reserved in advance. Instead packet switching leverages **statistical multiplexing**

#### Statisical Multiplexing

Relies on the assumption that not all flow bursts at same time.

The "summation" of packets and their time slot.

If two or more packets have the same time slot, there'll be a **Transient Overload**.

- In this case, push the extra packets into a buffer/queue.
  - If buffer too full, may lead to packet drop/packet loss hence corrupted file. *

### Packet Switching vs Circuit Switching

Packet switching allows more users to use the network.

Example:
  - 1MB/s link
  - Each user:
    - 100kb/s when "active".
    - active 10% of the time.
  - **Circuit-Switching**:
    - 10 users
 
  - **Packet Switching**:
    - with 35 users, probability > 10 active at the same time is less than 0.0004%

### Internet Structure: Network of Networks

Access ISP's connect to Regional ISP's, which then connect to **Tier 1 ISPs**.

- Tier 1 ISPs are connected together by **Peering links**.
- They also join at **Internet Exchange Points (IXPs)**.

### Delay, loss, throughput in networks

#### How do loss and delay occur?

Packets queue in router buffers
- Packet **arrival** rate to link (temporarily) **exceeds** **output** link capacity.
- Packets queue, wait for turn.

#### Four sources of packet delay

```
d_nodal = d_processing_time + d_queue_time + d_transmission_time +
d_propagation_time
```

- d_processing_time = processing delay
  - The checking of bit errors
  - Determining output link
  - Typically less than a msec.
- d_queue_time = amount of packets in queue
  - Depends on congestion level of router
  - Time waiting at output link for transmission
- d_transmission_time = time needed for a packet to be transmitted into the link (Depends on bandwidth)
  - L: Packet length (bits)
  - R: Link bandwidth (bps)
  - d_transmission_time = L/R
- d_propagation_time = physical law; depends on speed of medium (Depends on speed of light)
  - D: Length of physical link
  - S: Propagation speed in medium (~2*10^8 m/sec)
  - d_propagation_time = D/S

#### Queueing delay

#### End to end delay