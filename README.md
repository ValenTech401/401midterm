[Live Presentation](https://zoom.us/rec/play/LAI77hH4n9caRHIClLV6vylRx9qqcfbg0CFZOQf3Cu7a1CXxjm4rtsHrwGtaASSGx3b9jT6OfnhVLphT.pPk3I5jEEFUKLq5I?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2Faz5xZmPAKiFoszWkyzIjuR-6Gk_cQoI_VL9tuCRKP7fyuJD32paudEW4-XyDuFOV.u43SOVq5zfzZZere)
# Here is the ValenTech Midterm Project

### Devs

- [Andrew Carroll](https://github.com/iAmAndrewCarroll)
- [Eveangalina Campos](https://github.com/Eveangalina)
- [Christen Reinhart](https://github.com/christen-reinhart)
- [Nathalie Abdallah](https://github.com/nataliabdallah)
- [Renona Gay]()
- [Scotty Jokon](https://github.com/SteezyLoh)

### Project Description

Your team has been contracted to improve the cybersecurity processes and systems for a client company, focusing on logging, monitoring, and detection of adversarial activity on cloud infrastructure in AWS Cloud. The client has requested demonstrations of secure IAM practices, server hardening, data protection, SIEM/log aggregation system configurations, and cloud monitoring techniques to protect their cloud infrastructure.

- **Project Breakdown:**
  - Your team has been contracted to improve the cybersecurity processes and systems for a client company.
  - The focus is on logging, monitoring, and detection of adversarial activity on cloud infrastructure in AWS Cloud.

- **Client Requested Demonstrations:**
  - Secure IAM practices
  - Server hardening
  - Data protection
  - SIEM/log aggregation system configurations
  - Cloud monitoring techniques

- **Objective:**
  - Protect the client's cloud infrastructure by demonstrating and implementing the above security practices and configurations.

### Project Management Tool

- Checkout the milestones, MVPs, and other project related progress here
- [GitHub Project](https://trello.com/b/3tjWW9Ub/201-group-project)

### Client Pitch

We are thrilled to have the opportunity to collaborate with you on this vital project. Our team has been specifically contracted to elevate the cybersecurity landscape of your AWS Cloud infrastructure. Our focus is on fortifying your systems against adversarial activities through comprehensive logging, meticulous monitoring, and proactive detection strategies. Our approach is threefold:

1. **IAM Best Practices:** Ensuring the principle of least privilege is adhered to.

2. **Infrastructure Hardening and Monitoring:**
   - Deployment of Sysmon for monitoring.
   - Hardening includes taking CIS-compliant Windows Server DC within a private subnet of your VPC, accessible only through VPN tunneling.
   - Linux server instance will be meticulously configured to house your sensitive PII and PCI data, with encryption both at rest and in transit.

3. **SIEM/Log Aggregation:**
   - Utilizing top-tier CloudWatch, we will configure a real-time event log ingestion system from key assets, including EC2 instances.
   - This will enable us to swiftly identify and mitigate threats, ensuring continuous protection.

To top it off, we will implement **Cloud Monitoring with AWS Lambda.** Our strategy extends to leveraging VPC Flow Logs to monitor network traffic meticulously. AWS Lambda functions will be employed to automate responses to detect threats.

We are eager to embark on this journey with you, safeguarding your digital assets and fostering a secure cloud environment. Thank you for considering our team for this crucial initiative.

### Tools & Solutions

| Aspect                          | System/Platform/Tool | How it Fits into Scenario                          | Solution to Scenario                                        |
|---------------------------------|-----------------------|----------------------------------------------------|-------------------------------------------------------------|
| 1. Company organization and policies | AWS-IAM               | Implement best practices for secure access management | Create security rules, groups, and policies                   |
| 2. VPN Setup                     | AWS-VPC (VPN site-to-site) | Sets up a secure site-to-site VPN tunnel              | Provides Windows-Centric solution for secure access via VPN  |
| 3. Server Hardening              | EC2 Instance: Windows Server DC | CIS-compliant, hosted on a private subnet, accessible via VPN tunneling | Provides a secure server for operations and hardening     |
| 4. Data Protection               | AWS-KMS               | Encrypts data at rest and in transit. Deploy Sysmon for security-relevant system logs | Ensures data encryption at rest and in transit             |
| 5. CIS compliant Data Server      | EC2 Instance: Linux Server | Contains PII and PCI data, with data encrypted at rest and in transit | Secure storage for PII and PCI data                        |
| 6. SIEM/Log aggregation          | AWS-CloudWatch/CloudTrail/Sysmon/Splunk | Configured to ingest event logs in real time from key assets including EC2 instances | Real-time monitoring and alerting of AWS activity         |
| 7. Cloud Monitoring               | AWS-Lambda           | Utilize VPC Flow Logs for capturing traffic. Implement an AWS Lambda function to trigger relevant responses to detected threats, fulfilling the requirement for a shell script | Interact with CloudWatch through scripting language for monitoring |


### SOPs

- All SOPs will be worked on and committed as Markdown Files.  
- All images will be .png file types
- Project SOPs related to Space Pirate Industries can be found [here](sop.md)

### Slide Deck

- [ValenTech Slide Deck](https://docs.google.com/presentation/d/1kU41nfRd3NGU-itEinPWKOvGyyLmnkbF5OAuA6VdIgU/edit#slide=id.g2a928df11dc_1_0)

### Topology

<img width="1459" alt="Screenshot 2024-02-08 at 8 43 42 PM" src="https://github.com/ValenTech401/401midterm/assets/143548087/9a8de8ac-4998-4d99-868d-108c87bdc8d8">
