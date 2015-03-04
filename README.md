# RPi
Repo for Raspberry Pi Projects

### Notes on Pimoroni PiGlow
After a recent Raspbian upgrade to my RPi Model B, the PiGlow
would not work when running the Python code. Apparently the new kernel requires
you make a change to the bootup config file to enable the i2c interface. 

- Credit to [joan] for posting this solution on the [Raspberry Pi Forums]

```sh
$ sudo nano /boot/config.txt
```
- Add this line to the end of the file

```sh
dtparam=i2c1=on
```
- Reboot

Full explanation on how Device Tree is used to manage resources and module loading
can be found in the [Raspberry Pi Documentation]

[Raspberry Pi Forums]: http://www.raspberrypi.org/forums/viewtopic.php?f=45&t=89936
[joan]: http://www.raspberrypi.org/forums/memberlist.php?mode=viewprofile&u=24295&sid=e0aae467fd643bffe5b71bee0e65af22
[Raspberry Pi Documentation]: http://www.raspberrypi.org/documentation/configuration/device-tree.md
