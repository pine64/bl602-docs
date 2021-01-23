# GPIO configuration

*The base address for the registers described in this file is 0x40000000*

The BL602 has 28 GPIO pins, configurable and usable through reading and writing to memory.

`GPIO_CFGCTL0` through `GPIO_CFGCTL14` are used for configuring GPIO0 through GPIO28 for:

1. Function
2. Pulldown/Pullup Resistor
3. Driving control
4. Schmitt trigger
5. Input enable

`GPIO_CFGCTL0` contains configuration for GPIO0 and GPIO1, `GPIO_CFGCTL1` contains configuration for GPIO2 and GPIO3, and so on.
Every register except for `GPIO_CFGCTL14` contains configuration for two GPIO pins.

`GPIO_CFGCTL30` is used for reading the current input status for all GPIO pins.

`GPIO_CFGCTL32` is used for setting the output for all GPIO pins.

`GPIO_CFGCTL34` is used for enabling output for all GPIO pins.

`GPIO_INT_MASK1` is used for setting the masking and unmasking of interrupts for all GPIO pins.
1 is masked and 0 is unmasked.

`GPIO_INT_STAT1` is used for getting the status of GPIO interrupts for all GPIO pins.
1 is set and 0 is reset.

`GPIO_INT_CLR1` is used for clearing interrupts for all GPIO pins.
1 clears an interrupt and 0 does nothing.

`GPIO_MODE_SET1` is used for setting the interrupt mode and trigger for GPIO0 through GPIO09.
`GPIO_MODE_SET2` is used for setting the interrupt mode and trigger for GPIO10 through GPIO19.
`GPIO_MODE_SET3` is used for setting the interrupt mode and trigger for GPIO20 through GPIO29.

`GPIO_CFGCTL31`, `GPIO_CFGCTL33`, and `GPIO_CFGCTL35` are reserved and unused.

# Register: GPIO_CFGCTL0

- Register name: GPIO_CFGCTL0
- Register Offset: 0x100
- Description: GPIO0, GPIO1 configuration

| Offset | Size | Name                 | Access       | Description                        | Values |
| ------ | ---- | -------------------- | ------------ | ---------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_ie        | Read & Write | GPIO0 input enable.                | `GPIO0InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_0_smt       | Read & Write | Schmitt trigger enabled for GPIO0. | `GPIO0Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_0_drv       | Read & Write | Driving control for GPIO0.         | `GPIO0Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_0_pu        | Read & Write | Pull Up Resistor for GPIO0.        | `GPIO0PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_0_pd        | Read & Write | Pull Down Resistor for GPIO0.      | `GPIO0PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_0_func_sel  | Read & Write | Function select for GPIO0.         | `GPIO0FunctionSelect`<br/>1 = SDIO_CLK <br/>2 = SF_D1 <br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SCL <br/>7 = UART_SIG0 <br/>8 = PWM_CH0 <br/>9 = FEM_GPIO_0 <br/>10 = ATEST_IN <br/>11 = SWGPIO_0 <br/>14 = E21_TMS <br/>       |
| 0xc    | 4    | real_gpio_0_func_sel | Read Only    |                                    |        |
| 0x10   | 1    | reg_gpio_1_ie        | Read & Write | Input enable for GPIO1.            | `GPIO1InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_1_smt       | Read & Write | Schmitt trigger enabled for GPIO1. | `GPIO1Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_1_drv       | Read & Write | Driving control enabled for GPIO1. | `GPIO1Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_1_pu        | Read & Write | Pull Up Resistor for GPIO1.        | `GPIO1PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_1_pd        | Read & Write | Pull Down Resistor for GPIO1.      | `GPIO1PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_1_func_sel  | Read & Write | Function select for GPIO1.         | `GPIO1FunctionSelect`<br/>1 = SDIO_CMD <br/>2 = SF_D2 <br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SDA <br/>7 = UART_SIG1 <br/>8 = PWM_CH1 <br/>9 = FEM_GPIO_1 <br/>10 = ATEST_IP <br/>11 = SWGPIO_1 <br/>14 = E21_TDI <br/>       |
| 0x1c   | 4    | real_gpio_1_func_sel | Read Only    |                                    |        |


# Register: GPIO_CFGCTL1

- Register name: GPIO_CFGCTL1
- Register Offset: 0x104
- Description: GPIO2, GPIO3 configuration

| Offset | Size | Name                 | Access       | Description                        | Values |
| ------ | ---- | -------------------- | ------------ | ---------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_2_ie        | Read & Write | Input enable for GPIO2.            | `GPIO2InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_2_smt       | Read & Write | Schmitt trigger enabled for GPIO2. | `GPIO2Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_2_drv       | Read & Write | Driving control enabled for GPIO2. | `GPIO2Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_2_pu        | Read & Write | Pull Up Resistor for GPIO2.        | `GPIO2PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_2_pd        | Read & Write | Pull Down Resistor for GPIO2.      | `GPIO2PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_2_func_sel  | Read & Write | Function select for GPIO2.         | `GPIO2FunctionSelect`<br/>1 = SDIO_DAT0 <br/>2 = SF_D3 <br/>4 = SPI_SS <br/>6 = I2C_SCL <br/>7 = UART_SIG2 <br/>8 = PWM_CH2 <br/>9 = FEM_GPIO_2 <br/>10 = ATEST_QN <br/>11 = SWGPIO_2 <br/>14 = E21_TCK <br/>       |
| 0xc    | 4    | real_gpio_2_func_sel | Read Only    |                                    |        |
| 0x10   | 1    | reg_gpio_3_ie        | Read & Write | Input enable for GPIO3.            | `GPIO3InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_3_smt       | Read & Write | Schmitt trigger enabled for GPIO3. | `GPIO3Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_3_drv       | Read & Write | Driving control enabled for GPIO3. | `GPIO3Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_3_pu        | Read & Write | Pull Up Resistor for GPIO3.        | `GPIO3PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_3_pd        | Read & Write | Pull Down Resistor for GPIO3.      | `GPIO3PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_3_func_sel  | Read & Write | Function select for GPIO3.         | `GPIO3FunctionSelect`<br/>1 = SDIO_DAT1 <br/>4 = SPI_SCLK <br/>6 = I2C_SDA <br/>7 = UART_SIG3 <br/>8 = PWM_CH3 <br/>9 = FEM_GPIO_3 <br/>10 = ATEST_QP <br/>11 = SWGPIO_3 <br/>14 = E21_TDO <br/>       |
| 0x1c   | 4    | real_gpio_3_func_sel | Read Only    |                                    |        |


# Register: GPIO_CFGCTL2

- Register name: GPIO_CFGCTL2
- Register Offset: 0x108
- Description: GPIO4, GPIO5 configuration

