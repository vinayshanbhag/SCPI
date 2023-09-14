# HP 33120a 
## SCPI command summary[^1]

### The APPLy Commands
```
APPLy:SINusoid [<frequency> [,<amplitude> [,<offset>] ]]
APPLy:SQUare [<frequency> [,<amplitude> [,<offset>] ]]
APPLy:TRIangle [<frequency> [,<amplitude> [,<offset>] ]]
APPLy:RAMP [<frequency> [,<amplitude> [,<offset>] ]]
APPLy:NOISe [<frequency|DEFault> 1 [,<amplitude> [,<offset>] ]]
APPLy:DC [<frequency|DEFault> 1 [,<amplitude|DEFault> 1 [,<offset>] ]]
APPLy:USER [<frequency> [,<amplitude> [,<offset>] ]]
APPLy?
```

### Output Configuration Commands
```
[SOURce:]
 FUNCtion:SHAPe {SINusoid|SQUare|TRIangle|RAMP|NOISe|DC|USER}
 FUNCtion:SHAPe?
[SOURce:]
 FREQuency {<frequency>|MINimum|MAXimum}
 FREQuency? [MINimum|MAXimum]
[SOURce:]
 PULSe:DCYCle {<percent>|MINimum|MAXimum}
 PULSe:DCYCle? [MINimum|MAXimum]
[SOURce:]
 VOLTage {<amplitude>|MINimum|MAXimum}
 VOLTage? [MINimum|MAXimum]
 VOLTage:OFFSet {<offset>|MINimum|MAXimum}
 VOLTage:OFFSet? [MINimum|MAXimum]
 VOLTage:UNIT {VPP|VRMS|DBM|DEFault}
 VOLTage:UNIT?
OUTPut:LOAD {50|INFinity|MINimum|MAXimum}
OUTPut:LOAD? [MINimum|MAXimum]
OUTPut:SYNC {OFF|ON}
OUTPut:SYNC?
*SAV {0|1|2|3}                                        State 0 is the instrument state at power down.
*RCL {0|1|2|3}                                        States 1, 2, and 3 are user-defined instrument states.
MEMory:STATe:DELete {0|1|2|3}
```

### Modulation Commands
```
[SOURce:]
 AM:DEPTh {<depth in percent>|MINimum|MAXimum}
 AM:DEPTh? [MINimum|MAXimum]
 AM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NOISe|USER}
 AM:INTernal:FUNCtion?
 AM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
 AM:INTernal:FREQuency? [MINimum|MAXimum]
 AM:SOURce {BOTH|EXTernal}
 AM:SOURce?
 AM:STATe {OFF|ON}
 AM:STATe?
[SOURce:]
 FM:DEViation {<peak deviation in Hz>|MINimum|MAXimum}
 FM:DEViation? [MINimum|MAXimum]
 FM:INTernal:FUNCtion {SINusoid|SQUare|TRIangle|RAMP|NOISe|USER}
 FM:INTernal:FUNCtion?
 FM:INTernal:FREQuency {<frequency>|MINimum|MAXimum}
 FM:INTernal:FREQuency? [MINimum|MAXimum]
 FM:STATe {OFF|ON}
 FM:STATe?
[SOURce:]
 BM:NCYCles {<# cycles>|INFinity|MINimum|MAXimum}
 BM:NCYCles? [MINimum|MAXimum]
 BM:PHASe {<degrees>|MINimum|MAXimum}
 BM:PHASe? [MINimum|MAXimum]
 BM:INTernal:RATE {<frequency>|MINimum|MAXimum}
 BM:INTernal:RATE? [MINimum|MAXimum]
 BM:SOURce {INTernal|EXTernal}                        Gated Burst Mode
 BM:SOURce?
 BM:STATe {OFF|ON}
 BM:STATe?
TRIGger:SOURce {IMMediate|EXTernal|BUS}               Triggered Burst Mode
TRIGger:SOURce?
```

### Frequency-Shift Keying (FSK) Commands
```
[SOURce:]
 FSKey:FREQuency {<frequency>|MINimum|MAXimum}
 FSKey:FREQuency? [MINimum|MAXimum]
 FSKey:INTernal:RATE {<rate in Hz>|MINimum|MAXimum}
 FSKey:INTernal:RATE? [MINimum|MAXimum]
 FSKey:SOURce {INTernal|EXTernal}
 FSKey:SOURce?
 FSKey:STATe {OFF|ON}
 FSKey:STATe?
```

