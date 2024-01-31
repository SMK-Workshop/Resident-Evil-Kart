















macro CAMERA(xpos,ypos,angle)
		; Specify position and angle of camera
		dw	<xpos>*4,<ypos>*4,<angle>
endmacro

; Specify which camera to use for this zone
function cam(camera_idx) = camera_idx*6



; track order
;
; 00-04 | MC3 GV2 DP2 BC2 VL2
; 05-09 | RR  KB2 MC1 GV3 BC3
; 0A-0E | CI2 DP3 VL1 KB1 MC4
; 0F-13 | MC2 GV1 BC1 CI1 DP1
;
; 14-17 | BT3 BT4 BT1 BT2






TRACK_ZONES:
		; race tracks
		dw	zone_00,zone_01,zone_02,zone_03,zone_04
		dw	zone_05,zone_06,zone_07,zone_08,zone_09
		dw	zone_0A,zone_0B,zone_0C,zone_0D,zone_0E
		dw	zone_0F,zone_10,zone_11,zone_12,zone_13
		; battle tracks
		dw	zone_15,zone_15,zone_16,zone_15

TRACK_CAMERAS:
		; race tracks
		dw	camera_00,camera_01,camera_02,camera_03,camera_04
		dw	camera_05,camera_06,camera_07,camera_08,camera_09
		dw	camera_0A,camera_0B,camera_0C,camera_0D,camera_0E
		dw	camera_0F,camera_10,camera_11,camera_12,camera_13
		; battle tracks
		dw	camera_15,camera_15,camera_16,camera_15



; =============================================================================
;		RACE TRACKS
; =============================================================================

; ==============================================
; Track 00: Mario Circuit 3
; ==============================================
zone_00:		; (40 zones)
		db	cam($00),cam($00),cam($01),cam($01)
		db	cam($01),cam($01),cam($02),cam($02)
		db	cam($02),cam($03),cam($03),cam($03)
		db	cam($04),cam($04),cam($05),cam($05)
		db	cam($06),cam($06),cam($06),cam($06)
		db	cam($06),cam($06),cam($06),cam($06)
		db	cam($07),cam($07),cam($07),cam($08)
		db	cam($08),cam($08),cam($08),cam($09)
		db	cam($09),cam($0A),cam($0A),cam($0A)
		db	cam($0B),cam($0B),cam($00),cam($00)

camera_00:
		;       xpos  ypos  angle
		%CAMERA($0054,$0284,$0000)
		%CAMERA($FFF8,$0014,$5800)
		%CAMERA($0238,$01C4,$EC00)
		%CAMERA($0224,$0148,$2400)
		%CAMERA($03E0,$0004,$A400)
		%CAMERA($03D4,$0084,$9400)
		%CAMERA($00FC,$025C,$3C00)
		%CAMERA($03EC,$0228,$9C00)
		%CAMERA($0360,$0398,$C000)
		%CAMERA($022C,$02E8,$A000)
		%CAMERA($0054,$03E0,$2800)
		%CAMERA($0058,$0248,$8000)
		; ...

; ==============================================





; ==============================================
; Track 01: Ghost Valley 2
; ==============================================
zone_01:		; (45 zones)
		db	cam($00),cam($00),cam($01),cam($01)
		db	cam($01),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($03),cam($03),cam($04),cam($04)
		db	cam($04),cam($05),cam($05),cam($06)
		db	cam($06),cam($06),cam($07),cam($07)
		db	cam($07),cam($08),cam($08),cam($09)
		db	cam($09),cam($09),cam($09),cam($0A)
		db	cam($0A),cam($0A),cam($0B),cam($0B)
		db	cam($0C),cam($0C),cam($0C),cam($0D)
		db	cam($0D),cam($0D),cam($00),cam($00)
		db	cam($00)

camera_01:
		;       xpos  ypos  angle
		%CAMERA($0058,$01FC,$0000)
		%CAMERA($01B0,$003C,$B000)
		%CAMERA($0164,$0088,$7400)
		%CAMERA($0144,$01A4,$3000)
		%CAMERA($0368,$01D0,$E800)
		%CAMERA($03D8,$0098,$9000)
		%CAMERA($0338,$02D4,$2000)
		%CAMERA($03A8,$0274,$B000)
		%CAMERA($02C0,$0268,$9400)
		%CAMERA($0270,$03F0,$F000)
		%CAMERA($0200,$03C8,$D000)
		%CAMERA($008C,$0354,$4C00)
		%CAMERA($00F0,$03B0,$E400)
		%CAMERA($0054,$01D4,$8000)
		; ...

; ==============================================





