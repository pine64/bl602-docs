# GPIO configuration

*The base address for the registers described in this file is 0x40000000*

The BL602 has 28 GPIO pins, configurable and usable through reading and writing to memory.

`GPIO_CFGCTL0` through `GPIO_CFGCTL14` are used for configuring GPIO0 through GPIO28 for:

1. Function
2. Pulldown/Pullup Resistor
3. Driving control
4. Schmitt trigger
5. Input enable

`GPIO_CFGCTL0` contains configuration for GPIO0 and GPIO1.
`GPIO_CFGCTL1` contains configuration for GPIO2 and GPIO3 and so on.
Every register except for `GPIO_CFGCTL14` contains configuration for two GPIO pins.

`GPIO_CFGCTL30` is used for reading the current input status for all GPIO pins.

`GPIO_CFGCTL32` is used for setting the output for all GPIO pins.

`GPIO_CFGCTL34` is used for enabling output for all GPIO pins.

`GPIO_INT_MASK1` is used for setting the masking and unmasking of interrupts.
1 is masked and 0 is unmasked.

`GPIO_INT_STAT1` is used for getting the status of GPIO interrupts.
1 is set and 0 is reset.

`GPIO_INT_CLR1` is used for clearing interrupts.
1 clears an interrupt and 0 does nothing.

`GPIO_MODE_SET1` is used for setting the interrupt mode and trigger for GPIO0 through GPIO09.
`GPIO_MODE_SET2` is used for setting the interrupt mode and trigger for GPIO10 through GPIO19.
`GPIO_MODE_SET3` is used for setting the interrupt mode and trigger for GPIO20 through GPIO29.

`GPIO_CFGCTL31`, `GPIO_CFGCTL33`, and `GPIO_CFGCTL35` are reserved and unused.

## Register: GPIO0/GPIO1 Configuration

- Register name: `GPIO_CFGCTL0`
- Register offset: 0x100

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 1    | `reg_gpio_0_ie`   | R/W        | Input enable                  | 0 = Disable<br />1 = Enable                               |                                           |
| 0x01   | 1    | `reg_gpio_0_smt`  | R/W        | Schmitt trigger enable        | 0 = Disable<br />1 = Enable                               |                                           |
| 0x02   | 2    | `reg_gpio_0_drv`  | R/W        | Driving control               | TODO                                                      |                                           |
| 0x04   | 1    | `reg_gpio_0_pu`   | R/W        | Pull Up Resistor enable       | 0 = Disable<br />1 = Enable                               |                                           |
| 0x05   | 1    | `reg_gpio_0_pd`   | R/W        | Pull Down Resistor enable     | 0 = Disable<br />1 = Enable                               |                                           |
| 0x06   | 1    | `reg_gpio_0_pd`   | R/W        | Pull Down Resistor enable     | 0 = Disable<br />1 = Enable                               |                                           |
| 0x08   | 1    | `reg_gpio_0_func_sel` | R/W        | Function select     | 1 = `SDIO_CLK`<br />2 = `SF_D1`<br/>4 = `SPI_MISO_SPI_MOSI`<br/>6 = `I2C_SCL`<br/>7 = `UART_SIG0`<br/>8 = `PWM_CH0`<br/>9 = `FEM_GPIO_0`<br/>10 = `ATEST_IN`<br/>11 = `SWGPIO`<br/>14 = `E21_TMS` | 3 and 5 are listed as unused in the SDK. 12 and 13 are not listed in the SDK. |

