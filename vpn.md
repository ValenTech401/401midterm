AWS-VPN

<img width="617" alt="Screenshot 2024-02-06 at 12 16 04 PM" src="https://github.com/ValenTech401/401midterm/assets/143548087/6a0f28fd-8579-4750-bac4-d82e78283a7e">

First: Create a separate VPC for the Corporate Data Center to represent Corporate (in a different Region will keep things organized)

I chose to create 2 Instances in California Region, with their separate VPC

Instance 1: is AWS LInux (this will be the server that runs openswan-ipsec)
Instance 2: is any device of your choosing to be the instance that will route to the AWS Linux Openswan>> and openswan will go to the EC2 Instance in the AWS Account (Virginia Region) 

Instance 1:
<img width="1414" alt="Screenshot 2024-02-08 at 9 01 20 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/a38cf85d-1e65-4d1d-8ed6-50a81e7ee349">

Instance 2:
<img width="1427" alt="Screenshot 2024-02-08 at 9 02 22 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/5a89c7be-0cae-46d1-9041-d3ed6c463f9f">

You will need the Public IPv4 Address from instance 1 for the VPN

Because Instance 1 is forwarding connections you need to turn off the source destination checks  off

<img width="1426" alt="Screenshot 2024-02-08 at 9 03 33 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/2eaadfa3-47c7-4001-9fa7-d5d576f41765">

<img width="1235" alt="Screenshot 2024-02-08 at 9 04 19 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/b7b04e4a-5647-4af7-823f-0875393b54d6">
<img width="1421" alt="Screenshot 2024-02-08 at 9 09 10 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/edf62110-720a-49f6-ab72-a4bbe929f681">

Instance 1 Public IP: 54.151.51.91

I already have a VPC and an Instance created with 10.0.0.0/16

<img width="1423" alt="Screenshot 2024-02-08 at 9 06 16 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/e2460af3-c24b-4b3a-8710-47da0ec76bcc">

<img width="1418" alt="Screenshot 2024-02-08 at 9 05 28 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/f4c7fa55-7772-4744-9ca9-1709b5a1a3cb">

<img width="1418" alt="Screenshot 2024-02-08 at 9 07 01 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/bd3c2578-422b-451a-862d-14e600db056f">


<img width="206" alt="Screenshot 2024-02-07 at 8 40 37 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/f41b798d-9523-422b-8b94-ab894e8240cd">

This is where  you put the Public IP of the Instance 1: on the california side

<img width="1420" alt="Screenshot 2024-02-08 at 9 10 59 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/c38fac5f-fd11-474c-b841-c9a674660861">

Now create Virtual Private Gateway

<img width="1424" alt="Screenshot 2024-02-08 at 9 12 21 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/482d8060-1cd9-4d8f-bcf0-eb3a12c5c7ca">

<img width="777" alt="Screenshot 2024-02-07 at 8 45 23 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/9317d8a5-3108-4155-a13f-4d90066299fb">


Attach the Virtual Private Gateway to the VPC with 10.0.0.0/16 (the AWS Account side)

<img width="1720"<img width="756" alt="Screenshot 2024-02-07 at 8 50 59 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/b9543d89-3390-47eb-9bcf-107f337c8230">
 
<img width="1694" alt="Screenshot 2024-02-07 at 8 50 02 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/fbc65d5e-6b47-4755-be7d-4b292a250bf8">

Now create site-to-site

<img width="741" alt="Screenshot 2024-02-07 at 8 47 09 AM" src="https://github.com/ValenTech401/401midterm/assets/143548087/533250e4-f9c6-4806-a816-0d6f8754afb0">

This is where you add the Customer gateway and the virtual gateway







































































































