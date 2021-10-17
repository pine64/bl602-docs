Hardware Notes
==============

This file contains a compilation of various pieces of information about the
BL602's hardware (e.g. core, peripherals, debug, memory map), gathered from
the SDK repository and around the internet. This is the best we can do in lieu
of a proper Technical Reference Manual, which has not yet been released as of
this writing.

Contributions welcome!

CPU Core
--------
According to [soc602_reg.svd][2], the BL602 contains a RISC-V RV32IMAFC core.
Interestingly, the [datasheet][1] and online spec sheets from Bouffalo Lab
never mention RISC-V, simply calling the core a "32-bit RISC CPU."

CNX Software [claims][5] that the core is a [SiFive E24][6]. Although this
claim is unsourced, information in the datasheet seems to corroborate it. The
datasheet claims that the CPU achieves a Dhrystone score of 1.46 DMIPS/MHz and
a CoreMark score of 3.1 CoreMark/MHz. These numbers exactly match what SiFive
advertises for the E24. Similarly, the set of RISC-V extensions matches, as
does the pipeline length (3-stage) and number of breakpoints/watchpoints (4).

The BL602 appears to diverge from the reference E24 implementation in its
memory map, however: its peripherals are mapped starting at `0x4000_0000`,
whereas SiFive's [E24 Manual][7] has a memory map placing peripherals at
`0x2000_0000` (although these two regions alias one another on the BL602; see
below).  Likewise, the BL602 maps its memories at `0x2000_0000` but the E24
reference design maps them at `0x6000_0000`. Finally, the BL602's TCMs are
differently-mapped, differently-named (TCM vs TIM), and differently-sized
(48KiB vs 32KiB) from the reference E24 ones. SiFive does claim that the memory
map and TIM sizes are customizable, though, so none of these differences are
strong evidence against the core being an E24.

[clic.h][4], which is part of the BL602's register definition headers, appears
to be a SiFive-authored file (see the include guard), and its addresses match
the E24 reference. I think this is one of the clearest pieces of evidence for
the core being SiFive IP.

Memory Map
----------
The [datasheet][1] contains a memory map, as does [soc602_reg.svd][2] and
[bl602.h][3]. As mentioned above, [clic.h][4] also contains part of the map.
These sources have been synthesized into this unified table. (Accuracy is not
guaranteed; please contribute a correction if you notice an error.)

**The address ranges `0x2xxx_xxxx`, `0x3xxx_xxxx`, `0x4xxx_xxxx`, and
`0x5xxx_xxxx` all appear to alias one another.** `0x6xxx_xxxx` and
`0x7xxx_xxxx` alias the same region for writes but cannot be written to (at
least not via JTAG), whereas all addresses `0x8000_0000` and above produce a
bus error for both writes and reads, indicating that the internal physical
memory bus is only 31 bits wide. The datasheet says that, for the TCMs and main
RAM, the `0x2xxx_xxxx` mappings are "used as program memory" and the
`0x4xxx_xxxx` mappings are "used as data memory", but it is unclear why this is
or if the hardware makes any distinction between accesses via the various
mappings.

