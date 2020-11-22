# Peripheral: PHY

- It looks like there are multiple peripherals related to this, not just one.
  * mdm_stats(at 0x44c00000) - looks like modem status registers, read only
  * mdm_cfg(at 0x44c00800) - looks like modem config registers, read/write
  * mac_core(at 0x44b00000) - some sort of a hardware mac core, not exactly sure what
  * mac_pl(at 0x44b08040) - similar to above, no idea what
  * macbyp(at 0x44c600000) - addressed by functions names macbypass
  * riu(at 0x44c0b000) - could be multiple peripherals. Related to agc peripheral in alios repo (https://code.aliyun.com/alios_bull/alios/blob/cd8a215d9572f3b07d0f30fc96f43392b27cb2e4/platform/mcu/bk7231s/beken/driver/common/reg/reg_agc.h) (https://gist.github.com/Yangff/9abf8da778930c21d440c313c54d3661)

- To download the alios repo ` git clone https://code.aliyun.com/alios_bull/alios.git`, you don't have to be registered.

## Research notes

- 44c00000: Version/Flags (RO)
  phy_get_version
  phy_vht_supported
  phy_get_ntx
  phy_ldpc_tx_supported
  rxnssmax
  rxndpnstsmax
  txnssmax
  ntxmax/ntx
  txcbwmax

- 0x44c00800: mdm_mdmconf (WO)
  Set to 0 before mdm_reset (phy_init, phy_hw_set_channel)
  mdm_mdmconf_set(0)
  
- 0x44c00818: SMOOTHCTRL (R/W)
  phy_hw_set_channel
    mdm_smoothctrl_set(0x1880c06)
  phy_init
    mdm_cfgsmoothforce_setf(0)
  
- 0x44c0081c: DCESTIMCTRL (R/W)
  Set to 0xf07 in phy_hw_set_channel
    mdm_dcestimctrl_pack(starthtdc = 0, startdc = 0, delaysynctd20 = 0, delaysync = 0xf, waithtstf = 0xf)
    mdm_waithtstf_setf(7)
  
- 0x44c00820: ? (R/W)
  mdm_rxmode_set
  mdm_rxnssmax_setf
  mdm_rxndpnstsmax_setf
  phy_hw_set_channel sets 1st bit
  Lots of writes in phy_init with stuff from phy_version
  
- 0x44c00824: ? (R/W)
  txcbwmax (mdm_txcbwmax_setf, called from phy_hw_set_channel/phy_init)
  Lots of writes in phy_init with stuff from phy_version
  
- 0x44c00830: SMOOTHSNRTHR (R/W)
  only in phy_init
    mdm_smoothsnrthrhigh_setf(0x1b)
    mdm_smoothsnrthrmid_setf(0xf)
  
- 0x44c00834: ? (R/W)
  mdm_rxtdctrl1_set/mdm_rxtdctrl1_get
  mdm_tddchtstfmargin_setf
  phy_init sets 1st bit
  
- 0x44c00838: TXCTRL0 (WO)
  phy_hw_set_channel sets to 0xb4
  mdm_txstartdelay_setf(0xb4)
  
- 0x44c0083c: mdm_rxctrl1 (WO)
  phy_init sets to 0x4920492
  mdm_rxctrl1_set(0x4920492)
  
- 0x44c00858: TBECTRL0 (R/W)
  phy_hw_set_channel clears low byte
  mdm_tbe_count_adjust_20_setf(0x00)
  
- 0x44c00860: mdm_tbectrl2 (WO)
  phy_hw_set_channel sets to 0x7f03
  mdm_tbectrl2_set(0x7f03)
  
- 0x44c00874: ? (R/W)
  phy_init sets bits here
  mdm_rcclkforce_setf(1)
  mdm_agcmemclkforce_setf(1)
  mdm_agcmemclkforce_setf(0)

- 0x44c00888: mdm_reset (WO)
  mdm_reset causes a reset by writing 1, then 0; no delay
  
- 0x44c0088c: mdm_txctrl1 (WO)
  phy_hw_set_channel sets to 0x1c13
  mdm_txctrl1_pack(txfeofdm80delay = 0x13, txfeofdm40delay = 0x1c, txfeofdm20delay = 0, txfedsssdelay = 0)
 
- 0x44c00898: mdm_txctrl3 (WO)
  phy_hw_set_channel sets to 0x2d00438
  mdm_txctrl3_pack(txphyrdyhtdelay = 0x2d0, txphyrdynonhtdelay = 0x438)
  
- 0x44c0089c: mdm_rxframeviolationmask (WO)
  phy_init sets to 0xffffffff
  mdm_rxframeviolationmask_setf(0xffffffff)
  
- 0x44c03024: ? (R/W)
  phy_init sets _DAT_44c03024 & 0xffc0ffff | 0x2d0000
  mdm_precomp_setf(0x2d)
  
- 0x44c0b000: ? (RO)
  riu_iqcomp_getf
  
- 0x44c0b004: riu_activeant (WO)
  phy_init sets to 1
  riu_activeant_setf(1)

- 0x44c0b110: ? (R/W)
  only changed in phy_init
  riu_rxiqphaseesten_setf(0)
  riu_rxiqgainesten_setf(0)
  riu_rxiqphasecompen_setf(0)
  riu_rxiqgaincompen_setf(0)

- 0x44c0b118: riu_iqestiterclr (WO)
  phy_hw_set_channel: riu_iqestiterclr_setf(1)
  phy_init: riu_iqestiterclr_setf(0)

- 0x44c0b340: riu_rwnxagcaci20marg0 (WO)
  phy_hw_set_channel: riu_rwnxagcaci20marg0_set(0)

- 0x44c0b344: riu_rwnxagcaci20marg1 (WO)
  phy_hw_set_channel: riu_rwnxagcaci20marg1_set(0)

- 0x44c0b348: riu_rwnxagcaci20marg2 (WO)
  phy_hw_set_channel: riu_rwnxagcaci20marg2_set(0)

- 0x44c0b364: ? (R/W)
  only in agc_config
    riu_satdelay50ns_setf(8)
    riu_sathighthrdbv_setf(0x3c)
    riu_satlowthrdbv_setf(0x38)
    riu_satthrdbv_setf(0x39)

- 0x44c0b368: ? (R/W)
  only in agc_config
    riu_crossdnthrqdbm_setf(0x70)
    riu_crossupthrqdbm_setf(0x70)

- 0x44c0b36c: ? (R/W)
  only in agc_config
    riu_rampupgapqdb_setf(0x12)
    riu_rampupndlindex_setf(5)
    riu_rampdngapqdb_setf(0x28)
    riu_rampdnndlindex_setf(7)

- 0x44c0b370: ? (R/W)
  only in agc_config
    riu_adcpowdisthrdbv_setf(0x58)

- 0x44c0b380: riu_evt0 (R/W)
  only in agc_config
    riu_evt0op3_setf(0x3e)
    riu_evt0pathcomb_setf(0)
    riu_evt0opcomb_setf(1)
    incomplete!

- 0x44c0b384: riu_evt1 (R/W)
  only in agc_config
    riu_evt1op1_setf(0x39)
    riu_evt1op2_setf(0x37)
    riu_evt1op3_setf(0x14)
    riu_evt1pathcomb_setf(0)
    riu_evt1opcomb_setf(2)

- 0x44c0b388: riu_evt2 (R/W)
  only in agc_config
    riu_evt2op1_setf(0xf)
    riu_evt2op2_setf(0x17)
    riu_evt2op3_setf(0x2a)
    riu_evt2pathcomb_setf(0)
    riu_evt2opcomb_setf(5)

- 0x44c0b38c: riu_evt3 (R/W)
  only in agc_config
    riu_evt3op1_setf(0x19)
    riu_evt3op2_setf(0)
    riu_evt3op3_setf(0xe)
    riu_evt3opcomb_setf(2)

- 0x44c0b390: RWNXAGCCNTL (R/W)
  agc_config
    riu_htstfgainen_setf(0)
    riu_rifsdeten_setf(0)
  phy_hw_set_channel
    riu_ofdmonly_setf(0)
  phy_init
    riu_combpathsel_setf(1)
    riu_agcfsmreset_setf(1)
    riu_agcfsmreset_setf(0)

- 0x44c0b394: ? (R/W)
  only in agc_config
    riu_vpeakadcqdbv_setf(const1s -8)

- 0x44c0b398: ? (R/W)
  only in agc_config
    riu_adcpowmindbm_setf(const1s -98)

- 0x44c0b3a0: ? (R/W)
  only in agc_config
    riu_inbdpowmindbm_setf(const1s -98)

- 0x44c0b3a4: ? (R/W)
  only in agc_config
    riu_fe20gain_setf(0)
    riu_fe40gain_setf(0)

- 0x44c0b3bc: RWNXAGCCCATIMEOUT (WO)
  only in phy_init
    riu_rwnxagcccatimeout_set(4000000)

- 0x44c0b3c0: ? (R/W)
  only in agc_config
    riu_idinbdpowgapdnqdbm_setf(0x18)
    riu_inbdpowsupthrdbm_setf(const1s -92)
    riu_inbdpowinfthrdbm_setf(const1s -93)

- 0x44c0b3c4: ? (R/W)
  only in agc_config
    riu_adcpowsupthrdbm_setf(const1s -50)

- 0x44c0b414: ? (R/W)
  only in phy_init
    riu_irqmacccatimeouten_setf(1)

- 0x44c0b41c: riu_rwnxmacintstatmasked (RO)
  only in phy_rc_isr
    riu_rwnxmacintstatmasked_get()

- 0x44c0b420: riu_rwnxmacintack (WO)
  only in phy_rc_isr
    riu_rwnxmacintack_clear(<value from riu_rwnxmacintstatmasked>)

- 0x44c0b500: ? (R/W)
  only in phy_init
    riu_txshift4044_setf(2)

- 0x44c0c020: ? (R/W)
  only in phy_init
    rc_paoff_delay_setf(20)

- 0x44c0c040: ? (R/W)
  only in agc_config
    rc2_rx0_vga_idx_max_setf(0xc)
    rc2_rx0_vga_idx_min_setf(3)

- 0x44c0c044: ? (R/W)
  only in agc_config
    rc2_rx0_lna_idx_max_setf(8)
    rc2_rx0_lna_idx_min_setf(0)

- 0x44c0c080: ? (R/W)
  only in phy_config_rxgain

- 0x44c0c084: ? (R/W)
  only in phy_config_rxgain

- 0x44c0c088: ? (R/W)
  only in phy_config_rxgain

- 0x44c0c814: rc2_pkdet (R/W)
  only in agc_config
    rc2_pkdet_mode_setf(0)
    rc2_pkdet_cnt_thr_setf(2)
    rc2_pkdet_cnt_thr_setf(2) (yes, twice!)

- 0x44c0c82c: rc2_inbdpow (R/W)
  only in agc_config
    rc2_inbdpow_adj_thr_dbm_setf(const1u 181)
    rc2_inbdpowsupthr_adj_en_setf(1)
    rc2_inbdpowinfthr_adj_en_setf(1)
    rc2_inbdpowfastvalid_cnt_setf(0x40)

- 0x44c0c830: rc2_evt4 (R/W)
  only in agc_config
    rc2_evt4op1_setf(0x3f)
    rc2_evt4op2_setf(1)
    rc2_evt4op3_setf(0x36)
    rc2_evt4opcomb_setf(5)

- 0x44c0c838: ? (R/W)
  only in agc_config
    rc2_reflevofdmthd_en_setf(1)
    rc2_reflevofdmthd_setf(0x100)

- 0x44c0c83c: ? (R/W)
  only in agc_config
    rc2_reflevdsssthd_en_setf(1)
    rc2_reflevdsssthd_setf(0x17c)

- 0x44c0c840: ? (R/W)
  only in agc_config
    rc2_reflevdssscontthd_en_setf(1)
    rc2_reflevdssscontthd_setf(0x100)
