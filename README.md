#LookBook Grabber

A simple web crawler/grabber/parser/whatever to store favourite looks from lookbook.nu

Misc
=====
Unirest package is needed. Run `pip install unirest` from cli

Usage
=====
- Open grabber.py and place the link to the user profile in the getpage() function

- REMEMBER to specify the type of looks you want to download from the user

`http://lookbook.nu/user/1569863-John-D/looks/hyped`
or
`http://lookbook.nu/user/1569863-John-D/looks/loved`
or
`http://lookbook.nu/user/1569863-John-D/looks/posted`

Run `$ python grabber.py`

Looks will be saved in img folder


