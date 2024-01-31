
hirom



macro def_label(addr, lbl)
pushpc
org	<addr>
<lbl>:
pullpc
endmacro

macro write_byte(addr, val)
pushpc
org	<addr>
		db	<val>
pullpc
endmacro

macro write_word(addr, val)
pushpc
org	<addr>
		dw	<val>
pullpc
endmacro

macro write_long(addr, val)
pushpc
org	<addr>
		dl	<val>
pullpc
endmacro


macro write_JSR(addr, func)
pushpc
org	<addr>
		JSR.W	<func>
pullpc
endmacro

macro write_JSL(addr, func)
pushpc
org	<addr>
		JSL.L	<func>
pullpc
endmacro




%write_byte($00FFD7, $0A)	; rom size



; use camera mode 8 for "resident kart" cam?


!CAM_MODE_MIRROR = $0006
!CAM_MODE_RE = $0008





org	$8086A0			; US version
CAM_CONTROL_MAIN:
		LDA.B	$A4,X
		CMP.W	#$0002
		BEQ		+
		CMP.W	#!CAM_MODE_RE
		BEQ		+
		LDA.B	$AC,X
		BPL		.ret
		;BIT.W	#$4000
		;BEQ		.ret
	+
		JSL.L	RESIDENT_CAMERA
.ret
		RTS



org	$808632
		JML.L	CAMERA_ROTATE_SEL





org	$80A202
		JSL.L	RACE_START_CAMERA
		BRA	$80A218


org	$80A22E
		JSL.L	COUNTDOWN_START_CAMERA
		RTS


org	$80A202
		JSL.L	RACE_START_CAMERA
		BRA	start_cam_join

%def_label($80A218,start_cam_join)

org	$80A22E
		JSL.L	COUNTDOWN_START_CAMERA
		RTS




%def_label($81F83B,HDMA_set_1)
%def_label($81F840,HDMA_set_2)
%def_label($81F845,HDMA_set_3)

%write_word($81F899,HDMA_set_1)	; Cam mode 8 Bottom Screen HDMA Set
%write_word($81F8A7,HDMA_set_1)	; Cam mode 8 Top Screen HDMA Set


org	$81FA61
HDMA_SEL:
		LDX.B	$A4		; top screen cam mode
		JSR.W	(HDMA_SEL_A,X)
		LDX.B	$A6		; bottom screen cam mode
		JSR.W	(HDMA_SEL_B,X)
		RTL

		; prev tables here
		dw	0,0,0,0
		dw	0,0,0,0

warnpc	$81FA7C

%def_label($81FA9D,cam_A)
%def_label($81FA7C,cam_B)
%def_label($81FAF6,cam_C)
%def_label($81FA81,cam_D)









%write_JSR($81F7F1,MAP_PARAM)


org	$81FB4F
SCREEN_PARAM:
		JSL.L	SCREEN_PARAM_JSL
		RTS

MAP_PARAM:
		LDA.W	#$0006
		STA.B	$A4
		LDX.W	#$0000
		JSR.W	$FB4F
		JSR.W	$F9E0
		JSR.W	$F907
		RTS

HDMA_SEL_A:
		dw	cam_A,cam_A,cam_A,cam_B,cam_A

HDMA_SEL_B:
		dw	cam_C,cam_C,cam_C,cam_D,cam_C

raster_offset:
		dw	$0000,$0070

y_offset:
		dw	$0260,$02A0

camera_init_sel:
		dw	cam_init_1,cam_init_1,cam_init_1,cam_init_2,cam_init_1

cam_init_1:		; Normal view (camera mode)
		dw	$0050		; dist view<->base     ; $0040 by default
		dw	$3380		; zenith angle         ; $3400 by default
		dw	$0100		; dist view<->screen
		dw	$0066		; raster "center" offset


cam_init_2:		; Map view
		dw	$0880		; dist view<->base
		dw	$2A00		; zenith angle
		dw	$0200		; dist view<->screen
		dw	$0066		; raster "center" offset
		;
		dw	$0800		; center X
		dw	$1200		; center Y




warnpc	$81FBB4


org	$808AFE
		JSL.L	CAM_FLIP_PARAM_JSL
		NOP



org	$80CCA1
		JML.L	CAR_ROUT_SEL





%def_label($80C2E5,SUB_TABLE)
%def_label($80C2F7,SKIP_ENTRY)
%def_label($80CB7D,DISP_ENTRY_A)
%def_label($80CBF3,DISP_ENTRY_B)

%write_word($80CAF1,SKIP_ENTRY)
%write_word($80CAF9,SKIP_ENTRY)
%write_word($80CAFB,SUB_TABLE)
%write_word($80CAFD,DISP_ENTRY_A)

%write_word($80CB3D,SKIP_ENTRY)
%write_word($80CB43,SKIP_ENTRY)
%write_word($80CB45,SUB_TABLE)
%write_word($80CB47,DISP_ENTRY_B)




; fix shadow showing up in wrong spot when jumping
org $80ec4b
		BRA		SKIP_SHADOW_DISPLAY
