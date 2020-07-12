# Week 1

### What is meant by the term statistical multiplexing?

- Data sent by multiple users is sent via a link.
- If one user doesn't use its **share** of bandwidth, it is then free to be used by other users.

Hence, senders share the link bandwidth, with no user having all the link bandwidth allocated to them.

### Consider two hosts, A and B, connected by a single link of rate R bps. Suppose that the two hosts are separated by m meters, and suppose the propagation speed along the link is s meters/sec. Host A is to send a packet of size L bits to Host B. 

a -R- b
|-----| m meters
propagation speed: s m/s

1) Propagation delay: d_prop = length/speed = m/s
2) Transmission time: d_trans = bits/link_rate = L/R
3) End-to-end delay (ignore processing & queuing delays) = d_prop + d_trans = m/s + L/R

### It takes a single bit ten times longer to propagate over a 10Mb/s link than over a 100Mb/s link. True or False?
False, propagation delay isn't dependent on bps.

### Suppose users share a 1Mbps link. Also suppose each user requires 100 kbps when transmitting, but each user transmits only 10 percent of the time. 

(a) When circuit switching is used, how many users can be supported?
    - 10 Users.

(b) Suppose packet switching is used for the rest of the problem. Find the probability that a given user is transmitting.
    - 0.1

(c) Suppose there are x users. Find the probability that at any given time, exactly n users are transmitting simultaneously.
    - (x n)(p^n)(1-p)^x-n

###  Suppose there is exactly one packet switch between a sending host and the receiving host. Assume that the transmission speed of the links between the sending host and the switch and the switch and the receiving host are R1 and R2 respectively. Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L? Ignore queuing, propagation and processing delays. Ignoring queuing, propagation and processing delays.

end-to-end delay = d_proc + d_prop + d_queue + d_trans

d_trans = bits/link_rate = L/R1 + L/R2

### Why is SMTP not used for transferring e-mail messages from the recipient’s mail server to the recipient’s personal computer? 
Because SMTP is a push protocol, not a pull protocol.

# NOTES

TOTAL DELAY = (nhops)(d_prop + d_trans) + (n-1)(d_trans)

Throughput(how much data being sent(?)) = n_bits / total_delay

Queue delay: if R_1 > R_2
    - delay = L/R_2 - L/R_1

#### File distribution time (Client-Server vs P2P)
Client-Server:
- Must send N copies:
  - Time for one copy: F/u_s
  - Time for N copies: N*F/u_s
- Each client must download file copy
  - d_min = min client download rate
  - client download time = F/d_min
- Therefore time to distribute file F to N clients >= max{N*F/u_s, F/d_min}

P2P:
- Must send at least one copy
  - time to send one copy: F/u_s
- Client msut download file copy:
  - client download time: f/d_min
- Clients as aggregate must download NF bits
  - Max upload rate (limiting max download rate) is u_s + summation(u_i)
- Therefore time to distribute file F to N clients >= max{F/u_s, f/d_min, NF/(u_s + summation(u_i, i = 1..N))}

EstimatedRTT for TCP round trip timeout: eRTT = (1-a)eRTT - (a)(sRTT)
    - where a usually 0.125