| Offset | Size | Name                 | Access       | Description                        | Values |
| ------ | ---- | -------------------- | ------------ | ---------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_4_ie        | Read & Write | Input enable for GPIO4.            | `GPIO4InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_4_smt       | Read & Write | Schmitt trigger enabled for GPIO4. | `GPIO4Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_4_drv       | Read & Write | Driving control enabled for GPIO4. | `GPIO4Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_4_pu        | Read & Write | Pull Up Resistor for GPIO4.        | `GPIO4PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_4_pd        | Read & Write | Pull Down Resistor for GPIO4.      | `GPIO4PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_4_func_sel  | Read & Write | Function select for GPIO4.         | `GPIO4FunctionSelect`<br/>1 = SDIO_DAT2 <br/>4 = SPI_MISO_SPI_MOSI <br/>6 = I2C_SCL <br/>7 = UART_SIG4 <br/>8 = PWM_CH4 <br/>9 = FEM_GPIO_0 <br/>10 = GPIP_CH1 <br/>11 = SWGPIO_4 <br/>14 = E21_TMS <br/>       |
| 0xc    | 4    | real_gpio_4_func_sel | Read Only    |                                    |        |
| 0x10   | 1    | reg_gpio_5_ie        | Read & Write | Input enable for GPIO5.            | `GPIO5InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_5_smt       | Read & Write | Schmitt trigger enabled for GPIO5. | `GPIO5Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_5_drv       | Read & Write | Driving control enabled for GPIO5. | `GPIO5Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_5_pu        | Read & Write | Pull Up Resistor for GPIO5.        | `GPIO5PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_5_pd        | Read & Write | Pull Down Resistor for GPIO5.      | `GPIO5PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_5_func_sel  | Read & Write | Function select for GPIO5.         | `GPIO5FunctionSelect`<br/>1 = SDIO_DAT3 <br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SDA <br/>7 = UART_SIG5 <br/>8 = PWM_CH0 <br/>9 = FEM_GPIO_1 <br/>10 = GPIP_CH4 <br/>11 = SWGPIO_5 <br/>14 = E21_TDI <br/>       |
| 0x1c   | 4    | real_gpio_5_func_sel | Read Only    |                                    |        |


# Register: GPIO_CFGCTL3

- Register name: GPIO_CFGCTL3
- Register Offset: 0x10c
- Description: GPIO6, GPIO7 configuration

| Offset | Size | Name                | Access       | Description                        | Values |
| ------ | ---- | ------------------- | ------------ | ---------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_6_ie       | Read & Write | Input enable for GPIO6.            | `GPIO6InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_6_smt      | Read & Write | Schmitt trigger enabled for GPIO6. | `GPIO6Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_6_drv      | Read & Write | Driving control enabled for GPIO6. | `GPIO6Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_6_pu       | Read & Write | Pull Up Resistor for GPIO6.        | `GPIO6PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_6_pd       | Read & Write | Pull Down Resistor for GPIO6.      | `GPIO6PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_6_func_sel | Read & Write | Function select for GPIO6.         | `GPIO6FunctionSelect`<br/>4 = SPI_SS <br/>6 = I2C_SCL <br/>7 = UART_SIG6 <br/>8 = PWM_CH1 <br/>9 = FEM_GPIO_2 <br/>10 = GPIP_CH5 <br/>11 = SWGPIO_6 <br/>14 = E21_TCK <br/>       |
| 0x10   | 1    | reg_gpio_7_ie       | Read & Write | Input enable for GPIO7.            | `GPIO7InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_7_smt      | Read & Write | Schmitt trigger enabled for GPIO7. | `GPIO7Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_7_drv      | Read & Write | Driving control enabled for GPIO7. | `GPIO7Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_7_pu       | Read & Write | Pull Up Resistor for GPIO7.        | `GPIO7PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_7_pd       | Read & Write | Pull Down Resistor for GPIO7.      | `GPIO7PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_7_func_sel | Read & Write | Function select for GPIO7.         | `GPIO7FunctionSelect`<br/>4 = SPI_SCLK <br/>6 = I2C_SDA <br/>7 = UART_SIG7 <br/>8 = PWM_CH2 <br/>9 = FEM_GPIO_3 <br/>11 = SWGPIO_7 <br/>14 = E21_TDO <br/>       |


# Register: GPIO_CFGCTL4

- Register name: GPIO_CFGCTL4
- Register Offset: 0x110
- Description: GPIO8, GPIO9 configuration

| Offset | Size | Name                | Access       | Description                        | Values |
| ------ | ---- | ------------------- | ------------ | ---------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_8_ie       | Read & Write | Input enable for GPIO8.            | `GPIO8InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_8_smt      | Read & Write | Schmitt trigger enabled for GPIO8. | `GPIO8Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_8_drv      | Read & Write | Driving control enabled for GPIO8. | `GPIO8Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_8_pu       | Read & Write | Pull Up Resistor for GPIO8.        | `GPIO8PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_8_pd       | Read & Write | Pull Down Resistor for GPIO8.      | `GPIO8PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_8_func_sel | Read & Write | Function select for GPIO8.         | `GPIO8FunctionSelect`<br/>4 = SPI_MISO_SPI_MOSI <br/>6 = I2C_SCL <br/>7 = UART_SIG0 <br/>8 = PWM_CH3 <br/>9 = FEM_GPIO_0 <br/>11 = SWGPIO_8 <br/>14 = E21_TMS <br/>       |
| 0x10   | 1    | reg_gpio_9_ie       | Read & Write | Input enable for GPIO9.            | `GPIO9InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_9_smt      | Read & Write | Schmitt trigger enabled for GPIO9. | `GPIO9Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_9_drv      | Read & Write | Driving control enabled for GPIO9. | `GPIO9Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_9_pu       | Read & Write | Pull Up Resistor for GPIO9.        | `GPIO9PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_9_pd       | Read & Write | Pull Down Resistor for GPIO9.      | `GPIO9PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_9_func_sel | Read & Write | Function select for GPIO9.         | `GPIO9FunctionSelect`<br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SDA <br/>7 = UART_SIG1 <br/>8 = PWM_CH4 <br/>9 = FEM_GPIO_1 <br/>10 = GPIP_CH6_GPIP_CH7 <br/>11 = SWGPIO_9 <br/>14 = E21_TDI <br/>       |


# Register: GPIO_CFGCTL5

- Register name: GPIO_CFGCTL5
- Register Offset: 0x114
- Description: GPIO10, GPIO11 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_10_ie       | Read & Write | Input enable for GPIO10.            | `GPIO10InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_10_smt      | Read & Write | Schmitt trigger enabled for GPIO10. | `GPIO10Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_10_drv      | Read & Write | Driving control enabled for GPIO10. | `GPIO10Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_10_pu       | Read & Write | Pull Up Resistor for GPIO10.        | `GPIO10PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_10_pd       | Read & Write | Pull Down Resistor for GPIO10.      | `GPIO10PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_10_func_sel | Read & Write | Function select for GPIO10.         | `GPIO10FunctionSelect`<br/>4 = SPI_SS <br/>6 = I2C_SCL <br/>7 = UART_SIG2 <br/>8 = PWM_CH0 <br/>9 = FEM_GPIO_2 <br/>10 = MICBIAS_GPIP_CH8_GPIP_CH9 <br/>11 = SWGPIO_10 <br/>14 = E21_TCK <br/>       |
| 0x10   | 1    | reg_gpio_11_ie       | Read & Write | Input enable for GPIO11.            | `GPIO11InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_11_smt      | Read & Write | Schmitt trigger enabled for GPIO11. | `GPIO11Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_11_drv      | Read & Write | Driving control enabled for GPIO11. | `GPIO11Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_11_pu       | Read & Write | Pull Up Resistor for GPIO11.        | `GPIO11PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_11_pd       | Read & Write | Pull Down Resistor for GPIO11.      | `GPIO11PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_11_func_sel | Read & Write | Function select for GPIO11.         | `GPIO11FunctionSelect`<br/>4 = SPI_SCLK <br/>6 = I2C_SDA <br/>7 = UART_SIG3 <br/>8 = PWM_CH1 <br/>9 = FEM_GPIO_3 <br/>10 = IRLED_OUT_GPIP_CH10 <br/>11 = SWGPIO_11 <br/>14 = E21_TDO <br/>       |


