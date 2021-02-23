## Research notes

- 0x44c00000: Version/Flags (RO)
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
