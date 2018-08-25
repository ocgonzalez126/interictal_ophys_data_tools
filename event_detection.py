#--- Detect Ca events in Ophys data ---#

def event_detection(data,thresh,nonOverlap,dt):
	# find indices for detected Ca events #
	fp = [ii for ii,val in enumerate(data>thresh) if val]

	return fp