# Register: GPIO_CFGCTL6

- Register name: GPIO_CFGCTL6
- Register Offset: 0x118
- Description: GPIO12, GPIO13 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_12_ie       | Read & Write | Input enable for GPIO12.            | `GPIO12InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_12_smt      | Read & Write | Schmitt trigger enabled for GPIO12. | `GPIO12Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_12_drv      | Read & Write | Driving control enabled for GPIO12. | `GPIO12Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_12_pu       | Read & Write | Pull Up Resistor for GPIO12.        | `GPIO12PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_12_pd       | Read & Write | Pull Down Resistor for GPIO12.      | `GPIO12PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_12_func_sel | Read & Write | Function select for GPIO12.         | `GPIO12FunctionSelect`<br/>4 = SPI_MISO_SPI_MOSI <br/>6 = I2C_SCL <br/>7 = UART_SIG4 <br/>8 = PWM_CH2 <br/>9 = FEM_GPIO_0 <br/>10 = GPIP_CH0_GPADC_VREF_EXT <br/>11 = SWGPIO_12 <br/>14 = E21_TMS <br/>       |
| 0x10   | 1    | reg_gpio_13_ie       | Read & Write | Input enable for GPIO13.            | `GPIO13InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_13_smt      | Read & Write | Schmitt trigger enabled for GPIO13. | `GPIO13Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_13_drv      | Read & Write | Driving control enabled for GPIO13. | `GPIO13Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_13_pu       | Read & Write | Pull Up Resistor for GPIO13.        | `GPIO13PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_13_pd       | Read & Write | Pull Down Resistor for GPIO13.      | `GPIO13PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_13_func_sel | Read & Write | Function select for GPIO13.         | `GPIO13FunctionSelect`<br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SDA <br/>7 = UART_SIG5 <br/>8 = PWM_CH3 <br/>9 = FEM_GPIO_1 <br/>10 = GPIP_CH3 <br/>11 = SWGPIO_13 <br/>14 = E21_TDI <br/>       |


# Register: GPIO_CFGCTL7

- Register name: GPIO_CFGCTL7
- Register Offset: 0x11c
- Description: GPIO14, GPIO15 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_14_ie       | Read & Write | Input enable for GPIO14.            | `GPIO14InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_14_smt      | Read & Write | Schmitt trigger enabled for GPIO14. | `GPIO14Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_14_drv      | Read & Write | Driving control enabled for GPIO14. | `GPIO14Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_14_pu       | Read & Write | Pull Up Resistor for GPIO14.        | `GPIO14PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_14_pd       | Read & Write | Pull Down Resistor for GPIO14.      | `GPIO14PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_14_func_sel | Read & Write | Function select for GPIO14.         | `GPIO14FunctionSelect`<br/>4 = SPI_SS <br/>6 = I2C_SCL <br/>7 = UART_SIG6 <br/>8 = PWM_CH4 <br/>9 = FEM_GPIO_2 <br/>10 = GPIP_CH2 <br/>11 = SWGPIO_14 <br/>14 = E21_TCK <br/>       |
| 0x10   | 1    | reg_gpio_15_ie       | Read & Write | Input enable for GPIO15.            | `GPIO15InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_15_smt      | Read & Write | Schmitt trigger enabled for GPIO15. | `GPIO15Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_15_drv      | Read & Write | Driving control enabled for GPIO15. | `GPIO15Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_15_pu       | Read & Write | Pull Up Resistor for GPIO15.        | `GPIO15PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_15_pd       | Read & Write | Pull Down Resistor for GPIO15.      | `GPIO15PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_15_func_sel | Read & Write | Function select for GPIO15.         | `GPIO15FunctionSelect`<br/>4 = SPI_SCLK <br/>6 = I2C_SDA <br/>7 = UART_SIG7 <br/>8 = PWM_CH0 <br/>9 = FEM_GPIO_3 <br/>10 = PSW_IRRCV_OUT_GPIP_CH11 <br/>11 = SWGPIO_15 <br/>14 = E21_TDO <br/>       |


# Register: GPIO_CFGCTL8

- Register name: GPIO_CFGCTL8
- Register Offset: 0x120
- Description: GPIO16, GPIO17 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_16_ie       | Read & Write | Input enable for GPIO16.            | `GPIO16InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_16_smt      | Read & Write | Schmitt trigger enabled for GPIO16. | `GPIO16Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_16_drv      | Read & Write | Driving control enabled for GPIO16. | `GPIO16Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_16_pu       | Read & Write | Pull Up Resistor for GPIO16.        | `GPIO16PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_16_pd       | Read & Write | Pull Down Resistor for GPIO16.      | `GPIO16PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_16_func_sel | Read & Write | Function select for GPIO16.         | `GPIO16FunctionSelect`<br/>4 = SPI_MISO_SPI_MOSI <br/>6 = I2C_SCL <br/>7 = UART_SIG0 <br/>8 = PWM_CH1 <br/>9 = FEM_GPIO_0 <br/>11 = SWGPIO_16 <br/>14 = E21_TMS <br/>       |
| 0x10   | 1    | reg_gpio_17_ie       | Read & Write | Input enable for GPIO17.            | `GPIO17InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_17_smt      | Read & Write | Schmitt trigger enabled for GPIO17. | `GPIO17Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_17_drv      | Read & Write | Driving control enabled for GPIO17. | `GPIO17Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_17_pu       | Read & Write | Pull Up Resistor for GPIO17.        | `GPIO17PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_17_pd       | Read & Write | Pull Down Resistor for GPIO17.      | `GPIO17PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_17_func_sel | Read & Write | Function select for GPIO17.         | `GPIO17FunctionSelect`<br/>2 = SF_D3 <br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SDA <br/>7 = UART_SIG1 <br/>8 = PWM_CH2 <br/>9 = FEM_GPIO_1 <br/>10 = PMIP_DC_TP_OUT <br/>11 = SWGPIO_17 <br/>14 = E21_TDI <br/>       |


# Register: GPIO_CFGCTL9

