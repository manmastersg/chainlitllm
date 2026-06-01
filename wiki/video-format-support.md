# Video Format Support

**Summary**: A comprehensive guide to the supported video and audio formats for the Telestream PRISM series, covering SDI and IP-based standards.

**Sources**: raw/Video Test and Monitoring Equipment.md

**Last updated**: 2026-05-31

---

The Telestream PRISM series supports a wide range of video formats across various transport standards. Support depends on the model and optional licenses. MPS-100, MPD-100, and MPP-100 are SDI-only models and do not support IP formats.

## Supported SDI Video Formats

The following SDI formats are supported as Standard on all models (SDI and IP capable units alike):

### SD-SDI

| Format | Sample Structure | Bits | Frame/Field Rate | Audio | Option   |
| ------ | ---------------- | ---- | ---------------- | ----- | -------- |
| 525i   | 4:2:2 YCbCr      | 10b  | 59.94i           | 16ch  | Standard |
| 625i   | 4:2:2 YCbCr      | 10b  | 50i              | 16ch  | Standard |

### HD-SDI

| Format    | Sample Structure | Bits | Frame/Field Rate                             | Audio | Option   |
| --------- | ---------------- | ---- | -------------------------------------------- | ----- | -------- |
| 1280x720  | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50/59.94/60p            | 16ch  | Standard |
| 1920x1080 | 4:2:2 YCbCr      | 10b  | 50/59.94/60i, 23.98/24/25/29.97/30p, and psF | 16ch  | Standard |
| 2048x1080 | 4:2:2 YCbCr      | 10b  | 29.97/30p, and psF                           | 8ch   | Standard |
| 2048x1080 | 4:2:2 YCbCr      | 10b  | 23.98/24/25p, and psF                        | 16ch  | Standard |

### 3G SDI Level A

| Format    | Sample Structure | Bits   | Frame/Field Rate      | Audio | Option   |
| --------- | ---------------- | ------ | --------------------- | ----- | -------- |
| 1920x1080 | 4:2:2 YCbCr      | 10b    | 50/59.94/60p          | 16ch  | Standard |
| 2048x1080 | 4:2:2 YCbCr      | 10b    | 47.95/48/50/59.94/60p | 16ch  | Standard |
| 1920x1080 | 4:4:4 RGB        | 10/12b | 23.98/24/25/29.97/30p | 16ch  | PROD\*   |
| 2048x1080 | 4:4:4 RGB        | 10/12b | 23.98/24/25/29.97/30p | 16ch  | PROD\*   |

### 3G SDI Level B

| Format    | Sample Structure | Bits   | Frame/Field Rate      | Audio | Option   |
| --------- | ---------------- | ------ | --------------------- | ----- | -------- |
| 1920x1080 | 4:2:2 YCbCr      | 10b    | 50/59.94/60p          | 16ch  | Standard |
| 2048x1080 | 4:2:2 YCbCr      | 10b    | 59.94/60p             | 8ch   | Standard |
| 2048x1080 | 4:2:2 YCbCr      | 10b    | 47.95/48/50p          | 16ch  | Standard |
| 1920x1080 | 4:4:4 RGB        | 10/12b | 23.98/24/25/29.97/30p | 16ch  | PROD\*   |
| 2048x1080 | 4:4:4 RGB        | 10/12b | 29.97/30p             | 8ch   | PROD\*   |
| 2048x1080 | 4:4:4 RGB        | 10/12b | 23.98/24/25p          | 16ch  | PROD\*   |

**Note**: 6G/12G SDI formats (4K, 8K) require the [[prism-options|FMT-4K license]]. FMT-4K enables 6G/12G SDI support.

*When ordering options for MPS, MPD or MPP series, add prefix MPSDP- (e.g., FMT-4K becomes MPSDP-FMT-4K).
*MPSDP-FMT-8K license includes the formats supported by MPSDP-FMT-4K license.

## Supported Video Formats in SMPTE 2022-6 Streams

SMPTE 2022-6 carries SDI video over IP networks. Available on MPS-200/300, MPD-200/300, and MPP-200/300 models (not available on SDI-only models).

| Link           | Format    | Sample Structure | Bits | Frame/Field Rate                             | Option   |
| -------------- | --------- | ---------------- | ---- | -------------------------------------------- | -------- |
| SD-SDI         | 525i      | 4:2:2 YCbCr      | 10b  | 59.94i                                       | Standard |
| SD-SDI         | 625i      | 4:2:2 YCbCr      | 10b  | 50i                                          | Standard |
| HD-SDI         | 1920x1080 | 4:2:2 YCbCr      | 10b  | 50/59.94/60i, 23.98/24/25/29.97/30p, and psF | Standard |
| HD-SDI         | 1280x720  | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50/59.94/60p            | Standard |
| 3G SDI Level A | 1920x1080 | 4:2:2 YCbCr      | 10b  | 50/59.94/60p                                 | Standard |
| 3G SDI Level B | 1920x1080 | 4:2:2 YCbCr      | 10b  | 50/59.94/60p                                 | Standard |

