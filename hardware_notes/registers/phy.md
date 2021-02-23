# Peripheral: PHY

- It looks like there are multiple peripherals related to this, not just one.
  * [mdm_stats](phy/mdm.md)(at 0x44c00000) - looks like modem status registers, read only [5]
  * [mdm_cfg](phy/mdm.md)(at 0x44c00800) - looks like modem config registers, read/write [4]
  * [mac_core](phy/mac.md)(at 0x44b00000) - some sort of a hardware mac core, not exactly sure what [3]
  * [mac_pl](phy/mac.md)(at 0x44b08040) - similar to above, no idea what [2]
  * [macbyp](phy/mac.md)(at 0x44c600000) - addressed by functions names macbypass
  * [riu](phy/agc.md)(at 0x44c0b000) - could be multiple peripherals. Related to agc peripheral [in alios repo][1] (https://gist.github.com/Yangff/9abf8da778930c21d440c313c54d3661)

- To download the alios repo ` git clone https://code.aliyun.com/alios_bull/alios.git`, you don't have to be registered.


[1]: https://code.aliyun.com/alios_bull/alios/blob/cd8a215d9572f3b07d0f30fc96f43392b27cb2e4/platform/mcu/bk7231s/beken/driver/common/reg/reg_agc.h
[2]: https://code.aliyun.com/alios_bull/alios/blob/cd8a215d9572f3b07d0f30fc96f43392b27cb2e4/platform/mcu/bk7231s/beken/driver/common/reg/reg_mac_pl.h
[3]: https://code.aliyun.com/alios_bull/alios/blob/cd8a215d9572f3b07d0f30fc96f43392b27cb2e4/platform/mcu/bk7231s/beken/driver/common/reg/reg_mac_core.h
[4]: https://code.aliyun.com/alios_bull/alios/blob/cd8a215d9572f3b07d0f30fc96f43392b27cb2e4/platform/mcu/bk7231s/beken/driver/common/reg/reg_mdm_cfg.h
[5]: https://code.aliyun.com/alios_bull/alios/blob/cd8a215d9572f3b07d0f30fc96f43392b27cb2e4/platform/mcu/bk7231s/beken/driver/common/reg/reg_mdm_stat.h
