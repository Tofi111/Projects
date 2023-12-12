from dataclasses import dataclass

@dataclass
class Application:
	credit_records: bool = True
	criminal_records: bool = False
	employment_status: bool = True
	security_clearance: bool = True
