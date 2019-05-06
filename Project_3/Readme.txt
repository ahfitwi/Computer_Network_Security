===============================================================================
* *********************Project3: Network Scan Detection ***********************
===============================================================================
@Alem Fitwi, April 2018
afitwi1@binghamton.edu
Network Computer Security - EECE580F
Department of Electrical & Computer Engineering
Watson Graduate School of Engineering & Applied Science
The State University of New York @ Binghamton
-------------------------------------------------------------------------------
Contents:
  A- Major tasks ==> NMAP scanning & Network scansdetection using a python code
  B- SCANS ==> nmap scanning switch, targets, number of scans, scan identifying 
               flag or protocol, & log name
  C- Location of source code, logfiles, and report
  D- Instructive Information to the reader of this 'readme' file
  E- Warning: beware of IP Localhost in lieu of real IP Address
  F- References used to understand packet parsing using python
-------------------------------------------------------------------------------
A- Major Tasks:
**************
 1) Perform scanning and collect logs of scanns saved using --> 
                              tcpdump –i any –Q in > tcpdump_(log_name).log 
 2) Write a python code that detects scanning activity on a network by 
                              analyzing the recorded logs.
-------------------------------------------------------------------------------
B-SCANS ==> NMAP Target-IP-Address SWITCH ==> SWITCH = -F, or -O, etc
**************
The scans made and their corresponding logs are enumerated in what ensues. 
Totally, 12 logs were recorded and collected from the VMs set-ups
1) No scan:While recording the log on the monitoring VM, no scanning was made  
   from the attacking machine. Only normal Internet browsing traffics!
           ---> NMAP SCAN: not done
           ---> Identifying Flag/protocol: no 
           ---> log name: tcpdump_no_scan_1.log

2) -F scan:While recording the logs on the monitoring VM, -F scans were made 
    three times as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.129 -F  
                           nmap 192.168.184.132 -F
                           nmap 192.168.184.129 -F
           ---> Identifying Flag/protocol: "Flags [S]"
           ---> log name: tcpdump_F_scan_2.log  ===> it logs the 3 nmap scans 
                    with switch=-F, which were done one after the other

3) -sF scan:While recording the logs on the monitoring VM, three -sF scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.129 -sF  
                           nmap 192.168.184.132 -sF
                           nmap 192.168.184.129 -sF
           ---> Identifying Flag/protocol: "Flags [F]"
           ---> Log name:tcpdump_sF_scan_3.log  ===> it logs the 3 nmap scans 
                with switch=-sF, which were done one after the other

4) -sO scan:While recording the logs on the monitoring VM, three -sO scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.129 -sO  
                           nmap 192.168.184.132 -sO
                           nmap 192.168.184.129 -sO
           ---> Identifying Flag/protocol: "ip-proto"
           ---> Log name:tcpdump_sO_scan_4.log  ===> it logs the 3 nmap scans 
                with switch=-sO, which were done one after the other

5) -sS scan:While recording the logs on the monitoring VM, three -sS scans were 
   made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.129 -sS 
                           nmap 192.168.184.132 -sS
                           nmap 192.168.184.129 -sS
           ---> Identifying Flag/protocol: "Flags [F]"
           ---> Log name:tcpdump_sS_scan_5.log  ===> it logs the 3 nmap scans 
                with switch=-sS, which were done one after the other.

6) -sN scan:While recording the logs on the monitoring VM, three -sN scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.129 -sN 
                           nmap 192.168.184.132 -sN
                           nmap 192.168.184.129 -sN
           ---> Identifying Flag/protocol: "Flags [none]"
           ---> Log name:tcpdump_sN_scan_6.log  ===> it logs the 3 nmap scans 
                with switch=-sN, which were done one after the other

7) -sU scan:While recording the logs on the monitoring VM, three -sU scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.132 -sU
                           nmap 192.168.184.129 -sU
                           nmap 192.168.184.132 -sU
           ---> Identifying Flag/protocol: "UDP"
           ---> Log name:tcpdump_sU_scan_7.log  ===> it logs the 3 nmap scans 
                with switch=-sU, which were done one after the other

8) -sT scan:While recording the logs on the monitoring VM, three -sT scans were 
   made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.132 -sT
                           nmap 192.168.184.129 -sT
                           nmap 192.168.184.132 -sT
           ---> Identifying Flag/protocol: "Flags [S]"
           ---> Log name:ttcpdump_sT_scan_8.log  ===> it logs the 3 nmap scans 
                with switch=-sT, which were done one after the other

9) -sn scan:While recording the logs on the monitoring VM, three -sn scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.132 -sn
                           nmap 192.168.184.129 -sn
                           nmap 192.168.184.132 -sn
           ---> Identifying Flag/protocol: "Broadcast"
           ---> Log name:tcpdump_sn_scan_9.log  ===> it logs the 3 nmap scans 
                with switch=-sn, which were done one after the other

10) -O scan:While recording the logs on the monitoring VM, three -O scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.132 -O
                           nmap 192.168.184.129 -O
                           nmap 192.168.184.132 -O
           ---> Identifying Flag/protocol: "Flags [S]" or "Flags [R.]"
           ---> Log name:tcpdump_O_scan_10.log  ===> it logs the 3 nmap scans 
                with switch=-O, which were done one after the other

11) -sX scan:While recording the logs on the monitoring VM, 3 -sX scans were 
    made as delineated below:
           ---> NMAP SCAN: nmap 192.168.184.132 -sX
                           nmap 192.168.184.129 -sX
                           nmap 192.168.184.132 -sX
           ---> Identifying Flag/protocol: Flags [FPU] or Flags [R.]
           ---> Log name:tcpdump_sX_scan_11.log  ===> it logs the 3 nmap scans
                with switch=-sX, which were done one after the other

