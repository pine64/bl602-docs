# Memory Built-In Self Test

*The base address for the registers described in this file is 0x40000000*

## Register: Memory Built-In Self Test control

- Register name: MBIST_CTL
- Register offset: 0x0030

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 1    | irom_mbist_mode   | R/W        |                               |                                                           |                                           |
| 0x01   | 1    | hsram_mbist_mode  | R/W        |                               |                                                           |                                           |
| 0x02   | 1    | tag_mbist_mode    | R/W        |                               |                                                           |                                           |
| 0x03   | 1    | ocram_mbist_mode  | R/W        |                               |                                                           |                                           |
| 0x04   | 1    | wifi_mbist_mode   | R/W        |                               |                                                           |                                           |
| 0x1F   | 1    | reg_mbist_rst_n   | R/W        |                               |                                                           |                                           |

*Note: bits 5-30 are reserved and should always be set to 0*

## Register: Memory Built-In Self Test status

- Register name: MBIST_STAT
- Register offset: 0x0034

| Offset | Size | Name              | Direction  | Description                   | Values                                                    | Notes                                     |
| ------ | ---- | ----------------- | ---------- | ----------------------------- | --------------------------------------------------------- | ----------------------------------------- |
| 0x00   | 1    | irom_mbist_done   | R          |                               |                                                           |                                           |
| 0x01   | 1    | hsram_mbist_done  | R          |                               |                                                           |                                           |
| 0x02   | 1    | tag_mbist_done    | R          |                               |                                                           |                                           |
| 0x03   | 1    | ocram_mbist_done  | R          |                               |                                                           |                                           |
| 0x04   | 1    | wifi_mbist_done   | R          |                               |                                                           |                                           |
| 0x10   | 1    | irom_mbist_fail   | R          |                               |                                                           |                                           |
| 0x11   | 1    | hsram_mbist_fail  | R          |                               |                                                           |                                           |
| 0x12   | 1    | tag_mbist_fail    | R          |                               |                                                           |                                           |
| 0x13   | 1    | ocram_mbist_fail  | R          |                               |                                                           |                                           |
| 0x14   | 1    | wifi_mbist_fail   | R          |                               |                                                           |                                           |

*Note: bits 5-15 and 21-31 are reserved and should always be set to 0*