- Register name: GPIO_CFGCTL9
- Register Offset: 0x124
- Description: GPIO18, GPIO19 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_18_ie       | Read & Write | Input enable for GPIO18.            | `GPIO18InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_18_smt      | Read & Write | Schmitt trigger enabled for GPIO18. | `GPIO18Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_18_drv      | Read & Write | Driving control enabled for GPIO18. | `GPIO18Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_18_pu       | Read & Write | Pull Up Resistor for GPIO18.        | `GPIO18PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_18_pd       | Read & Write | Pull Down Resistor for GPIO18.      | `GPIO18PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_18_func_sel | Read & Write | Function select for GPIO18.         | `GPIO18FunctionSelect`<br/>2 = SF_D2 <br/>4 = SPI_SS <br/>6 = I2C_SCL <br/>7 = UART_SIG2 <br/>8 = PWM_CH3 <br/>9 = FEM_GPIO_2 <br/>11 = SWGPIO_18 <br/>14 = E21_TCK <br/>       |
| 0x10   | 1    | reg_gpio_19_ie       | Read & Write | Input enable for GPIO19.            | `GPIO19InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_19_smt      | Read & Write | Schmitt trigger enabled for GPIO19. | `GPIO19Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_19_drv      | Read & Write | Driving control enabled for GPIO19. | `GPIO19Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_19_pu       | Read & Write | Pull Up Resistor for GPIO19.        | `GPIO19PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_19_pd       | Read & Write | Pull Down Resistor for GPIO19.      | `GPIO19PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_19_func_sel | Read & Write | Function select for GPIO19.         | `GPIO19FunctionSelect`<br/>2 = SF_D1 <br/>4 = SPI_SCLK <br/>6 = I2C_SDA <br/>7 = UART_SIG3 <br/>8 = PWM_CH4 <br/>9 = FEM_GPIO_3 <br/>11 = SWGPIO_19 <br/>14 = E21_TDO <br/>       |


# Register: GPIO_CFGCTL10

- Register name: GPIO_CFGCTL10
- Register Offset: 0x128
- Description: GPIO20, GPIO21 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_20_ie       | Read & Write | Input enable for GPIO20.            | `GPIO20InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_20_smt      | Read & Write | Schmitt trigger enabled for GPIO20. | `GPIO20Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_20_drv      | Read & Write | Driving control enabled for GPIO20. | `GPIO20Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_20_pu       | Read & Write | Pull Up Resistor for GPIO20.        | `GPIO20PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_20_pd       | Read & Write | Pull Down Resistor for GPIO20.      | `GPIO20PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_20_func_sel | Read & Write | Function select for GPIO20.         | `GPIO20FunctionSelect`<br/>2 = SF_D0 <br/>4 = SPI_MISO_SPI_MOSI <br/>6 = I2C_SCL <br/>7 = UART_SIG4 <br/>8 = PWM_CH0 <br/>9 = FEM_GPIO_0 <br/>11 = SWGPIO_20 <br/>14 = E21_TMS <br/>       |
| 0x10   | 1    | reg_gpio_21_ie       | Read & Write | Input enable for GPIO21.            | `GPIO21InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_21_smt      | Read & Write | Schmitt trigger enabled for GPIO21. | `GPIO21Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_21_drv      | Read & Write | Driving control enabled for GPIO21. | `GPIO21Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_21_pu       | Read & Write | Pull Up Resistor for GPIO21.        | `GPIO21PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_21_pd       | Read & Write | Pull Down Resistor for GPIO21.      | `GPIO21PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x18   | 4    | reg_gpio_21_func_sel | Read & Write | Function select for GPIO21.         | `GPIO21FunctionSelect`<br/>2 = SF_CS <br/>4 = SPI_MOSI_SPI_MISO <br/>6 = I2C_SDA <br/>7 = UART_SIG5 <br/>8 = PWM_CH1 <br/>9 = FEM_GPIO_1 <br/>11 = SWGPIO_21 <br/>14 = E21_TDI <br/>       |


# Register: GPIO_CFGCTL11

- Register name: GPIO_CFGCTL11
- Register Offset: 0x12c
- Description: GPIO22, GPIO23 configuration

| Offset | Size | Name                 | Access       | Description                         | Values |
| ------ | ---- | -------------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_22_ie       | Read & Write | Input enable for GPIO22.            | `GPIO22InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_22_smt      | Read & Write | Schmitt trigger enabled for GPIO22. | `GPIO22Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_22_drv      | Read & Write | Driving control enabled for GPIO22. | `GPIO22Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_22_pu       | Read & Write | Pull Up Resistor for GPIO22.        | `GPIO22PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_22_pd       | Read & Write | Pull Down Resistor for GPIO22.      | `GPIO22PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 4    | reg_gpio_22_func_sel | Read & Write | Function select for GPIO22.         | `GPIO22FunctionSelect`<br/>2 = SF_CLK_OUT <br/>4 = SPI_SS <br/>6 = I2C_SCL <br/>7 = UART_SIG6 <br/>8 = PWM_CH2 <br/>9 = FEM_GPIO_2 <br/>11 = SWGPIO_22 <br/>14 = E21_TCK <br/>       |
| 0x10   | 1    | reg_gpio_23_ie       | Read & Write | Input enable for GPIO23.            | `GPIO23InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_23_smt      | Read & Write | Schmitt trigger enabled for GPIO23. | `GPIO23Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_23_drv      | Read & Write | Driving control enabled for GPIO23. | `GPIO23Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_23_pu       | Read & Write | Pull Up Resistor for GPIO23.        | `GPIO23PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_23_pd       | Read & Write | Pull Down Resistor for GPIO23.      | `GPIO23PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL12

- Register name: GPIO_CFGCTL12
- Register Offset: 0x130
- Description: GPIO24, GPIO25 configuration

| Offset | Size | Name            | Access       | Description                         | Values |
| ------ | ---- | --------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_24_ie  | Read & Write | Input enable for GPIO24.            | `GPIO24InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_24_smt | Read & Write | Schmitt trigger enabled for GPIO24. | `GPIO24Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_24_drv | Read & Write | Driving control enabled for GPIO24. | `GPIO24Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_24_pu  | Read & Write | Pull Up Resistor for GPIO24.        | `GPIO24PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_24_pd  | Read & Write | Pull Down Resistor for GPIO24.      | `GPIO24PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x10   | 1    | reg_gpio_25_ie  | Read & Write | Input enable for GPIO25.            | `GPIO25InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_25_smt | Read & Write | Schmitt trigger enabled for GPIO25. | `GPIO25Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_25_drv | Read & Write | Driving control enabled for GPIO25. | `GPIO25Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_25_pu  | Read & Write | Pull Up Resistor for GPIO25.        | `GPIO25PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_25_pd  | Read & Write | Pull Down Resistor for GPIO25.      | `GPIO25PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL13

- Register name: GPIO_CFGCTL13
- Register Offset: 0x134
- Description: GPIO26, GPIO27 configuration

