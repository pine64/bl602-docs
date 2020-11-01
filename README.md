BL602 Documentation
===================

The documentation can be found [online][1] at [pine64.github.io/bl602-docs][1]

Building The Documentation
--------------------------
To build the documentation your self:
```bash
$ cd src
$ python -m pip install --requirement=requirements.txt
$ make html
```
After successfully building the documentation navigate to `docs`.
There ought to be an `index.html` file. Open it with firefox/your browser of choice.


Hardware
--------
- [BL602/604 Datasheet](mirrored/BL602_BL604_DS_Datasheet.pdf)
  (34 pages): Includes pinout, memory map, and general peripheral descriptions
  but no detailed functional specification or register listings. Sipeed, a board
  vendor that plans to use the BL602, [claims](https://twitter.com/SipeedIO/status/1321658609990725633)
  that full register documentation will be available sometime in November 2020.
- [soc602_reg.svd][2]: Contains a seemingly-complete register listing, with
  names but no descriptions, for the BL602.
- [Hardware Notes](hardware_notes): Additional information
  gathered from the SDK repository and elsewhere on the internet.

[1]: https://pine64.github.io/bl602-docs/
[2]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/Device/Bouffalo/BL602/Peripherals/soc602_reg.svd