; ==============================================
; Track 02: Donut Plains 2
; ==============================================
zone_02:		; (37 zones)
		db	cam($00),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($03),cam($04),cam($04),cam($05)
		db	cam($05),cam($06),cam($06),cam($07)
		db	cam($07),cam($07),cam($08),cam($08)
		db	cam($09),cam($09),cam($0A),cam($0A)
		db	cam($0B),cam($0B),cam($0B),cam($0C)
		db	cam($0C),cam($0C),cam($0D),cam($0D)
		db	cam($0E),cam($0E),cam($0E),cam($00)
		db	cam($00)

camera_02:
		;       xpos  ypos  angle
		%CAMERA($03A4,$0318,$0000)
		%CAMERA($03F0,$01C4,$EC00)
		%CAMERA($0400,$0070,$B800)
		%CAMERA($01BC,$0068,$3400)
		%CAMERA($01C8,$002C,$A800)
		%CAMERA($0154,$01C0,$E400)
		%CAMERA($002C,$015C,$6800)
		%CAMERA($01E0,$0268,$AC00)
		%CAMERA($01C4,$0320,$AC00)
		%CAMERA($0280,$03D8,$DC00)
		%CAMERA($020C,$0320,$0800)
		%CAMERA($0264,$0084,$8400)
		%CAMERA($0334,$00A4,$9000)
		%CAMERA($02B4,$01D0,$7000)
		%CAMERA($03DC,$03E4,$DC00)
		; ...

; ==============================================





; ==============================================
; Track 03: Bowser Castle 2
; ==============================================
zone_03:		; (66 zones)
		db	cam($01),cam($01),cam($01),cam($01)
		db	cam($02),cam($02),cam($02),cam($02)
		db	cam($02),cam($03),cam($03),cam($04)
		db	cam($04),cam($04),cam($04),cam($04)
		db	cam($05),cam($05),cam($05),cam($06)
		db	cam($06),cam($06),cam($06),cam($07)
		db	cam($08),cam($08),cam($08),cam($08)
		db	cam($09),cam($09),cam($09),cam($0A)
		db	cam($0A),cam($0A),cam($0A),cam($0A)
		db	cam($0A),cam($0A),cam($0A),cam($0A)
		db	cam($0B),cam($0B),cam($0B),cam($0B)
		db	cam($0B),cam($0B),cam($0B),cam($0B)
		db	cam($0B),cam($0C),cam($0C),cam($0C)
		db	cam($0D),cam($0D),cam($0D),cam($0D)
		db	cam($0E),cam($0E),cam($0F),cam($10)
		db	cam($11),cam($11),cam($11),cam($12)
		db	cam($12),cam($00)

camera_03:
		;       xpos  ypos  angle
		%CAMERA($0044,$0240,$0000)
		%CAMERA($0028,$0154,$1000)
		%CAMERA($0208,$002C,$B000)
		%CAMERA($0218,$0064,$2400)
		%CAMERA($0300,$003C,$5400)
		%CAMERA($03D4,$0188,$D000)
		%CAMERA($01F8,$00D8,$6800)
		%CAMERA($01D0,$01EC,$0000)
		%CAMERA($0114,$00B4,$6C00)
		%CAMERA($00C8,$0338,$1800)
		%CAMERA($0274,$0260,$A800)
		%CAMERA($0284,$0240,$5800)
		%CAMERA($03BC,$02F4,$A000)
		%CAMERA($02F8,$03CC,$C000)
		%CAMERA($0220,$03CC,$C000)
		%CAMERA($01B8,$03CC,$C000)
		%CAMERA($0164,$03C8,$C000)
		%CAMERA($0014,$03D4,$3000)
		%CAMERA($0054,$021C,$8400)
		; ...

; ==============================================





; ==============================================
; Track 04: Vanilla Lake 2
; ==============================================
zone_04:		; (29 zones)
		db	cam($00),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($03),cam($03),cam($04),cam($04)
		db	cam($04),cam($04),cam($05),cam($05)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($08),cam($08),cam($09)
		db	cam($09),cam($0A),cam($0A),cam($00)
		db	cam($00)

camera_04:
		;       xpos  ypos  angle
		%CAMERA($03E8,$0348,$EC00)
		%CAMERA($03DC,$0080,$9000)
		%CAMERA($0350,$00A0,$C000)
		%CAMERA($0174,$01D0,$1000)
		%CAMERA($0104,$00B0,$9000)
		%CAMERA($0110,$027C,$C000)
		%CAMERA($0104,$028C,$9400)
		%CAMERA($000C,$03B8,$3800)
		%CAMERA($012C,$0328,$4400)
		%CAMERA($0274,$026C,$8000)
		%CAMERA($0294,$02DC,$4C00)
		; ...

; ==============================================





