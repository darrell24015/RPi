# RPi
Repo for Raspberry Pi Projects

### Notes on Pimoroni PiGlow
After a recent Raspbian and firmware upgrade to my RPi Model B, the PiGlow
would not work when running the Python code. Apparently the new firmware requires
you make a change to the bootup config file. 

- Credit to [joan] for posting this solution on the [Raspberry Pi Forums]

```sh
$ sudo nano /boot/config.txt
```
- Add this line to the end of the file

```sh
dtparam=i2c1=on
```
- Reboot


[Raspberry Pi Forums]: http://www.raspberrypi.org/forums/viewtopic.php?f=45&t=89936
[joan]: http://www.raspberrypi.org/forums/memberlist.php?mode=viewprofile&u=24295&sid=e0aae467fd643bffe5b71bee0e65af22
