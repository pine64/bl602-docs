# Global control registers

- Peripheral name: glb
- Base address: 0x40000000

Notes:
- All registers are 32 bits wide
- Field offsets and sizes are in bits

| Offset | Register           | Relates to                            |
| ------ | ------------------ | ------------------------------------- |
| 0x0000 | clk_cfg0           | [Clock configuration](clock.md)       |
| 0x0004 | clk_cfg1           | [Clock configuration](clock.md)       |
| 0x0008 | clk_cfg2           | [Clock configuration](clock.md)       | 
| 0x000C | clk_cfg3           | [Clock configuration](clock.md)       |
| 0x0010 | swrst_cfg0         | [Reset](reset.md)                     |
| 0x0014 | swrst_cfg1         | [Reset](reset.md)                     |
| 0x0018 | swrst_cfg2         | [Reset](reset.md)                     |
| 0x001C | swrst_cfg3         | [Reset](reset.md)                     |
| 0x0020 | cgen_cfg0          | [Clock configuration](clock.md)       |
| 0x0024 | cgen_cfg1          | [Clock configuration](clock.md)       |
| 0x0028 | cgen_cfg2          | [Clock configuration](clock.md)       |
| 0x002C | cgen_cfg3          | [Clock configuration](clock.md)       |
| 0x0030 | MBIST_CTL          | [Memory Built-In Self Test](mbist.md) |
| 0x0034 | MBIST_STAT         | [Memory Built-In Self Test](mbist.md) |
| 0x0050 | bmx_cfg1           |
| 0x0054 | bmx_cfg2           |
| 0x0058 | bmx_err_addr       |
| 0x005C | bmx_dbg_out        |
| 0x0060 | rsv0               | *Reserved*                            |
| 0x0064 | rsv1               | *Reserved*                            |
| 0x0068 | rsv2               | *Reserved*                            |
| 0x006C | rsv3               | *Reserved*                            |
| 0x0070 | sram_ret           |
| 0x0074 | sram_slp           |
| 0x0078 | sram_parm          |
| 0x007C | seam_misc          |
| 0x0080 | glb_parm           |
| 0x0090 | CPU_CLK_CFG        |
| 0x00A4 | GPADC_32M_SRC_CTRL |
| 0x00A8 | DIG32K_WAKEUP_CTRL |
| 0x00AC | WIFI_BT_COEX_CTRL  |
| 0x00C0 | UART_SIG_SEL_0     |
| 0x00D0 | DBG_SEL_LL         |
| 0x00D4 | DBG_SEL_LH         |
| 0x00D8 | DBG_SEL_HL         |
| 0x00DC | DBG_SEL_HH         |
| 0x00E0 | debug              |
| 0x0100 | GPIO_CFGCTL0       |
| 0x0104 | GPIO_CFGCTL1       |
| 0x0108 | GPIO_CFGCTL2       |
| 0x010C | GPIO_CFGCTL3       |
| 0x0110 | GPIO_CFGCTL4       |
| 0x0114 | GPIO_CFGCTL5       |
| 0x0118 | GPIO_CFGCTL6       |
| 0x011C | GPIO_CFGCTL7       |
| 0x0120 | GPIO_CFGCTL8       |
| 0x0124 | GPIO_CFGCTL9       |
| 0x0128 | GPIO_CFGCTL10      |
| 0x012C | GPIO_CFGCTL11      |
| 0x0130 | GPIO_CFGCTL12      |
| 0x0134 | GPIO_CFGCTL13      |
| 0x0138 | GPIO_CFGCTL14      |
| 0x0180 | GPIO_CFGCTL30      |
| 0x0184 | GPIO_CFGCTL31      |
| 0x0188 | GPIO_CFGCTL32      |
| 0x018C | GPIO_CFGCTL33      |
| 0x0190 | GPIO_CFGCTL34      |
| 0x0194 | GPIO_CFGCTL35      |
| 0x01A0 | GPIO_INT_MASK1     |
| 0x01A8 | GPIO_INT_STAT1     |
| 0x01B0 | GPIO_INT_CLR1      |
| 0x01C0 | GPIO_INT_MODE_SET1 |
| 0x01C4 | GPIO_INT_MODE_SET2 |
| 0x01C8 | GPIO_INT_MODE_SET3 |
| 0x0224 | led_driver         |
| 0x0308 | gpdac_ctrl         |
| 0x030C | gpdac_actrl        |
| 0x0310 | gpdac_bctrl        |
| 0x0314 | gpdac_data         |
| 0x0F00 | tzc_glb_ctrl_0     |
| 0x0F04 | tzc_glb_ctrl_1     |
| 0x0F08 | tzc_glb_ctrl_2     |
| 0x0F0C | tzc_glb_ctrl_3     |
