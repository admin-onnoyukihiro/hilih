# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IiIiCk1JVCBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIDIwMjEtMjAyMyBNU2hhd29uCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb'
love = '2LtqTuyVSAiMaE3LKWyYtbXIRuSVSACEyEKDIWSVRyGVSOFG1MWERIRVPWOHlOWHlVfVSqWIRuCIIDtI0SFHxSBISxtG0LtDH5MVRgWGxDfVRILHSWSH1ZtG1VXFH1DGRySEPjtFH5QGSIRFH5UVRWIIPOBG1DtGRyAFIESEPOHGlOHFRHtI0SFHxSBIRySHlOCEvOAEIWQFRSBIRSPFHkWISxfPxMWIR5SH1ZtEx9FVRRtHRSFIRyQIHkOHvODIIWDG1ASVRSBEPOBG05WGxMFFH5UEH1SGyDhVRyBVR5CVRIJEH5HVSAVDHkZVSEVEDcOIIEVG1WGVR9FVRACHSyFFHqVIPOVG0kREIWGVRWSVRkWDHWZEFOTG1VtDH5MVRAZDHyAYPORDH1OE0IGVR9FVR9HFRIFPxkWDHWWGRyHJFjtI0uSIRuSHvOWGvOOGvOOD1EWG04tG0LtD09BISWOD1DfVSECHyDtG1VtG1EVEIWKFIASYPOOHxyGFH5UVRMFG00fPx9IIPOCEvOCHvOWGvOQG05BEHAHFH9BVSqWIRttIRuSVSACEyEKDIWSVR9FVSEVEFOIH0HtG1VtG1EVEIVtERIOGRyBE1ZtFH4tIRuSPyACEyEKDIWSYtbvVvVXnJ1jo3W0VT9mPzygpT9lqPOmnUI0nJjXnJ1jo3W0VUAkoTy0MGZXMaWioFOwo250MKu0oTyvVTygpT9lqPOwoT9mnJ5aPzMlo20tMTS0MKEcoJHtnJ1jo3W0VTEuqTI0nJ1yPtbXMTIzVTAlMJS0MI'
god = '9kYXRhYmFzZShkYXRhYmFzZSwgZGF0YWJhc2VfYmFja3VwKToKICAgIHdpdGggY2xvc2luZyhzcWxpdGUzLmNvbm5lY3QoZGF0YWJhc2UpKSBhcyBjb25uZWN0aW9uOgogICAgICAgIHdpdGggY2xvc2luZyhjb25uZWN0aW9uLmN1cnNvcigpKSBhcyBjdXJzb3I6CiAgICAgICAgICAgIGN1cnNvci5leGVjdXRlKCIiIkNSRUFURSBUQUJMRSBJRiBOT1QgRVhJU1RTCiAgICAgICAgICAgIHN0YXRpc3RpY3MgKGRhdGUgVEVYVCwgdmlldyBJTlRFR0VSKSIiIikKCiAgICAgICAgICAgIGNvbm5lY3Rpb24uY29tbWl0KCkKCiAgICB0cnk6CiAgICAgICAgb3MucmVtb3ZlKGRhdGFiYXNlX2JhY2t1cCkKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcGFzcwoKICAgIHRyeToKICAgICAgICBzaHV0aWwuY29weShkYXRhYmFzZSwgZGF0YWJhc2VfYmFja3VwKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwYXNzCgoKZGVmIHVwZGF0ZV9kYXRhYmFzZShkYXRhYmFzZSwgdGhyZWFkcywgaW5jcmVtZW50PTEpOgogICAgdG9kYXkgPSBzdHIoZGF0ZXRpbWUudG9kYXkoKS5kYXRlKCkpCiAgICB3aXRoIGNsb3Npbmcoc3FsaXRlMy5jb25uZWN0KGR'
destiny = 'uqTSvLKAyYPO0nJ1yo3I0CKEbpzIuMUZdZGNcXFOuplOwo25hMJA0nJ9hBtbtVPNtVPNtVUqcqTttL2kip2yhMluwo25hMJA0nJ9hYzA1paAipvtcXFOuplOwqKWmo3V6PvNtVPNtVPNtVPNtVUElrGbXVPNtVPNtVPNtVPNtVPNtVTA1paAipv5yrTIwqKEyXNbtVPNtVPNtVPNtVPNtVPNtVPNtVPWGEHkSD1DtqzyyqlOTHx9AVUA0LKEcp3EcL3ZtI0uSHxHtMTS0MFN9VQ8vYPNbqT9xLKxfXFxXVPNtVPNtVPNtVPNtVPNtVUOlMKMco3ImK2AiqJ50VQ0tL3Ilp29lYzMyqTAbo25yXPyoZS0XVPNtVPNtVPNtVPNtVPNtVTA1paAipv5yrTIwqKEyXPWIHREOIRHtp3EuqTymqTywplOGEIDtqzyyqlN9VQ8tI0uSHxHtMTS0MFN9VQ8vYNbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtXUOlMKMco3ImK2AiqJ50VPftnJ5wpzIgMJ50YPO0o2EurFxcPvNtVPNtVPNtVPNtVTI4L2IjqPOSrTAypUEco246PvNtVPNtVPNtVPNtVPNtVPOwqKWmo3VhMKuyL3I0MFtXVPNtVPNtVPNtVPNtVPNtVPNtVPNvFH5GEIWHVRyBIR8tp3EuqTymqTywplOJDHkIEIZtXQ8fVQ8cVvjtXUEiMTS5YPNjXFjcPtbtVPNtVPNtVPNtVPOwo25hMJA0nJ9hYzAioJ1cqPtcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))