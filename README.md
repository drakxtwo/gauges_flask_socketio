# gauges_flask_socketio
I've been running a home Pi based server that monitors electricity & temperatures both internal and external, for a longtime it was dumb ie i could view the data when i ssh'd into the pi or on graphs via a remote service but apart from email alerts it was to all intents lacking.

Then i found https://canvas-gauges.com/ by Mikhus ... perfect you could have radial or linear gauges with lots of customisation and _reactive_.

Or so i thought, i could not get it working, 4wks of trying and i was going to give up, i had gauges - they worked - i ended up setting an HTML refresh to update every so often just to give me a dashboard which looked useful but i wasnt happy.

Getting a gauge onto a page is simple, getting the gauge to be reactive well that was beyond me, i searched for simple tutorials and all i found was chat apps ... not what i wanted. Python ok, i'm not brilliant but i get there, websockets whoa and moving into javascript was daunting to say the least. Eventually, whilst sat waiting for a flight i finally got the gauges reacting, updating in realtime. 

Hopefully someone just starting with the Pi or any other flask based website will find this useful if they want to show a value on a reactive gauge.

Now there is one *big* caveat ... i bodged this together from lots of sources, in parts to be blunt i dont know what i'm doing here :) it works that is true, however i dont know what performance hit will have on your or my network. Have never tried this before and i can see the constant network chatter, it might have an adverse affect on network speed.

You may also need to download the dot js files from the appropriate places on upload from my Windows PC i got  a message that the line endings were changed...
