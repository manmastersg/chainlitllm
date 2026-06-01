# Hardware and Setup

**Summary**: Comprehensive guide to the physical installation, connectivity, and power procedures for the Telestream PRISM series.

**Sources**: raw/PRISM-MPS-MPD-MPP-User-Manual-D00013488R-cc.md

**Last updated**: 2026-05-31

---

This page covers the physical aspects of setting up and maintaining your PRISM instrument, including mounting, cabling, SFP installation, power procedures, and physical specifications.

## Physical Specifications

### MPS Series Dimensions

| Model       | Height              | Width               | Depth (inc. Connectors) | Weight             |
| ----------- | ------------------- | ------------------- | ----------------------- | ------------------ |
| MPS-100     | 13.30 cm (5.24 in.) | 22.00 cm (8.66 in.) | 13.07 cm (5.15 in.)     | 2.77 Kg (6.1 lbs.) |
| MPS-200/300 | 13.30 cm (5.24 in.) | 22.00 cm (8.66 in.) | 12.46 cm (4.91 in.)     | 2.77 Kg (6.1 lbs.) |

### MPD Series Dimensions

| Model       | Height              | Width                | Depth (inc. Connectors) | Weight             |
| ----------- | ------------------- | -------------------- | ----------------------- | ------------------ |
| MPD-100     | 13.30 cm (5.24 in.) | 44.50 cm (17.52 in.) | 13.07 cm (5.15 in.)     | 3.95 Kg (8.7 lbs.) |
| MPD-200/300 | 13.30 cm (5.24 in.) | 44.50 cm (17.52 in.) | 12.46 cm (4.91 in.)     | 3.95 Kg (8.7 lbs.) |

### MPP Series Dimensions

| Model       | Height            | Width               | Depth (inc. Connectors) | Weight             |
| ----------- | ----------------- | ------------------- | ----------------------- | ------------------ |
| MPP-100     | 4.4 cm (1.73 in.) | 48.3 cm (19.01 in.) | 31.3 cm (12.32 in.)     | 3.5 Kg (7.72 lbs.) |
| MPP-200/300 | 4.4 cm (1.73 in.) | 48.3 cm (19.01 in.) | 31.3 cm (12.32 in.)     | 3.6 Kg (7.94 lbs.) |

### Packaging Dimensions

| Series          | Height             | Width               | Depth               | Weight             |
| --------------- | ------------------ | ------------------- | ------------------- | ------------------ |
| MPS-100/200/300 | 30.5 cm (12.0 in.) | 38.1 cm (15.0 in.)  | 27.9 cm (11.0 in.)  | 4.2 Kg (9.2 lbs)   |
| MPD-100/200/300 | 30.5 cm (12.0 in.) | 61.0 cm (24.0 in.)  | 27.9 cm (11.0 in.)  | 6.0 Kg (13.2 lbs)  |
| MPP-100/200/300 | 20 cm (11.81 in.)  | 63.8 cm (25.12 in.) | 47.2 cm (18.58 in.) | 8.0 Kg (17.64 lbs) |

### AUX SDI Output Characteristics

| Parameter    | Value                         |
| ------------ | ----------------------------- |
| Output Level | 800 mV +/- 10% into 75 Ω Load |

The AUX SDI output can be used for SDI Loop Through and ST 2110-20/22/30/31 IP gateway.

## Getting Started

### Product Description Overview

The PRISM series provides flexible options to monitor SDI and IP statistics. It is available in three form factors:

- **MPS**: 3RU half-rack with an integrated 9-inch HD display and touch panel.
- **MPD**: 3RU full-rack with two integrated 9-inch HD displays and touch panels.
- **MPP**: 1RU full-rack. Requires an external display or remote access for operation.

### Installation and Mounting

- **MPS Rack**: Uses the MPS Rack Accessory Kit (MPS-RACK) to install one or two units in a rack.
- **MPD/MPP Rack**: Mounting hardware is included with the instrument for standard rack installation.
- **Portability (MPS only)**: The MPS Portable Accessory Kit (MPS-PTBL) provides a handle, protective cover, tripod mount, and battery mount plate.

## Connectivity and Cabling

### SFP Module Installation

The following optional SFP modules are available for MPS-200/300, MPD-200/300, and MPP-200/300 models:

- **MP-SFP 10GESR**: 10G Ethernet short-range SFP+ transceiver (850 nm).
- **MP-SFP 10GELR**: 10G Ethernet long-range SFP+ transceiver (1310 nm).
- **MP-SFP 25GESR**: 25G Ethernet short-range SFP28 transceiver (850 nm).
- **MP-SFP 25GELR**: 25G Ethernet long-range SFP28 transceiver (1310 nm).

**Installation Tip**: Insert the module into the SFP connector until it latches. To remove, pull down on the latch and pull the module out.

### Network Installation

- **Direct Connection**: Connect the instrument directly to a PC via an Ethernet cable or switch. Set the instrument to **Manual IP mode** to ensure compatibility with the PC's subnet.
- **Network Connection**: Connect via an Ethernet switch/network. The instrument can use DHCP or Manual IP assignment.
- **Remote Access**: When using manual settings, ensure the IP address and subnet are correctly configured to prevent loss of connectivity.

## Power Procedures

### Power Cord Installation

Connect the provided power cord to the rear panel of the instrument. The connector is keyed; ensure the flat portion of the housing faces the left (as viewed from the rear).

### Power-on and Power-off

#### Power-on Procedure

1. Connect power to the instrument. (Note: For MPP, connect a monitor/keyboard/mouse first for initial setup).
2. Press the power button on the front panel.
   - **MPS/MPD**: The light turns on during the sequence, then turns off.
   - **MPP**: The power button blinks during startup, then remains on.

#### Power-off Procedure

1. Press the power button on the front panel to turn the instrument off.
2. Alternatively, via the UI: Select **Settings icon ( )** $\rightarrow$ **Utilities** $\rightarrow$ **Power** $\rightarrow$ **Power Down Now**.

**CAUTION**: Always shut down the instrument via the software/button before disconnecting the power cord to prevent data loss.

## Related pages

- [[prism-family]]
- [[mps-series]]
- [[mpd-series]]
- [[mpp-series]]
