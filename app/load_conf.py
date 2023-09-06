#import os
from pathlib import Path 
import xml.etree.ElementTree as ET 



def load_conf(fconf, func, protocol):
    """
    read settings
    """
    tree = ET.parse(fconf)
    root = tree.getroot()

    sender = root[0][0].get('emailAddress')
    password = root[0][0].get('password')
    receiver = root[0][1].get('emailAddress')

   
    for pro in root.find('Client'):
        if pro.tag==protocol:
            data = pro.attrib
            host = data.get('host')
            port = data.get('port')
            ports = data.get('ports')
        
        
    for attch in root.find('Attachment'):
        if attch.tag=='inputFolder':
            data = attch.attrib 
            path = data.get('path')

    return host, port, ports, path, sender, password, receiver 