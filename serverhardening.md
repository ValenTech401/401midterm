### The script automates the hardening of a Windows Server 2019 system to meet specific CIS Benchmarks. It performs the following actions:

<u>Configures Password Complexity:</u> <br/>
It exports the current security settings to a file named *SecConfig.cfg*. <br/>
It modifies the *SecConfig.cfg* file to require that passwords meet complexity requirements. <br/>
It applies the new security settings from the modified *SecConfig.cfg* file to the system.

<u> Disables SMBv1 Protocol:</u> <br/>
It disables SMB version 1, which is an outdated and less secure protocol.

<u>Cleans Up:</u> <br/>
It removes the *SecConfig.cfg* file after the configurations are applied.

<u>Outputs Result:</u> <br/>
It prints a message indicating that the CIS Benchmark configurations have been applied.

---
### Center for Internet Security (CIS) <br/>Benchmarks and their respective purposes:

**CIS Benchmark 1.1.5 (Level 1)** - <br/> "Password must meet complexity requirements":<br/>
<u>Purpose:</u> This setting ensures that all user account passwords meet certain complexity requirements, making them more resistant to brute-force and guessing attacks. The complexity requirements typically include a mix of uppercase letters, lowercase letters, digits, and non-alphabetic characters.

**CIS Benchmark 18.4.3 (Level 1)** - <br/> "Disable SMB v1 server":<br/>
<u>Purpose:</u> This disables the Server Message Block (SMB) version 1 protocol on the server. SMBv1 is an older protocol that has been superseded by newer versions (SMBv2 and SMBv3) and is known to have significant security vulnerabilities, including being exploited by ransomware attacks like WannaCry. Disabling SMBv1 helps protect against these vulnerabilities and encourages the use of more secure SMB versions.

#### Resources <br/>
[CIS Benchmarks](https://www.ibm.com/cloud/learn/cis-benchmarks)