import twitter

from datetime import datetime
import os
import time

import json

#
ck='PKfm9LGx6RIqXtpXALSZ9Wxxu'
cs='rbX9zUc5EtM52vPMvn6IlrAwUhOO8MhORtERAizm0wnps9q1ZH'

atk='1108144763902087171-YvxJxxOkdpik5EQ5mN35bClCfFLE08'
ats='XfIaiuRfG95Hgi55ddGy1loyAesa8ruVfXeY2Gxpd4E1L'

#
api = twitter.Api( consumer_key=ck,
                   consumer_secret=cs,
                   access_token_key=atk,
                   access_token_secret=ats,
                   sleep_on_rate_limit=True )

wait=15

def main():
    print( 'Script Started' )

    print( api.VerifyCredentials() )

    Continue = True

    while Continue:
        post()
        time.sleep( wait )


def post():
    now = datetime.now().strftime('%Y-%m-%d')

    query = 'q=lang%3Aen since%3A' + now + '&src=typed_query&count=100'

    result = api.GetSearch( raw_query=query )

    print("length of result:")
    print(len(result))
    print("\r\n")

    for st in result:
        #
        program_print(st)

#
def program_print(st):
    file_name = "./dump.json"
    state = "w+"

    if( os.path.exists( file_name ) ):
        state = "a"
    else:
        state = "w+"

    file_write = open(file_name, state)

    file_write.write(str(st))
    file_write.write("\r\n")

    file_write.close()

    return None


main()
