  def mainloop( self ):
	s = self.makeserversocket( self.serverport )
	s.settimeout(2)
	self.__debug( 'Server started: %s (%s:%d)'
		      % ( self.myid, self.serverhost, self.serverport ) )

	while not self.shutdown:
	    try:
		self.__debug( 'Listening for connections...' )
		clientsock, clientaddr = s.accept()
		clientsock.settimeout(None)

		t = threading.Thread( target = self.__handlepeer, args = [ clientsock ] )
		t.start()
	    except KeyboardInterrupt:
		self.shutdown = True
		continue
	    except:
		if self.debug:
		    traceback.print_exc()
		    continue
	# end while loop

	self.__debug( 'Main loop exiting' )
	s.close()
    # end mainloop method