org $80ec78
SKIP_SHADOW_DISPLAY:




; fix 'end-of-race' issue
org $81df8d
		NOP
		NOP



; fix zones for battle tracks
org $81fbc8
		LDA.W	$FF9B,X
		STA.B	$08
		CPX.W	#$0028		; $14 * 2
		BCS		.btl
		LDA.W	#$00C6
		BRA		.join
.btl:
		LDA.W	#((BT1_ZONES>>16)|$C0)
.join:
		STA.B	$0A
		STA.B	$0E
		LDA.W	$FFCB,X
		STA.B	$0C
		BRA		CP_JMP

org $81fbfb
CP_JMP:



%write_word($81FFC3,BT3_ZONES)
%write_word($81FFC5,BT4_ZONES)
%write_word($81FFC7,BT1_ZONES)
%write_word($81FFC9,BT2_ZONES)

%write_word($81FFF3,BT3_TARGETS)
%write_word($81FFF5,BT4_TARGETS)
%write_word($81FFF7,BT1_TARGETS)
%write_word($81FFF9,BT2_TARGETS)






org	$888000


RESIDENT_CAMERA:
		; X = screen num
		; Y = player ptr

		PHB
		PHK
		PLB

		LDA.B	$36			; gamemode
		CMP.W	#$0016		; course select
		BEQ		.norm
		CMP.W	#$000C		; credits
		BEQ		.norm
		BRA		.cont
.norm:
		JMP.W	NORMAL_CAMERA_OPERATION
.cont:
		
		STX.B	$04			; temp store screen num
		STY.B	$06			; temp store player ptr

		LDA.W	#(TRACK_ZONES>>16)&$00FF
		STA.B	$02			; table bank
		LDA.W	$C0,Y		; checkpoint
		AND.W	#$007F				; TODO: FF?
		
		TAY
		LDA.W	$0124		; track num
		ASL		A
		TAX
		LDA.W	TRACK_ZONES,X
		STA.B	$00			; table addr
		
		; get camera idx
		LDA.B	[$00],Y
		AND.W	#$00FF
		TAY

		; get camera params
		LDA.W	TRACK_CAMERAS,X
		STA.B	$00			; camera tbl addr

		; store camera params
		LDX.B	$04			; restore screen num

		LDA.B	[$00],Y
		STA.B	$88,X		; Screen.global_x
		INY
		INY
		LDA.B	[$00],Y
		STA.B	$8C,X		; Screen.global_y
		INY
		INY
		LDA.B	[$00],Y
		STA.B	$94,X		; Screen.angle

		;LDX.B	$04			; restore screen num
		LDY.B	$06			; restore player ptr
		PLB
		RTL


SCREEN_PARAM_JSL:
		LDY.B	$A4,X
		LDA.W	camera_init_sel,Y
		TAY
		LDA.W	0,Y
		STA.B	$7C,X
		LDA.W	2,Y
		STA.B	$80,X
		LDA.W	4,Y
		STA.B	$84,X
		LDA.W	6,Y
		CLC
		ADC.W	raster_offset,X
		STA.B	$98,X
		LDA.W	8,Y
		STA.B	$88,X
		LDA.W	10,Y
		SEC
		SBC.W	y_offset,X
		STA.B	$8C,X
		STZ.B	$94,X
		RTL

CAM_FLIP_PARAM_JSL:
		PHB
		PHK
		PLB
		LDA.W	CAM_FLIP,Y
		STA.B	$D4,X
		PLB
		RTL

CAM_FLIP:
		dw	$0000,$00C1,$0000,$00C0,$0000




RACE_START_CAMERA:
		PHB
		PHK
		PLB

		LDX.B	$2E
		LDA.W	#!CAM_MODE_RE
		JSR.W	(.start_cam,X)
		LDA.W	#$8000				; SETTING BIT8000 FUCKS THINGS UP
		JSR.W	(set_bits,X)
		;LDA.W	#$00C0
		;JSR.W	(reset_bits,X)

		PLB
		RTL

.start_cam:
		dw	.cam2p,.camp1,.camp2

.cam2p:	STA.B	$A4
.camp2:	STA.B	$A6
		RTS
.camp1:	STA.B	$A4
		RTS

COUNTDOWN_START_CAMERA:
		PHB
		PHK
		PLB
		LDX.B	$2E
		;LDA.W	#$C000
		;JSR.W	(set_bits,X)
		LDA.W	#$00C0
		JSR.W	(reset_bits,X)
		PLB
		RTL

set_bits:
		dw	.bit2p,.bitp1,.bitp2

.bit2p:	TSB.B	$AC
.bitp2:	TSB.B	$AE
		RTS
.bitp1:	TSB.B	$AC
		RTS

reset_bits:
		dw	.bit2p,.bitp1,.bitp2

.bit2p:	TRB.B	$AC
.bitp2:	TRB.B	$AE
		RTS
.bitp1:	TRB.B	$AC
		RTS



