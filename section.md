## [6.1](#6.1)
6.1 Ensure that all system components and software are protected from known vulnerabilities by having the latest vendor-supplied security patches installed. Install critical security patches within one month of release.  Note: An organization may consider applying a risk-based approach to  prioritize their patch installations. For example, by prioritizing critical infrastructure (for example, public-facing devices and systems, databases) higher than less-critical internal devices, to ensure high-priority systems and devices are addressed within one month, and addressing less critical devices and  z 
## [6.1.a](#6.1.a)
6.1.a For a sample of system components and related software, compare the list of security patches installed on each system to the most recent vendor security patch list, to verify that current vendor patches are installed. 
## [6.2](#6.2)
6.2 Establish a process to identify and assign a risk ranking to newly discovered security vulnerabilities.  Notes: ' Risk rankings should be based on  industry best practices. For example, criteria for ranking —High|l risk vulnerabilities may include a CVSS base score of4.0 or above, and/or a vendor-supplied patch classified by the vendor as —criticaI,|l and/or a vulnerability affecting a critical system component.  ' The ranking of vulnerabilities as defined in 6.2.a is considered a best practice until June 30, 2012, after which it becomes a requirement. 
## [6.2).](#6.2).)
6.2).  Note: This requirement is considered a best practice until June 30, 2012, after  which it becomes a reuirement   
## [6.2.a](#6.2.a)
6.2.a Interview responsible personnel to verify that processes are  implemented to identify new security vulnerabilities, and that a risk ranking is assigned to such vulnerabilities. (At minimum, the most  critical, highest risk vulnerabilities should be ranked as —High.|| 
## [6.3.1](#6.3.1)
6.3.1 Custom application accounts, user IDs and/or passwords are removed before system goes into production or is released to customers. 
## [6.3.1](#6.3.1)
6.3.1 Removal of custom application accounts, user IDs, and passwords before applications become active or are released to customers 
## [6.3.2](#6.3.2)
6.3.2 Review of custom code prior to release to production or customers in order to identify any potential coding vulnerability.  Note: This requirement for code reviews applies to all custom code  (both internal and public-facing), as part of the system development life cycle.  Code reviews can be conducted by knowledgeable internal personnel or third parties. Web applications are also subject to additional controls, if they are public facing, to address ongoing threats and vulnerabilities after implementation, as defined at PCI DSS  Reguirement 6.6.
## [6.3.2.a](#6.3.2.a)
6.3.2.a Obtain and review policies to confirm that all custom application code changes must be reviewed (using either manual or automated processes) as follows:  I Code changes are reviewed by individuals other than the originating code author, and by individuals who are knowledgeable in code review techniques and secure coding practices.  I Code reviews ensure code is developed according to secure coding guidelines (see PCI DSS Requirement 6.5).  I Appropriate corrections are implemented prior to release.  I Code review results are reviewed and approved by management prior to release. 
## [6.3.2.a,](#6.3.2.a,)
6.3.2.a, above. 
## [6.3.a](#6.3.a)
6.3.a Obtain and examine written software development processes to verify that the processes are based on industry standards and/or best practices. 
## [6.3.c](#6.3.c)
6.3.c Examine written software development processes to verify that software applications are developed in accordance with PCI DSS. 
## [6.4.1](#6.4.1)
6.4.1 Separate development/test and production environments 
## [6.4.1](#6.4.1)
6.4.1 The development/test environments are separate from the production environment, with access control in place to enforce the separation. 
## [6.4.3](#6.4.3)
6.4.3 Production data (live PANs) are not used for testing or development 
## [6.4.3](#6.4.3)
6.4.3 Production data (live PANs) are not used for testing or development. 
## [6.4.5](#6.4.5)
6.4.5 Change control procedures for the implementation of security patches and software modifications. Procedures must include the following: 
## [6.4.5.1](#6.4.5.1)
6.4.5.1 Verify that documentation of impact is included in the change control documentation for each sampled change. 
## [6.4.5.2](#6.4.5.2)
6.4.5.2 Documented change approval by authorized parties. 
## [6.4.5.3.a](#6.4.5.3.a)
6.4.5.3.a For each sampled change, verify that functionality testing is performed to verify that the change does not adversely impact the security of the system. 
## [6.4.5.4](#6.4.5.4)
6.4.5.4 Back-o ut procedures. 
## [6.4.5.4](#6.4.5.4)
6.4.5.4 Verify that back-out procedures are prepared for each sampled change. 
## [6.4.5.a](#6.4.5.a)
6.4.5.a Verify that change-control procedures related to implementing security patches and software modifications are documented and require items 6.4.5.1 — 6.4.5.4 below. 
## [6.5.1](#6.5.1)
6.5.1 Injection flaws, particularly SQL injection. Also consider OS Command Injection, LDAP and XPath injection flaws as well as other injection flaws. 
## [6.5.1](#6.5.1)
6.5.1 Injection flaws, particularly SQL injection. (Validate input to verify user data cannot modify meaning of commands and queries, utilize parameterized queries, etc.)           
## [6.5.3](#6.5.3)
6.5.3 Insecure cryptographic storage
## [6.5.3](#6.5.3)
6.5.3 Insecure cryptographic storage (Prevent cryptographic flaws)   
## [6.5.5](#6.5.5)
6.5.5 Improper error handling 
## [6.5.5](#6.5.5)
6.5.5 Improper error handling (Do not leak information via error messages) 
## [6.5.7](#6.5.7)
6.5.7 Cross-site scripting (XSS) (Validate all parameters before inclusion, utilize context-sensitive escaping, etc.) 
## [6.5.8](#6.5.8)
6.5.8 Improper Access Control (such as insecure direct object references, failure to restrict URL access, and directory traversal) 
## [6.5.9](#6.5.9)
6.5.9 Cross-site request forgery (CSRF). (Do not reply on authorization credentials and tokens automatically submitted by browsers.) 
## [6.5.b](#6.5.b)
6.5.b Interview a sample of developers and obtain evidence that they are knowledgeable in secure coding techniques. 
## [6.6](#6.6)
6.6 For public-facing web applications, address new threats and vulnerabilities on an ongoing basis and ensure these applications are protected against known attacks by either of the following methods:  I Reviewing public-facing web applications via manual or automated application vulnerability security assessment tools or methods, at least annually and after any changes  I Installing a web-application firewall in  front of public-facing web applications 
## [6.6](#6.6)
6.6 For public-facing web applications, ensure that either one of the following methods are in place as follows:  ' Verify that public-facing web applications are reviewed (using either manual or automated vulnerability security assessment  tools or methods), as follows:  — At least annually  — After any changes  — By an organization that specializes in application security — That all vulnerabilities are corrected  — That the application is re-evaluated after the corrections  I Verify that a web-application firewall is in place in front of public-facing web applications to detect and prevent web-based attacks.  N°te:—An organization that specializes in application  securityll can be eithera thirdpany company or an  internal organization, as long as the reviewers specialize  in application security and can demonstrate independence from the 
