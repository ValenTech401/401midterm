# Script Name:                  Server Hardening with CIS Standards
# Author:                       Eve Campos
# Date of latest revision:      6FEB2024      
# Purpose:                      Automate the configuration of Windows Server 2019 on AWS EC2 to meet CIS Benchmarks 1.1.5(L1) and 18.4.3(L1)

# Configure 'Password must meet complexity requirements' (Benchmark 1.1.5 L1)
# Enabling this setting requires passwords to contain characters from three of five categories: 
# Uppercase characters, Lowercase characters, Base 10 digits, Non-alphabetic characters, Unicode characters.
$secConfigPath = "C:\SecConfig.cfg"
secedit /export /cfg $secConfigPath
(Get-Content -path $secConfigPath).Replace("PasswordComplexity=0", "PasswordComplexity=1") | Set-Content -Path $secConfigPath
secedit /configure /db "C:\Windows\security\local.sdb" /cfg $secConfigPath /areas SECURITYPOLICY

# Disable SMB v1 server to comply with CIS Benchmark 18.4.3 (L1)
# This setting disables the older SMBv1 protocol which is less secure.
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

# Cleanup
Remove-Item -Path $secConfigPath

# Output result
Write-Host "CIS Benchmark configurations for 1.1.5(L1) and 18.4.3(L1) applied."


# Resources
# This script was improved with assistance from ChatGPT, OpenAI's language model and a fellow classmates; Renona G. Eveangalina C. 