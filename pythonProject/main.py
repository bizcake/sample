from modules import telegram
from modules import database as db
from modules import sftp
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # start

    # ===============================
    # [module] sftp =================
    # ===============================
    config={
        'key_filename': 'D:/Workspace/shinhan_sftp_key'
    }
    filepath = '/download/20210106/SHINHAN BANK_Financial_Product_Scraping_Result_20210106_CARD_Y.csv'
    localpath = './download/hello.csv'
    sftp.getSftpFile(config, filepath, localpath)


    # ===============================
    # [module] db =================
    # ===============================
    # conn = db.Database()
    #
    # sql = "INSERT INTO ot_col_auth ( AUTH_ID ) \
    #             VALUES('%s')" % ('testData')
    # conn.execute(sql)
    # conn.commit()

    # sql = "SELECT auth_id \
    #             FROM ot_col_auth"
    # row = conn.executeAll(sql)
    # print(row)


    # ===============================
    # [module] telegram =================
    # ===============================
    # telmodule.send_message("hello~message 3")
    print('complete ~!!')