; ==============================================
; Track 05: Rainbow Road
; ==============================================
zone_05:		; (46 zones)
		db	cam($00),cam($01),cam($01),cam($01)
		db	cam($01),cam($01),cam($02),cam($02)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($03),cam($03),cam($04),cam($04)
		db	cam($05),cam($05),cam($06),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($08),cam($08),cam($08)
		db	cam($08),cam($09),cam($09),cam($09)
		db	cam($09),cam($0A),cam($0B),cam($0A)
		db	cam($0B),cam($0A),cam($0B),cam($0B)
		db	cam($0C),cam($0C),cam($0D),cam($0D)
		db	cam($00),cam($00)

camera_05:
		;       xpos  ypos  angle
		%CAMERA($0064,$0290,$F800)
		%CAMERA($0118,$0004,$A000)
		%CAMERA($012C,$008C,$2C00)
		%CAMERA($0348,$01C0,$E000)
		%CAMERA($0200,$0158,$5C00)
		%CAMERA($023C,$0268,$E800)
		%CAMERA($00F8,$01D8,$6000)
		%CAMERA($0184,$028C,$4000)
		%CAMERA($03D0,$0264,$9000)
		%CAMERA($03CC,$03A8,$BC00)
		%CAMERA($00CC,$0380,$3400)
		%CAMERA($00CC,$03AC,$4400)
		%CAMERA($00A8,$03B0,$DC00)
		%CAMERA($0040,$0244,$8000)
		; ...

; ==============================================





; ==============================================
; Track 06: Koopa Beach 2
; ==============================================
zone_06:		; (25 zones)
		db	cam($00),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($02),cam($03)
		db	cam($03),cam($03),cam($03),cam($03)
		db	cam($03),cam($04),cam($04),cam($05)
		db	cam($05),cam($06),cam($06),cam($07)
		db	cam($07),cam($00),cam($07),cam($00)
		db	cam($00)

camera_06:
		;       xpos  ypos  angle
		%CAMERA($02F4,$00A0,$8000)
		%CAMERA($026C,$FFA8,$8000)
		%CAMERA($01D4,$0024,$A000)
		%CAMERA($0100,$0378,$F400)
		%CAMERA($01A8,$02AC,$8C00)
		%CAMERA($01D4,$02B0,$5000)
		%CAMERA($040C,$0368,$DC00)
		%CAMERA($034C,$02B8,$1400)
		; ...

; ==============================================





; ==============================================
; Track 07: Mario Circuit 1
; ==============================================
zone_07:		; (30 zones)
		db	cam($01),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($02),cam($02)
		db	cam($03),cam($03),cam($03),cam($03)
		db	cam($04),cam($04),cam($04),cam($04)
		db	cam($05),cam($05),cam($05),cam($05)
		db	cam($06),cam($06),cam($06),cam($06)
		db	cam($07),cam($07),cam($07),cam($00)
		db	cam($00),cam($00)

camera_07:
		;       xpos  ypos  angle
		%CAMERA($03B0,$0300,$0000)
		%CAMERA($03E0,$0080,$9000)
		%CAMERA($0100,$0080,$4400)
		%CAMERA($0100,$FFE0,$9000)
		%CAMERA($0060,$02C0,$0000)
		%CAMERA($0000,$0300,$3000)
		%CAMERA($0200,$01C0,$7800)
		%CAMERA($0400,$0400,$E000)
		; ...

; ==============================================





; ==============================================
; Track 08: Ghost Valley 3
; ==============================================
zone_08:		; (46 zones)
		db	cam($00),cam($01),cam($01),cam($01)
		db	cam($01),cam($02),cam($02),cam($02)
		db	cam($03),cam($03),cam($03),cam($03)
		db	cam($03),cam($04),cam($04),cam($04)
		db	cam($04),cam($04),cam($05),cam($05)
		db	cam($05),cam($05),cam($06),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($07),cam($07),cam($07),cam($08)
		db	cam($08),cam($08),cam($08),cam($09)
		db	cam($09),cam($09),cam($09),cam($09)
		db	cam($0A),cam($0A),cam($0A),cam($0A)
		db	cam($00),cam($00)

camera_08:
		;       xpos  ypos  angle
		%CAMERA($0094,$01FC,$F000)
		%CAMERA($0020,$0064,$3C00)
		%CAMERA($036C,$00CC,$D000)
		%CAMERA($0304,$FFEC,$6800)
		%CAMERA($0338,$0100,$A000)
		%CAMERA($0124,$017C,$6800)
		%CAMERA($032C,$02C8,$C400)
		%CAMERA($0348,$0260,$7000)
		%CAMERA($0220,$03C4,$3400)
		%CAMERA($01EC,$03B4,$D000)
		%CAMERA($0058,$01D4,$7800)
		; ...

; ==============================================





