import subprocess
import copy
import getpass


class Network:
    network_info = {
        'ssid': None,
        'signal': None
    }

    networks = []

    def list_nearby_networks(self):
        command = "nmcli -f IN-USE,SIGNAL,SSID device wifi | head -4"
        response_byte = subprocess.check_output(command, shell=True)
        response = response_byte.decode('utf-8')
        try:
            response_body = response.split('\n*')[1]
        except IndexError:
            response_body = ''
        print('Your available wifi networks are:')
        if response_body.replace(' ', ''):
            response_body = response_body.split('\n')
        else:
            response_body = []
        response_body = [each_body.split(' ') for each_body in response_body]
        self.networks = []
        for network in response_body[:3]:
            sample = copy.deepcopy(self.network_info)
            for element in network:
                if element != '':
                    if not sample.get('signal'):
                        sample['signal'] = element
                    else:
                        if sample.get('ssid'):
                            sample['ssid'] += (' '+element)
                        else:
                            sample['ssid'] = element
            self.networks.append(sample)
        for network in self.networks[:3]:
            print('[{}]'.format(self.networks.index(network)+1), network.get('ssid'))

    def connect_network(self, selection):
        try:
            if int(selection) > len(self.networks):
                print('Invalid selection!')
            else:
                selection = int(selection)
                network = self.networks[selection-1]
                password = getpass.getpass('Password: ')
                command = 'nmcli dev wifi connect ' + str(network.get('ssid')) + ' password ' + password
                try:
                    response_byte = subprocess.check_output(command, shell=True)
                    response = response_byte.decode('utf-8')
                    if 'activated' in response:
                        print('connected!')
                    else:
                        print('unable to establish connection')
                except subprocess.CalledProcessError:
                    print('unable to establish connection')
        except ValueError:
            print('Invalid selection!')


net = Network()
net.list_nearby_networks()
if net.networks:
    choice = input('Your choice? ')
    net.connect_network(choice)
