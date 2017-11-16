import time
import webbrowser as wb

def break_time(url, waittime=10,nobreaks=3):
  count = 0
  while (count<3):
    count = count + 1;
    wb.open(url);
    time.sleep(waittime);


break_time("https://www.youtube.com/watch?v=1G4isv_Fylg&list=PL5L9WUoPnW0cjk98cpw_68CnHmELV2g_z",2,3)