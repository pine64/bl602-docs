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
- [Official Documents](https://github.com/bouffalolab/bl_docs): Includes datasheets and reference manuals directly from Bouffalo. Not mirrored here since they are updated frequently.
- [soc602_reg.svd][2]: Contains a seemingly-complete register listing, with
  names but no descriptions, for the BL602.
- [Hardware Notes](hardware_notes): Additional information
  gathered from the SDK repository and elsewhere on the internet.

[1]: https://pine64.github.io/bl602-docs/
[2]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/Device/Bouffalo/BL602/Peripherals/soc602_reg.svd
