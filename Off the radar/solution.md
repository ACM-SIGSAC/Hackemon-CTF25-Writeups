# Off The Radar Writeup

1. Go to the provided link and download the image named `lookcloser.jpeg`.

2. Open your terminal and navigate to the downloads folder where you saved the `.jpeg`.

3. Extract the hidden file using `steghide`:

   ```
   sudo apt install steghide
   steghide extract -sf lookcloser.jpeg
   ```
   
4. When prompted for a passphrase, just press Enter (there’s none).
   
5. After extraction, you’ll get a `.wav` audio file in the same directory.

6. Upload this `.wav` file to [https://morsecode.world/international/decoder/audio-decoder-adaptive.html]

7. Wait for the site to decode the Morse code message automatically.

8. Read the decoded message carefully, that’s your flag!

9. Submit the flag: **ACM{Y0U_D3C0D3D_TH3_S0S_C@LL1NG}**