| Offset | Size | Name            | Access       | Description                         | Values |
| ------ | ---- | --------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_26_ie  | Read & Write | Input enable for GPIO26.            | `GPIO26InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_26_smt | Read & Write | Schmitt trigger enabled for GPIO26. | `GPIO26Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_26_drv | Read & Write | Driving control enabled for GPIO26. | `GPIO26Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_26_pu  | Read & Write | Pull Up Resistor for GPIO26.        | `GPIO26PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_26_pd  | Read & Write | Pull Down Resistor for GPIO26.      | `GPIO26PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x10   | 1    | reg_gpio_27_ie  | Read & Write | Input enable for GPIO27.            | `GPIO27InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_27_smt | Read & Write | Schmitt trigger enabled for GPIO27. | `GPIO27Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 2    | reg_gpio_27_drv | Read & Write | Driving control enabled for GPIO27. | `GPIO27Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_27_pu  | Read & Write | Pull Up Resistor for GPIO27.        | `GPIO27PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_27_pd  | Read & Write | Pull Down Resistor for GPIO27.      | `GPIO27PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL14

- Register name: GPIO_CFGCTL14
- Register Offset: 0x138
- Description: GPIO28 configuration

| Offset | Size | Name            | Access       | Description                         | Values |
| ------ | ---- | --------------- | ------------ | ----------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_28_ie  | Read & Write | Input enable for GPIO28.            | `GPIO28InputEnabled`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_28_smt | Read & Write | Schmitt trigger enabled for GPIO28. | `GPIO28Schmitt`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 2    | reg_gpio_28_drv | Read & Write | Driving control enabled for GPIO28. | `GPIO28Driving`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_28_pu  | Read & Write | Pull Up Resistor for GPIO28.        | `GPIO28PullUpResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_28_pd  | Read & Write | Pull Down Resistor for GPIO28.      | `GPIO28PullDownResistor`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL30

- Register name: GPIO_CFGCTL30
- Register Offset: 0x180
- Description: Input register for all GPIO pins. Input Enabled bit must be set in configuration register to work.

| Offset | Size | Name          | Access    | Description                | Values |
| ------ | ---- | ------------- | --------- | -------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_i  | Read Only |                            |        |
| 0x1    | 1    | reg_gpio_1_i  | Read Only | Input register for GPIO1.  | `GPIO1Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 1    | reg_gpio_2_i  | Read Only | Input register for GPIO2.  | `GPIO2Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x3    | 1    | reg_gpio_3_i  | Read Only | Input register for GPIO3.  | `GPIO3Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_4_i  | Read Only | Input register for GPIO4.  | `GPIO4Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_5_i  | Read Only | Input register for GPIO5.  | `GPIO5Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x6    | 1    | reg_gpio_6_i  | Read Only | Input register for GPIO6.  | `GPIO6Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x7    | 1    | reg_gpio_7_i  | Read Only | Input register for GPIO7.  | `GPIO7Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 1    | reg_gpio_8_i  | Read Only | Input register for GPIO8.  | `GPIO8Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x9    | 1    | reg_gpio_9_i  | Read Only | Input register for GPIO9.  | `GPIO9Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xa    | 1    | reg_gpio_10_i | Read Only | Input register for GPIO10. | `GPIO10Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xb    | 1    | reg_gpio_11_i | Read Only | Input register for GPIO11. | `GPIO11Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xc    | 1    | reg_gpio_12_i | Read Only | Input register for GPIO12. | `GPIO12Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xd    | 1    | reg_gpio_13_i | Read Only | Input register for GPIO13. | `GPIO13Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xe    | 1    | reg_gpio_14_i | Read Only | Input register for GPIO14. | `GPIO14Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xf    | 1    | reg_gpio_15_i | Read Only | Input register for GPIO15. | `GPIO15Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x10   | 1    | reg_gpio_16_i | Read Only | Input register for GPIO16. | `GPIO16Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_17_i | Read Only | Input register for GPIO17. | `GPIO17Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 1    | reg_gpio_18_i | Read Only | Input register for GPIO18. | `GPIO18Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x13   | 1    | reg_gpio_19_i | Read Only | Input register for GPIO19. | `GPIO19Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_20_i | Read Only | Input register for GPIO20. | `GPIO20Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_21_i | Read Only | Input register for GPIO21. | `GPIO21Input`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x16   | 1    | reg_gpio_22_i | Read Only | Input register for GPIO22. | `GPIO22Input`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL31

- Register name: GPIO_CFGCTL31
- Register Offset: 0x184
- Description: Reserved according to SDK.

No fields.

# Register: GPIO_CFGCTL32

- Register name: GPIO_CFGCTL32
- Register Offset: 0x188
- Description: Output register for all GPIO pins. Output Enabled bit must be set in Output Enable register to work.

| Offset | Size | Name          | Access       | Description                 | Values |
| ------ | ---- | ------------- | ------------ | --------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_o  | Read & Write | Output register for GPIO0.  | `GPIO0Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_1_o  | Read & Write | Output register for GPIO1.  | `GPIO1Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 1    | reg_gpio_2_o  | Read & Write | Output register for GPIO2.  | `GPIO2Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x3    | 1    | reg_gpio_3_o  | Read & Write | Output register for GPIO3.  | `GPIO3Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_4_o  | Read & Write | Output register for GPIO4.  | `GPIO4Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_5_o  | Read & Write | Output register for GPIO5.  | `GPIO5Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x6    | 1    | reg_gpio_6_o  | Read & Write | Output register for GPIO6.  | `GPIO6Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x7    | 1    | reg_gpio_7_o  | Read & Write | Output register for GPIO7.  | `GPIO7Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 1    | reg_gpio_8_o  | Read & Write | Output register for GPIO8.  | `GPIO8Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x9    | 1    | reg_gpio_9_o  | Read & Write | Output register for GPIO9.  | `GPIO9Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xa    | 1    | reg_gpio_10_o | Read & Write | Output register for GPIO10. | `GPIO10Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xb    | 1    | reg_gpio_11_o | Read & Write | Output register for GPIO11. | `GPIO11Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xc    | 1    | reg_gpio_12_o | Read & Write | Output register for GPIO12. | `GPIO12Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xd    | 1    | reg_gpio_13_o | Read & Write | Output register for GPIO13. | `GPIO13Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xe    | 1    | reg_gpio_14_o | Read & Write | Output register for GPIO14. | `GPIO14Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xf    | 1    | reg_gpio_15_o | Read & Write | Output register for GPIO15. | `GPIO15Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x10   | 1    | reg_gpio_16_o | Read & Write | Output register for GPIO16. | `GPIO16Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_17_o | Read & Write | Output register for GPIO17. | `GPIO17Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 1    | reg_gpio_18_o | Read & Write | Output register for GPIO18. | `GPIO18Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x13   | 1    | reg_gpio_19_o | Read & Write | Output register for GPIO19. | `GPIO19Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_20_o | Read & Write | Output register for GPIO20. | `GPIO20Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_21_o | Read & Write | Output register for GPIO21. | `GPIO21Output`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x16   | 1    | reg_gpio_22_o | Read & Write | Output register for GPIO22. | `GPIO22Output`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL33

- Register name: GPIO_CFGCTL33
- Register Offset: 0x18c
- Description: Reserved according to SDK.

No fields.

# Register: GPIO_CFGCTL34

- Register name: GPIO_CFGCTL34
- Register Offset: 0x190
- Description: Output enable register for GPIO.

