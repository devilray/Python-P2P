def sendtopeer( self, peerid, msgtype, msgdata, waitreply=True ):
	if self.router:
	    nextpid, host, port = self.router( peerid )
	if not self.router or not nextpid:
	    self.__debug( 'Unable to route %s to %s' % (msgtype, peerid) )
	    return None
	return self.connectandsend( host, port, msgtype, msgdata, pid=nextpid,
				    waitreply=waitreply )

    # end sendtopeer method
