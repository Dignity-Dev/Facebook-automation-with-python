import requests

# Set up your access token and post ID
access_token = 'YOUR_ACCESS_TOKEN'
post_id = 'POST_ID'

# Specify the reaction you want to use
reaction_type = 'LIKE'  # Can be 'LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', or 'ANGRY'

# Define the number of reactions you want to send
num_reactions = 100

# Make the API requests
for _ in range(num_reactions):
    response = requests.post(
        f'https://graph.facebook.com/v14.0/{post_id}/reactions',
        params={
            'access_token': access_token,
            'type': reaction_type
        }
    )
    
    if response.status_code == 200:
        print('Reaction sent successfully.')
    else:
        print('Failed to send reaction.')
