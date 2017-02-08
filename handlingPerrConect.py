def __handlepeer( self, clientsock ):
	self.__debug( 'Connected ' + str(clientsock.getpeername()) )

	host, port = clientsock.getpeername()
	peerconn = BTPeerConnection( None, host, port, clientsock, debug=False )

	try:
	    msgtype, msgdata = peerconn.recvdata()
	    if msgtype: msgtype = msgtype.upper()
	    if msgtype not in self.handlers:
		self.__debug( 'Not handled: %s: %s' % (msgtype, msgdata) )
	    else:
		self.__debug( 'Handling peer msg: %s: %s' % (msgtype, msgdata) )
		self.handlers[ msgtype ]( peerconn, msgdata )
	except KeyboardInterrupt:
	    raise
	except:
	    if self.debug:
		traceback.print_exc()

	self.__debug( 'Disconnecting ' + str(clientsock.getpeername()) )
	peerconn.close()

    # end handlepeer method
