## Research notes
  
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
