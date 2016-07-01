"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
	s=[]

        # Add hosts and switches
	s.append(self.addSwitch('s1'))
	s.append(self.addSwitch('s2'))
	s.append(self.addSwitch('s3'))
	s.append(self.addSwitch('s4'))    
	self.addLink(s[0],s[1])
        self.addLink(s[1],s[2],bw=5)
        self.addLink(s[2],s[3])

	h1=self.addHost('h1',mac='00:00:00:00:00:01')
	h2=self.addHost('h2',mac='00:00:00:00:00:02')
	h3=self.addHost('h3',mac='00:00:00:00:00:03')
	h4=self.addHost('h4',mac='00:00:00:00:00:04')

	
        self.addLink(s[0],h1)
	self.addLink(s[1],h2)
   	self.addLink(s[2],h3)	
	self.addLink(s[3],h4)

topos = { 'mytopo': ( lambda: MyTopo() ) }
