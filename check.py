from pyyoutube import Api
api = Api(api_key="") # ADD API KEY

channels = [
	
] #INSERT CHANNEL IDs, typically UC... (seperated by commas and enclosed in quotes because python)

for channel in channels:
        if not (api.get_channel_info(channel_id=channel).items): print("Channel " + channel + " broke") #This will only return true if the API returns an empty list with the channel
