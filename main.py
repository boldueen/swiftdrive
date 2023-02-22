from utils.process.excel_and_csv_worker import create_daily_report_from_file
from utils.process.swift_browser import download_report_file

from utils.process.mail_worker import send_daily_report_on_mail

from settings import FILEPATH

import time
import schedule    

from datetime import datetime
from datetime import timedelta


def main():
    start = time.time()
    print('_____start____programm____')

    yesterday = (datetime.today() - timedelta(days=1)).date()
    day_before_yesterday = yesterday - timedelta(days=1)
    first_day_of_month = yesterday.replace(day=1)

    download_report_file(start_date=day_before_yesterday, end_date=yesterday, base_or_proj='BASE')
    download_report_file(start_date=first_day_of_month, end_date=yesterday, base_or_proj='PROJ')
    create_daily_report_from_file(
        filepath='utils/process/reports/daily_report.xlsx', 
        start_date=first_day_of_month, 
        end_date=yesterday
        )

    send_daily_report_on_mail('nikon2283@gmail.com', 'Иван', FILEPATH, 'daily.xlsx')

    print('_____finish____programm____')
    print('work_time:', round(time.time()-start, 2), 'seconds')

    print(yesterday)


if __name__ == "__main__":
    # schedule.every().day.at("08:00").do(main) 
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    main()