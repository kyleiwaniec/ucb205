#! bin/bash


#####################################
# TWITTER KEYS
#####################################

# add twitter keys to environment:

function consumerKey {
	STR=$'Please enter your Twitter consumerKey: '
	echo "$STR"
	read answer

	if [[ "$answer" != "" ]]; then
		echo "export consumerKey=$answer" >> ~/.passwords
	else
		STR=$'consumerKey can\'t be empty: \n'
		echo "$STR"
		consumerKey	
	fi
}
function consumerSecret {
	STR=$'Please enter your Twitter consumerSecret: '
	echo "$STR"
	read answer

	if [[ "$answer" != "" ]]; then
		echo "export consumerSecret=$answer" >> ~/.passwords
	else
		STR=$'consumerSecret can\'t be empty: \n'
		echo "$STR"
		consumerSecret	
	fi
}
function accessToken {
	STR=$'Please enter your Twitter accessToken: '
	echo "$STR"
	read answer

	if [[ "$answer" != "" ]]; then
		echo "export accessToken=$answer" >> ~/.passwords
	else
		STR=$'accessToken can\'t be empty: \n'
		echo "$STR"
		accessToken	
	fi
}
function accessTokenSecret {
	STR=$'Please enter your Twitter accessTokenSecret: '
	echo "$STR"
	read answer

	if [[ "$answer" != "" ]]; then
		echo "export accessTokenSecret=$answer" >> ~/.passwords
	else
		STR=$'accessTokenSecret can\'t be empty: \n'
		echo "$STR"
		accessTokenSecret	
	fi
}

consumerKey
consumerSecret
accessToken
accessTokenSecret

source ~/.passwords