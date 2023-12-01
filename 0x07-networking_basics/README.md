# Networking Fundamentals #0

This particular assignment marked the commencement of two modules dedicated to elucidating networking principles. During this project, I engaged in addressing questions structured like quizzes and scripting in Bash, concurrently gaining insights into the OSI model, LAN and WAN networks, as well as TCP/UDP data transfer protocols.

## Objectives 📄

* **0. Understanding the OSI model**
  * [0-OSI_model](./0-OSI_model): A document responding to the subsequent inquiries:
  * What defines the OSI model?
    1. A set of specifications that manufacturers of network hardware must adhere to
    2. The OSI model serves as a conceptual framework characterizing the communication functions of a telecommunication system, irrespective of its underlying internal structure and technology.
    3. The OSI model provides a framework characterizing the communication functions of a telecommunication system, emphasizing its underlying internal structure and technology.
  * How is the OSI model structured?
    1. Alphabetically
    2. From the lowest to the highest level
    3. Randomly

* **1. Exploring Network Types**
  * [1-types_of_network](./1-types_of_network): A document addressing the following questions:
  * What network type is a computer locally connected to?
    1. Internet
    2. WAN
    3. LAN
  * What network type could link an office in one building to another office in a building a few streets away?
    1. Internet
    2. WAN
    3. LAN
  * What network is utilized when browsing www.google.com from a smartphone (not connected to WiFi)?
    1. Internet
    2. WAN
    3. LAN

* **2. Understanding MAC and IP Addresses**
  * [2-MAC_and_IP_address](./2-MAC_and_IP_address): A document elucidating the subsequent queries:
  * What constitutes a MAC address?
    1. The name of a network interface
    2. The unique identifier of a network interface
    3. A network interface
  * What defines an IP address?
    1. Similar to what a postal address is to houses, it is for devices connected to a network
    2. The unique identifier of a network interface
    3. A number employed by network devices to connect to networks

* **3. Insights into UDP and TCP**
  * [3-UDP_and_TCP](./3-UDP_and_TCP): A document addressing the subsequent questions:
  * Which statement accurately characterizes the TCP box:
    1. It is a protocol that transfers data slowly but reliably
    2. It is a protocol that transfers data rapidly and may lose data in the process
  * Which statement accurately characterizes the UDP box:
    1. It is a protocol that transfers data slowly but reliably
    2. It is a protocol that transfers data rapidly and may lose data in the process
  * Which statement accurately characterizes the TCP worker:
    1. Have you received boxes x, y, z?
    2. May I increase the rate at which I am sending you boxes?

* **4. TCP and UDP Ports**
  * [4-TCP_and_UDP_ports](./4-TCP_and_UDP_ports): A Bash script revealing listening ports.
  * Exclusively displaying listening sockets.
  * Providing the PID and name of the program to which each socket belongs.

* **5. Verifying the Presence of a Host on the Network**
  * [5-is_the_host_on_the_network](./5-is_the_host_on_the_network): A Bash script conducting 5 ping attempts to an IP address provided as an argument.
  * Usage: `5-is_the_host_on_the_network {IP_ADDRESS}`.
