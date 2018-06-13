# Filename: net.py
# -*- coding:utf-8 -*-  
import os,sys
base = 'C:/Users/quan/Desktop/python/'
hostname='C:/Users/quan/Desktop/python/host.txt'
floor=[4,6,7,8,9,10,12,13,20,31]
w='WW'
N='NW'
E='YW'
K='ZW'
V_W=4
V_N=4
V_E=2
V_K=2
###´´½¨Ŀ¼Î¼þ
j = 0
for j in range(10):
	file_name = base+str(floor[j])+'F'
	os.mkdir(file_name)
	file_name1=str(floor[j])+'F'
	for line in open(hostname,'r'):
		file_name2= file_name+'/'+line.rstrip('\n')+'.txt'
		#print str(file_name),str(line)
		if (file_name1 in str(line)):
		###ÄÍ½Ó뽻»»»úif (N in str(line)):
				f=open(file_name2,'w')
				cur='sys\n'+\
				'sysname '+str(line)+\
				'local-user admin\n'+\
				'password simple admin\n'+\
				'authorization-attribute user-role level-3\n'+\
				'authorization-attribute user-role network-admin\n'+\
				'service-type ssh\n'+\
				'service-type telnet\n'+\
				'quit\n'+\
				'telnet server enable\n'+\
				'ssh server enable\n'+\
				'stp global enable\n'+\
				'vlan 10\n'+\
				'port g1/0/1 to g1/0/48\n'+\
				'port Ten-GigabitEthernet1/0/50 to Ten-GigabitEthernet1/0/52\n'+\
				'quit\n'+\
				'int g1/0/48\n'+\
				'des TO_[NW-JR1/2-G1/0/48]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 10\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'int Ten-GigabitEthernet1/0/49\n'+\
				'des TO_[NW-04F-HX1/2]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 10\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'snmp-agent\n'+\
				'snmp-agent community read SWT_PUBLIC\n'+\
				'snmp-agent sys-info version all\n'+\
				'line vty 0 63\n'+\
				'authentication-mode scheme\n'+\
				'quit\n'+\
				'interface vlan-interface 10\n'+\
				'ip add 172.10.1.'+str(V_N)+' 255.255.255.0\n'+\
				'quit'
				f.write(str(cur)+'\n')
				f.close()
				V_N=V_N+1
			elif (w in str(line)):
				f=open(file_name2,'w')
			###ÍÍ½Ó뽻»»»ú	cur='sys\n'+\
				'sysname '+str(line)+\
				'local-user admin\n'+\
				'password simple admin\n'+\
				'authorization-attribute user-role level-3\n'+\
				'authorization-attribute user-role network-admin\n'+\
				'service-type ssh\n'+\
				'service-type telnet\n'+\
				'quit\n'+\
				'telnet server enable\n'+\
				'ssh server enable\n'+\
				'stp global enable\n'+\
				'vlan 11\n'+\
				'port g1/0/1 to g1/0/48\n'+\
				'port Ten-GigabitEthernet1/0/50 to Ten-GigabitEthernet1/0/52\n'+\
				'quit\n'+\
				'int g1/0/48\n'+\
				'des TO_[WW-JR1/2-G1/0/48]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 11\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'int Ten-GigabitEthernet1/0/49\n'+\
				'des TO_[WW-04F-HX1/2]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 11\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'snmp-agent\n'+\
				'snmp-agent community read SWT_PUBLIC\n'+\
				'snmp-agent sys-info version all\n'+\
				'line vty 0 63\n'+\
				'authentication-mode scheme\n'+\
				'quit\n'+\
				'interface vlan-interface 11\n'+\
				'ip add 172.11.1.'+str(V_W)+' 255.255.255.0\n'+\
				'quit\n'
				f.write(str(cur)+'\n')
				f.close()
				V_W=V_W+1
			elif (E in str(line)):
				f=open(file_name2,'w')
			###ҵÎ½Ó뽻»»»ú	cur='sys\n'+\
				'sysname '+str(line)+\
				'local-user admin\n'+\
				'password simple admin\n'+\
				'authorization-attribute user-role level-3\n'+\
				'authorization-attribute user-role network-admin\n'+\
				'service-type ssh\n'+\
				'service-type telnet\n'+\
				'quit\n'+\
				'telnet server enable\n'+\
				'ssh server enable\n'+\
				'stp global enable\n'+\
				'vlan 12\n'+\
				'des YW_VLAN\n'+\
				'port g1/0/1 to g1/0/48\n'+\
				'port Ten-GigabitEthernet1/0/50 to Ten-GigabitEthernet1/0/52\n'+\
				'quit\n'+\
				'vlan 13\n'+\
				'des ZW_VLAN\n'+\
				'quit\n'+\
				'int g1/0/48\n'+\
				'des TO_[ZW-JR1/2-G1/0/48]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 12 13\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'int Ten-GigabitEthernet1/0/49\n'+\
				'des TO_[YW/ZW-04F-HJ1]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 12 13\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'snmp-agent\n'+\
				'snmp-agent community read SWT_PUBLIC\n'+\
				'snmp-agent sys-info version all\n'+\
				'line vty 0 63\n'+\
				'authentication-mode scheme\n'+\
				'quit\n'+\
				'interface vlan-interface 12\n'+\
				'ip add 172.12.1.'+str(V_E)+' 255.255.255.0\n'+\
				'quit\n'
				f.write(str(cur)+'\n')
				f.close()	
				V_E=V_E+1
			elif (K in str(line)):
				f=open(file_name2,'w')
			###רÍ½Ó뽻»»»ú	cur='sys\n'+\
				'sysname '+str(line)+\
				'local-user admin\n'+\
				'password simple admin\n'+\
				'authorization-attribute user-role level-3\n'+\
				'authorization-attribute user-role network-admin\n'+\
				'service-type ssh\n'+\
				'service-type telnet\n'+\
				'quit\n'+\
				'telnet server enable\n'+\
				'ssh server enable\n'+\
				'stp global enable\n'+\
				'vlan 13\n'+\
				'des ZW_VLAN\n'+\
				'port g1/0/1 to g1/0/48\n'+\
				'port Ten-GigabitEthernet1/0/50 to Ten-GigabitEthernet1/0/52\n'+\
				'quit\n'+\
				'vlan 12\n'+\
				'des YW_VLAN\n'+\
				'quit\n'+\
				'int g1/0/48\n'+\
				'des TO_[YW-JR1/2-G1/0/48]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 12 13\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'int Ten-GigabitEthernet1/0/49\n'+\
				'des TO_[YW/ZW-04F-HJ1]\n'+\
				'port link-type trunk\n'+\
				'port trunk permit vlan 12 13\n'+\
				'undo port trunk permit vlan 1\n'+\
				'quit\n'+\
				'snmp-agent\n'+\
				'snmp-agent community read SWT_PUBLIC\n'+\
				'snmp-agent sys-info version all\n'+\
				'line vty 0 63\n'+\
				'authentication-mode scheme\n'+\
				'quit\n'+\
				'interface vlan-interface 13\n'+\
				'ip add 172.13.1.'+str(V_K)+' 255.255.255.0\n'+\
				'quit\n'
				f.write(str(cur)+'\n')
				f.close()
				V_K=V_K+1
###ÇÀ»·¾³¼°Ïʾ½á£¬²âÍ±Ϻóýúmport shutil
gname='C:/Users/quan/Desktop/python/4F/WW-04F-JR1.txt'
for line1 in open(gname,'r'):
	print line1
for k in range(10):
	file_name5 = base+str(floor[k])+'F'
#	shutil.rmtree(file_name5)
