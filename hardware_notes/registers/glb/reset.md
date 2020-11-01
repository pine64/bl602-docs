# Reset

*The base address for the registers described in this file is 0x40000000*

## Register: Software reset configuration 0

- Register name: swrst_cfg0
- Register offset: 0x0010

Note: this register isn't used in the SDK, descriptions are from ```bl602.h```.

| Offset | Size | Name                 | Direction  | Description                   |
| ------ | ---- | -------------------- | ---------- | ----------------------------- |
| 0x00   | 1    | swrst_s00            | R/W        | AHB slave 0 S2F               |
| 0x01   | 1    | swrst_s01            | R/W        | *Not defined*                 |
| 0x04   | 1    | swrst_s20            | R/W        | WiFi configuration            |
| 0x08   | 1    | swrst_s30            | R/W        | Bluetooth                     |

*Note: bits 2, 3, 5-7 and 9-31 are reserved and should always be set to 0*

## Register: Software reset configuration 1

- Register name: swrst_cfg1
- Register offset: 0x0014

This register controls the reset process for peripherals connected to AHB (Advanced High-speed Bus) slave 1.

Each of the bits in the register corresponds to a peripheral.
Setting a bit in this register puts the peripheral in reset state, clearing the bit resumes normal operation.

The SDK first clears the bit, then executes a few NOPs, sets the bit, executes a few NOPs again and finally clears the bit again.

| Offset | Size | Name                 | Direction  | Description                   |
| ------ | ---- | -------------------- | ---------- | ----------------------------- |
| 0x00   | 1    | swrst_s10            | R/W        | AHB slave 1 GLB               |
| 0x01   | 1    | swrst_s11            | R/W        | AHB slave 1 RF                |
| 0x02   | 1    | swrst_s12            | R/W        | AHB slave 1 GPIP              |
| 0x03   | 1    | swrst_s13            | R/W        | AHB slave 1 DBG               |
| 0x04   | 1    | swrst_s14            | R/W        | AHB slave 1 SEC               |
| 0x05   | 1    | swrst_s15            | R/W        | AHB slave 1 TZ1               |
| 0x06   | 1    | swrst_s16            | R/W        | AHB slave 1 TZ2               |
| 0x07   | 1    | swrst_s17            | R/W        | AHB slave 1 EFUSE             |
| 0x08   | 1    | swrst_s18            | R/W        | AHB slave 1 CCI               |
| 0x09   | 1    | swrst_s19            | R/W        | AHB slave 1 L1C               |
| 0x0A   | 1    | swrst_s1a            | R/W        | *Not defined*                 |
| 0x0B   | 1    | swrst_s1b            | R/W        | AHB slave 1 SFC               |
| 0x0C   | 1    | swrst_s1c            | R/W        | AHB slave 1 DMA               |
| 0x0D   | 1    | swrst_s1d            | R/W        | AHB slave 1 SDU               |
| 0x0E   | 1    | swrst_s1e            | R/W        | AHB slave 1 PDSHBN            |
| 0x0F   | 1    | swrst_s1f            | R/W        | AHB slave 1 WRAM              |
| 0x10   | 1    | swrst_s1a0           | R/W        | AHB slave 1 UART0             |
| 0x11   | 1    | swrst_s1a1           | R/W        | AHB slave 1 UART1             |
| 0x12   | 1    | swrst_s1a2           | R/W        | AHB slave 1 SPI               |
| 0x13   | 1    | swrst_s1a3           | R/W        | AHB slave 1 I2C               |
| 0x14   | 1    | swrst_s1a4           | R/W        | AHB slave 1 PWM               |
| 0x15   | 1    | swrst_s1a5           | R/W        | AHB slave 1 TMR               |
| 0x16   | 1    | swrst_s1a6           | R/W        | AHB slave 1 IRR               |
| 0x17   | 1    | swrst_s1a7           | R/W        | AHB slave 1 CKS               |

*Note: bits 24-31 are reserved and should always be set to 0*

## Register: Software reset configuration 2

- Register name: swrst_cfg2
- Register offset: 0x0018

This register is used to reset the whole chip. The SDK defines three reset procedures:
- System reset
- Software CPU reset
- Software power on reset

The ```system reset``` procedure executes the following steps:
- Switch the main clock source to the internal ```RC32M``` oscillator
- Set the divider of the ```BCLK``` and ```HCLK``` clocks to ```0```
- Set register ```0x40000FFC``` to ```1``` (GLB_REG_BCLK_DIS_TRUE)
- Set register ```0x40000FFC``` to ```0``` (GLB_REG_BCLK_DIS_FALSE)
- Waits for 8 NOPs
- Clear bits ```reg_ctrl_sys_reset```, ```reg_ctrl_cpu_reset``` and ```reg_ctrl_pwron_rst```
- Set bits ```reg_ctrl_sys_reset``` and ```reg_ctrl_cpu_reset```
- Enters an endless loop, awaiting reset

The ```software CPU reset``` procedure executes the following steps:
- Switch the main clock source to the internal ```RC32M``` oscillator
- Set the divider of the ```BCLK``` and ```HCLK``` clocks to ```0```
- Set register ```0x40000FFC``` to ```1``` (GLB_REG_BCLK_DIS_TRUE)
- Set register ```0x40000FFC``` to ```0``` (GLB_REG_BCLK_DIS_FALSE)
- Waits for 8 NOPs
- Clear bits ```reg_ctrl_sys_reset```, ```reg_ctrl_cpu_reset``` and ```reg_ctrl_pwron_rst```
- Set bits ```reg_ctrl_cpu_reset```
- Enters an endless loop, awaiting reset

The ```software power on reset``` procedure executes the following steps:
- Switch the main clock source to the internal ```RC32M``` oscillator
- Set the divider of the ```BCLK``` and ```HCLK``` clocks to ```0```
- Set register ```0x40000FFC``` to ```1``` (GLB_REG_BCLK_DIS_TRUE)
- Set register ```0x40000FFC``` to ```0``` (GLB_REG_BCLK_DIS_FALSE)
- Waits for 8 NOPs
- Clear bits ```reg_ctrl_sys_reset```, ```reg_ctrl_cpu_reset``` and ```reg_ctrl_pwron_rst```
- Set bits ```reg_ctrl_sys_reset```, ```reg_ctrl_cpu_reset``` and ```reg_ctrl_pwron_rst```
- Enters an endless loop, awaiting reset

| Offset | Size | Name                 | Direction  | Notes                                                                                                        |
| ------ | ---- | -------------------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| 0x00   | 1    | reg_ctrl_pwron_rst   | R/W        | Set as part of the ```software power on reset``` procedure                                                   |
| 0x01   | 1    | reg_ctrl_cpu_reset   | R/W        | Set as part of the ```system reset```, ```software CPU reset``` and ```software power on reset``` procedures |
| 0x02   | 1    | reg_ctrl_sys_reset   | R/W        | Set as part of the ```system reset``` and ```software power on reset``` procedures                           |
| 0x04   | 4    | reg_ctrl_reset_dummy | R/W        |                                                                                                              |
| 0x18   | 1    | pka_clk_sel          | R/W        | PKA clock source<br />0 = HCLK<br />1 = PLL 120MHz                                                           |

*Note: bits 3, 8-23 and 25-31 are reserved and should always be set to 0*

## Register: Software reset configuration 3

- Register name: swrst_cfg3
- Register offset: 0x001C

*Note: all bits of this register are reserved and should always be set to 0*