; ==============================================
; Track 09: Bowser Castle 3
; ==============================================
zone_09:		; (51 zones)
		db	cam($01),cam($01),cam($01),cam($01)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($04),cam($04),cam($04),cam($04)
		db	cam($06),cam($05),cam($06),cam($05)
		db	cam($07),cam($08),cam($09),cam($07)
		db	cam($08),cam($09),cam($0A),cam($0A)
		db	cam($0A),cam($0B),cam($0B),cam($0B)
		db	cam($0C),cam($0C),cam($0C),cam($0C)
		db	cam($0D),cam($0E),cam($0F),cam($0D)
		db	cam($0E),cam($0F),cam($10),cam($10)
		db	cam($10),cam($10),cam($10),cam($10)
		db	cam($11),cam($11),cam($11),cam($11)
		db	cam($00),cam($00),cam($00)

camera_09:
		;       xpos  ypos  angle
		%CAMERA($03B4,$020C,$F800)
		%CAMERA($0300,$0018,$6000)
		%CAMERA($0304,$004C,$C000)
		%CAMERA($01F0,$00A4,$E000)
		%CAMERA($00B4,$0180,$0000)
		%CAMERA($009C,$0274,$2000)
		%CAMERA($00E0,$0270,$DC00)
		%CAMERA($006C,$0270,$8000)
		%CAMERA($00B4,$0278,$8000)
		%CAMERA($0104,$0278,$8000)
		%CAMERA($01E4,$02C0,$9400)
		%CAMERA($01BC,$02DC,$0000)
		%CAMERA($01A0,$0118,$4800)
		%CAMERA($0278,$01C8,$8000)
		%CAMERA($02A0,$0188,$8000)
		%CAMERA($02C8,$0138,$8000)
		%CAMERA($02E4,$03EC,$F400)
		%CAMERA($03A4,$026C,$9000)
		; ...

; ==============================================





; ==============================================
; Track 0A: Choco Island 2
; ==============================================
zone_0A:		; (29 zones)
		db	cam($00),cam($01),cam($01),cam($01)
		db	cam($02),cam($02),cam($02),cam($02)
		db	cam($03),cam($03),cam($04),cam($04)
		db	cam($05),cam($05),cam($05),cam($06)
		db	cam($07),cam($08),cam($07),cam($09)
		db	cam($09),cam($0A),cam($0A),cam($0B)
		db	cam($0B),cam($0C),cam($0C),cam($00)
		db	cam($00)

camera_0A:
		;       xpos  ypos  angle
		%CAMERA($0068,$0380,$0400)
		%CAMERA($0100,$0108,$9400)
		%CAMERA($0000,$0054,$5800)
		%CAMERA($0080,$0058,$4000)
		%CAMERA($0354,$0024,$B000)
		%CAMERA($03E8,$00EC,$D400)
		%CAMERA($02F0,$0088,$8000)
		%CAMERA($0228,$0104,$6800)
		%CAMERA($0394,$022C,$E000)
		%CAMERA($0254,$03B8,$1C00)
		%CAMERA($0298,$036C,$C400)
		%CAMERA($01C4,$02EC,$A000)
		%CAMERA($0034,$0318,$6000)
		; ...

; ==============================================





; ==============================================
; Track 0B: Donut Plains 3
; ==============================================
zone_0B:		; (35 zones)
		db	cam($01),cam($01),cam($02),cam($02)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($03),cam($04),cam($04),cam($04)
		db	cam($04),cam($05),cam($05),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($08),cam($08),cam($08)
		db	cam($09),cam($09),cam($0A),cam($0A)
		db	cam($0B),cam($0B),cam($0B),cam($0B)
		db	cam($00),cam($00),cam($00)

camera_0B:
		;       xpos  ypos  angle
		%CAMERA($008C,$02FC,$0000)
		%CAMERA($002C,$00BC,$6C00)
		%CAMERA($01BC,$0064,$B400)
		%CAMERA($01B0,$0058,$4C00)
		%CAMERA($0314,$01C8,$1400)
		%CAMERA($02E4,$0130,$9C00)
		%CAMERA($013C,$015C,$6000)
		%CAMERA($0370,$02B8,$C800)
		%CAMERA($02D8,$029C,$5800)
		%CAMERA($02EC,$02F0,$A800)
		%CAMERA($0110,$028C,$5800)
		%CAMERA($01AC,$02F4,$A800)
		; ...

; ==============================================





; ==============================================
; Track 0C: Vanilla Lake 1
; ==============================================
zone_0C:		; (23 zones)
		db	cam($01),cam($01),cam($02),cam($02)
		db	cam($03),cam($03),cam($03),cam($04)
		db	cam($04),cam($05),cam($05),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($09),cam($0A),cam($0A)
		db	cam($00),cam($00),cam($00)

