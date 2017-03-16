from AddressReader import *
from GeoIPLookup import *
from RDAPLookup import *
from CommandTerminal import *
import sys
import subprocess as sp
from blessings import Terminal


commandTerminal = 0;
def commandHook(data):
	if data == "CTRL_C" or data == "exit":
		CommandTerminal.printSystem("Stopping");
		commandTerminal.end();
	else:
		print data;


if __name__ == "__main__":
	sp.call('clear', shell=True);
	terminal = Terminal();
	terminal.clear();
	terminal.fullscreen();
	commandTerminal = CommandTerminal(terminal, commandHook);
	commandTerminal.start()

	reader = AddressReader("list_of_ips.txt");
	addresses = reader.getAddresses();

	test_cases = ["4.2.2.2", "brokenaddress", addresses[0]];
	for test_case in test_cases:
		RDAPLookup.lookupRDAP(test_case);
		GeoIPLookup.lookupIP(test_case);

