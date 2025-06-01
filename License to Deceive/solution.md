# License to Deceive Writeup

1. Go to [https://excise.gos.pk] and search the number plate **BMW-123** to get vehicle details.

2. Expand the details and use the hint `Instagram @Lastname_HorsePower_` to find the Instagram username.

3. On the Instagram profile **@sohail_1497_** , click the link in the description and download the image named `ctf.jpeg`.

4. Open the terminal and navigate to the downloads folder where `.jpeg` is.

5. Extract hidden data from the image using `steghide`:

   ```
   sudo apt install steghide
   steghide extract -sf ctf.jpeg
   ```
   
6. When prompted for a passphrase, just press Enter (there’s none).

7. After extraction, you’ll get a ZIP file named `secret.zip`. Unzip it with:

   ```
   unzip secret.zip
   ```

8. Inside the ZIP, there are two files: `check.txt` and `flag.txt`. One contains the flag, the other is used for the next challenge, Digital Breadcrumbs.

9. View the files using:
   ```
   cat flag.txt
   cat check.txt
   ```
10. Submit the flag: **ACM{h3r3_1s_th3_p1x3l_2025}**
