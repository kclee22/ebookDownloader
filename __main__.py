import os, sys, argparse, time, datetime
import textwrap

try: import ujson as json
except: import json

import json as _jjjson
import itbooks



def getArgs_itebooks(parent_parser):
	p2 = argparse.ArgumentParser(parents=[parent_parser]
			,formatter_class=argparse.RawDescriptionHelpFormatter
			,epilog=textwrap.dedent("haha"
					)
			)
	#p2.add_argument('-c', '--configFile', dest='config', type=argparse.FileType('rb'), required=True)
	#p2.add_argument('-o', '--output-scoreFile', dest='scoreFileHandler', type=argparse.FileType('wb'), required=True)
	#p2.add_argument('-i', '--minimum-length-of-segment-not-ignored', dest='minimum', type=int, required=True)
	p2.add_argument('-from', '--from-address', dest='From', type=int, required=True)
	p2.add_argument('-to', '--to-address', dest='To', type=int, required=True)
	ns, rest = p2.parse_known_args()
	print ns
	#dictGetter = _data.sharedMemory.dict_client.Get()
	#_markov.create.getUsersFromSharedMemory(dictGetter)
	#_markov.create.createFromDevidedSegmentFile(ns.config, ns.minimum)
	#_markov.create.createFromDirectory(ns.config, ns.minimum, ns.dir, ns.idle, _intelligence.event3to4.map, ns.penalty, ns.error, ns.scoreFileHandler)
	itbooks.dw.fetch_info(ns.From, ns.To)
	#

def main():
	pmain = argparse.ArgumentParser()
	sp = pmain.add_subparsers(dest='subparsers')
	sp.add_parser('backup')
	ptest = sp.add_parser('test',
			add_help=False # parent parser should add this config
			)
	
	ns, rest = pmain.parse_known_args()
	
	if ns.subparsers=='backup':
		pass
	elif ns.subparsers=='test':
		ptest.add_argument('-j', '--job', dest='job', choices=['itebooks'], required=True)
		ns, rest = ptest.parse_known_args()
		
		if ns.job=='itebooks': getArgs_itebooks(ptest)
	#


if __name__ == "__main__":
	main()
	print "Done".center(50, "-")


"""
"""




