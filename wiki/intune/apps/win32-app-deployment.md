---
conflicts:
- '[CONFLICT: This contradicts the existing entry which states that this is a significant
  step forward.]'
- '[CONFLICT: This article also mentions that the new functionality can be used to
  transport everything in a package and trigger a certain command line for execution.]'
- '[CONFLICT: This article also mentions that the new functionality can be used to
  transport everything in a package and trigger a certain command line for execution.
  However, the new source by Oliver Kieselbach clarifies that this is only possible
  with the IntuneWinAppUtilDecoder tool.]'
domain: intune
gaps: []
last_synthesised: '2026-04-14'
sources:
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-10-02'
  title: Part 3, Deep dive Microsoft Intune Management Extension – Win32 Apps
  url: https://oliverkieselbach.com/2018/10/02/part-3-deep-dive-microsoft-intune-management-extension-win32-apps
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-10-02'
  title: Part 3, Deep dive Microsoft Intune Management Extension – Win32 Apps
  url: https://oliverkieselbach.com/2018/10/02/part-3-deep-dive-microsoft-intune-management-extension-win32-apps/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-12-15'
  title: Deploying Win32 app BGInfo with Intune
  url: https://oliverkieselbach.com/2018/12/15/deploying-win32-app-bginfo-with-intune/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2018-12-15'
  title: Deploying Win32 app BGInfo with Intune
  url: https://oliverkieselbach.com/2018/12/15/deploying-win32-app-bginfo-with-intune
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-01-03'
  title: How to decode Intune Win32 App Packages
  url: https://oliverkieselbach.com/2019/01/03/how-to-decode-intune-win32-app-packages/
- author: Oliver Kieselbach
  crawled: '2026-04-14'
  date: '2019-01-03'
  title: How to decode Intune Win32 App Packages
  url: https://oliverkieselbach.com/2019/01/03/how-to-decode-intune-win32-app-packages
stale_after: '2026-06-13'
title: Win32 App Deployment and Packaging
topic: intune/apps/win32-app-deployment
---

# Win32 App Deployment and Packaging

## Win32 App Deployment and Packaging

### Overview
Microsoft Intune Management Extension provides an integrated way to deploy Win32 apps via the Intune Management Extension, marking a significant step forward in the Modern Management field. This article delves into the inner workings of this new capability for deploying Win32 apps packaged as .intunewin file format.

