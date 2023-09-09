import webbrowser

# Make sure your PC possesses sufficient RAM to handle enormous amounts of web requests back-to-back

# Replace 'your_url_here' with the URL you want to open
url_to_open = 'https://github.com/mixed-farming'

# Number of times to open the URL
num_tabs = 100

# Loop to open the URL multiple times
for _ in range(num_tabs):
    webbrowser.open_new_tab(url_to_open)
