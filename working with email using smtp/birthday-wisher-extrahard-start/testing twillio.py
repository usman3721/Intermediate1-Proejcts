from twilio.rest import Client

twilio_number="+13149072367"
account_sid="ACff0202bcce08e3851df06bbf8227d587"
auth_token="5b60630f58479b641e757405f050f632"



client = Client(account_sid, auth_token)
message = client.messages.create(
    body="my name is usman",
    from_="+13149072367",
    to="+2348024230513"
    )

print(message.status)


