import paramiko


def getSftpFile(config, filepath, localpath):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(**config)
        sftp = ssh.open_sftp()

        # file = sftp.open(filepath)  # 파일 다운로드
        sftp.get(filepath, localpath)  # 파일 다운로드
    except Exception as e:
        print(e)
    finally:
        ssh.close()

# # sftp.get(filepath, localpath)  # 파일 다운로드
# with open(localpath, 'r') as f:
#     for line in f:
#         print( line )
# sftp.close()
# ssh.close()

# sftp = ssh.open_sftp()
# remote_file = sftp.open(filepath)
# sftp_client.close()