| Offset | Size | Name           | Access       | Description                        | Values |
| ------ | ---- | -------------- | ------------ | ---------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_oe  | Read & Write | Output enable register for GPIO0.  | `GPIO0OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x1    | 1    | reg_gpio_1_oe  | Read & Write | Output enable register for GPIO1.  | `GPIO1OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x2    | 1    | reg_gpio_2_oe  | Read & Write | Output enable register for GPIO2.  | `GPIO2OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x3    | 1    | reg_gpio_3_oe  | Read & Write | Output enable register for GPIO3.  | `GPIO3OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x4    | 1    | reg_gpio_4_oe  | Read & Write | Output enable register for GPIO4.  | `GPIO4OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x5    | 1    | reg_gpio_5_oe  | Read & Write | Output enable register for GPIO5.  | `GPIO5OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x6    | 1    | reg_gpio_6_oe  | Read & Write | Output enable register for GPIO6.  | `GPIO6OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x7    | 1    | reg_gpio_7_oe  | Read & Write | Output enable register for GPIO7.  | `GPIO7OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x8    | 1    | reg_gpio_8_oe  | Read & Write | Output enable register for GPIO8.  | `GPIO8OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x9    | 1    | reg_gpio_9_oe  | Read & Write | Output enable register for GPIO9.  | `GPIO9OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xa    | 1    | reg_gpio_10_oe | Read & Write | Output enable register for GPIO10. | `GPIO10OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xb    | 1    | reg_gpio_11_oe | Read & Write | Output enable register for GPIO11. | `GPIO11OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xc    | 1    | reg_gpio_12_oe | Read & Write | Output enable register for GPIO12. | `GPIO12OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xd    | 1    | reg_gpio_13_oe | Read & Write | Output enable register for GPIO13. | `GPIO13OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xe    | 1    | reg_gpio_14_oe | Read & Write | Output enable register for GPIO14. | `GPIO14OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0xf    | 1    | reg_gpio_15_oe | Read & Write | Output enable register for GPIO15. | `GPIO15OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x10   | 1    | reg_gpio_16_oe | Read & Write | Output enable register for GPIO16. | `GPIO16OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x11   | 1    | reg_gpio_17_oe | Read & Write | Output enable register for GPIO17. | `GPIO17OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x12   | 1    | reg_gpio_18_oe | Read & Write | Output enable register for GPIO18. | `GPIO18OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x13   | 1    | reg_gpio_19_oe | Read & Write | Output enable register for GPIO19. | `GPIO19OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x14   | 1    | reg_gpio_20_oe | Read & Write | Output enable register for GPIO20. | `GPIO20OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x15   | 1    | reg_gpio_21_oe | Read & Write | Output enable register for GPIO21. | `GPIO21OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |
| 0x16   | 1    | reg_gpio_22_oe | Read & Write | Output enable register for GPIO22. | `GPIO22OutputEnable`<br/>0 = disabled <br/>1 = enabled <br/>       |


# Register: GPIO_CFGCTL35

- Register name: GPIO_CFGCTL35
- Register Offset: 0x194
- Description: Reserved according to SDK.

No fields.

# Register: GPIO_INT_MASK1

- Register name: GPIO_INT_MASK1
- Register Offset: 0x1a0
- Description: Interrupt masking register. The SDK limits the GPIO pins to < 32 although the docs do not mention more than 28 GPIO pins.

| Offset | Size | Name             | Access       | Description               | Values |
| ------ | ---- | ---------------- | ------------ | ------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_mask  | Read & Write | Mask register for GPIO0.  | `GPIO0Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x1    | 1    | reg_gpio_1_mask  | Read & Write | Mask register for GPIO1.  | `GPIO1Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x2    | 1    | reg_gpio_2_mask  | Read & Write | Mask register for GPIO2.  | `GPIO2Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x3    | 1    | reg_gpio_3_mask  | Read & Write | Mask register for GPIO3.  | `GPIO3Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x4    | 1    | reg_gpio_4_mask  | Read & Write | Mask register for GPIO4.  | `GPIO4Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x5    | 1    | reg_gpio_5_mask  | Read & Write | Mask register for GPIO5.  | `GPIO5Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x6    | 1    | reg_gpio_6_mask  | Read & Write | Mask register for GPIO6.  | `GPIO6Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x7    | 1    | reg_gpio_7_mask  | Read & Write | Mask register for GPIO7.  | `GPIO7Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x8    | 1    | reg_gpio_8_mask  | Read & Write | Mask register for GPIO8.  | `GPIO8Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x9    | 1    | reg_gpio_9_mask  | Read & Write | Mask register for GPIO9.  | `GPIO9Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0xa    | 1    | reg_gpio_10_mask | Read & Write | Mask register for GPIO10. | `GPIO10Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0xb    | 1    | reg_gpio_11_mask | Read & Write | Mask register for GPIO11. | `GPIO11Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0xc    | 1    | reg_gpio_12_mask | Read & Write | Mask register for GPIO12. | `GPIO12Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0xd    | 1    | reg_gpio_13_mask | Read & Write | Mask register for GPIO13. | `GPIO13Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0xe    | 1    | reg_gpio_14_mask | Read & Write | Mask register for GPIO14. | `GPIO14Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0xf    | 1    | reg_gpio_15_mask | Read & Write | Mask register for GPIO15. | `GPIO15Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x10   | 1    | reg_gpio_16_mask | Read & Write | Mask register for GPIO16. | `GPIO16Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x11   | 1    | reg_gpio_17_mask | Read & Write | Mask register for GPIO17. | `GPIO17Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x12   | 1    | reg_gpio_18_mask | Read & Write | Mask register for GPIO18. | `GPIO18Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x13   | 1    | reg_gpio_19_mask | Read & Write | Mask register for GPIO19. | `GPIO19Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x14   | 1    | reg_gpio_20_mask | Read & Write | Mask register for GPIO20. | `GPIO20Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x15   | 1    | reg_gpio_21_mask | Read & Write | Mask register for GPIO21. | `GPIO21Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x16   | 1    | reg_gpio_22_mask | Read & Write | Mask register for GPIO22. | `GPIO22Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x17   | 1    | reg_gpio_23_mask | Read & Write | Mask register for GPIO23. | `GPIO23Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x18   | 1    | reg_gpio_24_mask | Read & Write | Mask register for GPIO24. | `GPIO24Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x19   | 1    | reg_gpio_25_mask | Read & Write | Mask register for GPIO25. | `GPIO25Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x1a   | 1    | reg_gpio_26_mask | Read & Write | Mask register for GPIO26. | `GPIO26Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x1b   | 1    | reg_gpio_27_mask | Read & Write | Mask register for GPIO27. | `GPIO27Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |
| 0x1c   | 1    | reg_gpio_28_mask | Read & Write | Mask register for GPIO28. | `GPIO28Mask`<br/>0 = unmasked <br/>1 = masked <br/>       |


# Register: GPIO_INT_STAT1

- Register name: GPIO_INT_STAT1
- Register Offset: 0x1a8
- Description: Interrupt status register. The SDK limits the GPIO pins to < 32 although the docs do not mention more than 28 GPIO pins.

