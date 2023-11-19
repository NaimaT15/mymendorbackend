
# # import os

# # from twilio import Client

# # account_sid = os.environ['ACae9c661cbd5ea9e61a23503c0b244db9']
# # auth_token = os.environ['edc7c2561b3c9b46b51ad6536a784389']

# # client = Client(account_sid, auth_token)

# # message = client.messages \
# #                 .create(
# #                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
# #                      from_='+14066294771',
# #                      to='+251910493259'
# #                  )

# # print(message.sid)
# import sms

# from sms import send_sms

# send_sms(
#     'Here is the message',
#     '+12065550100',
#     ['+441134960000'],
#     fail_silently=False
# )