| Base address  | Top address   |  Name                                                                                    | Register description                |
|---------------|---------------|------------------------------------------------------------------------------------------|-------------------------------------|
| `0x0200_0000` | `0x027F_FFFF` |  RISC-V CLINT                                                                            |                                     |
| `0x0280_0000` | `0x02FF_FFFF` |  Hart 0 CLIC                                                                             |                                     |
| `0x2100_0000` | `0x2101_FFFF` |  Mask ROM (holds boot and RomDriver code)                                                |                                     |
| `0x2200_8000` | `0x2201_3FFF` |  ITCM (Instruction Tightly Coupled Memory)                                               |                                     |
| `0x2201_4000` | `0x2201_FFFF` |  DTCM (Data Tightly Coupled Memory)                                                      |                                     |
| `0x2202_0000` | `0x2202_FFFF` |  Main RAM                                                                                |                                     |
| `0x2300_0000` | `0x23FF_FFFF` |  XIP (eXecute In Place) flash mapping                                                    |                                     |
| `0x4000_0000` | `0x4000_0FFF` |  `glb` (global control registers)                                                        | [GLB](registers/glb)                |
| `0x4000_1000` | `0x4000_1FFF` |  `rf` ("mixed signal"/radio)                                                             | [RF](registers/rf.md)               |
| `0x4000_2000` | `0x4000_2FFF` |  `gpip` (ADC+DAC+analog comparator config)                                               | [GPIP](registers/gpip.md)           |
| `0x4000_3000` | `0x4000_3FFF` |  *`sec_dbg`* (secure debug?)                                                             | [SEC_DBG](registers/sec_dbg.md)     |
| `0x4000_4000` | `0x4000_4FFF` |  `sec_eng` (security engine, e.g. SHA+AES)                                               | [SEC_ENG](registers/sec_eng.md)     |
| `0x4000_5000` | `0x4000_5FFF` |  `tzc_sec` ("trust isolation" #1)                                                        | [TZC_SEC](registers/tzc_sec.md)     |
| `0x4000_6000` | `0x4000_6FFF` |  `tzc_nsec` ("trust isolation" #2)                                                       | [TZC_NSEC](registers/tzc_nsec.md)   |
| `0x4000_7000` | `0x4000_707F` |  `ef_data_0` (eFuse data #1)                                                             | [EF_DATA_0](registers/ef_data_0.md) |
| `0x4000_7080` | `0x4000_70FF` |  `ef_data_1` (eFuse data #2)                                                             | [EF_DATA_1](registers/ef_data_1.md) |
| `0x4000_7800` | `0x4000_7FFF` |  `ef_ctrl` (eFuse control)                                                               | [EF_CTRL](registers/ef_ctrl.md)     |
| `0x4000_8000` | `0x4000_8FFF` |  *`cci`* (???)                                                                           | [CCI](registers/cci.md)             |
| `0x4000_9000` | `0x4000_9FFF` |  `l1c` (cache control)                                                                   | [L1C](registers/l1c.md)             |
| `0x4000_A000` | `0x4000_A0FF` |  `uart0` (UART #1)                                                                       | [UART](registers/uart.md)           |
| `0x4000_A100` | `0x4000_A1FF` |  `uart1` (UART #2)                                                                       | [UART](registers/uart.md)           |
| `0x4000_A200` | `0x4000_A2FF` |  `spi` (Serial Peripheral Interface)                                                     | [SPI](registers/spi.md)             |
| `0x4000_A300` | `0x4000_A3FF` |  `i2c` (I2C)                                                                             | [I2C](registers/i2c.md)             |
| `0x4000_A400` | `0x4000_A4FF` |  `pwm` (Pulse Width Modulation #1-#6)                                                    | [PWM](registers/pwm.md)             |
| `0x4000_A500` | `0x4000_A5FF` |  `timer` (Timer #1 and #2)                                                               | [TIMER](registers/timer.md)         |
| `0x4000_A600` | `0x4000_A6FF` |  `ir` (infrared remote accelerator)                                                      | [IR](registers/ir.md)               |
| `0x4000_A700` | `0x4000_A7FF` |  *`cks`* (checksum engine)                                                               | [CKS](registers/cks.md)             |
| `0x4000_B000` | `0x4000_B6FF` |  `sf_ctrl` (serial flash control)                                                        | [SF_CTRL](registers/sf_ctrl.md)     |
| `0x4000_B700` | `0x4000_BFFF` |  `sf_ctrl_buf` (serial flash data buffer)                                                |                                     |
| `0x4000_C000` | `0x4000_CFFF` |  `dma` (Direct Memory Access engine)                                                     | [DMA](registers/dma.md)             |
| `0x4000_D000` | `0x4000_DFFF` |  `sdu` (SDIO slave controller)                                                           |                                     |
| `0x4000_E000` | `0x4000_EFFF` |  `pds` (Power Down Sleep/sleep control)                                                  | [PDS](registers/pds.md)             |
| `0x4000_F000` | `0x4000_F7FF` |  `hbn` (Hibernate/deep sleep control)                                                    | [HBN](registers/hbn.md)             |
| `0x4000_F800` | `0x4000_FFFF` |  `aon` (Always-ON peripheral control)                                                    | [AON](registers/aon.md)             |
| `0x4001_0000` | `0x4001_0FFF` |  Deep sleep retention RAM                                                                |                                     |
| `0x4203_0000` | `0x4204_BFFF` |  Wireless RAM                                                                            |                                     |
| `0x44b0_0000` | `0x44b0_????` |  `mm` (MAC management), `txl`, `rxl` and `ps` (undocumented WiFi/BLE, see `mm_init`)     |                                     |
| `0x44c0_0000` | `0x44c?_????` |  `wifi phy` (identified from `phy_init`) (has many wifi related modules including `agc`) | [PHY](registers/phy.md)             |
| `0x54c0_a000` | `0x54c0_????` |  `agc` ucode (identified from `phy_init`)                                                |                                     |

(Peripherals in *`italics`* are present in the SVD but not the datasheet.)

bl602.h defines three extra mappings, labeled REMAP0, REMAP1, and REMAP2, in
addition to the ranges in the datasheet for each of flash XIP, main+wireless
RAM, and the TCMs. This appears to reflect the above-stated fact that
`0x2xxx_xxxx`, `0x3xxx_xxxx`, and `0x4xxx_xxxx` alias one another, but
unfortunately the names give no hint to if or how the mappings differ. The
remap base addresses are as follows:

| Memory | "Normal" base | REMAP0 base   | REMAP1 base   | REMAP2 base   |
|--------|---------------|---------------|---------------|---------------|
| XIP    | `0x2300_0000` | `0x3300_0000` | `0x4300_0000` | `0x5300_0000` |
| WRAM   | `0x4202_0000` | `0x2202_0000` | `0x3202_0000` | `0x5202_0000` |
| TCM    | `0x2200_8000` | `0x3200_8000` | `0x4200_8000` | `0x5200_8000` |

Note that the "WRAM" mapping in bl602.h, which starts at `0x4202_0000` and goes
to `0x4204_C000`, is badly named. It encompasses all of main RAM and all of
wireless RAM (but not the TCMs), instead of just wireless RAM like its name
implies.

The datasheet claims that the system has 276KiB of RAM, and indeed that is the
number we get by adding up 64KiB of main RAM, 112KiB of wireless RAM, 48KiB of
instruction TCM, 48KiB of data TCM, and 4KiB of deep sleep retention RAM.

On-chip ROM
-----------
The BL602 has 128KiB of "ROM," mapped at `0x2100_0000`. As far as I can tell,
this is an actual Mask ROM that's hardwired at the factory, not a flash or an
EEPROM. What immutable data could take up 128KiB? Code, it appears! In the
[OpenOCD configuration][8] for the BL602, `pc` is forced to the start of the
ROM after reset. Therefore, it seems likely that the beginning of the ROM holds
a BootROM which implements the various boot modes ("UART, SDIO, and Flash")
listed in the datasheet.

But that's not all that's in the ROM. There's an interesting peripheral driver
called [RomDriver][9], which exposes a number of functions for global register
configuration, power+clock+sleep management, serial flash setup, and general
operations like delay and memcpy. However, none of the functions are actually
implemented by the driver! Instead, it forwards each call to a corresponding
function pointer in a table at `0x2101_0800`, which is within the ROM. I assume
the function pointers in that table are also ROM addresses, meaning the bulk
of the ROM is likely taken up by library code. The SDK has a macro called
`BL602_USE_ROM_DRIVER` which selects whether to use the ROM implementation of
functions when available.

Registers in the TZ ("trust isolation") peripherals reference a ROM (for
example, `tzc_rom0_r0_lock`). This could indicate that areas of the ROM need
protection from unauthorized reads. Perhaps the ROM holds factory-provisioned,
per-device keys that are used as part of the secure boot flow? This, however,
is purely speculation.

Here are the known areas of the ROM's memory map:

| Base address  | Top address   |  Name                                      |
|---------------|---------------|--------------------------------------------|
| `0x2100_0000` | `0x2101_07FF` |  BootROM (+ other stuff?)                  |
| `0x2101_0800` | `0x2101_0FFF` |  RomDriver function table                  |
| `0x2101_1000` | `0x2101_FFFF` |  RomDriver functions (+ other stuff?)      |

[1]: ../mirrored/BL602_BL604_DS_1.6_en.pdf
[2]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/Device/Bouffalo/BL602/Peripherals/soc602_reg.svd
[3]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/Device/Bouffalo/BL602/Peripherals/bl602.svd
[4]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/RISCV/Core/Include/clic.h
[5]: https://www.cnx-software.com/2020/10/24/bl602-bl604-risc-v-wifi-bluetooth-5-0-le-soc-will-sell-at-esp8266-price-point/#comment-576285
[6]: https://www.sifive.com/cores/e24
[7]: https://sifive.cdn.prismic.io/sifive/dffb6a15-80b3-42cb-99e1-23ce6fd1d052_sifive_E24_rtl_full_20G1.03.00_manual.pdf
[8]: https://github.com/pine64/bl_iot_sdk/tree/master/tools/debug/tgt_602.cfg
[9]: https://github.com/pine64/bl_iot_sdk/tree/master/components/bl602/bl602_std/bl602_std/StdDriver/Inc/bl602_romdriver.h

RF IP
---
The BL602's RF stack is mostly based on CEVA RivieraWaves reference platform. The PHY is custom by Bouffalolab, but implements the standard RivieraWaves PHY. Luckily almost all the source code is publicy available in different SDKs. The RivieraWaves code has been published [here](https://github.com/cuihf1990/Alios_SDK/tree/edd416e7d2961db42c2100ac2d6237ee527d1aee/platform/mcu/moc108/mx108/mx378/ip) and the custom Bouffalolab PHY [here](https://github.com/jixinintelligence/bl602-604/tree/37f2d7b36b4c2ba6f073029d351551c33f9610f3/components/bl602/bl602_wifi/plf/refip/src/driver/phy/bl602_phy_rf). Some auxiliary code is als
o in either one of these repos. Together they cover most source in the demo binary.

RF PLL
===
The RF front-end of the BL602 uses a fractional-n PLL frequency synthesizer to synthesize a precise carrier and modulate it with the I/Q signal to produce the signal that will be transmitted.

Note that most of the content in this diagram is extrapolated from reverse analysis of RF driver code and typical analog designs, and does not necessarily match the actual design.

![LO Structure](./svg/RFLO.svg)

The output frequency `F` of the PLL is calculated by `frac = lo_sdmin / 2^22`, `crystal = fVCO / frac` and `F = fVCO * 3/4`.

On the other hand, to generate a target frequency of `F`, the `lo_sdmin` has to be `fVCO = 4/3 F`, `frac = fVCO / crystal` and `lo_sdmin = frac * 2^22`.

To improve the locking speed of the phase-locked loop, for each frequency point, the BL602 pre-calibrates a set of VCO inputs. It is conjectured that there is a voltage value and a current value that are calibrated in this process, where the voltage input is determined by the counter shown in the figure. For a given VCO input the resulting open-loop output is counted over a given period to fall around the theoretical value of the corresponding target frequency and the corresponding VCO input is recorded. The current value, on the other hand, is achieved by changing the input `lo_vco_idac_cw` of a digital-to-analog converter and detecting `acal_vco_ud` after correctly configuring the division frequency and voltage value of the SDM divider. The signal is presumed to be the control signal `up/down` from the phase detector output and is inferred to provide a more accurate frequency regulation capability compared to voltage.