CAMERA_ROTATE_SEL:
		LDA.B	$A4,X
		BEQ	.norm_cam
		CMP.W	#$0006
		BEQ	.map_cam
		CMP.W	#$0008
		BEQ	.re_cam
.rev_cam:
		JML.L	$80863B
.norm_cam:
		JML.L	$80865C
.map_cam:
		JML.L	$80869F
.re_cam:
		JML.L	$808673

CAR_ROUT_SEL:
		TXY
		LDX.B	$B8		; screen num
		LDA.B	$A4,X
		CMP.W	#!CAM_MODE_RE
		BEQ	.re_car
		LDA.B	$AC,X
		BPL	.other_car
		LDX.B	$B4		; car ptr
		LDA.B	$10,X	; flags
		AND.W	#$0020	; goal
		BNE	.goal_car
.re_car:
.reg_car:
		JML.L	$80CCB1
.goal_car:
		JML.L	$80CCB7
.other_car:
		JML.L	$80CCBD




NORMAL_CAMERA_OPERATION:
		LDA.W	$0016,Y
		STA.B	$00
		LDA.W	$0018,Y
		ROL.B	$00
		ROL		A
		ROL.B	$00
		ROL		A
		STA.B	$88,X
		
		LDA.W	$001A,Y
		STA.B	$00
		LDA.W	$001C,Y
		ROL.B	$00
		ROL		A
		ROL.B	$00
		ROL		A
		STA.B	$8C,X


		PLB
		RTL




org	$88A000
incsrc "zones.asm"


BT1_ZONES:
incbin "bt1_zones.bin"
BT1_TARGETS:
incbin "bt1_targets.bin"

BT2_ZONES:
BT3_ZONES:
BT4_ZONES:
incbin "bt4_zones.bin"
BT2_TARGETS:
BT3_TARGETS:
BT4_TARGETS:
incbin "bt4_targets.bin"






org $C70000
incbin "text_compressed.bin"

%write_word($81AEF4,RANKOUT_TEXT_DATA)
%write_word($81AFAD,GAMEOVER_TEXT_DATA)

%write_word($81AF11,$0007)
%write_word($81AFBF,$000A)


!rX = $5C


!txt_y1 = 0
!txt_o1 = 1
!txt_u1 = 2
!txt_d1 = 3
!txt_i1 = 4
!txt_e1 = 5

!txt_y2 = 6
!txt_o2 = 7
!txt_u2 = 8
!txt_a2 = 9
!txt_r2 = 10
!txt_e2 = 11
!txt_d2 = 12


org $81AF30
RANKOUT_TEXT_DATA:
	db	!rX+$00,$B6,!txt_y1 ;Y
	db	!rX+$08,$B6,!txt_o1 ;O
	db	!rX+$10,$B6,!txt_u1 ;U
	db	!rX+$20,$B6,!txt_d1 ;D
	db	!rX+$28,$B6,!txt_i1 ;I
	db	!rX+$30,$B6,!txt_e1 ;E
	db	!rX+$38,$B6,!txt_d1 ;D
	db	0
;print pc
warnpc $81AF4C


org $81AF74
txt_Y1:	db	0,$3B,$E7,$E6	; Y
txt_O1:	db	0,$3B,$E9,$E8	; O
txt_U1:	db	0,$3B,$EB,$EA	; U
txt_D1:	db	0,$3B,$ED,$EC	; D
txt_I1:	db	0,$3B,$EF,$EE	; I
txt_E1:	db	0,$3B,$F1,$F0	; E
;print pc
warnpc $81AF8D


org $81B0DA
char_sel:
	dw	txt_Y1,txt_O1,txt_U1,txt_D1
	dw	txt_I1,txt_E1
	
	dw	txt_Y2,txt_O2,txt_U2,txt_A2
	dw	txt_R2,txt_E2,txt_D2


!oX = $4C

GAMEOVER_TEXT_DATA:
	db	!oX+$00,$FE-($0C*0),!txt_y2 ;Y
	db	!oX+$08,$FE-($0C*1),!txt_o2 ;O
	db	!oX+$10,$FE-($0C*2),!txt_u2 ;U
	db	!oX+$20,$FE-($0C*3),!txt_a2 ;A
	db	!oX+$28,$FE-($0C*4),!txt_r2 ;R
	db	!oX+$30,$FE-($0C*5),!txt_e2 ;E
	db	!oX+$40,$FE-($0C*6),!txt_d2 ;D
	db	!oX+$48,$FE-($0C*7),!txt_e2 ;E
	db	!oX+$50,$FE-($0C*8),!txt_a2 ;A
	db	!oX+$58,$FE-($0C*9),!txt_d2 ;D
	db	0

txt_Y2:	db	0,$3B,$01,$00	; Y
txt_O2:	db	0,$3B,$03,$02	; O
txt_U2:	db	0,$3B,$05,$04	; U
txt_A2:	db	0,$3B,$07,$06	; A
txt_R2:	db	0,$3B,$09,$08	; R
txt_E2:	db	0,$3B,$0B,$0A	; E
txt_D2:	db	0,$3B,$0D,$0C	; D
warnpc $81B140