### Sweep Commands
```
[SOURce:]
 FREQuency:STARt {<frequency>|MINimum|MAXimum}
 FREQuency:STARt? [MINimum|MAXimum]
 FREQuency:STOP {<frequency>|MINimum|MAXimum}
 FREQuency:STOP? [MINimum|MAXimum]
[SOURce:]
 SWEep:SPACing {LINear|LOGarithmic}
 SWEep:SPACing?
 SWEep:TIME {<seconds>|MINimum|MAXimum}
 SWEep:TIME? [MINimum|MAXimum]
 SWEep:STATe {OFF|ON}
 SWEep:STATe?
TRIGger:SOURce {IMMediate|EXTernal|BUS}               Triggered Sweep Mode
TRIGger:SOURce?
```

### Arbitrary Waveform Commands
```
[SOURce:]
 FUNCtion:USER {<arb name> | VOLATILE}                Specify 1 of the 5 built-in waveforms or a user-defined waveform name.
 FUNCtion:USER?
 FUNCtion:SHAPe USER
 FUNCtion:SHAPe?

DATA VOLATILE, <value>,<value>, . . .
DATA:DAC VOLATILE, {<binary block>|<value>,<value>, . . . }
DATA:ATTRibute:AVERage? [<arb name>]
DATA:ATTRibute:CFACtor? [<arb name>]
DATA:ATTRibute:POINts? [<arb name>]
DATA:ATTRibute:PTPeak? [<arb name>]
DATA:CATalog?
DATA:COPY <destination arb name> [,VOLATILE]
DATA:DELete <arb name>
DATA:DELete:ALL
DATA:NVOLatile:CATalog?
DATA:NVOLatile:FREE?
FORMat:BORDer {NORMal|SWAPped}                         Specify Byte Order
FORMat:BORDer?
```

### Triggering Commands
```
TRIGger:SOURce {IMMediate|EXTernal|BUS}
TRIGger:SOURce?
TRIGger:SLOPe {POSitive|NEGative}
TRIGger:SLOPe?
*TRG 
```

### System-Related Commands
```
DISPlay {OFF|ON}
DISPlay?
DISPlay:TEXT <quoted string>
DISPlay:TEXT?
DISPlay:TEXT:CLEar
SYSTem:BEEPer
SYSTem:ERRor?
SYSTem:VERSion?
*IDN?
*RST
*TST?
*SAV {0|1|2|3}                                          State 0 is the instrument state at power down.
*RCL {0|1|2|3}                                          States 1, 2, and 3 are user-defined instrument states.
MEMory:STATe:DELete {0|1|2|3}
```

### Calibration Commands
```
CALibration?
CALibration:COUNt?
CALibration:SECure:CODE <new code>
CALibration:SECure:STATe {OFF|ON},<code>
CALibration:SECure:STATe?
CALibration:SETup <0|1|2|3| . . . |84>
CALibration:SETup?
CALibration:STRing <quoted string>
CALibration:STRing?
CALibration:VALue <value>
CALibration:VALue?
```

### RS-232 Interface Commands
```
SYSTem:LOCal
SYSTem:REMote
SYSTem:RWLock
```

### Status Reporting Commands
```
SYSTem:ERRor?
*CLS
*ESE <enable value>
*ESE?
*ESR?
*OPC
*OPC?
*PSC {0|1}
*PSC?
*SRE <enable value>
*SRE?
*STB?
*WAI
```

### IEE-488.2 Common Commands
```
*CLS
*ESE <enable value>
*ESE?
*ESR?
*IDN?
*OPC
*OPC?
*PSC {0|1}
*PSC?
*RST
*SAV {0|1|2|3} State 0 is the instrument state at power down.
*RCL {0|1|2|3} States 1, 2, and 3 are user-defined instrument states.
*SRE <enable value>
*SRE?
*STB?
*TRG
*TST?
*WAI
```

### Phase-Lock Commands (Option 001) 
```
PHASe:ADJust {<radians>|MINimum|MAXimum}
PHASe:ADJust?
PHASe:REFerence
PHASe:UNLock:ERRor:STATe {OFF|ON}
PHASe:UNLock:ERRor:STATe?
OUTPut:TRIGger:IMMediate
OUTPut:TRIGger:STATe {OFF|ON}
OUTPut:TRIGger:STATe?
*OPT?
```


[^1]: Source: [HP/Agilent/Keysight 33120a User Manual](https://www.keysight.com/il/en/assets/9018-04436/user-manuals/9018-04436.pdf)