12) -F, -sF, -sO, -sS, -sN,-sU, -sT, -sn, -O, and -sX. Totally 12 scans were 
    logged inot a single log file:
           ---> NMAP SCAN: nmap 192.168.184.132 -F
                           nmap 192.168.184.132 -sF
                           nmap 192.168.184.132 -sO
                           nmap 192.168.184.132 -sS
                           nmap 192.168.184.132 -sN
                           nmap 192.168.184.132 -sU
                           nmap 192.168.184.132 -sT
                           nmap 192.168.184.132 -sn
                           nmap 192.168.184.132 -O
                           nmap 192.168.184.132 -sX
           ---> Identifying Flag/protocol: all those stated 2 through 11
           ---> Log name:tcpdump_all_scan_12.log  ===> it logs the 10 nmap 
                scans, which were done one after the other in the order they
                appear with a time gap in between.

-------------------------------------------------------------------------------
C- Location: 
**************
-->All the log files, 'scanproject.py', and the 'report.txt' are placed in ./
-->The 12 Scan logs, the generated report named 'report.txt', and the source 
   code named 'scanproject.py", and three NMAP cheat-sheets in portable 
   document format are also included here just for reference.
--> What is more, the project description is also included here.
-------------------------------------------------------------------------------
D- Instructive Information:
**************
==> For detailed description of the "NMAP Switches", please refer to 
    https://www.stationx.net/nmap-cheat-sheet/
==>You can execute the source code by running ./scanproject.py on terminal or 
   on IDEs like spyder3
==>Once executed, it reads all log files on current directory with extention 
   name '.log' using os.chdir("./") & save the names onto a 'list'.
==>Then, the program reads each log, extracts lines, analyzes or parses each 
   line or packet, and classsifies it into ARP or IP traffics
==> Scan detection is then made based on some flags, protocols or scanned ports
    tersely described below:       
       ---> "-sF" scan ==> check for "Flags [F]" 
       ---> "-sO" scan ==> check for "ip-proto"
       ---> "-sS" scan ==> check for "Flags [F]" and the scanned port is 
                                                 usually 999 or so.
       ---> "-F" scan ==> check for "Flags [S]" and the  scanned Port must be 
                                               less than that of "-sS" switch
       ---> "-sN" scan ==> check for "Flags [none]"
       ---> "-sU" scan ==> check for "UDP"
       ---> "-sT" scan ==> check for "Flags [S]" 
       ---> "-sn" scan ==> check for "Broadcast"
       ---> "-O" scan ==> check for "Flags [S]" 
       ---> "-sX" scan ==> check for "Flags [S]"
==>Every subsquent scan was made after the preceding scan was complete. Then, 
   every traffic comprises ARP & IP because new session is created every now 
   and then for every start of scan. When you have one uninterrupted scan, 
   ARPing is required as the beginning only. But in the case of this project, 
   after one NMAP scan is done, and another follows.We know that a packet 
   trasmission is preceded by ARP broadcast to resolve the IP Address of the 
   local target into MAC address for successful frame transmission. 
   As a result,
   ---> one scan might have two lines of output: one for ARP & another for IP
   ---> if a scan was interrupted early immediately after started or was not
        successful, it might have only one output --> ARP
   ---> if you ignore the ARP phase or traffics in your analysis, you will have
        only one output for every scan in your final report.
   Example-1: Three consecutive scans with hiatus in between were carried out 
            using switch -O and the corresponding result is what ensues:
            1.tcpdump_O_scan_10.log-->
				Scanned from 192.168.184.131 at 19:04:43    ---> ARP 
				Scanned from 192.168.184.131 at 19:05:12    ---> IP
                -------------------------------------------
				Scanned from 192.168.184.131 at 19:05:23
				Scanned from 192.168.184.131 at 19:06:01
                -------------------------------------------
				Scanned from 192.168.184.131 at 19:06:13
				Scanned from 192.168.184.131 at 19:06:34
   ---> If no scans, the program returns nothing even though there is normal
        traffics
   Example-2: Normal traffic flow was recorded but no scaning actvities. Then,
              the output of the program is what follows
          9.tcpdump_no_scan_1.log--> 
   ---> If you NMAP -sn scan, you will end up with ARP broadcasts
          10.tcpdump_sn_scan_9.log-->
                Scanned from 192.168.184.131 at 19:03:18
                Scanned from 192.168.184.131 at 19:03:42
                Scanned from 192.168.184.131 at 19:04:04               
-------------------------------------------------------------------------------
E- Warning:
************** 
Non-real IP value in the packet is not handled. Please clean such things as 
         IP localhost.47029 > localhost.ipp: from your logs.
==> I observed that such things could happen while doing scanning, and it could
    cause some descrepancy in scanning and in the number of outputs.
===>A sample log is provided below:
18:31:47.958414 IP6 localhost.ipp > localhost.36692: Flags [R.], seq 0, 
     ack 254254753, win 0, length 0
18:31:47.958529 IP localhost.47029 > localhost.ipp: Flags [S], seq 735795270, 
     win 43690, options [mss 65495,sackOK,TS val 1957713 ecr 0,nop,wscale 6], 
     length 0
18:31:47.958641 IP localhost.ipp > localhost.47029: Flags [R.], seq 0, 
     ack 735795271, win 0, length 0
-------------------------------------------------------------------------------
F- References
************** 
    [1] Dr. M. O., Faruque Sarker, "Python Network Programming Coockbook"
    [2] Udemy courses: Network Programming I, II, and III
-------------------------------------------------------------------------------

