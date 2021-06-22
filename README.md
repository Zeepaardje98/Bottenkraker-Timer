# Bottenkraker-Timer
This repository contains the code for a tool that helps with timing clicks manually. This project is written in Python 3.

## Packages
This project uses several third-party packages. These can be found in ```requirements.txt```. To install the packages all at once, the following command can be run: ```pip install --no-cache-dir -r requirements.txt```. Keep in mind that you need to have installed python3-pip for this to work.

## Run Snipetool
To run this tool, follow these steps in the command line or terminal:
1. Navigate to the folder containing ```snipetool.py```: cd ```Bottenkraker-Timer/```
2. Run the snipetool: ```python snipetool.py```\
Additionaly, for windows, you can download the .zip file of the version you want from https://github.com/Zeepaardje98/TimeTool_Release. unzip this file, and execute snipetool.exe

## Guide to the Snipetool
When starting the snipetool. This window will show up:\
![image](https://user-images.githubusercontent.com/46892835/122901887-485e9500-d34e-11eb-8699-02505563765f.png)\
with the bottom bar filling up exactly once every second. This bar is filled when the time reaches the millisecond given by the user. This bar will change color when the time reaches the ```Snipe Time``` minus the ```Walk Time``` given by the user.

There are 3 entry fields in this window:\
![image](https://user-images.githubusercontent.com/46892835/122903609-db4bff00-d34f-11eb-8e45-d49ebe14e2bf.png)
- Snipe Time: The time entered here will partly determine when the bar changes color
- Walk Time: The time entered here will be subtracted from ```Snipe Time```, to determine the time when the bar will change color
- Snipe Ms: The millisecond entered here will determine at what millisecond the bar will be completely filled

Under these entry fields is a ```Send``` label. This shows the user at what time you need to click. The bar will be completely filled up in a different color at this time.\
![image](https://user-images.githubusercontent.com/46892835/122904296-7d6be700-d350-11eb-861a-5774d261fdf9.png)

The timeserver that's being used can be found under the ```Send``` label, with a ```Sync``` button right next to it.\
![image](https://user-images.githubusercontent.com/46892835/122905149-42b67e80-d351-11eb-846c-6b26be228614.png)

You can change the selected server by clicking on the currently used server, and selecting one of the options in the menu that drops down. Clicking the ```Sync``` button will synchronize the currently used time with the time of the selected server. To the right of the ```Sync``` button is an icon that shows you if you are currently synchronized with a server, and how long ago this synchronization took place. This icon will be green if you're synchronized to a server, and red if you're not synchronized to a server.

On the right side of the window, several icons can be found. 
The first being the ```Settings``` Icon.
![image](https://github.com/Zeepaardje98/Bottenkraker-Timer/blob/main/images/settings_light.png)

## Used assets
images from https://icons8.com/icon/set/settings/material-sharp--white
