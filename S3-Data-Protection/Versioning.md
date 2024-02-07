## S3 Versioning

## Summary
- Amazon S3 offers industry-leading scalability, availability, durability, security, and performance for storing and protecting data of any size and type, serving millions of customers worldwide.
- Key factors driving the need for additional data protection services beyond S3's default durability include human error, malicious activities such as ransomware, and regional disruptions.
- S3 Versioning allows keeping multiple variants of objects in the same bucket, aiding in recovery from accidental deletion or overwrite, with lifecycle configurations enabling cost-efficient storage management.

## Step-by-step Guide to set up S3 Versioning
**1.Sign in to the AWS Management Console:**
- Log in to your AWS account and navigate to the Amazon S3 console.

**2. Select the Desired Bucket:**
- From the list of buckets, choose the one for which you want to enable versioning.

**3. Access Bucket Properties:**
- Click on the name of the bucket to access its properties.

**4. Navigate to the Versioning Settings:**
- Within the bucket properties, locate the "Properties" tab. Under this tab, you'll find the "Versioning" option. Click on it to access versioning settings.

**5. Enable Versioning:**
- In the versioning settings, you'll see a toggle switch labeled "Suspend versioning" or "Enable versioning." By default, versioning is suspended. Click on the toggle to enable versioning for the bucket.

**6. Confirm Versioning Configuration:** 
- After enabling versioning, a dialog box or confirmation message may appear. Review the details to ensure that you're enabling versioning as intended.

**7. Apply Changes:**
- Once you're satisfied with the versioning configuration, confirm the changes to apply them to the bucket.

**8. Verify Versioning Status:**
- After applying the changes, ensure that versioning is now enabled for the selected bucket. You should see an indication that versioning is active for the bucket.

**9. Upload Objects:**
- Begin uploading objects to the bucket as usual. Each time you upload a new object or modify an existing one, Amazon S3 automatically creates a new version of that object.

**10. Manage Object Versions:**
- To view and manage object versions, navigate to the bucket in the S3 console and access the "Versions" tab. Here, you can see all versions of objects stored in the bucket, including the current and previous versions.

**11. Perform Operations on Object Versions:**
- From the "Versions" tab, you can perform various actions on object versions, such as downloading specific versions, restoring previous versions, or permanently deleting unwanted versions.

**12. Utilize Lifecycle Policies:**
- To optimize storage and lifecycle management, consider implementing lifecycle policies for the bucket. These policies can automatically transition objects to different storage classes or expire them based on predefined rules.

## Key commands to use S3 Versioning
*Bash*
### Enable Versioning:
- aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled
### Suspend Versioning:
- aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Suspended
### List object versions:
- aws s3api list-object-versions --bucket your-bucket-name
### Restore Object Version:
- aws s3api restore-object --bucket your-bucket-name --key your-object-key --version-id your-version-id
### Delete Specific Object Version:
aws s3api delete-object --bucket your-bucket-name --key your-object-key --version-id your-version-id
### Delete All Object Versions (Including Delete Markers):
- aws s3api delete-objects --bucket your-bucket-name --delete "$(aws s3api list-object-versions --bucket your-bucket-name --output json --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
### Enable MFA Delete (Multi-Factor Authentication):
- aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled,MFADelete=Enabled,MFADelete=your-mfa-serial, MFADelete=your-mfa-token

## Discription and Commands
| Command                         | Description                                       |
|---------------------------------|---------------------------------------------------|
| `aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled` | Enable versioning for a bucket |
| `aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Suspended` | Suspend versioning for a bucket |
| `aws s3api list-object-versions --bucket your-bucket-name` | List object versions in a bucket |
| `aws s3api restore-object --bucket your-bucket-name --key your-object-key --version-id your-version-id` | Restore a specific object version |
| `aws s3api delete-object --bucket your-bucket-name --key your-object-key --version-id your-version-id` | Delete a specific object version |
| `aws s3api delete-objects --bucket your-bucket-name --delete "$(aws s3api list-object-versions --bucket your-bucket-name --output json --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')" ` | Delete all object versions (including delete markers) |
| `aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled,MFADelete=Enabled,MFADelete=your-mfa-serial, MFADelete=your-mfa-token` | Enable MFA Delete for versioned objects |