camera_0C:
		;       xpos  ypos  angle
		%CAMERA($00A8,$0300,$0000)
		%CAMERA($0104,$00E8,$9400)
		%CAMERA($0074,$0094,$5400)
		%CAMERA($02F8,$004C,$AC00)
		%CAMERA($02F4,$0068,$6C00)
		%CAMERA($0378,$0268,$0000)
		%CAMERA($03CC,$0228,$9400)
		%CAMERA($0260,$035C,$3800)
		%CAMERA($0230,$0318,$8000)
		%CAMERA($0218,$0354,$C400)
		%CAMERA($0044,$0318,$5400)
		; ...

; ==============================================





; ==============================================
; Track 0D: Koopa Beach 1
; ==============================================
zone_0D:		; (36 zones)
		db	cam($01),cam($01),cam($01),cam($01)
		db	cam($02),cam($02),cam($02),cam($03)
		db	cam($04),cam($03),cam($04),cam($04)
		db	cam($04),cam($05),cam($05),cam($06)
		db	cam($06),cam($07),cam($08),cam($07)
		db	cam($08),cam($07),cam($08),cam($09)
		db	cam($0A),cam($09),cam($0A),cam($09)
		db	cam($0A),cam($0B),cam($0B),cam($0B)
		db	cam($0C),cam($0C),cam($00),cam($00)

camera_0D:
		;       xpos  ypos  angle
		%CAMERA($00AC,$01D4,$0000)
		%CAMERA($01AC,$00A8,$C400)
		%CAMERA($0188,$0048,$5400)
		%CAMERA($0304,$0060,$7C00)
		%CAMERA($0298,$0128,$6800)
		%CAMERA($040C,$02F0,$D400)
		%CAMERA($0400,$02D4,$BC00)
		%CAMERA($0198,$0250,$6000)
		%CAMERA($01B0,$03FC,$1C00)
		%CAMERA($0094,$02CC,$4800)
		%CAMERA($0078,$03B0,$3800)
		%CAMERA($0040,$0290,$6400)
		%CAMERA($00A0,$01A0,$8800)
		; ...

; ==============================================





; ==============================================
; Track 0E: Mario Circuit 4
; ==============================================
zone_0E:		; (41 zones)
		db	cam($00),cam($01),cam($01),cam($02)
		db	cam($02),cam($03),cam($03),cam($03)
		db	cam($03),cam($04),cam($04),cam($05)
		db	cam($05),cam($05),cam($05),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($08),cam($09),cam($09)
		db	cam($09),cam($0A),cam($0A),cam($0A)
		db	cam($0B),cam($0B),cam($0B),cam($0B)
		db	cam($0C),cam($0C),cam($0C),cam($0D)
		db	cam($0D),cam($0E),cam($0E),cam($00)
		db	cam($00)

camera_0E:
		;       xpos  ypos  angle
		%CAMERA($03A8,$030C,$0000)
		%CAMERA($03D8,$0038,$9400)
		%CAMERA($03A8,$0064,$BC00)
		%CAMERA($0190,$01F8,$2C00)
		%CAMERA($0214,$0180,$C400)
		%CAMERA($0234,$0034,$AC00)
		%CAMERA($000C,$0140,$2000)
		%CAMERA($001C,$0154,$6400)
		%CAMERA($0260,$023C,$C000)
		%CAMERA($0350,$0318,$E400)
		%CAMERA($029C,$0284,$AC00)
		%CAMERA($0030,$03F4,$1C00)
		%CAMERA($0244,$03E0,$D800)
		%CAMERA($01C8,$02FC,$5400)
		%CAMERA($03B4,$02AC,$8800)
		; ...

; ==============================================





; ==============================================
; Track 0F: Mario Circuit 2
; ==============================================
zone_0F:		; (35 zones)
		db	cam($00),cam($01),cam($01),cam($01)
		db	cam($02),cam($02),cam($02),cam($02)
		db	cam($00),cam($03),cam($03),cam($03)
		db	cam($03),cam($03),cam($04),cam($04)
		db	cam($04),cam($05),cam($05),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($08),cam($08),cam($08)
		db	cam($08),cam($09),cam($09),cam($0A)
		db	cam($0A),cam($00),cam($00)

camera_0F:
		;       xpos  ypos  angle
		%CAMERA($03FC,$027C,$E000)
		%CAMERA($0214,$011C,$3400)
		%CAMERA($02EC,$0020,$AC00)
		%CAMERA($0018,$0250,$1800)
		%CAMERA($006C,$01F4,$4000)
		%CAMERA($02A4,$019C,$B000)
		%CAMERA($0294,$031C,$F000)
		%CAMERA($0290,$0308,$A400)
		%CAMERA($0118,$027C,$9000)
		%CAMERA($0104,$02C0,$4000)
		%CAMERA($03A4,$025C,$9C00)
		; ...

