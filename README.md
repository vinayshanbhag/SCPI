# HP 34401a 
## SCPI command summary
```
MEASure
:VOLTage:DC? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:VOLTage:DC:RATio? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:VOLTage:AC? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:CURRent:DC? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:CURRent:AC? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:RESistance? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:FRESistance? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:FREQuency? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:PERiod? {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:CONTinuity?
:DIODe?

CONFigure
:VOLTage:DC {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:VOLTage:DC:RATio {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:VOLTage:AC {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:CURRent:DC {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:CURRent:AC {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:RESistance {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:FRESistance {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:FREQuency {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:PERiod {<range>|MIN|MAX|DEF},{<resolution>|MIN|MAX|DEF}
:CONTinuity
:DIODe

CONFigure?


[SENSe:]
FUNCtion "VOLTage:DC"
FUNCtion "VOLTage:DC:RATio"
FUNCtion "VOLTage:AC"
FUNCtion "CURRent:DC"
FUNCtion "CURRent:AC"
FUNCtion "RESistance"
FUNCtion "FRESistance"
FUNCtion "FREQuency"
FUNCtion "PERiod"
FUNCtion "CONTinuity"
FUNCtion "DIODe"
FUNCtion?

[SENSe:]
VOLTage:DC:RANGe {<range>|MINimum|MAXimum}
VOLTage:DC:RANGe? [MINimum|MAXimum]
VOLTage:AC:RANGe {<range>|MINimum|MAXimum}
VOLTage:AC:RANGe? [MINimum|MAXimum]
CURRent:DC:RANGe {<range>|MINimum|MAXimum}
CURRent:DC:RANGe? [MINimum|MAXimum]
CURRent:AC:RANGe {<range>|MINimum|MAXimum}
CURRent:AC:RANGe? [MINimum|MAXimum]
RESistance:RANGe {<range>|MINimum|MAXimum}
RESistance:RANGe? [MINimum|MAXimum]
FRESistance:RANGe {<range>|MINimum|MAXimum}
FRESistance:RANGe? [MINimum|MAXimum]
FREQuency:VOLTage:RANGe {<range>|MINimum|MAXimum}
FREQuency:VOLTage:RANGe? [MINimum|MAXimum]
PERiod:VOLTage:RANGe {<range>|MINimum|MAXimum}
PERiod:VOLTage:RANGe? [MINimum|MAXimum]

[SENSe:]
VOLTage:DC:RANGe:AUTO {OFF|ON}
VOLTage:DC:RANGe:AUTO?
VOLTage:AC:RANGe:AUTO {OFF|ON}
VOLTage:AC:RANGe:AUTO?
CURRent:DC:RANGe:AUTO {OFF|ON}
CURRent:DC:RANGe:AUTO?
CURRent:AC:RANGe:AUTO {OFF|ON}
CURRent:AC:RANGe:AUTO?
RESistance:RANGe:AUTO {OFF|ON}
RESistance:RANGe:AUTO?
FRESistance:RANGe:AUTO {OFF|ON}
FRESistance:RANGe:AUTO?
FREQuency:VOLTage:RANGe:AUTO {OFF|ON}
FREQuency:VOLTage:RANGe:AUTO?
PERiod:VOLTage:RANGe:AUTO {OFF|ON}
PERiod:VOLTage:RANGe:AUTO?

[SENSe:]
VOLTage:DC:RESolution {<resolution>|MINimum|MAXimum}
VOLTage:DC:RESolution? [MINimum|MAXimum]
VOLTage:AC:RESolution {<resolution>|MINimum|MAXimum}
VOLTage:AC:RESolution? [MINimum|MAXimum]
CURRent:DC:RESolution {<resolution>|MINimum|MAXimum}
CURRent:DC:RESolution? [MINimum|MAXimum]
CURRent:AC:RESolution {<resolution>|MINimum|MAXimum}
CURRent:AC:RESolution? [MINimum|MAXimum]
RESistance:RESolution {<resolution>|MINimum|MAXimum}
RESistance:RESolution? [MINimum|MAXimum]
FRESistance:RESolution {<resolution>|MINimum|MAXimum}
FRESistance:RESolution? [MINimum|MAXimum]

[SENSe:]
VOLTage:DC:NPLCycles {0.02|0.2|1|10|100|MINimum|MAXimum}
VOLTage:DC:NPLCycles? [MINimum|MAXimum]
CURRent:DC:NPLCycles {0.02|0.2|1|10|100|MINimum|MAXimum}
CURRent:DC:NPLCycles? [MINimum|MAXimum]
RESistance:NPLCycles {0.02|0.2|1|10|100|MINimum|MAXimum}
RESistance:NPLCycles? [MINimum|MAXimum]
FRESistance:NPLCycles {0.02|0.2|1|10|100|MINimum|MAXimum}
FRESistance:NPLCycles? [MINimum|MAXimum]

[SENSe:]
FREQuency:APERture {0.01|0.1|1|MINimum|MAXimum}
FREQuency:APERture? [MINimum|MAXimum]
PERiod:APERture {0.01|0.1|1|MINimum|MAXimum}
PERiod:APERture? [MINimum|MAXimum]

[SENSe:]
DETector:BANDwidth {3|20|200|MINimum|MAXimum}
DETector:BANDwidth? [MINimum|MAXimum]

[SENSe:]
ZERO:AUTO {OFF|ONCE|ON}
ZERO:AUTO?

INPut
:IMPedance:AUTO {OFF|ON}
:IMPedance:AUTO?

ROUTe:TERMinals?

CALCulate
:FUNCtion {NULL|DB|DBM|AVERage|LIMit}
:FUNCtion?
:STATe {OFF|ON}
:STATe?

CALCulate
:AVERage:MINimum?
:AVERage:MAXimum?
:AVERage:AVERage?
:AVERage:COUNt?

CALCulate
:NULL:OFFSet {<value>|MINimum|MAXimum}
:NULL:OFFSet? [MINimum|MAXimum]

CALCulate
:DB:REFerence {<value>|MINimum|MAXimum}
:DB:REFerence? [MINimum|MAXimum]

CALCulate
:DBM:REFerence {<value>|MINimum|MAXimum}
:DBM:REFerence? [MINimum|MAXimum]

CALCulate
:LIMit:LOWer {<value>|MINimum|MAXimum}
:LIMit:LOWer? [MINimum|MAXimum]
:LIMit:UPPer {<value>|MINimum|MAXimum}
:LIMit:UPPer? [MINimum|MAXimum]
DATA:FEED RDG_STORE, {"CALCulate"|""}
DATA:FEED?

INITiate

READ?

TRIGger
:SOURce {BUS|IMMediate |EXTernal}
:SOURce?

TRIGger
:DELay {<seconds>|MINimum|MAXimum}
:DELay? [MINimum|MAXimum]

TRIGger
:DELay:AUTO {OFF|ON}
:DELay:AUTO?

SAMPle
:COUNt {<value>|MINimum|MAXimum}
:COUNt? [MINimum|MAXimum]

TRIGger
:COUNt {<value>|MINimum|MAXimum|INFinite}
:COUNt? [MINimum|MAXimum]

FETCh? 
READ?
DISPlay {OFF|ON} 
DISPlay?

DISPlay
:TEXT <quoted string> 
:TEXT? 
:TEXT:CLEar

SYSTem
:BEEPer
:BEEPer:STATe {OFF|ON} 
:BEEPer:STATe?

SYSTem:ERRor?
SYSTem:VERSion?
DATA:POINts?
*RST
*TST?
*IDN?
L1
L2
L3

SYSTem:ERRor?

STATus
:QUEStionable:ENABle <enable value>
:QUEStionable:ENABle?
:QUEStionable:EVENt?

STATus:PRESet

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

CALibration?
CALibration:COUNt?

CALibration
:SECure:CODE <new code>
:SECure:STATe {OFF|ON},<code>
:SECure:STATe?

CALibration
:STRing <quoted string>
:STRing?

CALibration :VALue <value>

SYSTem:LOCal
SYSTem:REMote
SYSTem:RWLock

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
*SRE <enable value>
*SRE?
*STB?
*TRG
*TST?

```
