from mycroft import MycroftSkill, intent_file_handler
import nmap
nmScan = nmap.PortScanner()


class Snoopy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('snoopy.intent')
    def handle_snoopy(self, message):
        nmScan.scan('192.1.1.1', '21-443')
        
        for host in nmScan.all_hosts():
            print('Host : %s (%s)' % (host, nmScan[host].hostname()))
            print('State : %s' % nmScan[host].state())
            for proto in nmScan[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                
                lport = nmScan[host][proto].keys()
                lport.sort()
                for port in lport:
                    print('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state'])
        self.speak_dialog('snoopy')


def create_skill():
    return Snoopy()

