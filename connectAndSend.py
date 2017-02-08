 def connectandsend( self, host, port, msgtype, msgdata, pid=None, waitreply=True ):
	msgreply = []   # list of replies
	try:
	    peerconn = BTPeerConnection( pid, host, port, debug=self.debug )
	    peerconn.senddata( msgtype, msgdata )
	    self.__debug( 'Sent %s: %s' % (pid, msgtype) )

	    if waitreply:
		onereply = peerconn.recvdata()
		while (onereply != (None,None)):
		    msgreply.append( onereply )
		    self.__debug( 'Got reply %s: %s' % ( pid, str(msgreply) ) )
		    onereply = peerconn.recvdata()
	    peerconn.close()
	except KeyboardInterrupt:
	    raise
	except:
	    if self.debug:
		traceback.print_exc()

	return msgreply

    # end connectsend method
