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

## What is the internet: "nuts and bolts" view

- **Internet: "network of networks"**
  - Interconnected ISPs (Internet Service Provider)
- **Protocols** control sending and receiving of messages.
  - e.g., TCP (Transmission Control Protocol), IP (Internet Protocol), HTTP (Web), Skype (Interactive), 802.11 (Wi-Fi)
- **Internet Standards** 
  - RFC: Request for comments
  - IETF: Internet Engineering Task Force

## What is the internet: a service view

- **Infrastructure that provides services to applications**:
  - Web, VoIP, email, games, e-commerce, social nets, ...

- **Provides programming interface to apps**
  - Hooks that allow sending and receiving app programs to "connect" to Internet
  - Provides service options, analogous to postal service

## What is a protocol?

How computers talk to each other.

Protocols define format, order of messages sent and received among network entities and actions taken on message transmission.

### Human protocols:

- "What's the time?"
- "I have a question"

### Network Protocols:

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