; ==============================================





; ==============================================
; Track 10: Ghost Valley 1
; ==============================================
zone_10:		; (33 zones)
		db	cam($00),cam($01),cam($01),cam($01)
		db	cam($02),cam($02),cam($02),cam($03)
		db	cam($03),cam($03),cam($04),cam($04)
		db	cam($04),cam($05),cam($05),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($08),cam($08),cam($08),cam($09)
		db	cam($09),cam($08),cam($09),cam($0A)
		db	cam($0A),cam($0A),cam($0A),cam($00)
		db	cam($00)

camera_10:
		;       xpos  ypos  angle
		%CAMERA($03C8,$031C,$0000)
		%CAMERA($038C,$0094,$6800)
		%CAMERA($03F0,$0010,$A400)
		%CAMERA($0334,$0078,$C000)
		%CAMERA($0070,$0098,$3000)
		%CAMERA($0068,$0030,$8000)
		%CAMERA($0038,$0294,$1000)
		%CAMERA($016C,$02AC,$B400)
		%CAMERA($015C,$02EC,$4000)
		%CAMERA($0220,$02F8,$6800)
		%CAMERA($040C,$0280,$9C00)
		; ...

; ==============================================





; ==============================================
; Track 11: Bowser Castle 1
; ==============================================
zone_11:		; (35 zones)
		db	cam($01),cam($01),cam($01),cam($02)
		db	cam($02),cam($03),cam($03),cam($03)
		db	cam($04),cam($04),cam($05),cam($05)
		db	cam($06),cam($07),cam($07),cam($08)
		db	cam($08),cam($09),cam($09),cam($0A)
		db	cam($0B),cam($0B),cam($0C),cam($0C)
		db	cam($0C),cam($0D),cam($0E),cam($0F)
		db	cam($10),cam($10),cam($11),cam($11)
		db	cam($00),cam($00),cam($00)

camera_11:
		;       xpos  ypos  angle
		%CAMERA($03AC,$0370,$FC00)
		%CAMERA($0368,$0288,$0C00)
		%CAMERA($03EC,$0030,$B000)
		%CAMERA($00EC,$003C,$4400)
		%CAMERA($007C,$001C,$6000)
		%CAMERA($00AC,$00DC,$8000)
		%CAMERA($0114,$0260,$E800)
		%CAMERA($008C,$0270,$7000)
		%CAMERA($0200,$038C,$C400)
		%CAMERA($01D4,$03A8,$0000)
		%CAMERA($01D0,$02FC,$0000)
		%CAMERA($01D0,$0244,$0000)
		%CAMERA($0194,$00D4,$5800)
		%CAMERA($02AC,$0180,$8000)
		%CAMERA($022C,$0258,$4400)
		%CAMERA($0304,$02B0,$A400)
		%CAMERA($027C,$03DC,$2800)
		%CAMERA($03D4,$030C,$9C00)
		; ...

; ==============================================





; ==============================================
; Track 12: Choco Island 1
; ==============================================
zone_12:		; (24 zones)
		db	cam($01),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($03),cam($03)
		db	cam($03),cam($04),cam($04),cam($05)
		db	cam($06),cam($06),cam($07),cam($07)
		db	cam($08),cam($08),cam($09),cam($09)
		db	cam($0A),cam($00),cam($00),cam($00)

camera_12:
		;       xpos  ypos  angle
		%CAMERA($037C,$0308,$0000)
		%CAMERA($0278,$0100,$5000)
		%CAMERA($0254,$0148,$1C00)
		%CAMERA($02A8,$0044,$A800)
		%CAMERA($01F4,$0118,$B000)
		%CAMERA($0010,$0178,$5C00)
		%CAMERA($0064,$0388,$1000)
		%CAMERA($0074,$02C4,$7400)
		%CAMERA($0100,$0308,$4C00)
		%CAMERA($02F4,$03A0,$C400)
		%CAMERA($03A4,$0258,$9000)
		; ...

; ==============================================





; ==============================================
; Track 13: Donut Plains 1
; ==============================================
zone_13:		; (37 zones)
		db	cam($00),cam($01),cam($01),cam($02)
		db	cam($02),cam($02),cam($02),cam($03)
		db	cam($03),cam($03),cam($03),cam($04)
		db	cam($04),cam($04),cam($04),cam($05)
		db	cam($05),cam($05),cam($06),cam($06)
		db	cam($06),cam($07),cam($07),cam($07)
		db	cam($07),cam($08),cam($08),cam($08)
		db	cam($09),cam($09),cam($09),cam($0A)
		db	cam($0A),cam($0A),cam($00),cam($00)
		db	cam($00)

