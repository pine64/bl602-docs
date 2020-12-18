# Clock configuration

*The base address for the registers described in this file is 0x40000000*

The BL602 has two main clock sources, a slow clock and a fast clock.

The slow clock is a fixed 32kHz clock, which is used for the Power Management Unit (PMU). It can also be configured as clock source for the Analog to digital converter (ADC) and Pulse Width Modulation (PWM) peripherals.

The 32kHz slow clock has three possible sources:
- The internal 32kHz RC oscillator (RC32K)
- An external 32kHz crystal oscillator (XTAL32K)
- 32kHz derrived from the main crystal oscillator (XTAL)

The fast clock is used for driving the CPU and most of the other components of the SoC.

The fast clock has three possible sources:
- The internal 32MHz RC oscillator (RC32M)
- An external crystal oscillator (XTAL)
- A high frequency clock derrived from the main crystal oscillator using a Phase Locked Loop (PLL)

The supported crystal frequencies are:
- 24MHz
- 32MHz
- 38.4Mhz
- 40MHz

The Phase Locked Loop (PLL) can multiply the crystal clock frequency to:
- 48MHz
- 120MHz
- 160Mhz
- 192MHz

## Register: Clock configuration 0

- Register name: clk_cfg0
- Register offset: 0x0000

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 1    | reg_pll_en        | R/W        | PLL enable                    | 0 = Disable<br />1 = Enable                               | SDK always leaves the PLL enabled         |
| 0x01   | 1    | reg_fclk_en       | R/W        | Flash clock enable (*)        | 0 = Disable<br />1 = Enable                               | SDK always leaves the flash clock enabled |
| 0x02   | 1    | reg_hclk_en       | R/W        | MCU clock enable              | 0 = Disable<br />1 = Enable                               | SDK always leaves the MCU clock enabled   |
| 0x03   | 1    | reg_bclk_en       | R/W        | Base clock enable             | 0 = Disable<br />1 = Enable                               | SDK always leaves the base clock enabled  |
| 0x04   | 2    | reg_pll_sel       | R/W        | PLL output frequency select   | 0 = 48MHz<br />1 = 120MHz<br />2 = 160MHz<br />3 = 192MHz |                                           |
| 0x06   | 2    | hbn_root_clk_sel  | R (\*\*)   | Root clock source selection   | 0 = RC32M<br />1 = XTAL<br />2 = PLL<br />3 = PLL         |                                           |
| 0x08   | 8    | reg_hclk_div      | R/W        | MCU clock divider             |                                                           | SDK always sets this register to 0        |
| 0x10   | 8    | reg_bclk_div      | R/W        | Base clock divider            |                                                           | SDK sets this register to values 0 and 1  |
| 0x18   | 3    | fclk_sw_state     | R          |                               |                                                           |                                           |
| 0x1B   | 1    | chip_rdy          | R          |                               |                                                           |                                           |
| 0x1C   | 4    | glb_id            | R          |                               |                                                           |                                           |

\**Note: This is a guess! The clock name ```fclk``` is used as the name for the ungated MCU clock,
but as there is no gate in the ```fclk``` clock signal while there is a gate in the flash clock signal
I suspect the ```reg_fclk_en``` register to be switching the flash clock signal.*

\*\*Note: the file ```glb_reg.h``` states that this register is read-only while ```bl602_glb.c``` does (attempt to) write to this bit in the reset procedures.

## Register: Clock configuration 1

- Register name: clk_cfg1
- Register offset: 0x0004

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 4    | wifi_mac_core_div | R/W        | WiFi core clock divider       | 0 = 80MHz<br />1 = 40MHz                                  | Source: *bl_wifi.c*                       |
| 0x04   | 4    | wifi_mac_wt_div   | R/W        | WiFi encryption clock divider |                                                           |                                           |
| 0x10   | 6    | ble_clk_sel       | R/W        |                               |                                                           |                                           |
| 0x18   | 1    | ble_en            | R/W        | Bluetooth clock enable        | 0 = Disable<br />1 = Enable                               |                                           |

*Note: bits 8-15, 22, 23 and 25-31 are reserved and should always be set to 0*

## Register: Clock configuration 2

- Register name: clk_cfg2
- Register offset: 0x0008

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 3    | uart_clk_div      | R/W        | UART clock divider            | (root clock or 160M)/(N+1)                                | Clock source set by hbn_uart_clk_sel     |
| 0x04   | 1    | uart_clk_en       | R/W        | UART clock enable             |                                                           | Set to 1 on reset                         |
| 0x07   | 1    | hbn_uart_clk_sel  | R (\*\*)   | UART clock selection from HBN | 0 = root clock, 1 = PLL @ 160 MHz                         |                                           |
| 0x08   | 3    | sf_clk_div        | R/W        | Flash clock divider           |                                                           |                                           |
| 0x0B   | 1    | sf_clk_en         | R/W        | Flash clock enable            |                                                           |                                           |
| 0x0C   | 2    | sf_clk_sel        | R/W        | Flash clock select            | 0 = 120 MHz, 1 = 80 MHz, 2 = HCLK, 3 = 96 MHz             |                                           |
| 0x0E   | 2    | sf_clk_sel2       | R/W        |                               |                                                           |                                           |
| 0x10   | 6    | ir_clk_div        | R/W        |                               |                                                           |                                           |
| 0x17   | 1    | ir_clk_en         | R/W        |                               |                                                           |                                           |
| 0x18   | 8    | dma_clk_en        | R/W        |                               |                                                           |                                           |

