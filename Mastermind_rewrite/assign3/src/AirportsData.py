from src.airport import Airport

def fetchAirports():
	IAD = Airport("IAD", "Dulles Intl", "Washington", "DC", True, 71)
	ORD = Airport("ORD", "O'Hare International", "Chicago", "IL", True, 62)
	MDW = Airport("MDW", "Midway International", "Chicago", "IL", False, 60)
	IAH = Airport("IAH", "George Bush Intercont.", "Houston", "TX", True, 82)
	SFO = Airport("SFO", "San Francisco Intl.", "San Francisco", "CA", False, 59)
	LAX = Airport("LAX", "Los Angeles Intl.", "Los Angeles", "CA", False, 84)
	HOU = Airport("HOU", "Hobby", "Houston", "TX", False, 80)

	return [IAD, ORD, MDW, IAH, SFO, LAX, HOU]
