# Networking

## What is a network

A network is a set of computers connected together. There are local networks with computers connected directly to each other. There is also the public domain which is all the computers connected together through the internet.

## What is an IP

IP is a unique number assigned to a computer. This IP allows them to access each other's machine. There are 2 IP addresses assigned to each computer, one for the local network and one for the public domain. IP Address usually follows the same format of `0.0.0.0` and the numbers range from 0 to 255.

## What is IPv4

Its an IP address of version 4, this is a specific protocol used to access a computer.

## Binary and IP

## Demo Calculating and IP with Binary

## Maximum number of IPs in IPv4

4,294,967,296

## What are Subnets

Subnet also known as a subnetwork, is a smaller segment of a network. This allows for a specific IP addresses being assigned to a machine and be only accessible on the subnetwork.

## Subnets - Class Networks

Subnet classes are made unique by the number of bits their IP addresses have dedicated to a network and the number of bits dedicated to hosts.  They each have a default subnet mask. Classes can be identified by the number in the first octet of their address.
</br>

[source](https://www.solarwindsmsp.com/blog/overview-of-subnet-classes#:~:text=Subnet%20classes%20are%20made%20unique,first%20octet%20of%20their%20address.)

## Subnets - Subnet masks

A subnet mask is a 32-bit number created by setting host bits to all 0s and setting network bits to all 1s. In this way, the subnet mask separates the IP address into the network and host addresses. The “255” address is always assigned to a broadcast address, and the “0” address is always assigned to a network address. Neither can be assigned to hosts, as they are reserved for these special purposes. The IP address, subnet mask and gateway or router comprise an underlying structure—the Internet Protocol—that most networks use to facilitate inter-device communication.
</br>

[source](https://avinetworks.com/glossary/subnet-mask/)

## CIDR Blocks

An IPv4 address consists of 32 bits. This becomes clear when you convert the decimal notation into the binary equivalent: 201.105.7.34 corresponds to 11001001 01101001 00000111 00100010. The binary notation – and the calculation method with which computers operate – of an IP address consists of 32 digits, which can either be 1 or 0: hence 32 bits. So, the possible suffixes in CIDR notation range from 0 to 32.
</br>

[source](https://www.ionos.co.uk/digitalguide/server/know-how/cidrclassless-inter-domain-routing/)

## Demo Calculating if two networks are able to communicate with CIDR blocks

## NAT

NAT or Network address translation, is a method of remapping an IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device.

## TCP

TCP or Transmission control protocol, which means a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control and -- because it is meant to provide error-free data transmission -- handles retransmission of dropped or garbled packets and acknowledges all packets that arrive.
</br>

[source](https://searchnetworking.techtarget.com/definition/TCP)

## OSI Model and Layers

The OSI Model (Open Systems Interconnection Model) is a conceptual framework used to describe the functions of a networking system. The OSI model characterizes computing functions into a universal set of rules and requirements in order to support interoperability between different products and software.

### Layers

1. Physical layer
2. Data link layer
3. Network layer
4. Transport layer
5. Session layer
6. Presentation layer
7. Application layer
