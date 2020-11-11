BL602 Documentation
===================

This documentation can be found [online][1] at [pine64.github.io/bl602-docs][1].

Building The Documentation
--------------------------
To build the documentation yourself:
```bash
$ cd src
$ python -m pip install -r requirements.txt
$ cd en   # cd zh to build documentation in chinese
$ make html  # on Windows, set SPHINXBUILD="python -m sphinx" for this command
```
The documentation will be built inside the `docs` folder. To view it, open `docs/index.html`
in your browser of choice.

Hardware
--------
- [Official Documents](https://github.com/bouffalolab/bl_docs): Includes detailed core and peripheral documentation
- [BL602/604 Datasheet](mirrored/Bouffalo%20Lab%20BL602_BL604_DS_en_Combo_1.2.pdf)
  (34 pages): Includes pinout, memory map, and general peripheral descriptions
  but no detailed functional specification or register listings.
- [BL602/604 Reference Manual](mirrored/Bouffalo%20Lab%20BL602_Reference_Manual_en_1.1.pdf)
  (209 pages): Includes register map, clock tree and other information about implementing BL602/BL604
- [soc602_reg.svd][2]: Contains a seemingly-complete register listing, with
  names but no descriptions, for the BL602.
- [Hardware Notes](hardware_notes): Additional information
  gathered from the SDK repository and elsewhere on the internet.

[1]: https://pine64.github.io/bl602-docs/
[2]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/Device/Bouffalo/BL602/Peripherals/soc602_reg.svd
