# Spotify-Controls

Control your Spotify Desktop from any local device. It doesn't matter if Spotify Desktop is minimized/ not active.. this will work in every situation!

Made using Flask and AutoIT.

Works only on Windows

## Installation and Usage:

Assuming you have Python 2.7 already installed.

Run the following commands in command prompt:

`cd C:\Python27\Scripts` (or wherever you installed python)

`pip.exe install flask`

Now download the zip file of this repository and extract its contents in the root directory of your Python installation.

Run `spotify_start.bat` (edit the Python's installation if you changed the default directory in the .bat file)

Now goto `<PCsLocalAddress>:1080` on any local device.

<img src="http://i.imgur.com/QOTloOO.png" width="290">

(even though its not all that fancy but it does the job)

Have Fun!

## Running automatically in background on boot:

If you would like the script to run automatically in background on boot just create a shortcut of `spotify_background.vbs` and place the shortcut in `C:\Users\<UserName>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

Now the script will automatically run in the background next time you get into windows and you can just access it locally without doing anything else (except running Spotify Desktop itself ofcourse).

## How it Works:

The purpose of using Python is just to provide the Web Interface that can be accessed from local devices.
Rest of the job of controlling spotify is done using AutoIT (google it if you are not familiar with it).

Pressing a button in the WebUI runs `spotify_args.exe` (which is written in AutoIT) and sends the respective command to Spotify Desktop.
You can open `spotify_args.au3` if you want to take a look at its code.

I have just compiled the AutoIT script so we can easily pass resprective arguments to it (whether we want to pause the song or increase the volume etc.)

## Contributing:

If you would like to add more features or improve the Web Interface feel free to Contribute to the project!

The link for the AutoIT website is https://www.autoitscript.com/site/autoit/ (incase you are not familiar with it, should be easy to get the basics)
