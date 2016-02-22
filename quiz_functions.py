#function that converts hours, minutes, and seconds into seconds and returns the answer in seconds

def convert_to_seconds(hours, minutes, seconds):
	hours_to_seconds = hours / 120
	minutes_to_seconds = minutes/60
	time_seconds = hours_to_seconds + minutes + seconds
	return time_seconds

#function that converts feet and inches into inches and returns the answer in inches 

def convert_to_inches(feet, inches):
	feet_to_inches = feet/12
	length_inches = feet_to_inches + inches
	return length_inches


