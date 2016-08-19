#----------------------------------JSON POSTS-----------------------------------
#registers Discord with Gamesense
send_discord={
    "game":"DISCORD_CHAT",
    "game_display_name":"Discord"
    "game_color_id":7
}
#Creates an event for message notifications
message_event={
    "game":"DISCORD_CHAT",
    "event":"MESSAGE",
    "min_value":0,
    "max_value":100,
    "icon_id":0
}
#Set defaults for a message event
bind_message_event={
    "game":"DISCORD_CHAT",
    "event":"MESSAGE",
    "min_value":0,
    "max_value":100,
    "icon_id":0,
    "handlers":[
        '''{
            \"device-type\":\"rgb-1-zone\",
            \"zone\":\"two\",
            \"color\":[{
                \"low\":0,
                \"high\":49,
                \"colour\": {
                    \"red\":144,
                    \"green\":235,
                    \"blue\":223
                }
            },
            {
                \"low\":50,
                \"high\":80,
                \"colour\": {
                    \"red\":45,
                    \"green\":54,
                    \"blue\":85
                }
            },
            {
                \"low\":81,
                \"high\":100,
                \"colour\": {
                    \"red\":255,
                    \"green\":167,
                    \"blue\":13
                }
            }
            ]
            \"rate\":{
                \"frequency\":4,
                \"repeat_limit\":16
            }
        }'''
    ]
}
#When we recive a message we activate the colour change event to discord purple
message_event={
    "game":"DISCORD_CHAT",
    "event":"MESSAGE",
    "data":"{\"value\":50}"
}
#If the user is mentioned in a message we use a more vibrant orange
mention_event={
    "game":"DISCORD_CHAT",
    "event":"MESSAGE",
    "data":"{\"value\":100}"
}