| Offset | Size | Name                         | Access    | Description                           | Values |
| ------ | ---- | ---------------------------- | --------- | ------------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_interrupt_status  | Read Only | Interrupt status register for GPIO0.  | `GPIO0InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x1    | 1    | reg_gpio_1_interrupt_status  | Read Only | Interrupt status register for GPIO1.  | `GPIO1InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x2    | 1    | reg_gpio_2_interrupt_status  | Read Only | Interrupt status register for GPIO2.  | `GPIO2InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x3    | 1    | reg_gpio_3_interrupt_status  | Read Only | Interrupt status register for GPIO3.  | `GPIO3InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x4    | 1    | reg_gpio_4_interrupt_status  | Read Only | Interrupt status register for GPIO4.  | `GPIO4InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x5    | 1    | reg_gpio_5_interrupt_status  | Read Only | Interrupt status register for GPIO5.  | `GPIO5InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x6    | 1    | reg_gpio_6_interrupt_status  | Read Only | Interrupt status register for GPIO6.  | `GPIO6InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x7    | 1    | reg_gpio_7_interrupt_status  | Read Only | Interrupt status register for GPIO7.  | `GPIO7InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x8    | 1    | reg_gpio_8_interrupt_status  | Read Only | Interrupt status register for GPIO8.  | `GPIO8InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x9    | 1    | reg_gpio_9_interrupt_status  | Read Only | Interrupt status register for GPIO9.  | `GPIO9InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0xa    | 1    | reg_gpio_10_interrupt_status | Read Only | Interrupt status register for GPIO10. | `GPIO10InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0xb    | 1    | reg_gpio_11_interrupt_status | Read Only | Interrupt status register for GPIO11. | `GPIO11InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0xc    | 1    | reg_gpio_12_interrupt_status | Read Only | Interrupt status register for GPIO12. | `GPIO12InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0xd    | 1    | reg_gpio_13_interrupt_status | Read Only | Interrupt status register for GPIO13. | `GPIO13InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0xe    | 1    | reg_gpio_14_interrupt_status | Read Only | Interrupt status register for GPIO14. | `GPIO14InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0xf    | 1    | reg_gpio_15_interrupt_status | Read Only | Interrupt status register for GPIO15. | `GPIO15InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x10   | 1    | reg_gpio_16_interrupt_status | Read Only | Interrupt status register for GPIO16. | `GPIO16InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x11   | 1    | reg_gpio_17_interrupt_status | Read Only | Interrupt status register for GPIO17. | `GPIO17InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x12   | 1    | reg_gpio_18_interrupt_status | Read Only | Interrupt status register for GPIO18. | `GPIO18InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x13   | 1    | reg_gpio_19_interrupt_status | Read Only | Interrupt status register for GPIO19. | `GPIO19InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x14   | 1    | reg_gpio_20_interrupt_status | Read Only | Interrupt status register for GPIO20. | `GPIO20InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x15   | 1    | reg_gpio_21_interrupt_status | Read Only | Interrupt status register for GPIO21. | `GPIO21InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x16   | 1    | reg_gpio_22_interrupt_status | Read Only | Interrupt status register for GPIO22. | `GPIO22InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x17   | 1    | reg_gpio_23_interrupt_status | Read Only | Interrupt status register for GPIO23. | `GPIO23InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x18   | 1    | reg_gpio_24_interrupt_status | Read Only | Interrupt status register for GPIO24. | `GPIO24InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x19   | 1    | reg_gpio_25_interrupt_status | Read Only | Interrupt status register for GPIO25. | `GPIO25InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x1a   | 1    | reg_gpio_26_interrupt_status | Read Only | Interrupt status register for GPIO26. | `GPIO26InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x1b   | 1    | reg_gpio_27_interrupt_status | Read Only | Interrupt status register for GPIO27. | `GPIO27InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |
| 0x1c   | 1    | reg_gpio_28_interrupt_status | Read Only | Interrupt status register for GPIO28. | `GPIO28InterruptStatus`<br/>0 = reset <br/>1 = set <br/>       |


# Register: GPIO_INT_CLR1

- Register name: GPIO_INT_CLR1
- Register Offset: 0x1b0
- Description: Interrupt clearing register.

| Offset | Size | Name                        | Access       | Description                             | Values |
| ------ | ---- | --------------------------- | ------------ | --------------------------------------- | ------ |
| 0x0    | 1    | reg_gpio_0_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO0.  | `GPIO0InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x1    | 1    | reg_gpio_1_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO1.  | `GPIO1InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x2    | 1    | reg_gpio_2_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO2.  | `GPIO2InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x3    | 1    | reg_gpio_3_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO3.  | `GPIO3InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x4    | 1    | reg_gpio_4_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO4.  | `GPIO4InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x5    | 1    | reg_gpio_5_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO5.  | `GPIO5InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x6    | 1    | reg_gpio_6_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO6.  | `GPIO6InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x7    | 1    | reg_gpio_7_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO7.  | `GPIO7InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x8    | 1    | reg_gpio_8_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO8.  | `GPIO8InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x9    | 1    | reg_gpio_9_interrupt_clear  | Read & Write | Interrupt clearing register for GPIO9.  | `GPIO9InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0xa    | 1    | reg_gpio_10_interrupt_clear | Read & Write | Interrupt clearing register for GPIO10. | `GPIO10InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0xb    | 1    | reg_gpio_11_interrupt_clear | Read & Write | Interrupt clearing register for GPIO11. | `GPIO11InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0xc    | 1    | reg_gpio_12_interrupt_clear | Read & Write | Interrupt clearing register for GPIO12. | `GPIO12InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0xd    | 1    | reg_gpio_13_interrupt_clear | Read & Write | Interrupt clearing register for GPIO13. | `GPIO13InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0xe    | 1    | reg_gpio_14_interrupt_clear | Read & Write | Interrupt clearing register for GPIO14. | `GPIO14InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0xf    | 1    | reg_gpio_15_interrupt_clear | Read & Write | Interrupt clearing register for GPIO15. | `GPIO15InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x10   | 1    | reg_gpio_16_interrupt_clear | Read & Write | Interrupt clearing register for GPIO16. | `GPIO16InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x11   | 1    | reg_gpio_17_interrupt_clear | Read & Write | Interrupt clearing register for GPIO17. | `GPIO17InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x12   | 1    | reg_gpio_18_interrupt_clear | Read & Write | Interrupt clearing register for GPIO18. | `GPIO18InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x13   | 1    | reg_gpio_19_interrupt_clear | Read & Write | Interrupt clearing register for GPIO19. | `GPIO19InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x14   | 1    | reg_gpio_20_interrupt_clear | Read & Write | Interrupt clearing register for GPIO20. | `GPIO20InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x15   | 1    | reg_gpio_21_interrupt_clear | Read & Write | Interrupt clearing register for GPIO21. | `GPIO21InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x16   | 1    | reg_gpio_22_interrupt_clear | Read & Write | Interrupt clearing register for GPIO22. | `GPIO22InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x17   | 1    | reg_gpio_23_interrupt_clear | Read & Write | Interrupt clearing register for GPIO23. | `GPIO23InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x18   | 1    | reg_gpio_24_interrupt_clear | Read & Write | Interrupt clearing register for GPIO24. | `GPIO24InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x19   | 1    | reg_gpio_25_interrupt_clear | Read & Write | Interrupt clearing register for GPIO25. | `GPIO25InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x1a   | 1    | reg_gpio_26_interrupt_clear | Read & Write | Interrupt clearing register for GPIO26. | `GPIO26InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x1b   | 1    | reg_gpio_27_interrupt_clear | Read & Write | Interrupt clearing register for GPIO27. | `GPIO27InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |
| 0x1c   | 1    | reg_gpio_28_interrupt_clear | Read & Write | Interrupt clearing register for GPIO28. | `GPIO28InterruptClear`<br/>0 = no-clear <br/>1 = clear <br/>       |


