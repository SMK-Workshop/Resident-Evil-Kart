@echo OFF


copy "Super Mario Kart (U).sfc" "SMK-Resident-Kart.sfc"


asar --no-title-check --symbols=wla "code/main.asm" "SMK-Resident-Kart.sfc"

python3 ChecksumToolSMK.py "SMK-Resident-Kart.sfc"


pause