camera_13:
		;       xpos  ypos  angle
		%CAMERA($007C,$0304,$0000)
		%CAMERA($FFF4,$0118,$3800)
		%CAMERA($0264,$0070,$C000)
		%CAMERA($0264,$0030,$5400)
		%CAMERA($0324,$0118,$7800)
		%CAMERA($038C,$0238,$8400)
		%CAMERA($0284,$0268,$6C00)
		%CAMERA($02B4,$0248,$D400)
		%CAMERA($0128,$013C,$6400)
		%CAMERA($01EC,$023C,$8C00)
		%CAMERA($001C,$0318,$5000)
		; ...

; ==============================================

; =============================================================================











; =============================================================================
;		BATTLE TRACKS
; =============================================================================

; figure out what exactly to do with these :P

; ==============================================
; Track 14: Battle Course 3
; ==============================================
zone_14:		; (53 zones)
		db	cam($0E),cam($12),cam($12),cam($12)
		db	cam($11),cam($11),cam($15),cam($15)
		db	cam($15),cam($10),cam($14),cam($14)
		db	cam($14),cam($14),cam($14),cam($0F)
		db	cam($13),cam($13),cam($13),cam($0E)
		db	cam($0E),cam($0E),cam($11),cam($11)
		db	cam($11),cam($10),cam($10),cam($10)
		db	cam($0F),cam($0F),cam($0F),cam($0E)
		db	cam($0D),cam($0A),cam($0B),cam($0C)
		db	cam($0A),cam($0B),cam($0C),cam($0D)
		db	cam($05),cam($02),cam($03),cam($04)
		db	cam($02),cam($03),cam($05),cam($04)
		db	cam($06),cam($07),cam($08),cam($09)
		db	cam($00)

camera_14:
		;       xpos  ypos  angle
		%CAMERA($01FC,$00FC,$8000)
		%CAMERA($0204,$02E0,$0000)
		%CAMERA($028C,$0168,$C000)
		%CAMERA($0294,$0290,$0000)
		%CAMERA($0170,$0298,$4000)
		%CAMERA($0168,$0174,$8000)
		%CAMERA($00B0,$00B0,$6000)
		%CAMERA($034C,$00B0,$9C00)
		%CAMERA($034C,$0350,$E000)
		%CAMERA($00B0,$034C,$2000)
		%CAMERA($0200,$003C,$8000)
		%CAMERA($0200,$03CC,$0000)
		%CAMERA($03D8,$01FC,$C000)
		%CAMERA($0030,$0200,$4000)
		%CAMERA($000C,$0008,$6000)
		%CAMERA($0004,$03FC,$2000)
		%CAMERA($0400,$0400,$E400)
		%CAMERA($03FC,$0000,$A000)
		%CAMERA($036C,$0020,$B000)
		%CAMERA($0024,$003C,$7400)
		%CAMERA($0040,$03D4,$3800)
		%CAMERA($03E0,$0380,$F400)
		; ...

; ==============================================





; ==============================================
; Track 15: Battle Course 4
; ==============================================
zone_15:		; (53 zones)
		db	cam($0E),cam($12),cam($12),cam($12)
		db	cam($11),cam($11),cam($15),cam($15)
		db	cam($15),cam($10),cam($14),cam($14)
		db	cam($14),cam($14),cam($14),cam($0F)
		db	cam($13),cam($13),cam($13),cam($0E)
		db	cam($0E),cam($0E),cam($11),cam($11)
		db	cam($11),cam($10),cam($10),cam($10)
		db	cam($0F),cam($0F),cam($0F),cam($0E)
		db	cam($0D),cam($0A),cam($0B),cam($0C)
		db	cam($0A),cam($0B),cam($0C),cam($0D)
		db	cam($05),cam($02),cam($03),cam($04)
		db	cam($02),cam($03),cam($05),cam($04)
		db	cam($06),cam($07),cam($08),cam($09)
		db	cam($00)

camera_15:
		;       xpos  ypos  angle
		%CAMERA($01FC,$00FC,$8000)
		%CAMERA($0204,$02E0,$0000)
		%CAMERA($028C,$0168,$C000)
		%CAMERA($0294,$0290,$0000)
		%CAMERA($0170,$0298,$4000)
		%CAMERA($0168,$0174,$8000)
		%CAMERA($00B0,$00B0,$6000)
		%CAMERA($034C,$00B0,$9C00)
		%CAMERA($034C,$0350,$E000)
		%CAMERA($00B0,$034C,$2000)
		%CAMERA($0200,$003C,$8000)
		%CAMERA($0200,$03CC,$0000)
		%CAMERA($03D8,$01FC,$C000)
		%CAMERA($0030,$0200,$4000)
		%CAMERA($000C,$0008,$6000)
		%CAMERA($0004,$03FC,$2000)
		%CAMERA($0400,$0400,$E400)
		%CAMERA($03FC,$0000,$A000)
		%CAMERA($036C,$0020,$B000)
		%CAMERA($0024,$003C,$7400)
		%CAMERA($0040,$03D4,$3800)
		%CAMERA($03E0,$0380,$F400)
		; ...

