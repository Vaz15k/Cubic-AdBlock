**English** || [Português (Brasil)](README_PT.md)

<p align="center">
  <img width="220" height="auto" src="cubic_logo.png">
    <br/><strong>Cubic AdBlock</strong></b>
</p>

<p align="center">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Vaz15K/Systemless-AdBlocker/update_hosts.yml">
  <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/Vaz15K/Systemless-AdBlocker/total">
</p>

A simple AdBlock module based on the hosts file.

- Some links are allowed so that you can use some essential services, such as Facebook login, Google and Microsoft APIs, Samsung services and others.
- If an application is not working, you can make a request to allow it, as long as it is not related to advertising.

> [!NOTE]
> The hosts file is approximately 33 mb in size. \
> The module is updated weekly.

## How Install
Installing the module is very simple.

1. **Download the [latest module](https://github.com/Vaz15k/Cubic-AdBlocker/releases)**
> The module is also available on [**MMRL**](https://mmrl.dergoogler.com)
2. **Flash your preferred root manager**

## Using with Adaway
An alternative to the module is to use the [Adaway](https://adaway.org) application, which allows you to edit the file with absurd ease. \
I recommend using Adaway if you want to allow ads in a specific application.

> I don't recommend directly editing the hosts file due to its size and the number of lines, which might contain links similar to the one you want to unblock. \
> You can also disable the module temporarily and then activate it, but you would have to restart the device.

To use this list in AdAway, add the following URL to the in-app repository list:
```
https://raw.githubusercontent.com/Vaz15k/Cubic-AdBlocker/master/module/system/etc/hosts
```
- For Magisk users: enable the "Systemless hosts" module in the settings.
- For APatch or KernelSU users: use the [Systemless Hosts KSU](https://github.com/symbuzzer/systemless-hosts-KernelSU-module) module.

> [!NOTE]
> If you want, you can use Adway in VPN mode, so you won't be root

## Credits
Special thanks to the following lists for their contributions:

- [StevenBlack](https://github.com/StevenBlack/hosts)
- [NoTrack Block Lists](https://gitlab.com/quidsup/notrack-blocklists)
- [GoodbyeAds](https://github.com/jerryn70/GoodbyeAds)
- [1 Hosts](https://o0.pages.dev)
- [Peter Lowe](https://pgl.yoyo.org/adservers)
- [HaGeZi](https://github.com/hagezi/dns-blocklists)
