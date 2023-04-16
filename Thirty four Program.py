import webbrowser

url1 = "youtube.com "
url2 = "google.com"
url3 = "https://earth.google.com/web/@0.0000004,-2.98200068,-517.19686414a,22252270.29849529d,35y,0h,0t,0r"
chrome_path = r"C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe"
webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get("chrome").open_new_tab(url1)
webbrowser.get("chrome").open_new_tab(url2)
webbrowser.get("chrome").open_new_tab(url3)