; ==============================================





; ==============================================
; Track 16: Battle Course 1
; ==============================================
zone_16:		; (43 zones)
		db	cam($07),cam($07),cam($13),cam($04)
		db	cam($09),cam($14),cam($05),cam($05)
		db	cam($15),cam($15),cam($06),cam($16)
		db	cam($16),cam($0C),cam($0D),cam($0E)
		db	cam($0B),cam($0C),cam($0D),cam($0D)
		db	cam($0E),cam($0E),cam($0B),cam($0B)
		db	cam($0C),cam($11),cam($10),cam($12)
		db	cam($0F),cam($02),cam($00),cam($03)
		db	cam($02),cam($01),cam($08),cam($04)
		db	cam($09),cam($14),cam($05),cam($06)
		db	cam($07),cam($0A),cam($0A)

camera_16:
		;       xpos  ypos  angle
		%CAMERA($0200,$0128,$8000)
		%CAMERA($0200,$02D4,$0000)
		%CAMERA($02DC,$0200,$C000)
		%CAMERA($0124,$0200,$4000)
		%CAMERA($0358,$0084,$9000)
		%CAMERA($0380,$0354,$D000)
		%CAMERA($00B4,$0380,$1000)
		%CAMERA($0084,$00BC,$4C00)
		%CAMERA($024C,$008C,$D800)
		%CAMERA($02FC,$01FC,$4000)
		%CAMERA($02EC,$0370,$A800)
		%CAMERA($010C,$0200,$7000)
		%CAMERA($0208,$010C,$AC00)
		%CAMERA($02F4,$0200,$F000)
		%CAMERA($0200,$02EC,$3000)
		%CAMERA($0218,$021C,$6000)
		%CAMERA($0218,$01E0,$2000)
		%CAMERA($01E0,$01DC,$E000)
		%CAMERA($01E0,$021C,$A000)
		%CAMERA($0334,$00C4,$C000)
		%CAMERA($0340,$0324,$0000)
		%CAMERA($00DC,$0340,$4000)
		%CAMERA($00C8,$00D8,$8000)
		; ...

; ==============================================





; ==============================================
; Track 17: Battle Course 2
; ==============================================
zone_17:		; (53 zones)
		db	cam($0E),cam($12),cam($12),cam($12)
		db	cam($11),cam($11),cam($15),cam($15)
		db	cam($15),cam($10),cam($14),cam($14)
		db	cam($14),cam($14),cam($14),cam($0F)
		db	cam($13),cam($13),cam($13),cam($0E)
		db	cam($0E),cam($0E),cam($11),cam($11)
		db	cam($11),cam($10),cam($10),cam($10)
		db	cam($0F),cam($0F),cam($0F),cam($0E)
		db	cam($0D),cam($0A),cam($0B),cam($0C)
		db	cam($0A),cam($0B),cam($0C),cam($0D)
		db	cam($05),cam($02),cam($03),cam($04)
		db	cam($02),cam($03),cam($05),cam($04)
		db	cam($06),cam($07),cam($08),cam($09)
		db	cam($00)

camera_17:
		;       xpos  ypos  angle
		%CAMERA($01FC,$00FC,$8000)
		%CAMERA($0204,$02E0,$0000)
		%CAMERA($028C,$0168,$C000)
		%CAMERA($0294,$0290,$0000)
		%CAMERA($0170,$0298,$4000)
		%CAMERA($0168,$0174,$8000)
		%CAMERA($00B0,$00B0,$6000)
		%CAMERA($034C,$00B0,$9C00)
		%CAMERA($034C,$0350,$E000)
		%CAMERA($00B0,$034C,$2000)
		%CAMERA($0200,$003C,$8000)
		%CAMERA($0200,$03CC,$0000)
		%CAMERA($03D8,$01FC,$C000)
		%CAMERA($0030,$0200,$4000)
		%CAMERA($000C,$0008,$6000)
		%CAMERA($0004,$03FC,$2000)
		%CAMERA($0400,$0400,$E400)
		%CAMERA($03FC,$0000,$A000)
		%CAMERA($036C,$0020,$B000)
		%CAMERA($0024,$003C,$7400)
		%CAMERA($0040,$03D4,$3800)
		%CAMERA($03E0,$0380,$F400)
		; ...

; ==============================================
; ==============================================