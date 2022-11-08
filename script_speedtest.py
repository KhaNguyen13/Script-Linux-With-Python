# Python program to test
# internet speed
# Text....

import speedtest


st = speedtest.Speedtest()

option = int(input('''What speed do you want to test:

1) Download Speed

2) Upload Speed

3) Ping

Your Choice: '''))


if option == 1:
    download_s = str(round(st.download()//1000000))
    print(download_s + " Mb/s")
    
elif option == 2:
    upload_s = str(round(st.upload()//1000000))
    print(upload_s + " Mb/s")
elif option == 3:

	servernames =[]

	st.get_servers(servernames)

	print(st.results.ping)

else:

	print("Please enter the correct choice !")
