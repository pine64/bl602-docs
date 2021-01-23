# Peripheral: CKS

- Register base address: 0x4000A700

## Registers

| Register offset | Register size | Field offset | Field size | Name             | Direction  | Description                                      |
| --------------- | ------------- | ------------ | ---------- | ---------------- | ---------- | -----------                                      |
| 0x0000          | 32            |              |            | cks_config       | read-write | CKS control                                      |
|                 |               | 0x0000       | 1          | cr_cks_clr       |            | Write `1` to clear state                         |
|                 |               | 0x0001       | 1          | cr_cks_byte_swap |            | Endianness (`0`: little endian, `1`: big endian) |
| 0x0004          | 32            |              |            | data_in          | read-write |                                                  |
|                 |               | 0x0000       | 8          | data_in          |            | Single byte input                                |
| 0x0008          | 32            |              |            | cks_out          | read-write |                                                  |
|                 |               | 0x0000       | 16         | cks_out          |            | 16-bit output checksum                           |

## Sources

* [bl_cks.c](https://github.com/bouffalolab/bl_iot_sdk/blob/3bc544d9f3243d411cad249a49769980b9ac6b76/components/hal_drv/bl602_hal/bl_cks.c)