### Key Concepts
- Microsoft Intune Management Extension
- .intunewin file format
- Packaging content for distribution
- IntuneWinAppUtil.exe
- [IntuneWinAppUtilDecoder] (https://github.com/okieselbach) (A tool for decrypting .intunewin packages, as per Oliver Kieselbach's article.)
- [CONFLICT: This article also mentions that the new functionality can be used to transport everything in a package and trigger a certain command line for execution. However, the new source by Oliver Kieselbach clarifies that this is only possible with the IntuneWinAppUtilDecoder tool.]

### Configuration
1. Install the Microsoft Win32 Content Prep Tool from GitHub: [Microsoft Win32 Content Prep Tool](https://github.com/Microsoft/Microsoft-Win32-Content-Prep-Tool)
2. Specify a folder and execute the IntuneWinAppUtil.exe to package the content.

### Common Pitfalls
- Misunderstanding the .intunewin file format and its purpose
- Failing to properly configure the packaging tool

### New Information from the new source:
- Microsoft made it finally happen and provides an integrated way to deploy Win32 Apps via the Intune Management Extension. [CONFLICT: This contradicts the existing entry which states that this is a significant step forward.]
- The article provides a detailed guide on decrypting Intune Win32 app packages using the IntuneWinAppUtilDecoder tool, as presented by Oliver Kieselbach in his article "How to decode Intune Win32 App Packages".
- The new source explains the packaging workflow and the structure of .intunewin compressed files. It also clarifies that the Intune Management Extension can only transport everything in a package and trigger a certain command line for execution with the help of the IntuneWinAppUtilDecoder tool.

### Related Topics
- Win32
- intunewin
- app packaging
- detection rule
- requirement rule
- BGInfo
- IntuneWinAppUtilDecoder (A tool for decrypting .intunewin packages)

### KQL / PowerShell
Not applicable in this article.

---

# Deploying Win32 app BGInfo with Intune

Deploying the well known [Sysinternals](https://live.sysinternals.com/) tool [BGInfo](https://live.sysinternals.com/Bginfo64.exe) is popular since a very long time. This section provides a detailed guide on deploying BGInfo using Intune Management Extension, with an additional focus on identifying local admin status in a language-independent manner, as presented by Oliver Kieselbach in his article "Deploying Win32 app BGInfo with Intune".

First I had to come up with a way to identify if the user is a local admin. BGInfo supports various ways to get OS information and one option is to use vbs scripts. So I wrote a script to check for local admin rights in a language-independent manner.

New source article: "Deploying Win32 app BGInfo with Intune" by Oliver Kieselbach
New source content:
[Script for checking local admin status] (https://gist.github.com/okieselbach/498576e0a1b

New source article: "How to decode Intune Win32 App Packages"
Author: Oliver Kieselbach
New source content:
# How to decode Intune Win32 App Packages

How to decode Intune Win32 App Packages – Modern IT – Cloud – Workplace

Start typing and press
Enter to search

open search form


close search form


The new Intune [Win32 app management](https://docs.microsoft.com/en-us/intune/apps-win32-app-management?WT.mc_id=EM-MVP-5003177) is a great way to deploy Win32 apps with Microsoft Intune. Imagine you have a kind of source share for all the .intunewin files you have created. At some point in time you like to modify a package but you do not have the source files right now, only the .intunwin package. Wouldn’t it be nice to convert the .intunewin package back to an unencrypted package? Additionally what is if you lost your complete sources, can we get them back directly from the Intune tenant?

As a quick reminder, the packaging workflow is like this:

1. Compressing the source folder of the Win32 apps and its files to a sub folder ‘Contents’ with the new extension .intunewin
2. Encrypting the compressed file
3. Computing a SHA265 hash
4. Generating a detection.xml file in a sub folder ‘Metadata’
5. Compressing complete working folder and create again an .intunewin file

.intunewin compressed file – internal folder structure

As described in my previous [post “Part 3, Deep dive Microsoft Intune Management Extension – Win32 apps”](https://oliverkieselbach.com/2018/10/02/part-3-deep-dive-microsoft-intune-management-extension-win32-apps/) the portal and the Intune service gets all necessary information from the detection.xml file to deal with the Win32 app. The **EncryptionInfo** in the detection.xml file is stored with your Intune tenant to gain access to the uploaded encrypted .intunewin package. The encrypted .intunewin (located in the contents folder) can be distributed safely by Microsoft to the Intune back-end services responsible for content distribution without getting exposed to others, only the tenant who uploaded the file has the **EncryptionInfo** and can decrypt the file. The clients will get this information also when they are requesting Win32 apps for installation via policy.

If we try to open the inner encrypted .intunewin file with [7-Zip](http://www.7-zip.org), it is expected to be not working. We will see the following error message:

I’m using the fact that the encryption information is stored along with the package before uploading. As long as this information is available we can make use of it. I wrote a small .net tool “**IntuneWinAppUtilDecoder**” to extract the .intunewin file content, read the EncryptionInfo from the detection.xml file to get the encryption key and initialization vector and decrypt the inner .intunewin package from the contents folder back to an unencrypted .intunewin package. Et voila – we have an unencrypted .intunewin.decoded file, which we can open with our favorite archiver like [7-Zip](http://www.7-zip.org).

The **IntuneWinAppUtilDecoder** is available on my GitHub account here:

<https://github.com/okieselbach