# Register: GPIO_INT_MODE_SET1

- Register name: GPIO_INT_MODE_SET1
- Register Offset: 0x1c0
- Description: GPIO interrupt trigger and control register for GPIO0-GPIO9.

| Offset | Size | Name                              | Access       | Description                                | Values |
| ------ | ---- | --------------------------------- | ------------ | ------------------------------------------ | ------ |
| 0x0    | 2    | reg_gpio_0_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO0. | `GPIO0TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x2    | 1    | reg_gpio_0_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO0. | `GPIO0ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x3    | 2    | reg_gpio_1_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO1. | `GPIO1TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x5    | 1    | reg_gpio_1_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO1. | `GPIO1ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x6    | 2    | reg_gpio_2_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO2. | `GPIO2TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x8    | 1    | reg_gpio_2_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO2. | `GPIO2ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x9    | 2    | reg_gpio_3_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO3. | `GPIO3TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0xb    | 1    | reg_gpio_3_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO3. | `GPIO3ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0xc    | 2    | reg_gpio_4_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO4. | `GPIO4TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0xe    | 1    | reg_gpio_4_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO4. | `GPIO4ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0xf    | 2    | reg_gpio_5_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO5. | `GPIO5TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x11   | 1    | reg_gpio_5_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO5. | `GPIO5ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x12   | 2    | reg_gpio_6_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO6. | `GPIO6TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x14   | 1    | reg_gpio_6_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO6. | `GPIO6ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x15   | 2    | reg_gpio_7_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO7. | `GPIO7TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x17   | 1    | reg_gpio_7_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO7. | `GPIO7ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x18   | 2    | reg_gpio_8_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO8. | `GPIO8TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x1a   | 1    | reg_gpio_8_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO8. | `GPIO8ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x1b   | 2    | reg_gpio_9_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO9. | `GPIO9TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x1d   | 1    | reg_gpio_9_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO9. | `GPIO9ControlMode`<br/>0 = sync <br/>1 = async <br/>       |


# Register: GPIO_INT_MODE_SET2

- Register name: GPIO_INT_MODE_SET2
- Register Offset: 0x1c4
- Description: GPIO interrupt trigger and control register for GPIO10-GPIO19.

| Offset | Size | Name                               | Access       | Description                                 | Values |
| ------ | ---- | ---------------------------------- | ------------ | ------------------------------------------- | ------ |
| 0x0    | 2    | reg_gpio_10_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO10. | `GPIO10TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x2    | 1    | reg_gpio_10_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO10. | `GPIO10ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x3    | 2    | reg_gpio_11_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO11. | `GPIO11TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x5    | 1    | reg_gpio_11_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO11. | `GPIO11ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x6    | 2    | reg_gpio_12_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO12. | `GPIO12TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x8    | 1    | reg_gpio_12_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO12. | `GPIO12ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x9    | 2    | reg_gpio_13_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO13. | `GPIO13TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0xb    | 1    | reg_gpio_13_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO13. | `GPIO13ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0xc    | 2    | reg_gpio_14_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO14. | `GPIO14TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0xe    | 1    | reg_gpio_14_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO14. | `GPIO14ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0xf    | 2    | reg_gpio_15_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO15. | `GPIO15TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x11   | 1    | reg_gpio_15_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO15. | `GPIO15ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x12   | 2    | reg_gpio_16_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO16. | `GPIO16TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x14   | 1    | reg_gpio_16_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO16. | `GPIO16ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x15   | 2    | reg_gpio_17_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO17. | `GPIO17TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x17   | 1    | reg_gpio_17_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO17. | `GPIO17ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x18   | 2    | reg_gpio_18_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO18. | `GPIO18TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x1a   | 1    | reg_gpio_18_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO18. | `GPIO18ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x1b   | 2    | reg_gpio_19_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO19. | `GPIO19TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x1d   | 1    | reg_gpio_19_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO19. | `GPIO19ControlMode`<br/>0 = sync <br/>1 = async <br/>       |


# Register: GPIO_INT_MODE_SET3

- Register name: GPIO_INT_MODE_SET3
- Register Offset: 0x1c8
- Description: GPIO interrupt trigger and control register for GPIO20-GPIO29.

| Offset | Size | Name                               | Access       | Description                                 | Values |
| ------ | ---- | ---------------------------------- | ------------ | ------------------------------------------- | ------ |
| 0x0    | 2    | reg_gpio_20_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO20. | `GPIO20TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x2    | 1    | reg_gpio_20_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO20. | `GPIO20ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x3    | 2    | reg_gpio_21_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO21. | `GPIO21TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x5    | 1    | reg_gpio_21_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO21. | `GPIO21ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x6    | 2    | reg_gpio_22_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO22. | `GPIO22TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x8    | 1    | reg_gpio_22_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO22. | `GPIO22ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x9    | 2    | reg_gpio_23_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO23. | `GPIO23TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0xb    | 1    | reg_gpio_23_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO23. | `GPIO23ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0xc    | 2    | reg_gpio_24_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO24. | `GPIO24TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0xe    | 1    | reg_gpio_24_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO24. | `GPIO24ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0xf    | 2    | reg_gpio_25_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO25. | `GPIO25TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x11   | 1    | reg_gpio_25_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO25. | `GPIO25ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x12   | 2    | reg_gpio_26_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO26. | `GPIO26TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x14   | 1    | reg_gpio_26_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO26. | `GPIO26ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x15   | 2    | reg_gpio_27_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO27. | `GPIO27TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x17   | 1    | reg_gpio_27_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO27. | `GPIO27ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x18   | 2    | reg_gpio_28_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO28. | `GPIO28TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x1a   | 1    | reg_gpio_28_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO28. | `GPIO28ControlMode`<br/>0 = sync <br/>1 = async <br/>       |
| 0x1b   | 2    | reg_gpio_29_interrupt_trigger_mode | Read & Write | Interrupt trigger mode register for GPIO29. | `GPIO29TriggerMode`<br/>0 = negative_pulse <br/>1 = positive_pulse <br/>2 = negative_level <br/>3 = positive_level <br/>       |
| 0x1d   | 1    | reg_gpio_29_interrupt_control_mode | Read & Write | Interrupt control mode register for GPIO29. | `GPIO29ControlMode`<br/>0 = sync <br/>1 = async <br/>       |