Not available for MPS-100, MPD-100, and MPP-100 (SDI only).

## Supported ST 2110-20 Video Formats

ST 2110-20 defines uncompressed video over IP. Available on MPS-200/300, MPD-200/300, and MPP-200/300.

| Format    | Sample Structure | Bits | Frame/Field Rate                                  | Option\*              |
| --------- | ---------------- | ---- | ------------------------------------------------- | --------------------- |
| 525i      | 4:2:2 YCbCr      | 10b  | 59.94i                                            | Standard              |
| 625i      | 4:2:2 YCbCr      | 10b  | 50i                                               | Standard              |
| 1280x720  | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30p                             | Standard              |
| 1280x720  | 4:2:2 YCbCr      | 10b  | 50/59.94/60p                                      | Standard              |
| 1920x1080 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30p, 50/59.94/60i, 50/59.94/60p | Standard              |
| 1920x1080 | 4:4:4 RGB        | 12b  | 23.98/24/25/29.97/30/50/59.94/60p                 | PROD                  |
| 2048x1080 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50/59.94/60p                 | Standard              |
| 2048x1080 | 4:4:4 RGB        | 12b  | 23.98/24/25/29.97/30/50/59.94/60p                 | PROD                  |
| 3840x2160 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50p                          | FMT-4K                |
| 3840x2160 | 4:2:2 YCbCr      | 10b  | 59.94/60p                                         | FMT-4K and 25GE       |
| 3840x2160 | 4:4:4 RGB        | 12b  | 23.98/24/25/29.97/30                              | FMT-4K and PROD       |
| 4096x2160 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50p                          | FMT-4K                |
| 4096x2160 | 4:2:2 YCbCr      | 10b  | 59.94/60p                                         | FMT-4K and 25GE       |
| 4096x2160 | 4:4:4 RGB        | 12b  | 23.98/24/25                                       | FMT-4K and PROD       |
| 4096x2160 | 4:4:4 RGB        | 12b  | 29.97/30                                          | FMT-4K, PROD and 25GE |

Not available for MPS-100, MPD-100, and MPP-100 (SDI only).

\*When ordering, use prefix MPSDP- (e.g., MPSDP-FMT-4K). MPSDP-FMT-8K license includes FMT-4K.

## Supported ST 2110-22 (JPEG XS) Video Formats

ST 2110-22 defines JPEG XS compressed video over IP. Requires [[prism-options|JPXS license]] and, for 4K formats, FMT-4K license.

| Format    | Sample Structure | Bits | Frame/Field Rate                                  | Option\*        |
| --------- | ---------------- | ---- | ------------------------------------------------- | --------------- |
| 1280x720  | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30p/50/59.94/60p                | JPXS            |
| 1920x1080 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30p, 50/59.94/60i, 50/59.94/60p | JPXS            |
| 2048x1080 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50/59.94/60p                 | JPXS            |
| 3840x2160 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50p/59.94/60p                | JPXS and FMT-4K |
| 4096x2160 | 4:2:2 YCbCr      | 10b  | 23.98/24/25/29.97/30/50p/59.94/60p                | JPXS and FMT-4K |

## SMPTE 2110-30/31 Audio Streams

ST 2110-30/31 carry uncompressed audio over IP. Available on MPS-200/300, MPD-200/300, and MPP-200/300.

| Conformance Level   | Description                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Conformance Level A | Reception of 48 kHz streams with 1 to 8 channels at packet times of 1 ms                                              |
| Conformance Level B | Reception of 48 kHz streams with 1 to 8 channels at packet times of 1 ms or 1 to 8 channels at packet times of 125 µs |

- Reception of 48 kHz streams with 16 channels at packet times of 125 µs is also supported.
- PRISM instruments with 25GE module support up to eight ST 2110-30 streams of reception with up to 16 audio channels total. One of the streams can be replaced with ST 2110-31.
- Not available for MPS-100, MPD-100, and MPP-100 (SDI only).

## SMPTE 2110-40 ANC Data Stream

ST 2110-40 carries ancillary (ANC) data over IP. Available on MPS-200/300, MPD-200/300, and MPP-200/300.

- PRISM supports four ST 2110-40 streams with multiple ANC packets.
- One of four streams can be an ST 2110-43 stream with TTML (Timed Text Markup Language).
- Not available for MPS-100, MPD-100, and MPP-100 (SDI only).

## Related pages

- [[video-test-and-monitoring-equipment]]
- [[prism-options]]
- [[applications-catalog]]