*Note: bits 3, 5, 6 and 22 are reserved and should always be set to 0*

\*\*Note: the datasheet states that this register is read-only, but it should be writable to allow selection of the UART clock source.


## Register: Clock configuration 3

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 5    | spi_clk_div       | R/W        | SPI clock divider             | (BUS_CLK/(N+1))                                           | Default is BUSCLK/4                       |
| 0x08   | 1    | spi_clk_en        | R/W        | SPI clock enable              |                                                           |                                           |
| 0x10   | 8    | i2c_clk_div       | R/W        | I2C master clock out divider  | BCLK/(N+1)                                                |                                           |
| 0x18   | 1    | i2c_clk_en        | R/W        | I2C master clock out enable   |                                                           |                                           |

*Note: bits 5-7, 9-15 and 25-31 are reserved and should always be set to 0*

## Register: Clock gate configuration 0

- Register name: cgen_cfg0
- Register offset: 0x0020

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 8    | cgen_m            | R/W        |                               |                                                           |                                           |

*Note: bits 8-31 are reserved and should always be set to 0*

## Register: Clock gate configuration 1

- Register name: cgen_cfg1
- Register offset: 0x0024

This register controls the clock enable for peripherals connected to AHB (Advanced High-speed Bus) slave 1.

| Offset | Size | Name              | Direction  | Description                   | Values                                                    |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- |
| 0x00   | 1    | cgen_s10          | R/W        | AHB slave 1 GLB               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x01   | 1    | cgen_s11          | R/W        | AHB slave 1 RF                | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x02   | 1    | cgen_s12          | R/W        | AHB slave 1 GPIP              | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x03   | 1    | cgen_s13          | R/W        | AHB slave 1 DBG               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x04   | 1    | cgen_s14          | R/W        | AHB slave 1 SEC               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x05   | 1    | cgen_s15          | R/W        | AHB slave 1 TZ1               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x06   | 1    | cgen_s16          | R/W        | AHB slave 1 TZ2               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x07   | 1    | cgen_s17          | R/W        | AHB slave 1 EFUSE             | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x08   | 1    | cgen_s18          | R/W        | AHB slave 1 CCI               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x09   | 1    | cgen_s19          | R/W        | AHB slave 1 L1C               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x0A   | 1    | cgen_s1a          | R/W        | *Not defined*                 | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x0B   | 1    | cgen_s1b          | R/W        | AHB slave 1 SFC               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x0C   | 1    | cgen_s1c          | R/W        | AHB slave 1 DMA               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x0D   | 1    | cgen_s1d          | R/W        | AHB slave 1 SDU               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x0E   | 1    | cgen_s1e          | R/W        | AHB slave 1 PDSHBN            | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x0F   | 1    | cgen_s1f          | R/W        | AHB slave 1 WRAM              | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x10   | 1    | cgen_s1a0         | R/W        | AHB slave 1 UART0             | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x11   | 1    | cgen_s1a1         | R/W        | AHB slave 1 UART1             | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x12   | 1    | cgen_s1a2         | R/W        | AHB slave 1 SPI               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x13   | 1    | cgen_s1a3         | R/W        | AHB slave 1 I2C               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x14   | 1    | cgen_s1a4         | R/W        | AHB slave 1 PWM               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x15   | 1    | cgen_s1a5         | R/W        | AHB slave 1 TMR               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x16   | 1    | cgen_s1a6         | R/W        | AHB slave 1 IRR               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |
| 0x17   | 1    | cgen_s1a7         | R/W        | AHB slave 1 CKS               | 0 = Clock gate (disabled)<br /> 1 = Clock pass (enabled)  |

*Note: bits 24-31 are reserved and should always be set to 0*

## Register: Clock gate configuration 2

- Register name: cgen_cfg2
- Register offset: 0x0028

Note: this register isn't used in the SDK.

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                                        |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| 0x00   | 1    | cgen_s2           |            | *Not defined*                 |                                                           | Guess based on register ```swrst_cfg0```: WiFi configuration |
| 0x04   | 1    | cgen_s3           |            | *Not defined*                 |                                                           | Guess based on register ```swrst_cfg0```: Bluetooth          |

*Note: bits 1-3 and 5-31 are reserved and should always be set to 0*

## Register: Clock gate configuration 3

- Register name: cgen_cfg3
- Register offset: 0x002C

*Note: all bits of this register are reserved and should always be set to 0*