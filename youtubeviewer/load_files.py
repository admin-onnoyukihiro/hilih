# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IiIiCk1JVCBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIDIwMjEtMjAyMyBNU2hhd29uCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHB'
love = 'ypz1cp3Aco24toz90nJAyVUAbLJkfVTWyVTyhL2k1MTIxVTyhVTSfoNcwo3OcMKZto3Vtp3Ivp3EuoaEcLJjtpT9lqTyioaZto2LtqTuyVSAiMaE3LKWyYtbXIRuSVSACEyEKDIWSVRyGVSOFG1MWERIRVPWOHlOWHlVfVSqWIRuCIIDtI0SFHxSBISxtG0LtDH5MVRgWGxDfVRILHSWSH1ZtG1VXFH1DGRySEPjtFH5QGSIRFH5UVRWIIPOBG1DtGRyAFIESEPOHGlOHFRHtI0SFHxSBIRySHlOCEvOAEIWQFRSBIRSPFHkWISxfPxMWIR5SH1ZtEx9FVRRtHRSFIRyQIHkOHvODIIWDG1ASVRSBEPOBG05WGxMFFH5UEH1SGyDhVRyBVR5CVRIJEH5HVSAVDHkZVSEVEDcOIIEVG1WGVR9FVRACHSyFFHqVIPOVG0kREIWGVRWSVRkWDHWZEFOTG1VtDH5MVRAZDHyAYPORDH1OE0IGVR9FVR9HFRIFPxkWDHWWGRyHJFjtI0uSIRuSHvOWGvOOGvOOD1EWG04tG0LtD09BISWOD1DfVSECHyDtG1VtG1EVEIWKFIASYPOOHxyGFH5UVRMFG00fPx9IIPOCEvOCHvOWGvOQG05BEHAHFH9BVSqWIRttIRuSVSACEyEKDIWSVR9FVSEVEFOIH0HtG1VtG1'
god = 'RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgoiIiIKaW1wb3J0IGhhc2hsaWIKZnJvbSByYW5kb20gaW1wb3J0IGNob2ljZXMKCmZyb20gLmNvbG9ycyBpbXBvcnQgKgoKCmRlZiBsb2FkX3VybCgpOgogICAgcHJpbnQoYmNvbG9ycy5XQVJOSU5HICsgJ0xvYWRpbmcgdXJscy4uLicgKyBiY29sb3JzLkVOREMpCgogICAgd2l0aCBvcGVuKCd1cmxzLnR4dCcsIGVuY29kaW5nPSJ1dGYtOCIpIGFzIGZoOgogICAgICAgIGxpbmtzID0gW3guc3RyaXAoKSBmb3IgeCBpbiBmaCBpZiB4LnN0cmlwKCkgIT0gJyddCgogICAgcHJpbnQoYmNvbG9ycy5PS0dSRUVOICsKICAgICAgICAgIGYne2xlbihsaW5rcyl9IHVybCBsb2FkZWQgZnJvbSB1cmxzLnR4dCcgKyBiY29sb3JzLkVOREMpCgogICAgbGlua3MgPSBjaG9pY2VzKGxpbmtzLCBrPWxlbihsaW5rcykqMykgKyBsaW5rcwoKICAgIHJldHVybiBsaW5rcwoKCmRlZiBsb2FkX3NlYXJjaCgpOgogICAgcHJpbnQoYmNvbG9ycy5XQVJOSU5HICsgJ0xvYWRpbmcgcXVlcmllc'
destiny = 'l4hYvptXlOvL29fo3WmYxIBERZcPtbtVPNtq2y0nPOipTIhXPqmMJSlL2thqUu0WljtMJ5wo2Ecozp9VaI0Mv04VvxtLKZtMzt6PvNtVPNtVPNtp2IupzAbVQ0tJ1g5YaA0pzyjXPxtMz9lVUxtnJ4trP5mqUWcpPtcYaAjoTy0XPp6Bwb6WlyqPvNtVPNtVPNtVPNtVPNtVPNtVTMipvO4VTyhVTMbVTyzVUthp3ElnKNbXFNuCFNaWlOuozDtWmb6BwbaVTyhVUuqPtbtVPNtpUWcoaDbLzAioT9lpl5CF0qFEHIBVPfXVPNtVPNtVPNtVTLar2kyovumMJSlL2tcsFOkqJIlrFOfo2SxMJDtMaWioFOmMJSlL2thqUu0WlNeVTWwo2kipaZhEH5RDlxXPvNtVPOmMJSlL2ttCFOwnT9cL2ImXUAyLKWwnPjtnm1fMJ4bp2IupzAbXFbmXFNeVUAyLKWwnNbtVPNtPvNtVPOlMKE1pz4tp2IupzAbPtbXMTIzVTqyqS9bLKAbXUOuqTtcBtbtVPNtq2y0nPOipTIhXUOuqTtfVPWlLvVcVTSmVTL6PvNtVPNtVPNtL3IlpzIhqS9bLKAbVQ0tnTSmnTkcLv5gMQHbMv5lMJSxXPxcYzuyrTEcM2ImqPtcPtbtVPNtpzI0qKWhVTA1paWyoaEsnTSmnNb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
